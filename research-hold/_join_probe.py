"""A28: the loop's ONE joining mouthful, at the live seam. A2's witnesses
recorded the join LANED (synthesis:fell-back) TWICE, so the loop's live
joining has never been witnessed. This prints the mouth's RAW bytes first
(the diagnosis), then research.live's artifact (the outcome).
"""
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import research
import stages

SRC = {
    "17": ("Bhagavad Gita 18.7 separates the renunciation that flees from the "
           "renunciation that relinquishes thirst for the fruit: sacrifice, "
           "gift and austerity are not to be relinquished, they are to be done."),
    "2": ("Tao Te Ching ch.48 contrasts ordinary learning, which increases "
          "knowledge, with following the Way, which progressively diminishes "
          "doing, arriving at wu wei where nothing is left undone."),
}
spec = {"id": "A28-PROBE",
        "description": "How do the two designated sources bound acting "
                       "without thirst for the fruit?",
        "designated": [{"id": k, "text": v, "work": k} for k, v in SRC.items()],
        "bounds": {"min_sources": 2}}

# 1. the raw seam, at the joining contract (what the mouth ACTUALLY sends)
user = ("TASK: " + spec["description"] + "\nBOUNDS: min_sources=2\nSOURCES:\n"
        + research._sources_text({"rows": [
            {"id": "17", "captured": SRC["17"], "work": "Bhagavad Gita",
             "loculus": "18.7"},
            {"id": "2", "captured": SRC["2"], "work": "Tao Te Ching",
             "loculus": "ch. 48"}]})
        + '\nRespond ONLY with JSON: {"node": "one plain sentence",'
          ' "cites": [ids shown]}')
t0 = time.time()
out = stages.call(research.LIVE_SYS, user)
print("RAW (%.1fs) content=%r" % (time.time() - t0, out.get("content")))
print("    reasoning?%s truncated=%s" % (bool(out.get("reasoning")),
                                          out.get("truncated")))
try:
    print("    grab_json ->", stages.grab_json(out.get("content") or "", "{"))
except ValueError as e:
    print("    grab_json RAISED:", e)

# 2. the same through the agent's own road
t0 = time.time()
art = research.live(spec)
print("live (%.1fs) status=%s syn=%s" % (time.time() - t0, art["status"],
                                        json.dumps(art["synthesis"])[:220]))
