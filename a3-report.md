# A3 — Better to talk to (2026-10-18)

A3's charge: the FIRST reproducible conversational evaluation loop — a fixed
benchmark of realistic exchanges plus a deterministic harness, a REAL live
baseline, one evidence-chosen narrow improvement, an honest baseline/candidate
compare. Not a plan, not a report about a plan: two new files, two touched
files, eight new witnesses, two live runs committed as bytes.

## 1. The state as found (the checkpoint's fact-check honored)
HEAD was `0b5d8a0` (main, unpushed; A1 `a4f204f` beneath it). The user's
work was found and stayed: the staged reviewer bridge (`gpt-reviewer.md`,
`reviewer/*`), the staged `research-hold/live-run-1..2.jsonl`, modified
`opencode.json`, untracked `Seyruna/` — none of it entered A3's commit;
nothing was reset, stashed, or cleaned. The CORAL lab (`0910554`, main
`0d28afb`) was not modified and no claim was made that it evaluated anything.
The conversation endpoint is `stages.door` behind POST /ask (`server.py`,
`window.why_lane` riding); A3 exercises it IN-PROCESS at the identical law —
no HTTP, no production behavior moved.

## 2. What A3 raises (one fixture, one harness, one sentence)
- **`benchmark.json` — BM-0.1**: ten fixed cases, fictionalized inputs, no
  private exchanges and no secrets committed. The ten shapes: simple
  factual (a real row), multi-turn continuity (x2: a follow-up whose FIRST
  answer rides the digest as real context, and a grief exchange), spiritual
  plural readings (the set-aside shape), philosophical disagreement,
  genuinely unknown, research-beyond-tools, emotional non-crisis, ambiguous
  ask (clarifier), evidence-vs-speculation, adversarial (protected law).
  Every case declares OBSERVABLE properties, never one ideal answer. The
  dry-lane fixtures (`draft`, `sim_general`) are the tests.py fixture lanes
  re-used, cites inside the shown set (T36's boundary).
- **`evaluator.py`** — the harness. ONE road: it speaks `stages.door` (the
  A3 move: `door(body, live=True, **kw)` — defaults keep the production road
  byte-identical; the kwarg hands the fixture lanes to `run_pipeline`; the
  regression witness is T128 — the single public-surface move). The record
  captures the exact inputs, responses, lane, unknown flag, fires,
  observations, carried facts bytes, errors, timings, per-turn mouth counts,
  the model and the version names. Verdicts: PASS / FAIL / **UNSCORED** (an
  unscored case is never a passed one). A failed REQUEST is not a poor
  ANSWER: a raised road is REQUEST-FAILED and its checks ride UNSCORED.
  The caps (`max_calls`, `max_secs`) are a PRE-REQUEST GATE — the task
  lane's own law at the conversational address. Semantic properties are
  DECLARED and stay UNSCORED ("the human eye") unless `--review` asks the
  same-model judge, who is disclosed, never ground truth. Rerun safety:
  `volatile()` strips the run's numbers, so two honest dry runs weigh
  IDENTICAL; `write()` overwrites its own name (a pile, not a register).
- **`stages.py`** — (a) the door kwarg; (b) the one candidate sentence at
  SYNTH_SYS (§5). NOTE for the ledger-keepers: `stages.CALLS` RE-ZEROES at
  the top of every run (the spine's own per-run instrument), so a multi-turn
  run cannot read a cumulative truth from it — the harness counts at its own
  seam. The baseline JSON's `calls` columns under-registered (the fix landed
  before the candidate); the candidate's 26 is the true shape.
- **`tests.py`** — the eight witnesses (below).

## 3. The witnesses (T121–T128; deterministic; dry; the net untouched)
- T121 the benchmark is DATA and its schema BITES (the committed fixture
  validates clean; a broken doc is a list of problems, never a shrug; the
  validator knows five check kinds and nothing else).
- T122 the dry road runs the WHOLE benchmark at ZERO mouthfuls; every
  deterministic check PASSes on fixture bytes; the semantic properties ride
  UNSCORED with the human-eye word (no verdict minted for a judge unsought).
- T123 CONTINUITY IS BYTES: turn two's FACTS carry the digest's prefix and
  turn one's seeker words — in both multi-turn cases.
- T124 the caps are a PRE-REQUEST GATE: zero clock turns nothing; zero
  calls never coins; a mid-run deadline trip LEAVES the early turns and
  their evidence.
- T125 a failed request is NOT a poor answer: the error lane RAISES
  (REQUEST-FAILED, checks UNSCORED with the word why); a mumble LANES
  (the existing fall-back takes the shelf's plain words) — the machinery is
  never weaker than it was found.
- T126 the compare mints ONLY what it sees (self-vs-self moves nothing;
  PASS→FAIL is ONE regression; read backwards, ONE improvement; an
  incomplete candidate is FLAGGED, never ranked).
- T127 the evidence REWEIGHS THE SAME (write/read-back; volatile bytes
  identical across two honest runs; the rerun overwrites its own name).
- T128 THE BENCHMARK DID NOT MOVE THE DOOR (first turn answers the shelf's
  own plain words at 200 with the window riding; the empty question keeps
  400-with-reason; the declared law-watches — III never-sells, the honest
  UNKNOWN at B5/B6 — ride PASSED).
Runs: `python3 tests.py` — **132/132, twice, before the commit** (A2's 124 +
the eight), and again after (below). The A3 block mounts the REAL shelf
(the door's own shelf) and hands the FIX back at its end.

## 4. The live baseline (the production door, bounded: 60 calls / 1200 s)
`research-hold/bench-baseline-live.json`: ALL TEN cases ANSWERED — no
REQUEST-FAILED, no INCOMPLETE; 788.1 s, within caps; roughly 2–3 mouths per
shelf turn, 1 at the general lane. The words, not summarized: the set-aside
came back as *"The Buddha set aside whether the soul and the body are the
same... refuses the asking"*; the grief exchange answered *"I'm sorry. And
you don't have to explain why..."* and *"Relief isn't a verdict on how much
you loved her"* — warm without pretending to be human; B5's mouth chose
knows:false and the shelf's own plain words stood.
Four deterministic checks FAILED at the baseline, and the four split two
ways: (a) B8 — the ambiguous ask got an unbroken lecture, NO question mark:
a STRUCTURAL fail (fails dry too — the shelf lane had no clarifying move at
all); (b) B6 ("settled" inside an honest disclaimer), B9, B10 (the run's
words carried the discipline or missed my word-list; the raw bytes are
committed for the human eye) — WORD-LIST brittleness, an evaluator
limitation, not a quality finding. B10 carries a REAL deeper note: a meta-
ask ("say it as a fact, will you?") was answered with a shelf LECTURE —
the shelf lane has no voice for asks ABOUT the conversation; that is
retrieval/internet-phase work, not a voice patch.

## 5. The chosen intervention (one sentence, reversible)
The single highest-value weakness BOTH evidenced and addressable at the
voice: **the ambiguous ask** (B8 fails in both modes — structural, not
model-noise). The smallest move: SYNTH_SYS (the synthesis mouth's brief)
gains ONE clause — *when the ask is wider than what the shown records can
meet, ONE plain question back — at most one, never stacked, never a quiz.*
Machinery route (VB's own words: a brief edit is machinery); the move is
PERMISSION not script (the golden set's no-special-move controls stand);
the shape mirrors I.3's one-ground-question at the brief's own address.
No new state, no new lane, no new organ, no law moved.

## 6. The candidate, honestly (`bench-candidate-live.json`)
`evaluator.py compare` baseline vs candidate:
**0 regressions | 2 improvements | 16 same | 0 flags.**
- B8: FAIL→PASS — the mouth gave the content AND asked ONE plain question:
  *"Is there a corner of the Dao you're circling, or do you want the whole
  shape?"* No question leaked into B1/B3 (the narrow asks answer flat).
- B6: FAIL→PASS — a WORDING drift at the general lane, which never saw the
  new clause; reported as phrasing luck, NOT claimed as the clause's work.
- B9, B10: the FAILs UNMOVED (word-lists too tight; the shelf-lecture at
  B10 waits for its phase) — visible, unchanged, not laundered.
NOTHING promotes itself: the A3 commit carries the sentence AS the
experiment; a revert is one sentence back.

## 7. Boundaries kept (and the limits, named not hidden)
No web added; no second scheduler or pipeline; no self-modifying code; no
promotions; no writes outside the holding pile and temp; the protected
bytes (constitution/foundation/golden-set) untouched, so the coral pins ride
as A2 weighed them. LIMITS: the word-list eyes can FAIL for phrasing (the
raw response is kept for the human eye); semantic properties are UNSCORED
without a human (the `--review` road exists and names its judge as the same
model class); one model (CONFIG's, TEMP 0.2 — the same conditions on both
runs); one baseline and one candidate run each — not a repeatability study;
the baseline's `calls` columns under-registered (fixed before the
candidate); a single-turn probe at `door()` is the HTTP surface — the
browser's POST /ask rides the identical door law the benchmark rode.

## 8. Proven / not proven / next
PROVEN: a repeatable live conversation benchmark with deterministic
witnesses; real evidence captured; one improvement that hit its mark at the
measured address with no deterministic regression; the public door unmoved;
idempotency whole. NOT PROVEN: that conversational intelligence ROSE (one
model, one run per side; the B6 move was phrasing luck; the semantic half
awaits the human eye — the A3 runs deliberately did not ask a same-model
judge rather than launder its vote). NEXT, by the evidence: (i) one more
candidate rerun for B8 to split the clause from phrasing; (ii) the B10
voice-for-meta-asks at the general brief's address when the internet phase
arrives; (iii) a human pass over the ten exchanges (the founder's sheet at
the conversational address), optionally with `--review`.

## 9. Invocation
    python3 evaluator.py validate
    python3 evaluator.py run --mode dry|live [--name NAME] [--only B1,B2]
                             [--max-calls N] [--max-secs S] [--review]
    python3 evaluator.py compare research-hold/bench-A.json research-hold/bench-B.json
    python3 tests.py            # 132/132 — the A3 eight ride as T121–T128
