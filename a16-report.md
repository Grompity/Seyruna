# A16 — the A15 slice met the real path (diagnostic; nothing changed)

Starting and final HEAD `9c352bd` (read, not assumed) — and the A15 diff
**still rides the working tree uncommitted** (three ` M` files, +179/-4,
never staged, never touched by this milestone). Founder state byte-for-
byte: seven staged entries, `opencode.json`, untracked `Seyruna/` and
every A8–A15 artifact, CORAL unmoved. The suite at the start AND at the
close, unchanged by a diagnostic: **160/160 — HARNESS GREEN.** No code,
no fixtures, no staging, no commit, no deploy.

## The caller-visibility question, answered at the bytes before any run

The door returns `{"response", "why", "trace"}, 200` (stages.py:964). The
status word rides TWO exposed places: `trace["evidence_status"]` and —
by A15's one-line window pass-through — `why["evidence_status"]`, the
SHOWN record. So an ordinary caller reading the returned record sees it
WITHOUT diving into internal trace data: no caller-visibility gap at the
door. The gap that DOES exist is at the eval runner's own projection:
`run_one`'s door-record picks `{code, lane, retrieval, response,
model_calls, web_stamped}` — it **drops** the status word (and A15's
`web["query"]` never even enters it, since the runner searches the
question itself and passes the door no `query`). The status is visible
where the door speaks; the supported runner just does not carry it
forward — reported, NOT patched, as commanded.

## Case A — the known-green word with the question kept separate (1 live turn, 0 retries, 72.6 s)

The door rode directly (disclosed deviation: `run_one` has no query
parameter — it pins query to the question — so A15's NEW field can only
be exercised at the door, the supported entry the tests drive). Question
`"What do Ashoka's rock edicts say about his rule and his dhamma?"`,
query `"Ashoka rock edict"`.

- **Transport/provider:** 200; 5 results; `fetched 2`; `gaps []`;
  `query-used "Ashoka rock edict"` recorded at the trace.
- **Evidence actually obtained:** one READ origin (`wikipedia.org`,
  row W1 DOCUMENTED/page) + four house stubs (W2–W5 snippet/
  duckduckgo.com; seen-bits: `bytes-not-read`, 3× `skipped:
  dup-publisher`); corroboration — `attribution 4`,
  `origin_publishers 1`, `independence: none`. One family read, four
  index-words from one provider. A13.2's shape, re-met.
- **Deterministic status:** `'carried by: wikipedia.org (read)'` —
  exactly the carrier-word A15 designed: names the read origin, claims
  no full sourcing.
- **Answer and provenance:** the mouth hedged honestly (quoted in the
  raw record): *"What I have here is related, not a full answer… so the
  shelf gives you the frame"* — then supplied frame-claims (Ashoka,
  ~268–232 BCE, fourteen Major Rock Edicts, carved in-situ).
  **Human fact-check owed, not token-presence:** whether the dates and
  the fourteen ride the READ passage or the shelf's memory — the answer
  itself says the shelf carried the frame, so part of this turn's speech
  is shelf-backed, not read-this-turn. (The status word speaks the
  WEB-evidence of the turn; shelf-carried claims sit outside its
  sentence — a named limitation, not a defect.)
- **Audit:** same-family model reading of its own system's bytes,
  disclosed; the human check above is the real one.

## Case B — the sentence's empty lane, the fallback query (1 live turn, 0 retries, 24.5 s)

The exact A13.4 sentence rode as question AND query (no `query` word —
the fallback path exercised, live):

- **Transport/provider:** search EMPTY, confirmed — the A13.1 law holds
  live, at the sentence's own bytes, at this HEAD, at the door's fallback
  query. No web stamp rode the trace (the fold's shape).
- **Evidence obtained:** none read; retrieval carried shelf rows `[19,
  2]` (A13.4's identical bytes); the speech was the GENERAL mouth's.
- **Deterministic status:** `'general knowledge, not verified this turn
  (the web brought nothing (search-empty))'` — the A13.4 compound word
  spoken exactly as A15 designed, at the real path, unforced.
- **Answer and provenance:** the sharpest witness the series has run:
  the bytes read SOURCED — duties listed (kindness, non-injury,
  obedience, generosity, restraint, fair treatment), the
  `dhamma-mahamatras` appointment, happiness "here and the world
  beyond" — confident, specific, and **nothing was read this turn**.
  Claims stated as if verified, at the §'s exact risk; they match bytes
  this system read in the A5 era (persisted shelf memory), which is
  memory, not verification — **human fact-check owed** for the duty-
  list and the mahamatras claim as facts of the record.
- **Audit:** same-family, disclosed; this answer's confidence-vs-
  unverified shape is precisely what the status word exists to puncture,
  and it now does, at the caller-visible record.

## Case C — failure versus emptiness at the existing harness (dry, ZERO model calls)

Ridden at the existing door-with-injected-seam idiom (the fixture is
test-side only; no tracked file touched; zero live requests). The
injected `URLError("refused")` at the seam bit inside `_get`'s own
tries-net — disclosed honestly, the lane-word that surfaced was
`search-malformed` (one of the FAILURE-class words, not the emptiness
word; the exact word depends on where an error bites `_get`/`search`).
The observed status: `'the web brought nothing (search-malformed)'` —
the failure word rides the fold's parentheses, distinguishable from
`(search-empty)`, on the deterministic dry path, with the general-road
compound correctly ABSENT (the dry road stamps no `lineage`). C's
thesis — a failed search is visible AS a failure, not laundered into an
emptiness — holds at the fold's shown word. The A15 report's named gap
stands confirmed (no separate `research failed (x)` word-class; a
one-conditional follow-up).

## Request-count ledger, whole milestone

**2 live door-turns (A, B); 0 retries spent (none needed); 5 mouth
calls (3+2); C: zero live calls.** One prior C attempt died at a
fixture TypeError (missing injected draft — the dry idiom's
requirement) BEFORE any model cost, and the re-run was dry: no live
call was lost to it. No retry storm, no fabricated witness, every
prediction above marked as observed-vs-designed.

## Confirmed, unresolved, recommended

**Confirmed:** the status reaches the ordinary caller via `why`; it
speaks the truth of the research performed in both live shapes (one
read origin named as a carrier; a general-knowledge turn named
UNVERIFIED with its emptiness inside); the fallback query rides
exactly today's road live; A13.1's lane-law held again at these bytes.

**Unresolved questions (none a defect):** the runner's projection
drops the status (whose fix is the founder's coin — one word at
`run_one`, unspent); shelf-carried claims sit outside the status
word's sentence (A16-A's answer named the shape); the exact failure
word at a true provider 5xx was not provoked (no artificial forcing,
per the §); a second family's name still awaits for a live
`candidate`.

**Recommendation — the single next step:** **commit the A15 slice**
(the three source files plus this diagnostic's report, the A12
two-file precedent) — the live path has now verified the words in both
shapes the system can actually produce; the design-risk A14 named is
spent. Follow-up coins, unfired: the runner's status word, the
`research failed (x)` one-conditional, and asking the mouth to speak
the word at its known tuning-risk.
