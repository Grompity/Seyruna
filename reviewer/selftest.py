# selftest.py - the bridge's own battery (printed witness; the count is the
# machine's, not a claim). Spawns the MCP server over stdio, walks the
# handshake, every tool, and every guard; then a FIXTURE pass: a mini
# workspace (REVIEWER_ROOT) whose shelf carries a deliberately wrong
# epistemic level - the reviewer must SEE it and must not be able to
# change it (read-only by construction). Zero funnel consumed.
import json
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SERVER = os.path.join(HERE, "reviewer_mcp.py")
EXPECT = ["reviewer_get_project_map", "reviewer_git_diff", "reviewer_git_log",
          "reviewer_git_status", "reviewer_read_file", "reviewer_run_batteries",
          "reviewer_run_tests", "reviewer_search_repo"]

def start(root=None):
    env = dict(os.environ)
    env.pop("REVIEWER_ROOT", None)
    if root:
        env["REVIEWER_ROOT"] = root
    return subprocess.Popen([sys.executable, "-B", SERVER],
                            stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                            stderr=subprocess.DEVNULL, text=True, cwd=ROOT, env=env)

def rpc(p, i, method, params=None):
    p.stdin.write(json.dumps({"jsonrpc": "2.0", "id": i, "method": method,
                              "params": params or {}}) + "\n")
    p.stdin.flush()
    if method.startswith("notifications/"):
        return None
    line = p.stdout.readline()
    return json.loads(line) if line else {"result": {}, "_dead": True}

LINES, OK = [], 0
def check(label, cond, note=""):
    global OK
    OK += 1 if cond else 0
    LINES.append(("ok    " if cond else "FAIL  ") + label
                  + ("" if cond else "   (" + str(note)[:70] + ")"))

def text_of(r):
    return ((r.get("result") or {}).get("content") or [{}])[0].get("text", "")

p = start()
r = rpc(p, 1, "initialize", {"protocolVersion": "2025-06-18", "capabilities": {}})
check("handshake names the server",
      ((r.get("result") or {}).get("serverInfo") or {}).get("name") == "ascended-reviewer")
rpc(p, 2, "notifications/initialized")
r = rpc(p, 3, "tools/list")
names = sorted(t["name"] for t in (r.get("result") or {}).get("tools", []))
check("tools/list == the eight (no more)", names == EXPECT, ",".join(names))

def call(i, name, args):
    return rpc(p, i, "tools/call", {"name": name, "arguments": args})

t = text_of(call(4, "reviewer_read_file", {"path": "constitution.md"}))
check("reads a document", "ascended" in t.lower() or t.strip() != "")
check("'..' is REJECTED, not escaped", "escapes" in text_of(call(5, "reviewer_read_file", {"path": "../constitution.md"})))
check(".env.local invisible (secrets stay out)", "blocked" in text_of(call(6, "reviewer_read_file", {"path": ".env.local"})))
check("missing file answers plainly", "no such" in text_of(call(7, "reviewer_read_file", {"path": "does-not-exist.md"})))
check("a directory is answered, not dumped", "is a directory" in text_of(call(8, "reviewer_read_file", {"path": "js"})))
t = text_of(call(9, "reviewer_search_repo", {"pattern": "Ascended", "glob": "*.md", "limit": 3}))
check("search hits with paths", ":" in t and "no matches" not in t, t[:60])
check("bad regex answered", "bad regex" in text_of(call(10, "reviewer_search_repo", {"pattern": "[unclosed"})))
check("git status shows the branch", text_of(call(11, "reviewer_git_status", {})).startswith("##"))
t = text_of(call(12, "reviewer_git_diff", {}))
check("git diff witnesses the bridge's own edit", "opencode.json" in t, t[:60])
check("git log knows the baseline", "baseline" in text_of(call(13, "reviewer_git_log", {"n": 3})))
check("harness gate rides through", "HARNESS GREEN" in text_of(call(14, "reviewer_run_tests", {})))
check("batteries run (integrity count seen)", "integrity battery" in text_of(call(15, "reviewer_run_batteries", {})))
check("project map names its sections", "SPINE" in text_of(call(16, "reviewer_get_project_map", {})))
p.stdin.close(); p.wait(timeout=10)
check("the server stops when stdin closes", p.returncode == 0, p.returncode)

# the FIXTURE: a mini-workspace, one deliberate architectural slip
with tempfile.TemporaryDirectory() as td:
    for f in ("constitution.md", "shelf.jsonl", "rule_pack.json", "config.json"):
        data = open(os.path.join(ROOT, f), "rb").read()
        if f == "shelf.jsonl":
            data = data.replace(b'"level": "DOCUMENTED"', b'"level": "VIBES"', 1)
        open(os.path.join(td, f), "wb").write(data)
    before = open(os.path.join(td, "shelf.jsonl"), "rb").read()
    q = start(root=td)
    rpc(q, 1, "initialize", {})
    rpc(q, 2, "notifications/initialized")
    t = text_of(rpc(q, 3, "tools/call", {"name": "reviewer_search_repo",
                                         "arguments": {"pattern": "VIBES"}}))
    check("the fixture's VIBES-level card is SEEN", "shelf.jsonl" in t, t[:60])
    check("the guard holds at any root", "escapes" in text_of(
        rpc(q, 4, "tools/call", {"name": "reviewer_read_file",
                                 "arguments": {"path": "../constitution.md"}})))
    q.stdin.close(); q.wait(timeout=10)
    after = open(os.path.join(td, "shelf.jsonl"), "rb").read()
    check("read-only by construction (bytes unchanged)", before == after)

for l in LINES:
    print(l)
print("\n%d/%d pass - %s" % (OK, len(LINES), "BRIDGE GREEN" if OK == len(LINES) else "BRIDGE HAS RED"))
sys.exit(0 if OK == len(LINES) else 1)
