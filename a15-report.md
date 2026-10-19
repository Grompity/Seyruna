# A15 — Surface the Evidence Status, Preserve the Question (implemented)

Milestone status: implemented and verified; no commit, no staging, no
deploy. The slice's bytes were found ALREADY IN THE WORKING TREE (unstaged,
carrying explicit `A15` marks — the door's `fold` memory, the
`evidence_status` law, the `body.get("query") or q` search lane, the
`"query"` trace stamp, the shown-record line, and the two new tests). This
pass verified them against the A14 design and the A15 brief, ran the suite,
and delivers this report — the same verify-and-report stance the milestone's
own rules require.

## Files changed, and why (all UNSTAGED, as found)

- `stages.py` — the door's web branch only. (a) accepts an optional
  `body["query"]` and rides it to `web_research.research` alone
  (`body.get("query") or q`); (b) remembers the fold's phrase in `fold` so
  the status law can speak it (the fold still rides the facts byte-for-byte
  as before); (c) chooses the turn's `evidence_status` word by
  deterministic law from the turn's OWN already-computed fields (the
  packet's rows, A7's corroboration words, the fold's phrase, the general
  road's OWN `lineage: UNSOURCED` stamp) — no model call, no new mouth;
  (d) stamps `trace["web"]["query"]` from the packet's own recorded query,
  so the word ACTUALLY USED is inspectable, not assumed.
- `web_research.py` — UNTOUCHED (verified: `research`/`reads` already return
  `{"query": <string sent>, …}`, which is what makes the trace-word honest
  at no cost).
- `window.py` — ONE added line: the shown record carries
  `evidence_status` beside `lane`/`relevance`/`evidence` (A14's "DISPLAY,
  not prose, and not a mouth" at bytes).
- `tests.py` — two added tests, T159 (the six status shapes + determinism +
  identical response bytes) and T160 (the query/question separation with
  recording spies). No network: canned packets are canned.

## Evidence status: before vs after

BEFORE: the truth was computed and stopped at the trace and the table
(A14 findings 4-6) — A13.4's live turn printed a flat, confident 726-char
telling that had read nothing.
AFTER: a deterministic word rides BESIDE the answer (trace + shown record;
the answer's bytes never touched — no refusal-by-design):
- read origins: `carried by: <publisher(s)> (read)` — carriers, not a
  warrant that every claim rode them (no claim-level over-claiming);
- all fetches failed: `research inconclusive (fetches failed)` (a failed
  fetch is never silent-success);
- provider index-words only: `provider words only; no origin read`
  (A7's attribution law, at last DISPLAYED);
- empty fold: the house's own phrase shown rather than hidden —
  `the web brought nothing (search-empty)`, and a FAILED search carries
  its own lane-word inside the parentheses (`search-http-503`), so failure
  and emptiness are distinguishable at the word;
- the A13.4 shape (fold + the general road's own stamp):
  `general knowledge, not verified this turn (…)`;
- no research asked: `research not asked`;
- belt when the fields cannot classify the packet:
  `no origin read (rows unweighed)` — the word stays plain rather than
  guessing (A14's rule honored).
Read origins are named by PUBLISHER (via the existing `publisher` law), so
same-publisher snippets never count as separate carriers at this line.

## Query separation (what landed, what deferred)

Landed: the door accepts an optional `query`; absent ⇒ today's road is
byte-identical (the spy sees the question; the trace records the question
AS the used query — the fallback is inspectable, not assumed); present ⇒
the search rides the query while the pipeline seam RECEIVES THE QUESTION
UNTOUCHED. No name-core heuristic was needed or added; query GENERATION
stays the caller's (or a later model coin's). Deferred by design: the
deterministic name-core generator, the provider's sentence-tolerance probe
(the five-word form), and a second-family name ride.

## Tests and actual results

T1..T158 rode unchanged and green. T159 and T160 added (the seven mandated
cases: plain-road byte-identity; query-does-not-overwrite-question; empty
⇒ correct status word; failed fetches not success-shaped; attribution-only
never presented as read; a read source reported without claiming every
claim verified; determinism with byte-identical answer text).
Actual run: `python3 -B tests.py` ⇒ **160/160 pass — HARNESS GREEN**
(exit 0). Deterministic facts and live answer-quality records were kept
apart: nothing here claims the real-world lane works; the A13 live records
remain that evidence.

## Known limitations / follow-ups

The word is turn-level, not claim-level (claim-to-window truth remains
human-review territory, A14's Design C cases 4 and 6's second half). The
word may be ignored by readers — promoting it INTO the mouth's sentence is
tuning, deliberately not taken. A status that rides the record may not
reach every mouth (the speech itself still never says it — by design).
Follow-ups, unspent coins: the name-core generator; the five-word
tolerance probe; whether a second real family rides green; whether to
nudge the mouth to speak the word.

## State at delivery (verified, not assumed)

HEAD `9c352bd` unchanged (A15 moved no commits). The founder's seven staged
entries byte-intact and still staged (`gpt-reviewer.md`, `opencode.json`,
`research-hold/live-run-1.jsonl`, `research-hold/live-run-2.jsonl`,
`reviewer/reviewer_ask.py`, `reviewer/reviewer_mcp.py`,
`reviewer/selftest.py`); unstaged set exactly the three A15 files;
`Seyruna/`, `CORAL` (`coral.py`), every A-era report and `research-hold/`
record unmoved. No `git add -A` was spent anywhere; this report is the
only file this pass created. The nested `Paper Website` repo moved on its
own account (its release commit `6400ee2` lives in the inner repo, invisible
to this one). Path-limited staging only, whenever a commit is authorized.
