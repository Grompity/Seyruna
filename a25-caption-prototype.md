# A25 — the evidence-kind caption prototype (read-only; a PRESENTATION experiment, nothing implemented)

Start HEAD `1c7a74c`, end HEAD `1c7a74c`, branch `main` (read at the open and
the close, not assumed). The seven founder-staged entries rode byte-exact in
the index (status column-2 clean at both ends); `research_eval.py` and
`tests.py` rode the same ` M` as before (A22's work; A25 touched neither).
**A25 changed no code, no artifact, no index; spent no live request; touched
no nested repository (Seyruna/, Paper Website/); wrote exactly two new
untracked files.** The reviewer was NOT reridden — A24's report recorded the
ride and its A6-integrity echo (true); A25 prefers those recorded bytes,
re-reading only the A22 RAW bytes behind them (rows, lane-notes, door
status/lane words, corroboration words) plus `shelf.jsonl` for the carried
rows 19/2 — strictly read-only, the same bytes A24 rode.

## The input inventory (sha256, taken BEFORE any reading)

| file | sha256 (first 16) |
|---|---|
| a24-review-results.json | 58733b19350e363c |
| a24-review-comparison.md | 3e1458f1c5d7527 |
| a24-report.md | 8fc7ee3f630a6b26 |
| research-hold/a24-review-input.json | 6caf07249273f050 |
| a23-report.md | 465ac207c6b0e200 |
| a22-report.md | b94a3cc78f02ec0d |
| a22-eval-design.md | ddc2d631025364a9 |
| research-eval-a22.json | 2b522e31fc8113e2 |
| research-hold/a22-eval-live.json | 70f1e96105aaf1aa |
| research-hold/a22-raw-C1.json | 7b5063546527ca9c |
| research-hold/a22-raw-C2.json | 4f68c494da77ca8f |
| research-hold/a22-raw-C3.json | f0963be185e2211e |
| research-hold/a22-raw-C4.json | 8d658154c83abf8d |
| shelf.jsonl | 02669d548ac9f55c |

Full digests ride `a25-caption-fixtures.json`.

## The design — the caption's shape and its ONLY labels

One line per claim, four slots, in the reader's plain words:

```
<case> · <claim — the recorded bytes> — WHERE-slot — lane-notes verbatim — WHAT-slot (the humility words)
```

The WHERE-slot speaks the distinction the aggregate hides. Its labels come
ONLY from bytes that already exist — two are the rows' OWN kind-words, three
are A25's presentation words standing over recorded bytes, and they are
labelled as such:

| caption word | what bytes back it |
|---|---|
| `READ-WINDOW` (the brief's read/page) | the row's kind-word `page` verbatim (W1 only — at A22 exactly ONE row carries it) + A19's status word `carried by: wikipedia.org (read)` (the record's own words) |
| `SNIPPET` | the row's kind-word `snippet` verbatim (W2..W5) |
| `NOT-FETCHED` (the brief's not-fetched) | REPRESENTED in the bytes — as the LANE-NOTE verbatim `'not-fetched:dup-publisher'` (W3/W4/W5 — the never-fetched lane); W2's lane reads `'http 202'` with bytes that are only the words `Edicts of Ashoka Category` — A18's fetched-empty shape. NOT a kind-word: the kind is `snippet`; the lane NOTE carries the not-fetchedness |
| `TOKEN-ABSENT` | the machine's OWN word (T142 pins the three-word law) — at C3/C4 it fires over `rows=[]` |
| `TOKEN-FREE` | the machine's OWN word — the stand-aside; NOT evidence against |
| `NO BYTES GIVEN` | A25's presentation word for `web.rows=[]` at C3/C4, the record's lane words verbatim beside it: gaps `['search-empty']`; C3/C4 `door.evidence_status` verbatim: `general knowledge, not verified this turn (the web brought nothing (search-empty))` |
| `UNKNOWN` | A25's LAST word — used only where no recorded word speaks (below, at C4's carried-shelf relevance: the record's OWN words already speak it) |

The WHAT-slot carries the humility the § commands: **a token match is a
TRACE of reach, never a claim of entailment** — never plain
"verified"/"proven"/"fact-checked". (The frozen module's own docstring
already decreed it; A25 only shows it to the reader.)

The claim-to-bytes mapping is NOT invented here: it rides A23's Phase-2
nine-claim table (the recorded bytes of the claims) with A24 §3's byte-for-byte
re-verification of the tokens/rows/kinds. A25 projects; it adds no fact.

## The four fixtures (recorded bytes; the caption as the reader would see it)

### C1 — the deliberately misleading aggregate (mandatory example)

The aggregate today, verbatim: the reviewer's `CLEANS of absent signatures`
+ per-sentence `tokens-present`; A19's status word, all three homes:
`carried by: wikipedia.org (read)`. It reads like READ-BACKED — yet at A24's
recorded bytes the sentence's decisive token rode:

> **C1 · claim 1 — token 14 seen ONLY in SNIPPET words at W5 (kind snippet;
> lane 'not-fetched:dup-publisher'); the READ window (W1, kind page) saw no
> such byte. The machine's words here (tokens-present, CLEANS) speak that the
> BYTES REACHED the mouth — NOT that any row ENTAILS the count.**

The mandated read-window match rides the same case (nothing fabricated):

> **C1 · claim 3 — tokens Ashoka/Mauryan/Empire/268/232 seen in the READ
> window's OWN bytes at W1 (kind page; note 'http 200 (capped)' — the bytes
> END at 'from 268 BCE'; A23's flag: the mouth's 'c.' rides NO byte). A token
> match is the POSSIBILITY of support, not the PROOF of it — entailment
> stays the reader's.**

Prevents: the headline reading as wholly read-backed — the count byte lives
at a never-fetched snippit; `(read)` rides on the attribution, not the count.
New ambiguities, disclosed: (1) A23's claim-units vs the machine's
sentence-units differ (the house splitter cut the mouth's ONE sentence into
five bytes at the parenthesis — A24 verbatim — so one caption spans two
sentences); (2) the turn's own corroboration block (`read: 1`,
`independence: "none"`, one origin, `conflict: "insufficient"`) means the
`(read)` word names exactly ONE row and no second voice — the caption must
not whisper "corroborated".

### C2 — the token-free case: the mouth's claim ABOUT the record

The aggregate today: the same `CLEANS` and the same `carried by:
wikipedia.org (read)` — while the claim at hand is that the bytes say
NOTHING of dhamma:

> **C2 · claim 6 — the machine STANDS ASIDE: token-free (the claim carries NO
> reviewable token), which is NEITHER pass NOR fail. The claim speaks ABOUT
> the RECORD, and A23's byte-scan (a human reading, marked so) found the word
> 'dhamma' in NONE of the five rows' bytes.**

> **C2 · claim 8 (the companion that names its own kind) — the quote's tokens
> (Delhi, Buddha) seen ONLY in the SNIPPET W4 (lane 'not-fetched:dup-publisher'),
> never in the READ window — AND the mouth's OWN words already named the kind
> ('One snippet…'). The token-law adds the KIND-WORD to what the mouth said;
> it weighs the REACH, never the truth.**

Prevents: reading `token-free` as "no support found" (it is no token at all —
the stand-aside), and reading `(read)` as covering the dhamma claim (whose
own content is that no row BYTES it). New ambiguity: two DIFFERENT absences
now ride near each other — token-free (no token exists) vs the byte-scan's
word-not-in-any-row (looked, not found) — the caption labels which is which.

### C3 — the vacuous case: an absence-flag over a NON-claim

The aggregate today: `ABSENT SIGNATURES: e:Hello, e:Zzzyx` over a phatic
greeting — the flag could read as disproof:

> **C3 — the greeting asserts NOTHING, yet the law flags its two proper
> forms: token-absent (e:Hello, e:Zzzyx) over NO BYTES GIVEN (rows []; the
> record's own word 'the web brought nothing'). Absence of a byte is NOT a
> mark against the claim — for a phatic word it can be NO MARK AT ALL (a
> disclosed vacuity of the instrument: 'Hello' is no stop-cap, A24 pinned).**

Prevents: "the greeting was DISPROVEN" — and (read)-flavour where NOTHING
was given. The record's own words stand right beside the flag: the door's
evidence_status verbatim `general knowledge, not verified this turn (the web
brought nothing (search-empty))` + A19's truth-words (`web_stamped: False`).
New ambiguity: one short word carrying the DOUBLE absence (the
non-claim's — possibly no mark; the turn's — no bytes) at the cost of length.

### C4 — the insufficient-and-blocked case (the independence constraint)

The aggregate today: `ABSENT SIGNATURES: e:Ashoka's, n:1` over zero rows:

> **C4 · claim 9 — this turn INSUFFICIENT BY ITS OWN BYTES: no row was given
> (gaps ['search-empty']); the mouth OPENED by saying 'No record stands
> behind this; I speak from general knowledge'; the machine weighed NOTHING
> (5 token-free) and flagged 2 token-absent (e:Ashoka's — a possessive form;
> n:1 — the folded phatic 'one'). The corroboration's OWN words: independence
> unknown, conflict insufficient. The reviewer-side independence: BLOCKED
> (OPENAI_API_KEY absent; DESIGNED, not proven). NOTHING here is verified,
> and NOTHING is contradicted.**

Prevents exactly the acceptance distinction #4: a BLOCKED reviewer-side
check and the record's own NOT-ESTABLISHED words are shown as words about
CORROBORATION, never as corroboration-success; token-absent stands as a
falsifiable REACH-check, not refutation. New ambiguity: the TWO
independence words (record-side `unknown`/`none`, reviewer-side `BLOCKED`)
could read as one — the caption keeps them APART (A14's own law supplies the
meaning: independence is UNKNOWN unless two independent publishers READ —
and at C3/C4 nothing was read at all; at C1/C2 one origin with `duplication
3` says `none` + `insufficient`).

## Limitations, UNKNOWNs, and what could NOT be captioned

- **The claim-to-bytes bridge is hand-made and recorded** (A23's table,
  re-verified by A24), not a reviewer output — A25's words must not imply
  the reviewer speaks claim-grain. It does not: it speaks per SPLITTER-SENTENCE.
- **No fixture needed the UNKNOWN escape** — every mandated state rides
  recorded bytes: the kind-words `page`/`snippet` and lane-notes verbatim
  (`'not-fetched:dup-publisher'`, `'http 202'`, `'http 200 (capped)'`) really
  encode the read/snippet/not-fetched distinction; the three status words
  really exist (T142). The single UNKNOWN worth naming sits at C4: the
  shelf carryover's relevance — and the RECORD ITSELF already speaks it
  (rows 19/2 carry `wu wei` / `hard problem` bytes and NO ashoka/dhamma byte
  — A23's byte-scan; at a fold turn the carryover CANNOT enter, A23 verbatim),
  so A25 marks it recorded-unknown, not invention-blank.
- **What no caption can ever carry** at these bytes: SEMANTIC entailment
  (the operator's standing weigh; A23's open J-flags) and the real-world
  truth of any claim (the standing human fact-check). A reader must leave
  the caption knowing four things: WHERE each byte was seen, THAT the
  machine weighed only bytes, THAT absence and stand-aside are not disproof,
  and THAT independence is here designed-unproven and BLOCKED at the leg.
- The C1 headline shows the standing limit in miniature: `tokens-present` +
  `CLEANS` + `(read)` are all TRUE words — and all three are KIND-BLIND at
  the sentence grain; the count's only byte sat at a never-fetched snippit,
  and the READ window's own note says its bytes were `capped`.

## The decision

**PASS** — all four fixtures are grounded at recorded bytes with no invented
mapping; the four acceptance distinctions all come out separable at the
captions (read-window vs snippet; token-match vs semantic support; absence
vs disproof; BLOCKED/unknown independence vs corroboration). The §'s own
boundary held: A25 PROPOSED presentation words (READ-WINDOW, NO BYTES GIVEN,
UNKNOWN) and changed no law — the frozen reviewer, its protocol, and every
historical artifact rode untouched, and A25 authored exactly two new files:
`a25-caption-prototype.md` (this file) and `a25-caption-fixtures.json`
(validated by the stdlib parser; both untracked; nothing staged or
committed).
