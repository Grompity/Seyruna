"""A28 Stage-D measurement: where does an answered turn ACTUALLY spend its
seconds? stages_ms says grade=5..17s, synthesize=6..14s, audit=5..9s at the
live door, while a trivial mouthful costs 1.7s. So: is the cost the PROMPT
(the voice brief + the packet) or the GENERATION (the model's own reasoning
tokens)? The seam already accepts a per-call max_tokens and no caller ever
passes one - so the question is answerable at bytes.
"""
import json
import os
import ssl
import sys
import time
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import stages

CFG = stages.CONFIG
CTX = stages.CTX


def timed(system, user, maxtok):
    body = {"model": CFG["MODEL"],
            "messages": [{"role": "system", "content": system},
                         {"role": "user", "content": user}],
            "max_tokens": maxtok, "temperature": CFG["TEMP"]}
    req = urllib.request.Request(CFG["BASE"] + "/chat/completions",
                                  data=json.dumps(body).encode(),
                                  headers={"Content-Type": "application/json",
                                           "Authorization": "Bearer " + CFG["KEY"]})
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=300, context=CTX) as r:
        d = json.loads(r.read().decode())
    dt = time.time() - t0
    u = d.get("usage") or {}
    ch = d["choices"][0]
    return dt, u, ch.get("finish_reason"), len(user)


GRADE_SYS = ("Grade each record for the question it is shown with; never for "
             "what it is about in itself.")
FRAME = ("Question: What does the Tao say about wu wei?\nRECORDS:\n"
         + stages.packet_text(["2", "17", "18", "26"])
         + '\nReturn JSON array, every id exactly once: '
           '[{"id": "...", "grade": "ANSWER|CONTEXT|ANALOGY|NOT_RELEVANT"}]')

print("prompt bytes:", len(GRADE_SYS) + len(FRAME))
for label, mt in (("cap=4096 (today's byte)", 4096), ("cap=200", 200),
                  ("cap=120", 120), ("cap=60", 60)):
    dt, u, fin, nb = timed(GRADE_SYS, FRAME, mt)
    print("%-24s %5.1fs finish=%-8s completion=%-4s reasoning=%-4s"
          % (label, dt, fin, u.get("completion_tokens"),
             (u.get("completion_tokens_details") or {}).get("reasoning_tokens")))
