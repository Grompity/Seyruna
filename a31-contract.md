# A31 experiment contract — written BEFORE the lap's outcome was seen

## The road and the question
- Road: the shelf-silent general road, ridden through `stages.door` with
  `live=True` — the same door the conversation rides, the same A28/A30
  proven question: **"Does fasting help adults lose weight?"** (proven at
  A30 to reach the general arm at exactly ONE mouthful).
- Shape: unchanged A30 bytes (`GENERAL_THINKING: false` rides). ONE word is
  in question: the seam's OUTPUT CAP.

## The word in question, as found
- The general seam speaks NO cap word today: absent from `config.json`,
  so the road rides the global `MAXTOK` (4096) by `stages.call`'s own
  fallback — A30's open ledger, A31's lap topic.

## The candidate, and why that number
- Candidate: `GENERAL_MAXTOK = 1024`.
- Why (measured bytes, not taste): A30's live witness records the general
  seam's no-thinking completions at 267-430 BYTES of content (~300 max),
  i.e. well under a quarter of the candidate; the candidate doubles the
  largest legitimate observed shape, quarters the global bound (a TAIL
  BOUND for the runaways, never a widening), and leaves room for the
  thinking-ON future at its OBSERVED A29 sizes WITHOUT promising it
  (if that word is ever turned back on, the clause below re-prices it).

## Trials
- 3 live door runs before the change, 3 after (alternating order is moot
  for a single condition each; the point is sample-of-three to tell a
  BROKEN configuration from a WORKING one — a single fast run decides
  nothing). Endpoint noise is DISCLOSED (A29 measured ~30% at identical
  bytes); the medians and the clause-table carry the decision, not one
  trial.

## Pre-declared acceptance (ALL clauses, every after-trial)
1. the run ARRIVES (code 200, no raise);
2. the road keeps its LANE (`lane == "general"` — the mouth spoke a real
   node; a truncated cap that empties the completion lands at the SHELF's
   exit, and THAT is the visible rejection word at the door);
3. the lane speaks NO fall-back word (`general_note` absent —
   `mouth-fell-back` here would mean the cap ate the answer);
4. the road's own word rides (`GENERAL:UNSOURCED` in fires — the road's
   identity, unchanged by any cap);
5. no NEW FLOOR: the after-trials' wall-median may not exceed the
   before-trials' wall-median by more than a factor of **2.0** (generous
   against the disclosed noise; its only job is to catch a configuration
   that ADDS a floor).

## Pre-declared rejection
Any clause failing on any trial: a `raised` record, a lane that left the
road (shelf exit), a drawn `mouth-fell-back`, a missing lane fire, or a
floor over the band. Any rejection ⇒ RESTORE the exact prior bytes of
`config.json`, verify the restore, and record the experiment as FAILED
HONESTLY.

## The pre-declared reason to change NOTHING
If the candidate is inadmissible by construction (it would WIDEN the
bound, or the word already rides the candidate value), the word stays
absent or as-is; the lap still completes (measure, decide, no-change,
record) and says what held.

## What must not move after the bytes
The clauses above, the candidate, the question, and the trial count were
fixed before any new live request was sent. The only legitimate
after-the-bytes edit is a fact recorded wrong, corrected at bytes with
the correction named.

## The loop's own powers (bounded, disclosed)
- reads the charter (`config.json`), measures through the door (one
  mouthful a run), writes ONE key at the charter (`loop.apply_word`),
  re-measures, and may ROLL BACK by restoring the exact prior bytes;
- persists the lap's provenance through the EXISTING single write-path
  `research.hold` (the holding area; the root stays protected);
- no daemon, no new framework: one module, one entry function,
  replayable in tests from the preserved bytes with ZERO live calls.
