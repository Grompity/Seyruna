# reviewer_mcp.py — the ascended-reviewer MCP server (v0.1).
# One stdio JSON-RPC loop over a small READ-ONLY tool registry. The bridge
# is development infrastructure: the Ascended runtime (spine, shelf,
# rule-pack, window, constitution) is not imported and not touched here.
# Zero dependencies: stdlib only. Every path passes ONE guard; the only
# subprocesses are git and the two test-runners - never a shell.
import fnmatch
import json
import os
import re
import subprocess
import sys

ROOT = os.path.abspath(os.environ.get("REVIEWER_ROOT")
                       or os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NAME, VERSION = "ascended-reviewer", "0.1.0"
READ_CAP = 12000

def _ignore_rules():
    pats = []
    for f in (".gitignore", ".vercelignore"):
        try:
            for line in open(os.path.join(ROOT, f)):
                s = line.strip().rstrip("/")
                if s and not s.startswith("#"):
                    pats.append(s)
        except OSError:
            pass
    return pats
IGNORED = _ignore_rules()
DOT_OK = {".gitignore", ".vercelignore"}          # the rules themselves are visible
TEXT_EXT = {".md", ".py", ".js", ".mjs", ".css", ".html", ".json",
            ".jsonl", ".jsonc", ".txt", ".toml", ".yml", ".yaml", ".csv", ".ts"}

def _guard(path):
    # the ONE path policy. Root-relative by law: '..' cannot escape, it is
    # REJECTED. Dot-paths and ignore-rule matches (.env*, .venv, .vercel,
    # .git, __pycache__) are invisible to the reviewer. Returns None (ok)
    # or a spoken reason.
    if not isinstance(path, str) or not path.strip():
        return "give a non-empty path (root-relative)"
    p = path.strip().lstrip("/")
    segs = [s for s in p.split("/") if s not in ("", ".")]
    if ".." in segs:
        return "escapes root (..) - paths are root-relative by law"
    for s in segs:
        if s.startswith(".") and s not in DOT_OK:
            return "blocked (dot-path: " + s + ")"
        for pat in IGNORED:
            if fnmatch.fnmatch(s, pat):
                return "blocked (ignore-rule " + pat + ")"
    return None

def _under_root(abs_p):
    return abs_p == ROOT or abs_p.startswith(ROOT + os.sep)

def read_file(path, limit=None):
    bad = _guard(path)
    if bad:
        return bad
    p = os.path.normpath(os.path.join(ROOT, path.lstrip("/")))
    if not _under_root(p):
        return "escapes root (not under the workspace)"
    if os.path.isdir(p):
        return "is a directory (read_file takes a file)"
    try:
        raw = open(p, "rb").read()
    except OSError:
        return "no such file: " + path
    cap = max(1, min(int(limit), READ_CAP)) if limit else READ_CAP
    text = raw[:cap].decode("utf-8", "replace")
    return text + ("... [truncated]" if len(raw) > len(text.encode("utf-8", "replace")) else "")

def _walk_ok(name):
    if name.startswith("."):
        return False
    return not any(fnmatch.fnmatch(name, pat) for pat in IGNORED)

def search_repo(pattern, glob=None, limit=None):
    try:
        rx = re.compile(pattern)
    except re.error as e:
        return "bad regex: " + str(e)
    hits, total, cap = [], 0, (max(1, int(limit)) if limit else 30)
    for base, dirs, files in os.walk(ROOT):
        dirs[:] = sorted(d for d in dirs if _walk_ok(d))
        rel_base = os.path.relpath(base, ROOT)
        if rel_base != "." and not _walk_ok(rel_base.split(os.sep)[0]):
            continue
        for f in sorted(files):
            rel = f if rel_base == "." else os.path.join(rel_base, f)
            if _guard(rel):
                continue
            if glob and not (fnmatch.fnmatch(f, glob) or fnmatch.fnmatch(rel, glob)):
                continue
            if os.path.splitext(f)[1] not in TEXT_EXT:
                continue
            try:
                lines = open(os.path.join(ROOT, rel),
                             encoding="utf-8", errors="replace").read().splitlines()
            except OSError:
                continue
            for n, line in enumerate(lines, 1):
                if rx.search(line):
                    total += 1
                    if len(hits) < cap:
                        hits.append(rel + ":" + str(n) + ":" + line.strip()[:160])
    if total == 0:
        return "no matches for " + pattern
    return "\n".join(hits + (["(+ more matches)"] if total > len(hits) else []))

def _git(*args):
    try:
        r = subprocess.run(["git", "-C", ROOT] + list(args),
                           capture_output=True, text=True, timeout=30)
    except FileNotFoundError:
        return "git is not on PATH (the bridge degrades; nothing else does)"
    if r.returncode != 0:
        tail = (r.stdout + r.stderr).strip().splitlines()
        return tail[-1] if tail else "git failed"
    return r.stdout.rstrip() or "(nothing to report)"

def git_status(): return _git("status", "--short", "-b")
def git_diff():   return _git("diff", "HEAD")
def git_log(n=10):
    try:
        n = max(1, min(20, int(n)))
    except Exception:
        n = 10
    return _git("log", "--oneline", "-n" + str(n))

def _runner(script, tail):
    try:
        r = subprocess.run([sys.executable, "-B", script], cwd=ROOT,
                           capture_output=True, text=True, timeout=240)
        lines = (r.stdout + r.stderr).strip().splitlines()
        return "\n".join(lines[-tail:]) + "\nexit=" + str(r.returncode)
    except Exception as e:
        return script + " failed to run: " + str(e)

def run_tests():      return _runner("tests.py", 4)
def run_batteries():  return (_runner("retrieval_battery.py", 3) + "\n--\n"
                              + _runner("integrity_battery.py", 3))

def get_project_map():
    sections = [
        ("DOCUMENTS", ["constitution.md", "foundation.md", "architecture.md",
                       "golden-set.md", "voice_brief.md", "founder-eval.md",
                       "README.md", "gpt-reviewer.md"]),
        ("SPINE+DOORS", ["stages.py", "window.py", "server.py", "api/ask.py",
                         "mvp_run.py", "pilot_run.py"]),
        ("DATA", ["shelf.jsonl", "rule_pack.json", "config.json"]),
        ("TESTS", ["tests.py", "retrieval_battery.py", "integrity_battery.py"]),
        ("WEB", ["index.html", "css", "js"]),
        ("BRIDGE", ["reviewer/reviewer_mcp.py", "reviewer/selftest.py",
                    "reviewer/reviewer_ask.py", "opencode.json", "vercel.json"]),
        ("WITNESSES", ["battery7.json", "battery-broad-before.json",
                       "battery-broad-after.json", "mvp-run-1.json"]),
    ]
    out = ["workspace: " + ROOT]
    for name, items in sections:
        out.append(name + ": " + ", ".join(
            i if os.path.exists(os.path.join(ROOT, i)) else i + " (missing)"
            for i in items))
    out.append("blocked from the reviewer: .env* (secrets), .venv, .vercel,"
               " .git, __pycache__ - the ignore-rules are honored, not re-invented")
    return "\n".join(out)

# registry: name -> (fn, description, {arg: (json-type, description, required)})
REGISTRY = {
  "reviewer_read_file": (read_file,
    "Read one workspace file, root-relative. Text only; 12000-char cap.",
    {"path": ("string", "root-relative file path", True),
     "limit": ("integer", "max chars (<=12000)", False)}),
  "reviewer_search_repo": (search_repo,
    "Regex search over workspace text files. Hits as 'path:line:preview'.",
    {"pattern": ("string", "python regex", True),
     "glob": ("string", "optional file glob, e.g. *.py", False),
     "limit": ("integer", "max hits (default 30)", False)}),
  "reviewer_git_status": (git_status, "git status --short (with branch).", {}),
  "reviewer_git_diff":   (git_diff,   "git diff HEAD (the uncommitted work).", {}),
  "reviewer_git_log":    (git_log,    "One-line history (n <= 20).",
                         {"n": ("integer", "how many lines", False)}),
  "reviewer_run_tests": (run_tests,
    "Run the frozen harness (tests.py - runs WITHOUT the funnel). Tail + exit code.", {}),
  "reviewer_run_batteries": (run_batteries,
    "Run the two deterministic zero-funnel probe batteries (retrieval, integrity).", {}),
  "reviewer_get_project_map": (get_project_map,
    "Computed workspace map: sections, files, and what the bridge blocks.", {}),
}

def _tools_list():
    out = []
    for name, (fn, desc, args) in REGISTRY.items():
        props = {a: {"type": t, "description": d} for a, (t, d, req) in args.items()}
        out.append({"name": name, "description": desc,
                    "inputSchema": {"type": "object", "properties": props,
                                    "required": [a for a, (t, d, req) in args.items() if req],
                                    "additionalProperties": False}})
    return out

def _send(obj):
    print(json.dumps(obj), flush=True)

def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            msg = json.loads(line)
        except ValueError:
            err = {"jsonrpc": "2.0", "id": None,
                   "error": {"code": -32700, "message": "parse error"}}
            _send(err)
            continue
        mid, method = msg.get("id"), msg.get("method", "")
        params = msg.get("params") or {}
        if method.startswith("notifications/"):
            continue
        if method == "initialize":
            info = {"protocolVersion": params.get("protocolVersion", "2025-06-18"),
                    "capabilities": {"tools": {}},
                    "serverInfo": {"name": NAME, "version": VERSION}}
            _send({"jsonrpc": "2.0", "id": mid, "result": info})
        elif method == "tools/list":
            _send({"jsonrpc": "2.0", "id": mid, "result": {"tools": _tools_list()}})
        elif method == "tools/call":
            name = params.get("name")
            if name not in REGISTRY:
                miss = {"content": [{"type": "text", "text": "unknown tool"}],
                        "isError": True}
                _send({"jsonrpc": "2.0", "id": mid, "result": miss})
                continue
            fn, _desc, schema = REGISTRY[name]
            args = params.get("arguments") or {}
            if isinstance(args, str):
                try:
                    args = json.loads(args)
                except ValueError:
                    args = {}
            try:
                text = fn(**{k: v for k, v in args.items() if k in schema})
            except Exception as e:
                text = "tool error: " + str(e)
            bad = str(text).startswith(("escapes", "blocked", "bad regex",
                                        "tool error:", "no such",
                                        "give a non-empty"))
            res = {"content": [{"type": "text", "text": str(text)}],
                   "isError": bad}
            _send({"jsonrpc": "2.0", "id": mid, "result": res})
        elif mid is not None:
            nf = {"code": -32601, "message": "method not found"}
            _send({"jsonrpc": "2.0", "id": mid, "error": nf})

if __name__ == "__main__":
    main()
