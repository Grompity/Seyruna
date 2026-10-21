# A27 — human-comprehension pilot for the A25 evidence captions — the report

A27 continues from the verified A26 checkpoint (`INSTRUMENT-ONLY`) to answer the one
question the synthetic matrix could not settle: whether a **real reader** interprets A25's
evidence captions more accurately than the comparison condition. The objective is to determine
that — **not to prove the captions work.**

## 1 Verified repository state and preservation checks (on the open of A27)

- Branch `main`, HEAD `1c7a74c` — **matches** the expected checkpoint.
- The seven founder-owned staged entries (`gpt-reviewer.md`, `opencode.json`, the two
  `research-hold/live-run-*.jsonl`, the three `reviewer/*.py`) are present in the index and
  byte-identical at the open (index blobs captured before any change; `opencode.json` remains
  `MM`, i.e. staged + the founder's own further worktree edit, exactly as found).
- A22's two work files `research_eval.py` and `tests.py` remain exactly ` M` (unstaged),
  byte-identical at the open (`684803d4…` / `f4ccb2a6…`).
- The A22–A26 artifacts are present and untouched; nothing older than A27 was written.
- Nested repositories `Seyruna/` and `Paper Website/` are present and untouched. CORAL is a
  separate project, out of scope.
- The pinned reviewer/protocol was not modified; no `git add -A`, broad staging, reset, clean,
  stash, history rewrite, commit, or deploy was run. **The Git index did not move.**

## 2 A26 manifest-verification result (mechanical, via the standard library)

`a26-manifest.sha256` was re-verified with `hashlib` (the standard library — the existing local
tooling): **all 21 recorded entries (16 inputs + 5 A26 artifacts) match their recorded digests;
0 mismatches, 0 missing.** This includes the instrument file itself, which hashes
`2f8e0fe7…88580` exactly as recorded. The manifest cannot hash itself (noted by A26; restated).

## 3 Preregistered follow-up criteria (read from the actual files, not rewritten)

The preregistration (`258154ff…7bfe`), instrument (`2f8e0fe7…88580`), and answer key
(`aa2e94e0…176a1`) were read in full and verified. The follow-up criterion is A26 §7.5: *the founder
administers the frozen instrument to at least one consenting human reader (counterbalanced order,
never the same case back-to-back); if the human shows the A-trap→B-correct pattern on D1 without
regression, A27 may weigh coining.* That criterion, its rubric, the conditions, and the captions
were **not** rewritten by A27.

## 4 Administration gate — real human participant

**A real human participant is available to the founder:** YES / NO *(answered below — see §4.1).*

The participant procedure is prepared and ready in `a27-administration-guide.md` (voluntary, stop
anytime; independent interpretation without coaching; no coaching before answers are recorded; the
answer key held back until completion; order counterbalanced as far as n=1 allows; the same case
never back-to-back; verbatim answers; scoring per the frozen key; record every clarification,
interruption, and deviation). Only minimum information is collected; anonymous participant IDs;
no names/contact/sensitive/demographic data. **No institutional ethics approval, formal research
oversight, or consent procedure is claimed** — this is a small exploratory usability pilot, not a
representative study.

### 4.1 Gate outcome and what actually happened

- If a real consenting reader sat down and answered, their **actual** answers are in
  `a27-administration-record.json` and scored in `a27-results.json` against the frozen key.
- If no reader was available at this sitting, **no administration occurred**, no response row
  was filled, no consent event was recorded, and the status stands at
  **`AWAITING FOUNDER ADMINISTRATION`**. Nothing was invented, simulated, AI-generated, or inferred
  to make the milestone look complete.

## 5 Participants and results (kept separate: criteria / responses / scoring / observations / interpretation)

- **Exact number of real participants:** see §4.1 (0 at the open; +1 per real administration).
- **Complete / incomplete administrations:** see §4.1.
- **Response pattern per probe:** see `a27-results.json → response_pattern_per_probe`.
- **Preregistered D1 A-trap→B-correct pattern, without regression:** see
  `a27-results.json → d1_a_trap_to_b_correct_pattern_occurred`. *(With n=1 a favorable reading is
  reported as an observation, not a validated pattern; the D1 criterion is a weak signal on one
  reader. Note honestly that the criterion **cannot fire** on form A→form B when form A is correctly
  read as `not-presentable` (S1's reading); it only exists when form A actually fires a trap — so an
  honest A-score on a single reader makes the D1 criterion unassessable and the run a pilot.)*
- **Misconceptions persisted or new:** see `a27-results.json`.
- **Procedural deviations:** see `a27-results.json → procedural_deviations`.
- **Findings that remain indeterminate:** see `a27-results.json → findings_remain_indeterminate`.

No statistical significance is claimed from a single participant; no population-level effect is
generalized from a convenience pilot. An ambiguous answer stays ambiguous; a favorable result is
**not** permission to tune the instrument against that response and re-test for confirmation.

## 6 MC8 and terminology

MC8 asks whether A25's **own terminology** confuses real readers — the synthetic matrix cannot settle
it. Genuine participant misunderstandings are recorded in the reader's own words and classified as:
already covered by MC1–MC7; a genuinely new interpretation not in the frozen rubric; ambiguous; or an
apparent terminology problem not confidently attributable to the caption. A25 captions were **not**
revised within A27. A single correct answer does **not** establish that terminology is clear.

## 7 Limitations and deviations (carried + A27)

n = 1. A single reader cannot establish a pattern, cannot set a baseline, cannot be truly
counterbalanced (single recorded order), cannot support an inferential claim, and cannot establish
population-level effects. The A-series has no prior human administration; a single reader is a
convenience pilot. No instrument wording, rubric, criterion, or caption was changed.

## 8 Final A27 status

`AWAITING FOUNDER ADMINISTRATION` — materials are ready; no real administration has occurred as of
the open of A27 (see §4.1 for the outcome). *(A real administration, if it occurs, must record actual
responses before the status moves to `HUMAN-PILOT-PASS` / `MIXED`; a BLOCKED status is reserved for
a frozen instrument that cannot be administered or scored faithfully.)*

## 9 What A27 does and does not stop at

A27 does not advance to A28, revise captions, change reviewer rules, or integrate anything into
production. The narrowest justified next step (report §10) is reported and the milestone stops.

## 10 Narrowest justified next step

The **founder administers the prepared, frozen materials** to at least one real consenting reader
(and ideally more than one) and the actual responses are scored against the frozen key. The milestone
does not proceed on its own; it does not recommend coining; it does not touch the reviewer. If the
founder has no real participant, the gate stays `AWAITING FOUNDER ADMINISTRATION` and no human data is
claimed.

## 11 End-state confirmation

All A22–A26 artifacts byte-for-byte unchanged (`a26-manifest.sha256` mechanical re-verification: 21/21
match, 0 mismatches); the seven staged entries column-2 clean and byte-for-byte at the close; A22's two
work files still exactly ` M`; `HEAD` `1c7a74c`, branch `main`; the Git index unmoved; nested repos
(`Seyruna/`, `Paper Website/`) and CORAL untouched; the pinned reviewer/protocol unchanged; the
untracked field gained exactly the five A27 names (guide, record, results, report, manifest) and nothing
else. Existing local batteries re-run without the funnel: integrity 18/18, retrieval/content-blindness
exit 0; frozen harness 166/166, HARNESS GREEN — no code moved.
