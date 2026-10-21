# A27 — administration guide — the frozen A26 comprehension instrument

_Generated from the frozen instrument (`a26-comprehension-instrument.json`, sha256 `2f8e0fe7fba5…88580`; frozen preregistration sha256 `258154ff…7bfe`); condition materials below are byte-exact extracts from it — not retyped. The answer key (`a26-answer-key.md`, sha256 `aa2e94e0…176a1`) is held back from the participant until after every answer is recorded. No instrument wording, rubric, criterion, or caption was changed by this guide; it only makes the frozen instrument administrable by a real reader._

## 0 What this is, and what it is not
A small **exploratory usability pilot**. It is **not** a representative scientific study, and it has **no institutional ethics approval, formal research oversight, or consent procedure** — none is claimed. With **n = 1** reader, no population effect can be established. A real consenting reader is required; their actual, verbatim answers are the data. No simulated, AI-generated, or inferred answers may stand as participant data.

## 1 Participation and consent
- Participation is **voluntary** and the reader may **stop at any time**, for any reason, with no penalty.
- Consent here is simply a recorded "yes" from the reader, at the moment they sit down, before any material is shown. It is not a signed form and no formal consent procedure is claimed.
- The reader interprets the material **independently, without coaching**. The administrator does not explain the intended distinction, the dimensions, or what a "correct" reading is before the answers are recorded.
- The administrator does **not** reveal the answer key before completion.
- The reader's answers are recorded **verbatim, in their own words** — lightly transcribed only for spelling, never paraphrased.

## 2 What the reader sees
There are four cases (**C1, C2, C3, C4**). Each case is shown in **two forms**: form **A** (the existing presentation) and form **B** (the same facts plus the A25 caption). The facts shown are identical between the two forms; only the A25 caption differs. The reader answers each question **about the form currently on screen**.
The reader is **not** told which form is which, which is "intended," or that the difference is a caption.

### Reader packet — presentation order
_Counterbalanced as far as one reader allows: each case is shown twice (once as form A, once as form B) but never the same case twice in a row, so no case is answered twice in a row from the same form and no form dominates a single case. With one reader the order is fixed below and is recorded as a limitation — true counterbalancing needs more than one reader, and the A-pass-before-B-pass shape is itself a limitation against the preregistered order policy (which the synthetic run already declared as a deviation for humans to fix)._

- **Reading order:** C3-formA, C1-formA, C4-formA, C2-formA, C2-formB, C1-formB, C4-formB, C3-formB  (no case repeated back-to-back).

### Reader packet — materials (byte-exact from the frozen instrument)
_Present these blocks in the order above. Show each block with its label. Do not explain the labels._

**Case C1** — the deliberately misleading aggregate: present/CLEAN words over a count whose ONLY byte rode a SNIPPET

*Form A:*
```json
{
  "the_answer_words_verbatim_A25_claim_bytes": [
    "\"fourteen separate inscriptions\" (C1)",
    "\"attributed to Emperor Ashoka of the Mauryan Empire (r. c. 268–232 BCE)\" (C1)"
  ],
  "door_evidence_status_verbatim": "carried by: wikipedia.org (read)",
  "gaps_verbatim": [],
  "the_records_own_corroboration_words_verbatim": {
    "independence": "none",
    "conflict": "insufficient"
  },
  "reviewer_recorded_C_line_word": "CLEANS of absent signatures",
  "reviewer_machine_findings_verbatim": [],
  "reviewer_per_sentence_status_words_verbatim": {
    "token-free": 2,
    "tokens-present": 3
  }
}
```

*Form B (A adds exactly — A25's exact caption strings):*
```json
[
  "C1 · claim 1 — token 14 seen ONLY in SNIPPET words at W5 (kind snippet; lane 'not-fetched:dup-publisher'); the READ window (W1, kind page) saw no such byte. The machine's words here (tokens-present, CLEANS) speak that the BYTES REACHED the mouth — NOT that any row ENTAILS the count.",
  "C1 · claim 3 — tokens Ashoka/Mauryan/Empire/268/232 seen in the READ window's OWN bytes at W1 (kind page; note 'http 200 (capped)'). A token match is the POSSIBILITY of support, not the PROOF of it — entailment stays the reader's (A23's J-flag open)."
]
```

*Why C1 is shown both forms:* A23's claim units vs the machine's sentence units: the house splitter cut the mouth's one sentence into 5 bytes (A24 verbatim), so the caption spans two sentences — the claim-to-bytes mapping is A23's/A24's RECORDED hand mapping, disclosed

**Case C2** — the token-free case: the mouth's claim ABOUT THE RECORD — absence of a token, not absence of support

*Form A:*
```json
{
  "the_answer_words_verbatim_A25_claim_bytes": [
    "\"the records … describe the edicts' form and number … none quote what they say about dhamma\" (C2)",
    "\"One snippet … 'a series of edicts on the teachings of Buddha' … a one-line summary\" (C2)"
  ],
  "door_evidence_status_verbatim": "carried by: wikipedia.org (read)",
  "gaps_verbatim": [],
  "the_records_own_corroboration_words_verbatim": {
    "independence": "none",
    "conflict": "insufficient"
  },
  "reviewer_recorded_C_line_word": "CLEANS of absent signatures",
  "reviewer_machine_findings_verbatim": [],
  "reviewer_per_sentence_status_words_verbatim": {
    "token-free": 3,
    "tokens-present": 3
  }
}
```

*Form B (A adds exactly — A25's exact caption strings):*
```json
[
  "C2 · claim 6 — the machine STANDS ASIDE: token-free (the claim carries NO reviewable token), which is NEITHER pass NOR fail. The claim speaks ABOUT the RECORD, and A23's byte-scan (a human reading, marked so) found the word 'dhamma' in NONE of the five rows' bytes. The claim-about-the-record is thus VERIFIED BY BYTES, NOT by the token-law.",
  "C2 · claim 8 — the quote's tokens (Delhi, Buddha) seen ONLY in the SNIPPET W4 (kind snippet; lane 'not-fetched:dup-publisher'), never in the READ window — AND the mouth's OWN words already named the kind ('One snippet…'). The token-law adds the KIND-WORD to what the mouth said; it weighs the REACH, never the truth."
]
```

*Why C2 is shown both forms:* two different 'absences' now ride near each other — token-free (no token exists) vs the byte-scan's absence (a word looked for and NOT found in every row) — the caption labels which is which

**Case C3** — the vacuous case: an absence-flag over a NON-claim — absence must not be read as disproof

*Form A:*
```json
{
  "the_answer_words_verbatim_A25_claim_bytes": [
    "door.response verbatim: \"Hello, Zzzyx plingworth.\" (A22 raw C3)"
  ],
  "door_evidence_status_verbatim": "general knowledge, not verified this turn (the web brought nothing (search-empty))",
  "gaps_verbatim": [
    "search-empty"
  ],
  "the_records_own_corroboration_words_verbatim": {
    "independence": "unknown",
    "conflict": "insufficient"
  },
  "reviewer_recorded_C_line_word": "ABSENT SIGNATURES: e:Hello, e:Zzzyx",
  "reviewer_machine_findings_verbatim": [
    "e:Hello",
    "e:Zzzyx"
  ]
}
```

*Form B (A adds exactly — A25's exact caption strings):*
```json
[
  "C3 — the greeting asserts NOTHING, yet the law flags its two proper forms: token-absent (e:Hello, e:Zzzyx) over NO BYTES GIVEN (rows [], the record's own word 'the web brought nothing'). Absence of a byte is NOT a mark against the claim — for a phatic word it can be NO MARK AT ALL (a disclosed vacuity of the instrument: 'Hello' is no stop-cap, A24 pinned)."
]
```

*Why C3 is shown both forms:* one short word now carries a DOUBLE absence — the greeting's (a non-claim; possibly no mark at all) and the turn's (no bytes) — the caption's own words separate them, at the cost of length

**Case C4** — the insufficient-and-blocked case: zero rows, the mouth's OWN denial, and TWO independence words saying not-established

*Form A:*
```json
{
  "the_answer_words_verbatim_A25_claim_bytes": [
    "the whole dhamma-content answer (C4); door.response verbatim opener: \"No record stands behind this; I speak from general knowledge.\""
  ],
  "door_evidence_status_verbatim": "general knowledge, not verified this turn (the web brought nothing (search-empty))",
  "gaps_verbatim": [
    "search-empty"
  ],
  "the_records_own_corroboration_words_verbatim": {
    "independence": "unknown",
    "conflict": "insufficient"
  },
  "reviewer_recorded_C_line_word": "ABSENT SIGNATURES: e:Ashoka's, n:1",
  "reviewer_machine_findings_verbatim": [
    "e:Ashoka's",
    "n:1"
  ]
}
```

*Form B (A adds exactly — A25's exact caption strings):*
```json
[
  "C4 · claim 9 — this turn INSUFFICIENT BY ITS OWN BYTES: no row was given (the record: 'web brought no search this turn' — A23's words — and gaps ['search-empty']); the mouth OPENED by saying 'No record stands behind this; I speak from general knowledge'; the machine weighed NOTHING (5 token-free) and flagged 2 token-absent (e:Ashoka's — a possessive form; n:1 — the folded phatic 'one'). The corroboration's OWN words: independence unknown, conflict insufficient. The reviewer-side independence: BLOCKED (DESIGNED, not proven). NOTHING here is verified, and NOTHING is contradicted."
]
```

*Why C4 is shown both forms:* TWO independence words could read as ONE; the caption must keep them APART (record-side unknown vs reviewer-side BLOCKED), and A19's own law ('unknown unless two independent publishers read'; one-origin 'insufficient') supplies their meaning

### Reader packet — questions
_Ask each applicable question about the form currently shown. Record the reader's answer verbatim. Ask it once for form A (while A is on screen) and once for form B (while B is on screen). The reader does not know the forms differ in the caption._

- **Q-C1-KIND** (shown at C1): For the answer's count (fourteen inscriptions): WHICH kind of source's bytes carried it - a read web page's full text, a search result's short words, both, or is this not said?
- **Q-C1-PROVES** (shown at C1): Does anything shown PROVE the web page establishes the count (the claim settled by what is shown)?
- **Q-C2-VERDICT** (shown at C2): On the claim 'the presented records describe form and number and say nothing of dhamma' - did the token-law PASS it, FAIL it, or DECLINE to speak of it?
- **Q-C2-WHO** (shown at C2): Who checked that the word dhamma rides NONE of the record's row bytes - the frozen token-law, a human byte-scan, or is this not said?
- **Q-C3-MARKED** (shown at C3): The law flagged the greeting's two proper forms ABSENT SIGNATURES. Is the greeting therefore WRONG?
- **Q-C4-ESTABLISHED** (shown at C4): Has this turn's answer been ESTABLISHED (corroborated) by the bytes, REFUTED by them, or NEITHER?
- **Q-SHARED-MAP** (shown at C1): The bridge claim-to-row - a reviewer output of the frozen token-law, or a RECORDED HUMAN mapping (A23) that A24's ride re-derived at the machine's own words?
- **Q-SHARED-WORDS** (shown at C1): The second presentation displays the words READ-WINDOW and SNIPPET - are those the law's FOURTH and FIFTH words?

---
_Administrator-only from here down: the scoring key. Do not show it, and do not reveal it, before every answer is recorded._

## 3 Scoring sheet — follow the frozen answer key (sha256 `aa2e94e0…176a1`); scored condition-appropriately
Statuses (frozen rubric): `correct` / `not-presentable` (the fact is genuinely not in that form's shown words — recorded, never a trap) / `misconception:MCn` / `ambiguous` (the answer does not match the key under the frozen rubric — record it ambiguous; do not bend the rule after seeing the answer). A reader's wrong answer is an **observation, not a failure of the reader**; a favorable reading is **not** permission to tune the instrument and re-test for independent confirmation.

Per-question scoring (from the frozen instrument; A-accepted forms included):

| question | form A accepted | form B accepted | preregistered trap |
|---|---|---|---|
| Q-C1-KIND | not said | SNIPPET (W5); the read window (W1) saw no such byte | the read page (MC2) |
| Q-C1-PROVES | the shown words do not say (accepted) | no - the shown words speak of bytes REACHING the mouth; whether the page MEANS the count is not weighed here | yes, it is proved (MC1) |
| Q-C2-VERDICT | a stand-aside word sits among the shown words but is not attached to this claim | DECLINE (token-free - the stand-aside; neither pass nor fail) | FAIL (MC4); the conflationist's PASS is the same word-as-verdict error, wrong direction |
| Q-C2-WHO | not said | the human byte-scan (A23, marked so) | the token-law did it (tag-extension MC6) |
| Q-C3-MARKED | no - absence of bytes is no mark of error | no - the flag marks bytes NOT PRESENT; for a phatic word the flag can be NO MARK AT ALL | wrong / refuted (MC3) |
| Q-C4-ESTABLISHED | NEITHER (the compound word and the record's own words say so) | NEITHER - insufficient by its own bytes (no row given; record-side independence unknown + conflict insufficient; reviewer-side BLOCKED) | corroborated (MC5); refuted (MC3) |
| Q-SHARED-MAP | not said (not-presentable) | the recorded human mapping | the token-law minted it (MC7) |
| Q-SHARED-WORDS | the words are not shown (not-presentable) | no - presentation words standing over the bytes' OWN kind-words (page/snippet); the law's words are exactly three | yes (MC6) |

**The preregistered follow-up criterion (from A26 §7.5):** if the reader shows the **D1 `A-trap→B-correct` pattern** (form A fires a preregistered trap, form B correct) **without a regression** (A-correct→B-new-trap), A27 may *weigh* coining. Note honestly: this criterion **cannot fire** on form A→form B when form A is correctly read as `not-presentable` (S1's reading); it only exists when form A actually **fires a trap**. With one reader this is a **weak, single-instance signal**, not a validated pattern; report whether it occurred, do not claim it as established. The two conditions must be **fair** (the shared facts are identical) — scoring form A as a mere "not-presentable" is the honest reading, not a trap the reader failed.

**Per-reader recording fields (minimum necessary, anonymised):** anonymous reader id; consent moment (yes/stopped); per-presentation verbatim answer + its scoring status; administrator observations (clarifications, interruptions, deviations, the reader's own words where they confuse them); time-to-answer if noted. **No names, no contact info, no sensitive personal data, no unrelated demographics.**

## 4 Data-collection, privacy, and limits
- Use **anonymous reader ids** (`P1`, …). Record only the minimum needed to reproduce the scoring.
- **No institutional ethics approval, formal oversight, or consent procedure is claimed.** This is an exploratory pilot; n=1 cannot establish a population effect.
- Record **every** clarification, interruption, or deviation. A partial administration stays partial; never fill a gap with a guessed answer.
- Scoring **must** follow the frozen answer key and criteria; do not change a rule after seeing the answer.

## 5 Presentation order (as scheduled above)
| # | case | form | questions asked while shown |
|---|---|---|---|
| 1 | C3 | A | Q-C3-MARKED |
| 2 | C1 | A | Q-C1-KIND, Q-C1-PROVES, Q-SHARED-MAP, Q-SHARED-WORDS |
| 3 | C4 | A | Q-C4-ESTABLISHED |
| 4 | C2 | A | Q-C2-VERDICT, Q-C2-WHO |
| 5 | C2 | B | Q-C2-VERDICT, Q-C2-WHO |
| 6 | C1 | B | Q-C1-KIND, Q-C1-PROVES, Q-SHARED-MAP, Q-SHARED-WORDS |
| 7 | C4 | B | Q-C4-ESTABLISHED |
| 8 | C3 | B | Q-C3-MARKED |

The reader sees the four questions above each time a case is shown (each question is answered about the form on screen at that moment). Each case appears once in the A pass and once in the B pass; the same case is never back-to-back. The reader answers each question **twice** — once about form A, once about form B — recorded with its condition label, scoring form A condition-appropriately. The reader never knows the two forms differ by the caption. Scoring happens only after all answers are recorded.

## 6 Record of what happened at the open of A27 (before administration)
- Branch `main`, HEAD `1c7a74c`; the seven founder-owned staged entries byte-for-byte at the open; A22's `research_eval.py` (`684803d4…`) and `tests.py` (`f4ccb2a6…`) still exactly ` M`; opencode.json `c49743e1…` worktree (staged blob `c4cf2505…`, `MM`).
- A26 manifest **mechanically re-verified**: all 21 entries (16 inputs + 5 A26 artifacts) match their recorded digests; the instrument file itself hashes `2f8e0fe7…88580` = its manifest entry.
- Existing local batteries re-run **without the funnel**: integrity **18/18**, retrieval/content-blindness **exit 0**; the frozen harness `tests.py` ran **166/166, HARNESS GREEN** — matching A24's close, **no code moved**.
- Nested repositories `Seyruna/`, `Paper Website/` present and untouched; CORAL out of scope.
- **Administration gate:** whether a real, consenting human reader is available to the founder is decided *before* administration and is reported in the final report. If one is available, the founder administers the frozen materials and the reader's **actual** answers are recorded verbatim in `a27-administration-record.json` and scored against the frozen key in `a27-results.json`. If none is available at this sitting, no real administration occurred, no response row is filled, and this milestone stands at **AWAITING FOUNDER ADMINISTRATION**. Nothing in this guide, record, or results file may be filled with an invented, simulated, AI-generated, or inferred human answer.

_Guide written from the frozen instrument only; no condition material, question, criterion, rubric, or caption was rewritten here. This file is new (an A27 artifact); it does not modify the pinned reviewer/protocol._
