"""A30: the voice's thinking, PRICED at the door (not at the raw wire).

One wrapper over stages.call decides the word per seam per trial; every
other byte of the request is the road's own (same prompt, same model,
same caps, same temperature, same door, same question). Trials ALTERNATE
ON/OFF to split the endpoint's own mood across the conditions.

Synthesis road:  the shelf-hit question (A29's, proven to reach the seam).
General road:    the shelf-silent question (A28's, proven to reach the
                 general arm at ONE mouthful).
The two roads and their ledgers ride the witness APART (one result for
one road may not spend the other's coin).

Rubric decided BEFORE the bytes, all of it the house's own deterministic
words (no taste smuggled in as a verdict):
  synth:  valid contract parse; zero cite_dropped; no synth_note; blocked
          False; the fires count rides (the constitutional eyes, RP-07's
          promotion among them); the node's BYTES ride for the human eye.
  general: knows true with a non-placeholder node (the lane spoke, not
          the shelf's exit); no general_note; the UNSOURCED fire rides;
          the answer's BYTES ride for the human eye.
"""
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import stages

SYN_Q = "What does the Tao say about wu wei?"
GEN_Q = "Does fasting help adults lose weight?"
N = int(sys.argv[1]) if len(sys.argv) > 1 else 3   # trials per condition

_real_call = stages.call
REC = []            # what the wrapper saw per seam call

def wrapper(system, user, maxtok=None, thinking=True):
    seam = ("synth" if system == stages.SYNTH_SYS
            else "general" if system == stages.GENERAL_SYS
            else "other")
    word = WORD[seam] if seam in WORD else thinking
    out = _real_call(system, user, maxtok, word)
    REC.append({"seam": seam, "thinking": bool(word),
                "content_len": len(out.get("content") or ""),
                "reasoning_len": len(out.get("reasoning") or ""),
                "truncated": bool(out.get("truncated"))})
    return out

WORD = {}
stages.call = wrapper

def trial(road, qtext, thinking):
    """ONE door run; the witness is the trace's own bytes plus the
    wrapper's ledger. 'live' labels the whole file (every trial here IS
    one live road) - a replay never wears this label."""
    global WORD
    WORD = ({"synth": thinking, "general": thinking} if road == "synth"
            else {"synth": True, "general": thinking})
    REC.clear()
    t0 = time.time()
    rec = {"road": road, "thinking": bool(thinking), "label": "live"}
    try:
        payload, code = stages.door({"question": qtext}, live=True)
        tr = payload["trace"]
        ms = tr.get("stages_ms", {})
        rec.update({"code": code, "wall_ms": round((time.time() - t0) * 1000),
                    "lane": tr.get("lane"),
                    "model_calls": tr.get("model_calls"),
                    "seam_stage_ms": round(ms.get("synthesize" if road == "synth"
                                                  else "general", 0)),
                    "blocked": bool(tr.get("blocked")),
                    "synth_note": tr.get("synth_note"),
                    "general_note": tr.get("general_note"),
                    "fires": list(tr.get("fires", [])),
                    "answer": tr.get("response"),
                    "calls": json.loads(json.dumps(REC))})
        if road == "synth":
            draft = tr.get("draft") or [{}]
            rec["contract_valid"] = bool(draft) and all(
                "node" in d for d in draft)
            rec["cite_dropped"] = sorted({c for d in draft
                                           for c in (d.get("cite_dropped") or [])})
            rec["lineages"] = [d.get("lineage", "").split(":")[0] for d in draft]
    except Exception as e:
        rec.update({"raised": type(e).__name__, "note": str(e)[:160],
                    "wall_ms": round((time.time() - t0) * 1000)})
    return rec

out = {"model": stages.CONFIG["MODEL"], "trials_per_condition": N,
       "synth": [], "general": []}

for i in range(N):                     # ALTERNATE the conditions
    for th in (True, False):
        out["synth"].append(trial("synth", SYN_Q, th))
for i in range(N):
    for th in (True, False):
        out["general"].append(trial("general", GEN_Q, th))

stages.call = _real_call
path = os.path.join(HERE, "a30-ab.json")
json.dump(out, open(path, "w"), indent=1)

for road in ("synth", "general"):
    print(road.upper())
    for r in out[road]:
        seam_ms = r.get("seam_stage_ms")
        calls = [c for c in r.get("calls", []) if c["seam"] == ("synth" if road == "synth" else "general")]
        print("  %-5s wall=%-6s seam_ms=%-6s seam_tokens(seam calls)=%s "
              "raised=%s" % (str(r["thinking"]), r.get("wall_ms"), seam_ms,
                            [(c["content_len"], c["reasoning_len"]) for c in calls],
                            r.get("raised")))
        if road == "synth":
            print("       note=%s blocked=%s dropped=%s fires=%s" %
                  (r.get("synth_note"), r.get("blocked"), r.get("cite_dropped"),
                   r.get("fires")))
        else:
            print("       lane=%s note=%s fires=%s" %
                  (r.get("lane"), r.get("general_note"), r.get("fires")))
        print("       answer: %s" % (r.get("answer") or "")[:110])
