import os
import sys
import time
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import web_research as w

for q in sys.argv[1:]:
    t0 = time.time()
    rows, gap = w.search(q)
    lanes = [r["lane"] for r in rows]
    print("%-24s rows=%d gap=%s lanes=%s (%.1fs)"
          % (q, len(rows), gap, lanes, time.time() - t0))
    for r in rows[:3]:
        print("   ", r["url"][:70], "|", (r.get("snippet") or "")[:48])
