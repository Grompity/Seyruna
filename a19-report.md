# A19 — the word is said, and a failure says its own name (implementation; uncommitted)

Starting HEAD `fbdf227` (read at preflight — A18 found there, present and
uncommitted, as the § required); ending HEAD `fbdf227` — **no commit, no
staging, no deploy, no history touch, no `add -A`, no reset/stash/clean.**
No live request, no model call, no query generation, no CORAL change.

## Exact files changed

- **`stages.py`** — the door, two places + one comment: the fold branch
  now ALSO captures the lane-word (`fold_why = pkt["gaps"][0] if
  pkt["gaps"] else "empty"`, the phrase bytes UNMOVED); the status law's
  fold arm refit to pick between the house's emptiness phrase and the
  NEW failure word; the A15 statute's comment updated where it had
  claimed the failure was named (A15 named it only *inside* the phrase —
  A19 makes the claim literal).
- **`research_eval.py`** — one pure helper `status_word(rec)` (reads the
  RECORD: `door.evidence_status`; no door record says
  `no-door (search-only)`; a door record with no word — pre-A15 shape or
  the over-budget lane's sparse record — says `status-unspoken`; nothing
  ever leans toward verified), and the print line gains
  `"| status:", status_word(r),` before the seconds.
- **`tests.py`** — T159 CORRECTED (its `fail` expectation moved from the
  fold phrase to the new word — the change A15's own report named as the
  one-conditional awaiting this very milestone; and the message clause
  rewritten, which incidentally healed the grammar its own A15 repair
  passes had left). Two new witnesses: **T162, T163** at the tail (dry,
  canned, the net seam left raising past T163).
- The present report, untracked.

## The output format, before and after

**Before (human line):** `id | ok: … | results: n | gaps: […] | indep: …
| lane: … | calls: n | T.t s` — the status rode the JSON *record* (A18)
but the human line never selected it. **After:** the same fields, plus
`| status: <the record's word or its honest absence-word>` before the
seconds. **Serialization is byte-undisturbed** (`main`'s `json.dumps` of
the record unchanged — the print merely READS what A18 propagated); the
record itself grew no key this milestone. No consumer pins the print's
shape (nothing in tests or reviewer/ touches `main`).

## Emptiness versus failure, at bytes, from existing fields only

- A **successful empty search** keeps the house's fold phrase, byte-for-
  byte as A15/A16 left it: `the web brought nothing (search-empty)` (and
  the A13.4 compound around it, pinned intact).
- A search that **FAILED at a laned word** now rides its OWN word:
  `research failed (search-http-503)` — the reason VERBATIM from the
  packet's own `gaps[0]`, the word-class generic over every lane word
  (http-status, malformed, unreachable, timeout — all arrive here).
- The discriminator is the **laned word, never an empty results-list** —
  which every failed AND every empty search shares (the §'s trap, named
  and avoided).
- **Missing failure metadata** (`gaps` bare) rides the `(empty)` arm of
  the fold phrase — no failure invented where no reason rode.
- The general-road compound NESTS whichever content the arm chose:
  `general knowledge, not verified this turn (research failed (search-http-503))`.
- **No promotion:** neither the failed nor the empty turn grows a URL-
  bearing (web) row, so neither can reach DOCUMENTED by a promotion it
  never earned (asserted against the shown evidence); evidence
  classification and answer wording untouched — the mouth's input (the
  facts' fold phrase) rides its SAME bytes.

## Tests added and the exact suite result

**T162** (the selector, pure — four record shapes): a present word rides
verbatim; a door record whose key holds `None` and the sparse over-
budget record both say `status-unspoken`; a search-only record says
`no-door (search-only)`; no absence ever reads as verified. **T163**
(the door's words at the dry road): the emptiness word, the failure
word, their DISTINCTNESS asserted by the fixture's own eyes, the
missing-metadata arm, the nested compound, and the no-promotion
evidence-check. **T159**'s corrected `fail` leg now asserts
`research failed (search-http-503)` — the one pinned expectation the
spent coin obliged to move, disclosed.

**Full suite, exact: 163/163 — HARNESS GREEN** (first ride at the
splice; second ride at the closing battery; baseline entering A19 was
161/161).

## State at delivery

The seven founder-staged entries byte-exact and still staged (the index
untouched); `Seyruna/` (nested repo) and CORAL unmodified — this
milestone ran only file edits, test runs, and read-only git; the A8–A14
artifacts and both prior reports ride untracked as ever; the three
modified files carry UNSTAGED working-tree changes only. No historical
live-run artifact was rewritten — A16's C-case recorded
`the web brought nothing (search-malformed)` at its date and keeps those
bytes as history; the same run today would say `research failed
(search-malformed)`.

## Blockers and limitations

**No blocker.** Known limitations: the two absence-words are print-side
only (the record carries ABSENCE, not these words — a deliberate
display choice, never a verification lean); the compound's nested
parentheses read heavy but are byte-deterministic and pinned; the
A15 report's prose (which described the pre-A19 fold route) stands as
history, as all prior reports do. Unspent coins unchanged: the runner's
`query` body word, the print's `indep`-adjacent tuning, and a fresh
live eval run — the A13/A16 records remain the only live witnesses,
byte-unchanged, and status said is still not claims verified (same-
family review; `OPENAI_API_KEY` absent).
