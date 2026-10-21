"""A28: the lane at a HUMAN PACE (the A-series' own law is one search per
question; my earlier probes fired dozens back-to-back). Three paced looks,
8 s apart, printing the transport's own words and the byte-count.

Also: the ONE-mouthful latency and the full door turn on each road, so the
speed baseline rides bytes rather than impressions.
"""
import json
import os
import sys
import time
import urllib.error
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import web_research as w
import stages

print("== the lane, paced ==")
for i in range(3):
    t0 = time.time()
    rows, gap = w.search("Tao Te Ching")
    print("   look%d %6.1fs rows=%d gap=%s lanes=%s"
          % (i + 1, time.time() - t0, len(rows), gap,
             sorted({r["lane"] for r in rows})))
    if i < 2:
        time.sleep(8)

print("== one mouthful (the seam alone) ==")
for i in range(2):
    t0 = time.time()
    out = stages.call("Reply with exactly the requested words.",
                      "Say: the lamp is at arm's length.")
    print("   call%d %5.1fs content=%r truncated=%s"
          % (i + 1, time.time() - t0, (out.get("content") or "")[:40],
             out.get("truncated")))

print("== one door turn, the shelf road ==")
t0 = time.time()
payload, code = stages.door({"question": "What does the Tao say about wu wei?"})
tr = payload["trace"]
print("   %5.1fs code=%s calls=%s ms=%s"
      % (time.time() - t0, code, tr["model_calls"],
         {k: round(v) for k, v in tr["stages_ms"].items()}))
