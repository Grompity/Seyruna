"""Sprint live probe: one door through the ONE door, timed, printed.

Usage: python3 research-hold/_live_probe.py [--shelf | --web SENTENCE | --task]
Deterministic parts ride the real bytes; the mouth is the real configured
endpoint (stages.CONFIG). No writes outside research-hold.
"""
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import stages


def show(label, body):
    t0 = time.time()
    payload, code = stages.door(body, live=True)
    dt = time.time() - t0
    tr = payload.get("trace") or {}
    why = payload.get("why") or {}
    print("%-10s code=%s secs=%.1f calls=%s lane=%s status=%r"
          % (label, code, dt, tr.get("model_calls", stages.CALLS[0]),
             tr.get("lane") or why.get("lane"),
             (tr.get("evidence_status") or why.get("evidence_status"))))
    print("   response:", (payload.get("response") or "")[:220].replace("\n", " "))
    w = tr.get("web")
    if w:
        print("   web: provider=%s query=%r fetched=%s gaps=%s corr=%s"
              % (w.get("provider"), w.get("query"), w.get("fetched"),
                 w.get("gaps"), w.get("corroboration")))
    print("   stages_ms:", tr.get("stages_ms"))
    return payload


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "--shelf"
    if mode == "--shelf":
        show("SHELF", {"question": "What does the Tao say about wu wei?"})
    elif mode == "--web":
        show("WEB", {"question": sys.argv[2], "web": True})
    elif mode == "--task":
        show("TASK", {"question": "/task inspect"})
