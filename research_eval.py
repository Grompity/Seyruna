#!/usr/bin/env python3
"""research_eval.py - A5's fixed evaluation (fixture: research-eval.json,
EA-0.1). Six questions at the web lanes, the wording FROZEN (the seeker's
words ride as spoken); the expected-lane words were written from a live
search-level probe of the day BEFORE any scoring (an expectation is not a
score).

The runner records TRUTH, never a verdict: per question it runs
web_research (the search, the fetches, the kinds, the corroboration words),
then - live mode - the SAME real door the conversation rides (web:true:
the eval asks of the WEB lanes; the auto lanes' sufficiency was weighed at
T140 and the A5 live file). The axes (§6's separate scores) are filled by
the MACHINE where they are counts (retrieval, traceability, independence
- the words ride below) and by the OPERATOR by hand elsewhere (factual
correctness, citation support, appropriate uncertainty, evasiveness) -
the same brain that wrote the code, disclosed, never an independent
model judging its own child.

The caps are PRE-REQUEST like the whole house's law: a leg does not START
without margin (max_secs_per_question rides the wall-clock of the
question's own run; the web phase carries its own MAX_SECS inside, and
the door's mouths are bounded by their own road). Over-budget legs ride
the word "over-budget" - a stated skip, never a silent loss.

Modes: no argument = the full live road (search + fetches + the door's
mouths - the run the report's numbers come from); --search = the cheap
re-check (web lanes only, zero mouthfuls). The deterministic truths of
this eval's machinery ride the T-series; this runner IS live by nature
(an eval that never saw the net is a fixture).
"""
import json
import os
import sys
import time

import stages
import web_research

HERE = os.path.dirname(os.path.abspath(__file__))


def load_doc():
    return json.loads(open(os.path.join(HERE, "research-eval.json")).read())


def run_one(qtext, live, caps):
    t0 = time.time()
    out = {"question": qtext}
    pk = web_research.research(qtext)              # its own MAX_SECS bounds it
    rows, ids = web_research.to_rows(pk)
    out["web"] = {"provider": pk["provider"], "ok": pk["ok"],
                  "results": len(pk["results"]), "gaps": pk["gaps"],
                  "spent": pk["spent"],
                  "corroboration": web_research.corroboration(pk),
                  "rows": [{"id": r["id"], "kind": r.get("kind"),
                            "evidence": r.get("evidence"),
                            "note": r.get("note"), "work": r.get("work"),
                            "publisher": r.get("publisher"),
                            "url": r["url"], "claim": r["claim"]}
                           for r in rows]}        # THE BYTES THE MOUTH SAW
    left = caps.get("max_secs_per_question", 240) - (time.time() - t0)
    if live:
        if left > 0:
            payload, code = stages.door({"question": qtext, "web": True},
                                        live=True)
            tr = payload["trace"]
            # A18: the runner's record now carries the door's OWN status
            # word VERBATIM (a tr.get, never a reconstruction from prose):
            # a missing word rides as ABSENCE (null), never as an invented
            # stronger claim; the over-budget lane stays sparse as built.
            out["door"] = {"code": code, "lane": tr.get("lane"),
                           "retrieval": tr.get("retrieval"),
                           "response": tr.get("response"),
                           "model_calls": tr.get("model_calls"),
                           "evidence_status": tr.get("evidence_status"),
                           "web_stamped": tr.get("web") is not None}
        else:
            out["door"] = {"lane": "over-budget"}    # the word, not a shrug
    out["secs"] = round(time.time() - t0, 1)
    return out


def status_word(rec):
    # A19: main's readable line SELECTS the word the RECORD already
    # carries (never the answer's prose, never the trace). A run whose
    # door never rode (the search-only mode) says so; a door record whose
    # trace left the word un-spoken (a pre-A15 shape, the over-budget
    # lane) says so; neither ever leans toward VERIFIED.
    d = rec.get("door")
    if d is None:
        return "no-door (search-only)"
    s = d.get("evidence_status")
    return s if s else "status-unspoken"


def main(argv):
    live = "--search" not in argv
    doc = load_doc()
    caps = doc.get("caps") or {}
    rec = {"eval": doc.get("eval"),
           "mode": "live" if live else "search-only",
           "provider": web_research.provider_name(),
           "caps": caps, "date": time.strftime("%Y%m%d"),
           "review": "operator (the A5 hand; same brain that wrote the "
                     "code - disclosed, not independent)",
           "questions": []}
    for q in doc.get("questions") or []:
        r = run_one(q["question"], live, caps)
        r["id"] = q.get("id")
        r["kind"] = q.get("kind")
        r["expect"] = q.get("expect")
        rec["questions"].append(r)
        d = r.get("door")
        print(r["id"], "| ok:", r["web"]["ok"], "| results:", r["web"]["results"],
               "| gaps:", r["web"]["gaps"], "| indep:",
               r["web"]["corroboration"]["independence"],
               "| lane:", (d or {}).get("lane"),
               "| calls:", (d or {}).get("model_calls"),
               "| status:", status_word(r),
               "| %.1fs" % r["secs"])
    out = os.path.join(HERE, "research-hold",
                       "a5-eval-live.json" if live else "a5-eval-search.json")
    open(out, "w").write(json.dumps(rec, indent=1))
    print("wrote", out)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
