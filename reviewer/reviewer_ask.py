# reviewer_ask.py - the GPT leg of the bridge (v0.1): a Responses-API loop
# driving the SAME registry the MCP server exposes (one shared repo, one
# tool surface; no second door). env: OPENAI_API_KEY (required; never
# printed, never committed), OPENAI_REVIEWER_MODEL (default gpt-6-astra -
# the docs' flagship for reasoning+coding; GPT-6.1 Sol / GPT-6 Luna are the
# cheaper siblings), OPENAI_BASE_URL (default https://api.openai.com/v1).
# The reviewer's standing orders ride the doc beside this file.
import json
import os
import ssl
import sys
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import reviewer_mcp as mcp

KEY = os.environ.get("OPENAI_API_KEY")
if not KEY:
    print("OPENAI_API_KEY unset: the bridge (server + selftest) stands;")
    print("the GPT leg waits for the key. Never printed, never committed.")
    sys.exit(0)
MODEL = os.environ.get("OPENAI_REVIEWER_MODEL", "gpt-6-astra")
BASE = os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1")
QUESTION = " ".join(sys.argv[1:]) or \
    "Review the current state of this project for architecture-soundness."

try:
    INSTRUCTIONS = open(os.path.join(ROOT, "gpt-reviewer.md")).read()
except OSError:
    INSTRUCTIONS = "You are an adversarial architectural reviewer."
INSTRUCTIONS += ("\n\nCall the reviewer tools as needed (all read-only). "
                 "Finish with exactly these headings: FINDING, EVIDENCE, "
                 "CLASSIFICATION, ASSESSMENT, RECOMMENDATION, CONFIDENCE, "
                 "DO NOT CHANGE.")

def tools():
    out = []
    for name, (fn, desc, schema) in mcp.REGISTRY.items():
        out.append({"type": "function",
                    "name": name,
                    "description": desc,
                    "parameters": {"type": "object",
                                   "properties": {a: {"type": t}
                                                  for a, (t, d, req) in schema.items()},
                                   "required": [a for a, (t, d, req) in schema.items() if req],
                                   "additionalProperties": False},
                    "strict": False})
    return out

def post(payload):
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    req = urllib.request.Request(BASE.rstrip("/") + "/responses",
                                 data=json.dumps(payload).encode(),
                                 headers={"Content-Type": "application/json",
                                          "Authorization": "Bearer " + KEY})
    with urllib.request.urlopen(req, timeout=180, context=ctx) as r:
        return json.loads(r.read().decode())

input_items = [{"role": "user", "content": QUESTION}]
turns, calls = 0, 0
while turns < 8:
    turns += 1
    resp = post({"model": MODEL, "instructions": INSTRUCTIONS,
                 "input": input_items, "tools": tools(), "tool_choice": "auto"})
    outs = resp.get("output", []) or []
    texts, fns = [], []
    for it in outs:
        kind = it.get("type") or it.get("item_type") or ""
        if kind in ("function_call", "functionCall", "function_call_item"):
            fns.append(it)
        elif kind == "message":
            texts.append("".join(p.get("text", "") for p in (it.get("content") or [])
                                 if p.get("type") == "output_text" or "text" in p))
        elif it.get("text"):
            texts.append(it["text"])
    if not outs:
        print("openai answered without output items:", resp.get("status"))
        sys.exit(1)
    if not fns:
        print("\n".join(t for t in texts if t) or "(empty response)")
        print("\n[reviewer: %s | %d turn(s) | %d tool call(s)]" % (MODEL, turns, calls))
        sys.exit(0)
    cont = []
    for it in fns:
        calls += 1
        name = it.get("name") or it.get("function", {}).get("name")
        args = it.get("arguments") or it.get("function", {}).get("arguments") or "{}"
        if isinstance(args, str):
            try:
                args = json.loads(args)
            except ValueError:
                args = {}
        sys.stderr.write("  reviewer used %s %s\n" % (name, json.dumps(args)[:110]))
        try:
            fn, _d, schema = mcp.REGISTRY[name]
            out = str(fn(**{k: v for k, v in args.items() if k in schema}))
        except KeyError:
            out = "unknown tool"
        except Exception as e:
            out = "tool error: " + str(e)
        cont.append({"type": "function_call_output",
                     "call_id": it.get("call_id") or it.get("id"),
                     "output": out})
    input_items = outs + cont
print("(the reviewer kept calling tools through 8 turns; the loop gave up - not the bridge)")
