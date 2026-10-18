# A1 — Conversational Research Agent Foundation — Report (2026-10-18)

## 1. Diagnosis of the existing experience (verified in code, not documentation)
The live surface is one door and one element: `POST /ask {question, facts}`
(`server.py` and `api/ask.py`, same spine) → `stages.run_pipeline(live=True)`
→ `{response, why, trace}`; the browser element `ascended-chat.js` keeps the
turns in sessionStorage and carried, at most, **ONE prior exchange** folded
into the FACTS channel (a 160-char deterministic digest). The pipeline itself
is deterministic stages with the model confined to named seams
(`stages.call`, retries ≤3 with an error lane); the shelf retrieves by
word-overshoot; `self_gate` answers greetings/phatics with ZERO mouths; the
general lane (the "RESPONSE ≠ RETRIEVAL" round) lets the mouth answer
shelf-silent questions as UNSOURCED; `research.py` is a bounded WORKER (task
in, artifact out, four statuses all passes, `hold()` the single write-path,
the url lane honestly gapped: **no web access exists — network is
not-designated**). `tests.py` is the frozen stage set (custom harness, T-
numbered witnesses, prints `N/M pass — HARNESS GREEN|RED`).

The friction, concretely: a third turn forgot the first two; every non-browser
client had to re-invent the digest; there was no task at all — research.run
takes a hand-built dict and has no lifecycle, no progress line, no resume;
two doors were drifting apart (400-lane already differed); and the model's
ignorance/tool-failure answers were excellent — that part needed no change.

## 2. The working improvement (one coherent increment)
- **One door law** — `stages.door(body)`: `/task …` commands (zero mouths) →
  no-question ⇒ 400 with the reason → conversational lane. Both doors became
  transport (the route-check stayed where the route lives). `window` rides the
  door's late import; the one-way dependency is kept.
- **The carrying law** — `stages.digest(history)`: pure, bounded,
  deterministic; the browser's former byte-shape kept byte-for-byte
  (`Earlier - you asked '…', Ascended said '…' then ….`) so no spoken word
  moves; empty history ⇒ `''` ⇒ the first turn stays byte-identical to a
  one-question ask. Caps ride `rule_pack.json` params
  (`carry_turns: 3`, `carry_cap_msg: 160`) — letter C: the figures live in the
  rule-pack. The browser now sends its turns (`history`); an explicit `facts`
  still rides VERBATIM (the compatibility road never launders). The window is
  now ONE law's home — T95 was re-anchored to witness that (its law clauses —
  messy-facts ride whole, lane, provisional eye — kept verbatim; nothing
  weakened).
- **The runner** — `task.py` (kept SEPARATE from the conversation, per the
  mission): one record, one checkpoint file (`research-hold/task_state.json`,
  crash-safe tmp+replace), statuses OPEN/PAUSED (resumable) and
  DONE/BUDGET/STALLED/CANCELLED (terminal-for-the-run). A door-call runs ONE
  pass; `auto()` is the unattended foundation on the SAME pass function. The
  budget is an ACCUMULATOR (spent.secs sums pass-durations — an overnight
  pause costs nothing; a resume cannot un-spend) gated PRE-REQUEST with a
  one-mouth margin (a zero-seconds voyage coins nothing). The pass reuses
  `research.run` + the ONE joining mouthful (the dry law rides inside:
  one source never mouths to join); picks outside the founder's menu die
  noted (the cite-law's shape); an ambiguous request gets ONE coin, its
  repeat STALLS (the anti-reroll law); `start` refuses while afloat
  (ALREADY_COMPLETE, adopted). The report distinguishes completed from
  unresolved in words: *settled (sourced) / ours (synthesis, UNSOURCED by
  kind) / open (gaps, notes)* — "the open work rides the gaps and the notes,
  not the silence." The runner's pen is `research.hold` — the protected bytes
  answer it with a refusal (T115).
- Nothing new was installed: no framework, no registry, no bus, no second
  pipeline, no second door, no paid service, zero new dependencies.

## 3. Verification (exact, not estimated)
- `python3 tests.py`: **119/119 pass — HARNESS GREEN**, run TWICE back-to-back
  (the re-run law: the holding area is a pile, so witnesses that own a premise
  wipe it — `_a1f` — and riders `_a1` ride it; idempotency is now witnessed by
  the double-run). Baseline before A1: 109/109. The ten new witnesses
  (T106–T115) cover: the served lane's byte discipline, the cross-pass floor,
  the stall/anti-reroll lane, the afloat guard both ways, the pre-request
  budget gate (two lanes), pause-across-a-fresh-reader, the terminal word and
  the report's own last line, the zero-mouth door lane (the CALLS ledger
  standing as the instrument), the carrying law's exact bytes, and the
  protected-bytes scale re-weighed around a full voyage.
- The bridge's own battery (`reviewer/selftest.py`): **18/19** — the single
  red is its own stale premise, not an A1 regression: `reviewer_git_log(n:3)`
  wants the string "baseline" in the last three commits, and the user's own
  three pre-A1 commits (0d2a975, 8e19c9d, c2cd76f…) had already buried
  `f5479ec baseline:` to position −7. Their file, their staged work — left
  red, named here.
- Root batteries: integrity **18/18**; retrieval green (gaps named, not
  patched — pre-existing, documented).
- Live demonstration (BOUNDED: 4 request-attempts, 42 s wall):
  lane 1 — one door-call, shelf-silent question, general lane, the carried
  exchange REACHED the mouth (the trace's `context_size: 104` is the byte
  proof), and the mouth's answer was honest general speech (2 model_calls:
  one transient at the seam consumed stages.call's own bounded retry —
  recovery already lives at the seam, no new machinery).
  lane 2 — a real voyage over two REAL designated docs (spine.md,
  mvp_proposal.md): the plan mouth picked both by id, the evidence passed on
  file fetches, ONE joining mouthful, `status=DONE passed=1 calls=2`, report
  written (`research-hold/task-LIVE1-done.json`, `task_state.json` —
  committed as evidence).
- Transport proof: `server.py 5178` + one curl `{"question":"/task inspect"}`
  returned the status line (`task LIVE1 status=DONE …`) with `lane:"task"`
  and zero mouths spent — the command rides the bytes, not the model.
- Protected set: `constitution.md`/`foundation.md`/`golden-set.md` match the
  authoritative prefixes (af3117a6ca / d7724cb793 / be650831cf — the same
  bytes CORAL pins); `shelf.jsonl` and the tests-file protected list rode
  unharmed (T115); `rule_pack.json` gained exactly the two carrying figures;
  `tests.py` gained witnesses (T95 re-anchored in place; nothing removed).

## 4. Phase 5 — CORAL inspected, unmoved
This repo holds no CORAL integration code (grep found none to change); the
integration IS the sibling lab (`../ascended-coral-p1/loop`): it already
evaluates proposals in isolated candidate trees under its frozen law, pins
these very documents (its `_PROT`/protected-doc hashes), and O1/O2 accepted
two changes end-to-end. The A1 loop shape maps exactly onto it (propose
→ isolated evaluation → best-verified version preserved → inspect → next
proposal). Constraints honored: no promotion to main automatic, no touch to
constitution/foundation/evaluator/safety pins, no unrestricted autonomous run
launched here.

## 5. Remaining capability gaps (named, not patched)
- **No web access** (the honest one): the url lane gaps (`network-not-
  designated`). Cheapest viable path when wanted: a designated fetcher at the
  door level (stdlib `urllib` fetch + a founder-listed domain allowlist) —
  one function, no dependency; NOT added here because nothing demanded a
  remote source yet.
- The **menu is founder-handed** (designations are not yet DISCOVERED):
  "identify information gaps → reach for them" rides a hand menu; a shelf-
  query designation (`stages.retrieve` as the search tool, free and present)
  is the natural next step — the plumbing (drop-notes, stall law) already
  handles a wider designator without new law.
- **One afloat task** (no queue) and **pause at the pass boundary** (no
  threads) — stated limits, both honored by the checkpoint's truth.
- The browser's rendering of a `/task` answer rides the verbatim-speech law
  (no UI change was needed); the UI itself was exercised at the transport,
  not re-clicked in a browser this session.
- The bridge battery's stale `n:3` premise (user's staged file; left red,
  one number away).

## 6. Recommended next step toward hours of independent work
Give the runner its hours in the ONE shape the architecture already blessed:
`task.auto()` driven by a founder-handed menu whose designations come from
`stages.retrieve` (the free search), capped exactly as the live demo was
(`max_passes`/`max_calls`/`max_secs` as an accumulator, margin gate before
each pass). Concretely next: a second live voyage whose plan mouth is allowed
a SHELF-QUERY lane (designate-by-retrieval), then the same shape under
CORAL's acceptance — Ascended proposes, the lab says which one rode, nothing
promotes itself.
