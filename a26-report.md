# A26 — evidence caption comprehension test — the report

A26 asked what A25 could not answer: not whether the four distinctions CAN be
represented (they can, at recorded bytes — A25's PASS), but whether the A25
caption HELPS A READER understand what the evidence establishes. No human was
available to administer the instrument to, so per §5/§9 this run is scored
**INSTRUMENT-ONLY**: the instrument and rubric were validated with three
explicitly synthetic answer profiles, and the human-comprehension hypothesis
stands **NOT TESTED**. Nothing was invented in its place: no model answer is
counted as human data; the executor's readings are not entered as responses.
No live call was spent; no test was run; the Git index did not move; no file
older than A26 was touched. The frozen preregistration
(`a26-comprehension-preregistration.md`, sha256 `258154ffc713…7bfe`) was hashed
BEFORE the answer key and before any scored response.

## 1 What the reader actually receives (the two conditions, at bytes)

Condition A reproduces the EXISTING presentation: the answer's own words, the
record's own status words verbatim (`carried by: wikipedia.org (read)` at C1/C2;
`general knowledge, not verified this turn (the web brought nothing
(search-empty))` at C3/C4 — verbatim equal in the raw bytes), the record's own
corroboration words (`independence: none/unknown`, `conflict: insufficient`),
and the reviewer's recorded words (`CLEANS of absent signatures` /
`ABSENT SIGNATURES: …`, the per-sentence word COUNTS — never a row table,
never a kind-word). Condition B = A plus EXACTLY A25's caption strings
(extracted from `a25-caption-fixtures.json`, never retyped). The shared facts
are identical; the only difference is whether the presentation makes the
record's OWN kind-split (`page`/`snippet`, lane-notes, the stand-aside, the
reach-not-entailment tails) LAND for the reader.

## 2 Inputs pinned and re-verified

Sixteen inputs (A23 report; A24 results/comparison/report + the A24 adapter;
the A25 prototype/fixtures pair; A22 report/design/fixture/envelope + the four
raw turns; `shelf.jsonl`) all re-hashed at the END of the run: NONE changed
(`a26-results.json → hash_verification`; the A25 pair start-matched the A25
close-record `25a8020e…` / `02041f75…`; every full digest lives in
`a26-manifest.sha256`). Verbatim-containment checks passed: all six A25
captions appear byte-for-byte in the A25 fixtures file; all six claim-byte
strings appear in the A22 report; the C-line and ABSENT words appear in the
A24 records; A24's `BLOCKED: OPENAI_API_KEY absent…` word appears in the A24
results file.

Reviewer output vs presentation layer, as the key holds it: the compound
status words and the corroboration words are the RECORD's own bytes; the
C-line, per-sentence words, machine-findings and independence-BLOCKED word are
the REVIEWER's recorded output; A25's captions are the PRESENTATION layer — a
projection over the two, adding no new fact (A25's own ruling).

## 3 Preregistered design (one paragraph pointer)

Six dimensions (D1 kind-split, D2 match-is-not-proof, D3 absence-is-not-
disproof, D4 independence, D5 the aggregate trap, D6 the mapping's authorship);
eight neutral probes; three response statuses (`correct` / `misconception:
MCn` / `not-presentable`); the pair law (improvement = A-trap→B-correct;
regression reserved for A-correct→B-trap); profiles S1 careful / S2
conflationist / S3 absence-as-disproof, with the full expected matrix frozen
in the preregistration before the key; fixed A→B order, declared as a
deviation a human run must not repeat (counterbalance). Four-fixture limits
declared there: one provider, one fictional domain, one read row against four
snippets, n far too small for any inferential claim.

## 4 What the synthetic run showed (INSTRUMENT facts, not human facts)

`a26-results.json` carries the matrix verbatim. Headline: of 24 pairs,
**zero regressions**; five `A-trap→B-correct` cures; four `trap-persists-at-B`
(all the conflationist, by his rule — the caption SHOWS him the cure and he
underweights it, a declared instrument property, not a human finding); eight
`B-only-cures` where A could not speak at all (the mapping and A25's-words
probes); two `B-only-fires` for MC6 — A25's own words confusing a reader is
ONLY POSSIBLE at B, by nature. Per dimension: D1 detected at A (1) and cured
(1); D2 detected (1), persists (1); D3 detected (4), cured (3), persists (1);
D4 detected (2), cured (1), persists (1); D5 detected (2), cured (1),
persists (1); D6 detected at A (1), three B-side observations (the two MC6
fires + the MC7 persistence). No statistic is claimed (n=4 fixtures,
synthetic profiles). The fixture-by-fixture notes ride in the results file:
C1 is the aggregate-trap demonstration (fires exactly as preregistered); C2's
stand-aside cures the verdict question for all profiles; C3's phatic flag
cures the absence-reader; C4's `NEITHER` stands while the conflationist keeps
reading `BLOCKED` as corroboration — the persisted misconception the human
run must watch.

## 5 The required failure checks (the eight §7 modes)

1. `tokens-present` as semantic proof — DETECTED at A (Q-C1-PROVES); persists
   at B for the conflationist by rule. 2. `(read)` meaning every token came
   from the read page — DETECTED at A (Q-C1-KIND), CURED at B. 3. `token-absent`
   as disproof — DETECTED at A (C3 and C4), cured at B for the absence-reader,
   persists for the conflationist. 4. `token-free` as a failed claim —
   DETECTED at A (right- and wrong-direction instances), CURED at B (the
   STANDS-ASIDE/NEITHER words). 5. `unknown`/`BLOCKED` independence read as
   corroboration success — DETECTED at A, persists at B (by rule). 6. a
   presentation word read as a new reviewer status word — CANNOT fire at A
   (the words are absent there); fires at B by design — the detection IS the
   B-only fire. 7. the claim-to-row mapping assumed auto-generated — DETECTED
   at A, persists at B for the conflationist. 8. A25's own terminology causing
   confusion — **INDETERMINATE-BY-SYNTHETIC**: the profiles accept their own
   words by construction; only humans can exhibit it. No new ambiguity was
   found in the caption that A25 had not already recorded — and two
   presentation-layer wobbles were PRESERVED, not fixed: A25's C4 caption
   attributes `'web brought no search this turn'` to A23 while a grep of
   `a23-report.md` finds ZERO hits (the phrase's real home is the A22 design),
   and A25's C2 claim-8 caption spells `(Delhi, Buddha)` where A24's recorded
   sig bytes carry the mouth's own morph `Buddha`.

## 6 Human results

`NOT TESTED`. Participants: 0; completed responses: n/a; no raw anonymous
responses file exists (nothing to separate from identity). No consent question
was raised because nobody sat down. `PASS` is therefore NOT claimed: per §9,
PASS needs actual human data, and this run's status is exactly `INSTRUMENT-ONLY`.

## 7 Interpretations and open questions (kept apart from facts above)

(1) The instrument is VALIDATED in the preregistered sense: every testable
misconception MC1–MC7 fires somewhere, the two conditions are distinguishable
on every recorded fact, and nothing regressed. (2) What it does NOT show:
that humans will cure the conflationist's persisting tags — the matrix shows
only that B hands them the cure. (3) If A25's extra words themselves confuse
a human (MC8), §9's FAIL clause stays reserved — synthetic life cannot
exhibit it. (4) The founder's coin decision (and any A24-listed extension)
remains unmade and unforced; A26 neither recommends coining nor weighs the
extensions. (5) Proposed follow-up: the founder administers the frozen
instrument to at least one consenting human reader (counterbalanced order,
never the same case back-to-back); if the human shows the A-trap→B-correct
pattern on D1 without regression, A27 may weigh coining.

## 8 End-state confirmation

All sixteen input files byte-identical at close (none changed). `HEAD`
`1c7a74c`, branch `main`; the seven founder-owned staged entries column-2
clean and byte-for-byte; A22's two work files still exactly ` M`; the
untracked field gained EXACTLY six A26 names (preregistration, instrument,
key, results, this report, manifest) and nothing else. A26 ran no tests
(read-only), so A24's close battery — 166/16 pass, HARNESS GREEN — still
stands with no code moved. Nested repositories (`Seyruna/`, `Paper Website/`)
and CORAL untouched. The manifest cannot hash itself, the same self-digest
absence A25 noted for its own pair.

## 9 Where A26 stops

A26 stops. A27 is not begun; A25's captions were not revised; the reviewer's
rules were not changed; the prototype was not integrated into production.
