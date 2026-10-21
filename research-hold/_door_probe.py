"""A28 live probe: the ONE door, three roads, timed and spoken.

1. the shelf road (retrieval lane)
2. the web road asked with the seeker's SENTENCE (the A20/A13.1 fold shape)
3. the web road asked with the SAME question plus a deterministic,
   zero-mouth KEYWORD-FORM designation (the A22 query word, spent at the
   door) -- the question still rides the road byte-for-byte.
Prints the trace's own words: lane, calls, stages_ms, the evidence-status,
the query actually ridden, and the response.
"""
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import stages


def door(label, body):
    t0 = time.time()
    payload, code = stages.door(body, live=True)
    dt = time.time() - t0
    tr = payload.get("trace") or {}
    w = tr.get("web") or {}
    print("%-26s code=%s %5.1fs calls=%s lane=%-9s" % (
        label, code, dt, tr.get("model_calls", stages.CALLS[0]),
        tr.get("lane")))
    print("   status  :", tr.get("evidence_status"))
    if w:
        print("   rode    : provider=%s query=%r fetched=%s gaps=%s"
              % (w.get("provider"), w.get("query"), w.get("fetched"), w.get("gaps")))
        print("   corr    :", w.get("corroboration"))
    print("   ms      :", {k: round(v, 1) for k, v in (tr.get("stages_ms") or {}).items()})
    print("   response:", (payload.get("response") or "")[:300].replace("\n", " "))
    print()


S = "Where does the Tao Te Ching speak of non-forcing?"
door("SHELF(wu wei)", {"question": "What does the Tao say about wu wei?"})
door("WEB(sent)", {"question": S, "web": True})
door("WEB(query-word)", {"question": S, "web": True, "query": "Tao Te Ching"})
