# projection.py — the PROJECTION gate (the sign-off letter's item 4):
# offline, deterministic, the mouths asleep. The five cards' ACTUAL text
# (question + FACTS, as the re-runs carried them) through the RETRIEVAL
# GATE ALONE, against the shelf as POPULATED. The gate's claims: every
# INTENDED record surfaces (>= 2 per card); the kinds and levels of what
# surfaced print so the lesson-kinds can be judged as PRESENT or not;
# and every surfacing prints THE SHARED TOKENS THAT CARRIED IT - so a
# stranger is judged on its tokens (a counting-word accident is a
# FAILURE, an honest neighbor is not), not on taste. An EMPTY surfacing
# is UNKNOWN speaking - reported, never hidden. The shelf is not touched
# to make the gate look good: the gate SHOWS the gaps, and the gaps
# named the fixes - the first run's misses were DATA (exact-token
# misses: the stem-equality bound biting, as it was left to do, on real
# cards) and top-4 starvation (the shelf doubled; the four-slot gate was
# sized for ten - a named economics, DATA in config, unraised by
# preemption).
import json
import stages

BY = stages.BY_ID

def toks(s):
    return s.lower().replace("?", " ").replace(".", " ").replace(",", " ") \
            .replace(";", " ").replace("'", " ").split()

def carried(qf, rid):
    rq = {w for w in toks(qf) if w not in stages.STOP and len(w) > 2}
    rr = {w for w in toks(BY.get(rid, {}).get("claim", ""))
          if w not in stages.STOP and len(w) > 2}
    return sorted(rq & rr)

CARDS = [
 ("C1 intuition vs the story",
  "How can I distinguish genuine intuition from desire, fear, projection, pattern-recognition, or a story I am unconsciously creating because I want something to be true?",
  "Asking for years; a friend who can check in sometime; alone with it tonight.",
  ["11", "12"]),
 ("C2 convergence of traditions",
  "When the traditions appear to point toward similar ideas about ego, attachment, surrender, compassion, or unity, have they discovered something similar about reality, or am I imposing a modern synthesis onto traditions that fundamentally disagree?",
  "Long study of wu wei, action without attachment, ego-transcendence, mystical union; the pull toward synthesis is felt; the traditions disagree on doctrine; and the seeker has come to doubt that the traditions agree even on which questions are worth answering, the soul and the world among them.",
  ["13", "14"]),
 ("C3 spirituality without identity",
  "How do I pursue deep spiritual practice and transformation without becoming attached to being spiritual, believing I am specially chosen or awakened, or using spiritual ideas to avoid ordinary human responsibilities?",
  "Wants to be more capable, loving, grounded, responsible; family and work remain; slept well last night; no special claims made.",
  ["15", "16"]),
 ("C4 surrender vs responsibility",
  "How do I know when I should surrender and allow life to unfold, and when surrender or going with the flow is actually avoidance, fear, indecision, or refusal to take responsibility?",
  "Practiced for years; the judgment of each hour is the hour's own; responsibility stays with the person.",
  ["17", "18"]),
 ("C5 what we can say of consciousness",
  "What can we responsibly say about consciousness when neuroscience and philosophy sit next to contemplative reports of awareness, selfhood, witness-consciousness, soul, mind, or ultimate reality?",
  "No settled account; the reports are prior; the setting aside of the questions about the soul and what comes after death the seeker has read; alone tonight; no risk.",
  ["13", "19"]),
]

gaps = 0
for tag, q, f, want in CARDS:
    key = q + " " + f
    ids = stages.retrieve(key)
    missing = [i for i in want if i not in ids]
    strays = [i for i in ids if i not in want]
    gaps += len(missing)
    print("\n" + tag)
    print("  surfaced:", ids or "EMPTY - UNKNOWN would legitimately win")
    print("  intended:", "ALL IN" if not missing else "MISSING " + str(missing))
    for i in ids:
        r = BY.get(i, {})
        print("    [" + i + "] kind=" + str(r.get("kind", "-"))
              + " | level=" + str(r.get("level", "?"))
              + " | carried-by " + ",".join(carried(key, i)) or "(?)")
    if strays:
        print("  strays (judge the tokens printed, not the taste):", strays)

print("\nGATE: " + str(gaps) + " intended-record gap(s) across the five."
      + "\nThe bounds (stem-equality, content-blindness) bit HERE first,"
      + "\non real cards, as left: classified BEFORE repairing, repaired"
      + "\nat the SMALLEST layer - which today meant the DATA, not the"
      + "\nmachinery. TOPK (four slots, sized for ten records) is a named"
      + "\neconomics in config - raised only if the shelf itself proves"
      + "\nit starves a lesson.")
