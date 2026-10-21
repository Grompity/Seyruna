# A24 — comparison: the frozen reviewer's words vs A23's manual nine-claim audit

Both sides are bytes. A23's table rides `a23-report.md` Phase 2 (its row
bytes byte-checked there). The machine's words ride the A24 ride
(`a24-review-results.json` → `pass`), produced by `review.pass_eval` over
`research-hold/a24-review-input.json` — the A22 envelope's four case blocks
under one renamed list-key, the case blocks themselves re-asserted
byte-equal to the raw files at run time. No artifact was edited; no code was
changed; the run made zero network calls.

## 1 — The pass, at the instrument's own status words

```
C1 | 5 sentences | CLEANS of absent signatures   (3 sentences tokens-present, 2 token-free)
C2 | 6 sentences | CLEANS of absent signatures   (3 sentences tokens-present, 3 token-free)
C3 | 1 sentence  | ABSENT SIGNATURES: e:Hello, e:Zzzyx
C4 | 7 sentences | ABSENT SIGNATURES: e:Ashoka's, n:1   (2 sentences token-absent, 5 token-free)
```

This re-derives A23's manual re-speaking exactly — every count, every
token, every row, every kind-word — with two A24-pinned clarifications:
first, the per-token evidence the hand-table quoted (`14@W5(snippet)`,
`232@W1(page)`, `Minor@W5(snippet)`, `Buddha/Delhi@W4(snippet)`) is what
`check` returns per token — **all of** a token's row-hits, so a mixed-kind
sentence (identity forms on the read page, the count on a snippet) arrives
as an evidence LIST, not a sentence-level kind; second, the C-line word
`CLEANS of absent signatures` is the instrument's **aggregate** word ("no
signature found absent from the given rows"), and it is KIND-BLIND — it
would print the same word for a sentence whose every token rode the read
page. The kind truth lives one level down, in the per-token evidence
entries. (The module's own print idiom is the same two words —
"CLEAN of absent signatures", review.py:164 — its `main` prints the
per-question status lines the same way.)

## 2 — The five categories, mapped at the instrument's own words

| A23 category | can the machine speak it? | at which of its words |
|---|---|---|
| readable-window support | YES, per token | `@W1(page)` entries (`232@W1(page)`, `268@W1(page)`; `Ashoka@W1(page)` among its hits) |
| snippet-only support | YES, per token | the sole-hit pattern `14@W5(snippet)`; `Delhi/Buddha@W4(snippet)` |
| insufficient-for-this-turn | YES, humbly, per sentence | `token-absent` — at C4 the words `e:Ashoka's` and `n:1` (the subject itself and a folded phatic "one") are exactly the claim "this signature rides no byte the mouth was given" |
| record-verified meta-claims | STANDS ASIDE | C2's meta sentence ("the records … describe the edicts' form and number … none quote …") has NO signature: 0 numbers, 0 proper forms — `token-free`. A23's byte-scan (no `dhamma` in any of the five rows' bytes) is out of the machine's reach: it matches tokens INTO rows, not absence FROM rows |
| vacuous / phatic claims | FLAGS, then over-flags | C3's greeting raises `ABSENT SIGNATURES: e:Hello, e:Zzzyx` — `Hello` is not in the 26-word stop-list, so a NON-claim gets flagged; and C2's phatic `One snippet…` folds to the CLAIM-signature `n:1` (the house's PINNED number-fold, T142), whose byte then matched vacuously inside snippet URL bytes (`…k7=1`) |

## 3 — The nine claims, claim by claim

1. **"fourteen separate inscriptions" (C1) — A23: snippet.** Machine:
   evidence `14@W5(snippet)` ALONE (no page byte saw the count at this
   sentence). AGREEMENT at token level; at the sentence aggregate the word
   `CLEANS of absent signatures` says NOTHING about which kind saw it.
2. **"carved into in-situ rocks" (C1) — A23: snippet.** Machine: the
   proper-form token `Rock` (the mouth's `Major Rock Edicts`) matches
   case-insensitively — and so also matched the SNIPPET bytes
   `carved on in-situ rocks` at W4/W5 (`Rock@W4/W5(snippet)`; no page hit).
   AGREEMENT at token level — with the substring-law vacuity disclosed:
   the match CANNOT TELL WHICH occurrence of `rock` it found, proper-form
   or lowercase.
3. **attribution + Mauryan span (C1) — A23: readable window.** Machine:
   `Ashoka/Edicts/Emperor@W1(page)`, `Empire/Mauryan@W1(page)`; the date
   sentence `232@W1(page)`, `268@W1(page)`. AGREEMENT — the strongest case;
   where A23 found read bytes, the machine's first-or-only hit is the
   `page` row, W1.
4. **"earliest dated … preceded by the Minor Rock Edicts" (C1) — A23:
   snippet.** Machine: `Minor@W5(snippet)` (sole hit); `Rock@W4/W5(snippet)`
   (again no page hit); the identity/`Indian` tokens also hit `@W1(page)`.
   AGREEMENT on the decisive tokens; the sentence aggregate is again
   kind-blind — a naive "tokens present!" reading of such a sentence hides
   that its news-carrying tokens (`Minor`, `Rock`) sit only on
   never-fetched rows.
5. **"more than thirty inscriptions…" (C1) — A23: readable window.**
   Machine: `token-free` — the clause carries no reviewable token: `thirty`
   is NOT in the fold-table, which stops at `twenty` (`ORD` at `tenth`).
   THE MACHINE CANNOT SEE THIS CLAIM AT ALL, and its silence here happens
   to fall on the side where A23's bytes sat — agreement by silence, NOT by
   instrument.
6. **the record-describes-its-own-absence meta-claim (C2) — A23: the record
   itself.** Machine: `token-free` (see §2 row 4). Agreement by silence;
   the meta-claim needs an ANTI-JOIN (the word `dhamma` matched in NO row),
   which the instrument was never built to speak.
7. **the count sentence (C2) — A23: mixed readable+snippet.** Machine:
   `14@W5(snippet)` alone for the count; `Ashoka/Empire/Mauryan`
   dual-hitting `page`+snippets. AGREEMENT at token level; the MIX is
   visible only in the evidence list, never in the aggregate word.
8. **"One snippet … Delhi edicts … a one-line summary" (C2) — A23:
   snippet, self-labelled.** Machine: `Delhi@W4(snippet)`,
   `Buddha@W4(snippet)` (the quote's own row), plus the vacuous `n:1` fold
   riding snippet URL bytes (never W1, so no page byte claims it).
   AGREEMENT, with the known fold vacuity disclosed.
9. **the whole dhamma-content answer (C4) — A23: insufficient this turn.**
   Machine: 2 `token-absent` (`e:Ashoka's` at the answer's own head
   sentence; `n:1` at `One edict urges…` — again the phatic `one` fold,
   here UNMATCHED, rows=`[]`) + 5 `token-free`. AGREEMENT in the humble
   direction: `token-absent` here is the instrument's own restatement of
   "no byte the mouth was given carries the subject." But note its
   AMBIGUITY: `token-absent` does not say WHY — at C4 it would read
   identically at a turn WITH rows whose bytes merely lacked the token.
   The WHY (`web brought nothing`) is the door-record's lane word, NOT the
   reviewer's. That distinction is not a reviewer defect — it is the
   boundary of the one thing it was built to weigh.

## 4 — Where a token-match can falsely READ LIKE entailment (and where it doesn't even reach)

- **False entailment looks.** The date sentence (`268–232 BCE`) is
  `tokens-present` on `@W1(page)` — support possible, yes, and the
  attribution itself rides a different sentence, so the machine never
  claims the two halves of the mouth's claim as one. The C1/C2 count
  sentences: `tokens-present` with the count token `14` SNIPPET-ONLY — the
  aggregate word hides which kind saw what. C2's Delhi sentence: the
  phatic `1`-fold matches URL bytes (`…k7=1`) — a match no human would call
  support of a count. C1's earliest-dated sentence: the aggregate word
  alone cannot show that its news tokens (`Minor`, `Rock`) rode
  NEVER-FETCHED rows.
- **Reach limits (no verdict either way).** The `c.` circa token, the
  mouth's welds (`set of` ← window `collection of` + W5 `14`), the
  meta-claim about the record, the phatic vs numeric `one`, and `thirty`
  itself — none of these are reviewable tokens. Every judgement about them
  stays **operator-weighed** (the module's own docstring: support is
  POSSIBLE at most; the operator weighs entailment; the machine does not).
- **Two A24-pinned boundary details.** The apostrophe rides INSIDE an
  entity token (`Ashoka's` matched as one form), so at C4 the absent word
  `e:Ashoka's` is vacuously strict — the strict form could not have matched
  bare `Ashoka` bytes either; moot at C4 (rows empty), disclosed. And the
  case-insensitive substring law (claim 2 above) means a proper-form token
  also matches lowercase bytes — the token-law cannot distinguish WHICH
  occurrence it found.

## 5 — Agreement tally

AGREEMENT at token level: claims 1, 2, 3, 4, 7, 8, 9 (seven of nine) — at
the machine's own tokens, rows, kinds — plus C3's and C4's absence words
and the sentence-status counts re-deriving A23's figures exactly.
AGREEMENT BY SILENCE (`token-free`; no token to weigh): claims 5 and 6 —
where A23's bytes-quotes and byte-scans stand alone.
CONFLICT: none. The instrument never contradicted a hand claim; it
under-spoke two of nine — as its design promises.

## 6 — Three pinned findings (all disclosed; nothing changed)

1. **The number fold stops at twenty / ordinals at tenth.** The one claim
   A23 located in the READ WINDOW (claim 5) has signature `thirty`, OUTSIDE
   the fold-table; the instrument reads the sentence `token-free` and
   cannot caption it. A fold extension is a one-line, T142-shape-testable
   change (`thirty` would fold to `30`) — it would make the caption speak
   MORE of the sentence, not change the verdict, since the read-window
   truth came from the bytes anyway. NOT applied: no code change was
   authorized; it rides as the founder's later coin with the caption.
   (A23's Phase 1 had already recorded the fold's reach; A24 supplies the
   consequence for claim 5.)
2. **`Hello` is no stop-cap.** The 26-word STOP_CAPS holds the usual
   sentence-starters but no greeting; C3's phatic greeting therefore raises
   a per-sentence `ABSENT SIGNATURES: e:Hello, e:Zzzyx` over a claim that
   asserts NOTHING. A23 disclosed the vacuity; A24 pins the REASON at code
   — disclosure, not defect.
3. **A possessive morph rides inside the entity token** (`e:Ashoka's` at
   C4 vs `e:Ashoka` at C1/C2 — the same name, two different token
   identities), so a possessive claim-token is strictly WEAKER at matching
   than its bare form. A24-pinned at bytes.

(Recollection correction, disclosed at the ride: the A-series prose
elsewhere names the protocol's commit as `9c352bd` — itself A12's commit;
at bytes the commit
that touched `review.py` AND `review-protocol.json` is `b3a7ecf` (A6) —
what `a24-review-results.json` records; A23's report rides untouched.)
