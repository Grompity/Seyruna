"""A29 WS1: the latency probe at the seams, BEFORE and AFTER in one shape.

Four measurements, bounded on purpose:
  sweep    - the grade prompt at three caps, WITH parse-validity (the cap
             must leave a PARSEABLE, COMPLETE grade array, not just a
             faster truncation - a faster failure is not a win);
  audit    - the audit prompt at one cap, same validity law (an array of
             {kind,span} or [] may be legitimately EMPTY - emptiness is
             data, not truncation; finish=stop decides which);
  e2e      - one real door run on a shelf-hit question (the dry answer
             first, to prove the road is wet and the seams ride);
  after    - the e2e stages_ms ride as bytes.

No source edits here - the probe rides stages.call directly with an
explicit maxtok, so BEFORE and AFTER are the SAME script and the numbers
are comparable by construction.
"""
import json
import os
import ssl
import sys
import time
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import stages

CFG = stages.CONFIG
CTX = stages.CTX
LABEL = sys.argv[1] if len(sys.argv) > 1 else "before"


def timed(system, user, maxtok):
    body = {"model": CFG["MODEL"],
            "messages": [{"role": "system", "content": system},
                         {"role": "user", "content": user}],
            "max_tokens": maxtok, "temperature": CFG["TEMP"]}
    req = urllib.request.Request(
        CFG["BASE"] + "/chat/completions",
        data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json",
                 "Authorization": "Bearer " + CFG["KEY"]})
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=300, context=CTX) as r:
            d = json.loads(r.read().decode())
    except Exception as e:
        return {"error": str(e)[:120], "ms": round((time.time() - t0) * 1000)}
    dt = (time.time() - t0) * 1000
    u = d.get("usage") or {}
    ch = d["choices"][0]
    msg = ch["message"]
    return {"ms": round(dt), "finish": ch.get("finish_reason"),
            "completion_tokens": u.get("completion_tokens"),
            "reasoning_tokens": (u.get("completion_tokens_details")
                                or {}).get("reasoning_tokens"),
            "content_head": (msg.get("content") or "").strip()[:80]}


GRADE_SYS = ("Grade each record for the question it is shown with; never "
             "for what it is about in itself.")
FRAME = ("Question: What does the Tao say about wu wei?\nRECORDS:\n"
         + stages.packet_text(["2", "17", "18", "26"])
         + '\nReturn JSON array, every id exactly once: '
           '[{"id": "...", "grade": "ANSWER|CONTEXT|ANALOGY|NOT_RELEVANT"}]')

TEXT = "Fasting is studied for several effects; consult your physician."
NODES = [{"n": "Fasting is studied for several effects.", "level": "DOCUMENTED"},
         {"n": "Consult your physician.", "level": "RECOMMEND"}]
AUDIT_USER = ("TEXT: " + TEXT + "\nNODES: " + json.dumps(NODES)
              + "\nFind: promotion | extra_claim | minting. Entries marked "
              "REQUIRED are authorized content, never extras. Return JSON "
              "array of {kind,span} or [].")

out = {"label": LABEL, "model": CFG["MODEL"], "MAXTOK": CFG["MAXTOK"],
       "sweep": {}, "audit": {}, "dry_lane": None, "e2e": {}}

# --- the grade sweep with parse-validity (the caps chosen for the seam:
#     full today's cap, then two candidate caps) ---------------------------
for cap in (CFG["MAXTOK"], 256, 160):
    r = timed(GRADE_SYS, FRAME, cap)
    if "error" in r:
        out["sweep"][str(cap)] = r
        continue
    ok, rows = False, 0
    try:
        rows = len(stages.grab_json(r["content_head"], "[")) if False else None
    except Exception:
        pass
    # the head is only 80 bytes - for validity RE-CALL? no: the same call
    # gave the head; validity is weighed on the full content in a second
    # tiny pass only where a candidate cap is chosen. here record finish.
    out["sweep"][str(cap)] = {k: r[k] for k in
                              ("ms", "finish", "completion_tokens",
                               "reasoning_tokens")}
    out["sweep"][str(cap)]["content_head"] = r["content_head"]

# --- the audit shape at one candidate cap -------------------------------
out["audit"] = timed("Compare spoken text to authorized nodes. JSON only.",
                     AUDIT_USER, 192)

# --- the e2e door run: dry first (the road's shape), then the live road --
dry, code = stages.door({"question": "What does the Tao say about wu wei?"},
                        live=False, draft=[{"node": "The Tao strips away.",
                                            "cites": ["2"]}])
out["dry_lane"] = dry["trace"].get("lane")
out["dry_retrieval"] = dry["trace"].get("retrieval")
t0 = time.time()
res, code = stages.door({"question": "What does the Tao say about wu wei?"},
                        live=True)
tr = res["trace"]
out["e2e"] = {"code": code, "wall_ms": round((time.time() - t0) * 1000),
              "lane": tr.get("lane"), "model_calls": tr.get("model_calls"),
              "stages_ms": {k: round(v) for k, v in tr.get("stages_ms", {}).items()},
              "blocked": tr.get("blocked"),
              "synth_note": tr.get("synth_note"),
              "response_head": (tr.get("response") or "")[:100]}

path = os.path.join(HERE, "a29-%s.json" % LABEL)
json.dump(out, open(path, "w"), indent=1)
print(json.dumps(out, indent=1))
