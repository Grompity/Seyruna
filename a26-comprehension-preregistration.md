# A26 — the comprehension preregistration (frozen BEFORE the answer key and any scored response)

A26 tests A25's presentation experiment's next question: does the evidence-kind
caption help a READER understand what the evidence does and does not
establish. This file freezes the dimensions, the probes, the accepted
criteria, the rubric, the synthetic profiles and their EXPECTED outcomes,
the order policy, and the decision law — all before any key is written and
before any response is scored. No A22–A25 file was touched, no live request
spent, the Git index unmoved (HEAD `1c7a74c`, `main`; the seven staged
entries and A22's two ` M` work files byte-verified at the open).

**Participants: none exist for this run.** No human was administered the
instrument (the A-series has never run one), so per §5 this run is an
**instrument validation only** and the human-comprehension result is
**NOT TESTED**. No model answer is counted as human data; the executor's
own readings are not entered as responses.

## The six dimensions (preregistered)

- **D1 evidence-kind** — fetched/read content vs snippet-only content.
- **D2 token-match vs semantic support** — a token match is a trace of
  reach, never a proof that a source ENTAILS the claim.
- **D3 absence vs disproof** — `token-absent`/`token-free` is not evidence
  against a claim (C3's phatic flag and C2's stand-aside are the probes).
- **D4 independence** — `independence: unknown` (record-side) and
  `BLOCKED` (reviewer-side, key absent) are NOT corroboration.
- **D5 the aggregate trap** — a technically true aggregate word
  (`carried by: wikipedia.org (read)` + `CLEANS of absent signatures` +
  `tokens-present`) can hide which KIND of row carried the DECISIVE token.
- **D6 the claim mapping** — the claim-to-row bridge is A23's recorded
  HUMAN mapping (re-derived byte-for-byte by A24's run), not reviewer output.

## The instrument — eight neutral probes (locked wording)

Conditions per fixture: **A** = exactly what the existing aggregate
presentation shows (the answer's bytes, the record's verbatim status/lane
words, the reviewer's recorded per-case and per-sentence words — NO row
table); **B** = the same shared context plus A25's EXACT caption string
(from `a25-caption-fixtures.json`, extracted not retyped). Same questions,
same factual key in both; only the presentation differs.

- **Q-C1-KIND (D1, D5):** For the answer's count (fourteen inscriptions):
  WHICH kind of source's bytes carried it — a read web page's full text, a
  search result's short words, both, or is this not said?
  ACCEPTED: B: `SNIPPET (W5); the read window showed no such byte`.
  A: `not said` (the truthful A answer). TRAP: `the read page` — an
  inference the shown words do not support.
- **Q-C1-PROVES (D2, D5):** Does anything shown PROVE the web page
  establishes the count? ACCEPTED: `no — the shown words speak of bytes
  REACHING the mouth; whether the page MEANS the count is not weighed here`
  (A: the careful `the shown words do not say` is accepted too).
  TRAP: `yes, it is proved`.
- **Q-C2-VERDICT (D3):** On the claim "the presented records describe form
  and number and say nothing of dhamma" — did the token-law PASS it, FAIL
  it, or DECLINE to speak of it? ACCEPTED: `DECLINE (token-free — the
  stand-aside; neither pass nor fail)`; at A, `a stand-aside word sits
  among the shown words but is not attached to this claim` is accepted as
  the honest A reading. TRAP: `FAIL` (and, preregistered, the conflationist
  `PASS` is scored as the same word-as-verdict error, wrong direction).
- **Q-C2-WHO (D6, tag-extension MC6):** Who checked that the word `dhamma`
  rides NONE of the record's row bytes — the frozen token-law, a human
  byte-scan, or is this not said? ACCEPTED: B: `the human byte-scan (A23,
  marked so)`; A: `not said`. TRAP: `the token-law did it`.
- **Q-C3-MARKED (D3):** The law flagged the greeting's two proper forms
  `ABSENT SIGNATURES`. Is the greeting therefore WRONG? ACCEPTED: `no —
  the flag marks bytes NOT PRESENT; and for a phatic word the flag can be
  NO MARK AT ALL`. TRAP: `wrong / refuted`.
- **Q-C4-ESTABLISHED (D4):** Has this turn's answer been ESTABLISHED
  (corroborated) by the bytes, REFUTED by them, or NEITHER? ACCEPTED:
  `NEITHER — insufficient by its own bytes (no row given; record-side
  independence unknown + conflict insufficient; reviewer-side BLOCKED)`.
  TRAPS: `corroborated` (MC5) and `refuted` (MC3).
- **Q-SHARED-MAP (D6):** The bridge claim-to-row — a reviewer output of the
  frozen token-law, or a RECORDED HUMAN mapping (A23) that A24's ride
  re-derived at the machine's own words? ACCEPTED: `the recorded human
  mapping`. A: `not said` (not-presentable — counted, not a trap). TRAP:
  `the token-law minted it` (MC7).
- **Q-SHARED-WORDS (D6, MC6):** The second presentation displays the words
  READ-WINDOW and SNIPPET — are those the law's FOURTH and FIFTH words?
  ACCEPTED: `no — presentation words standing over the bytes' OWN
  kind-words (page/snippet); the law's words are exactly three`. A: the
  words are not shown (not-presentable). TRAP: `yes` (MC6).

## The rubric (preregistered)

Each (fixture-probe, condition, profile) response gets ONE status:
`correct` (matches the fact key; the accepted A-forms listed above included)
/ `not-presentable` (the fact is genuinely not in the condition's material —
recorded, never counted as a trap) / `misconception:MCn` (one of the
preregistered tags below). Pair law (the SAME fixture-probe, A then B):
**improvement** = A fired a preregistered trap and B is correct;
**regression** = A correct and B fires a NEW misconception (named, caused by
the caption's own words); **inconclusive** = everything else.
Per-dimension tallies are PRIMARY; a combined average is reported but
hides nothing. **No statistical significance is claimed** (n=4 fixtures,
3 synthetic profiles).

The preregistered misconception tags, per the failure list A26 must test:
MC1 `tokens-present` read as semantic proof; MC2 `(read)` read as EVERY
token from the read page; MC3 `token-absent` read as disproof;
MC4 `token-free` read as a failed claim (wrong-direction word-as-verdict
included); MC5 `unknown`/`BLOCKED` independence read as corroboration;
MC6 a presentation-layer word read as a NEW law word (or a human fact read
as machine output — the tag-extension at Q-C2-WHO, declared here);
MC7 the claim mapping assumed auto-generated; MC8 A25's own words causing
confusion (preregistered INDETERMINATE-BY-SYNTHETIC: the profiles accept
defined words by construction; only humans can exhibit MC8).

## The synthetic profiles and their LOCKED expectations

(Synthetic answer PROFILES — not participants, not human data.)
- **S1 the careful reader** — answers only from what is shown; no inferences;
  a missing fact yields `not said`; expected to fire NO trap anywhere.
- **S2 the token/truth conflationist** — reads every status/law word as a
  verdict about the subject's truth; reports shown kind-words correctly but
  UNDERWEIGHTS the humility tail and the stand-aside words; reads A25's
  words as law words.
- **S3 the absence-as-disproof reader** — reads `absent` as disproof and
  `token-free` as a failed claim, unless the shown words themselves negate
  it (A25's C3 caption and C2 caption say so verbatim — and by construction
  S3 reads them).

Locked expected outcomes (so the KEY, written after this file, cannot bend
the expectations):

| probe | A/S1 | A/S2 | A/S3 | B/S1 | B/S2 | B/S3 |
|---|---|---|---|---|---|---|
| Q-C1-KIND | not-said | **MC2** | not-said | correct | correct | correct |
| Q-C1-PROVES | correct | **MC1** | correct | correct | **MC1 persists** | correct |
| Q-C2-VERDICT | accepted-A | **MC4 (wrong direction)** | **MC4** | correct | correct | correct |
| Q-C2-WHO | not-said | not-said | not-said | correct | **MC6** | correct |
| Q-C3-MARKED | correct | **MC3** | **MC3** | correct | **MC3 persists** | correct |
| Q-C4-ESTABLISHED | correct | **MC5** | **MC3** | correct | **MC5 persists** | correct |
| Q-SHARED-MAP | not-said | **MC7** | not-said | correct | **MC7 persists** | correct |
| Q-SHARED-WORDS | not-shown | not-shown | not-shown | correct | **MC6** | correct |

Order policy (preregistered): fixed A→B per fixture for the synthetic run;
the profiles are stateless between fixtures; a future human run must
counterbalance (recorded as a deviation of the synthetic run). The shared
factual context (claim bytes + the verbatim record/lane/corroboration/reviewer
words) is IDENTICAL in both conditions — the ONLY difference is A25's caption,
so a fair test never hands B facts A lacks.

## The decision law and the four-fixture limitations

Statuses: PASS needs real human data (it is NOT claimed here); PARTIAL /
FAIL as A26's §9 words; **INSTRUMENT-ONLY** is this run's shape: the
instrument and rubric are validated against synthetic profiles, the human
hypothesis stays untested. The instrument is validated iff EVERY preregistered
tag MC1..MC7 FIRES somewhere in the matrix and MC8 is reported
indeterminate-by-synthetic. Limitations, declared: 4 fixtures (1 provider
`ddg-ia`, 1 fictional-history domain, exactly 1 read row and 4 snippet rows);
the synthetic matrix shows the caption CREATES the OPPORTUNITY for cure,
not cure itself; per the brief, no usability claim is made at all.
