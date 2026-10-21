# A24 — the frozen claim-level reviewer ridden at the A22 bytes (read-only; no code changed, nothing committed)

Start HEAD `1c7a74c`, end HEAD `1c7a74c`, branch `main` (read, not assumed).
The A22 implementation still rides as-is (`research_eval.py`, `tests.py`
still ` M`); the seven founder-staged entries stand byte-exact in the index
with nothing unstaged beneath them. **A24 changed no code**: the four files
it wrote are all new and all A24-named; no historical artifact was edited;
no live request was spent; no deployment. Status: **A24 AUDIT COMPLETE**.

## Phase 0 — state, reads, and the byte ledger

`a23-report.md`, `a22-report.md`, `a22-eval-design.md`,
`research-eval-a22.json`, and all six `research-hold/a22-*` artifacts were
read before any act. Before the ride began, sha256 was taken of
`review.py`, `review-protocol.json`, and the five A22 byte-riders (the
digests ride `a24-review-results.json`); the A24 run wrote nothing to them.
The ride itself is the module's own `pass_eval` — pure stdlib, zero network
— so the no-live-requests constraint held trivially.

## Phase 1 — the interface, from code and its pinned tests

At bytes (review.py + tests.py), the instrument is:
- `load_protocol()` — validates RRV-0.1 (`review-protocol.json`: nine
  measures; claim-support six words, verdicts four) and returns `probs`;
  today's load returned `[]` (recorded).
- `signatures(text)` — digits: `SIG_NUM` digit-runs (commas stripped), with
  the PINNED spelled-number fold `NUMWORDS` — which reaches `one`..`twenty`
  only — and the ordinal fold `ORD` — `first`..`tenth` only; entities:
  capitalized forms of length >= 4 (apostrophes and hyphens ride INSIDE the
  token) beyond the 26-word `STOP_CAPS`.
- `check(claim_text, rows)` — the token-law: each signature token
  case-insensitively substring-matched against each row's `claim` OR `url`
  bytes; per token ALL row-hits speak, each with the row id, its `kind`
  (`page`/`snippet`, else `none`), and its `work`; first-miss tokens list as
  `missing`. Its status words are EXACTLY THREE — `tokens-present`,
  `token-absent`, `token-free` — and its docstring pins its humility:
  tokens present means support POSSIBLE; the operator weighs entailment;
  the machine does not.
- `pass_eval(path)` — walks `rec["questions"]`; the answer is
  `q.door.response`; the rows are `q.web.rows`; sentences split by the
  house splitter `web_research.SENTENCE`; returns (and with `--write`
  writes the FIXED historical name `research-hold/a6-machine.json` — never
  written today). `main` additionally runs the protocol check.
- The instrument's OWN pinned tests are **T141 (the protocol schema),
  T142 (the token-law and its three humble words), T143 (the independence
  word)** — established at bytes (tests.py:2005/2019/2038). **T129 is not a
  reviewer pin** — it pins the PROVIDER PARSE (`web_research`'s lane,
  tests.py:1625); A23's report's parenthetical "(T129/T142)" over-credited
  it. Disclosed here; A23's artifact rides byte-untouched.
- Version: `review.py` and `review-protocol.json` byte-clean at HEAD; last
  touched at commit `b3a7ecf` (A6) — recomputed from git at the ride, which
  corrects the A-series prose's remembered `9c352bd` (itself A12's commit).
  The task's
  "version/commit" slot therefore reads: RRV-0.1 protocol, instrument
  bytes == HEAD, authoring commit `b3a7ecf`, file digest recorded.

## Phase 2 — the envelope mismatch, resolved at the invocation level only

The interface fact, re-spoken at bytes: `pass_eval` over
`research-hold/a22-eval-live.json` **AS-IS** saw `questions: 0` — a
VACUOUS-CLEAN pass (the key word `questions` is absent from the envelope).
Had A24 run `main` at the A22 file with no adaptation, it would have
printed a clean nothing. The resolution is the adapter:
`research-hold/a24-review-input.json` — the envelope's four case blocks
under the key `questions` (a one-key rename; the case blocks re-asserted
`json.dumps`-equal to their raw files INSIDE the run). The historical
artifacts ride unedited; the adapter is clearly A24-named and is an input,
not a deliverable.

## Phase 3 — the ride (exact invocation, output, exit status)

Invocation: `.venv/bin/python3 -B` heredoc, `OPENAI_API_KEY` explicitly
UNSET at the call (matching T143's BLOCKED-by-named-var "now" word and
A6's bytes; the environment itself shows the key absent), calling
`review.pass_eval("research-hold/a24-review-input.json")`, no `--write`;
exit status 0. The frozen pass, at its own words:

```
C1 | 5 sentences | CLEANS of absent signatures   (3 tokens-present, 2 token-free)
C2 | 6 sentences | CLEANS of absent signatures   (3 tokens-present, 3 token-free)
C3 | 1 sentence  | ABSENT SIGNATURES: e:Hello, e:Zzzyx
C4 | 7 sentences | ABSENT SIGNATURES: e:Ashoka's, n:1   (2 token-absent, 5 token-free)
independence: BLOCKED: OPENAI_API_KEY absent — independence is DESIGNED,
  not proven; the deterministic audit and the DISCLOSED OPERATOR carry
  the review
```

Integrity echoes: `load_protocol().probs == []`; and the instrument
recomputed over the FROZEN A5 bytes reproduces the stored A6 artifact's
findings exactly (echo boolean **true**) — the reviewer is byte-untouched
and deterministic since A6. The full pass output, the input paths, the
digests, and the invocation ride in `a24-review-results.json`.

## Phase 4 — the comparison (full table in `a24-review-comparison.md`)

The machine's per-case words, sentence counts, and per-token evidence
re-derive A23's manual figures exactly. Against A23's nine claims: SEVEN
AGREE at token level — the count token at the SNIPPET (`14@W5(snippet)`),
the attribution/span forms at the READ page (`232/268@W1(page)` etc.), the
never-fetched-row tokens (`Minor@W5(snippet)`, `Rock@W4/W5(snippet)`), the
quote row (`Delhi@W4(snippet)`, `Buddha@W4(snippet)`), and the C4 absence
words (`e:Ashoka's`, `n:1` at `rows=[]` — the instrument's humble echo of
the compound word). TWO AGREE BY SILENCE (`token-free`): the thirty-
inscriptions clause (`thirty` sits OUTSIDE the fold-table) and C2's
record-about-itself meta-claim — the categories the token-law cannot
speak. NO CLAIM CONFLICTED. The task's step-6 watchlist resolves at the
aggregate word `CLEANS of absent signatures`, which is KIND-BLIND (the C1
headline's count rode a snippet alone); the vacuous folds (`One`→`n:1`,
URL byte `…k7=1`) and the greeting-flag (`e:Hello`) re-pin as disclosed
vacuities; the qualitative claims stand aside as `token-free` — the
machine neither passes nor fails them.

## Phase 5 — the decision gate (no caption implemented)

**The existing reviewer is sufficient for a narrowly worded evidence-kind
caption — as projection, not as new fact.** The caption needs exactly the
words the instrument already returns per token — `token@row(kind)` — and
its three status words plus its docstring humility already bound every
over-claim:
- `tokens-present` never entails — it says bytes reached the mouth, not
  that they PROVE the claim (the mix-kind sentence is the standing lure:
  `14@W5(snippet)` beside `Ashoka@W1(page)` under ONE aggregate word);
- `token-absent` is falsifiable but not WHY-answering (empty rows vs
  missing byte vs the possessive-token artifact `e:Ashoka's` vs the
  phatic-fold `n:1`);
- `token-free` is the stand-aside — the caption on a qualitative claim is
  silence-with-a-shape, and a caption may not fill it with a machine
  verdict the machine never spoke.
A separate diagnostic improvement is NOT needed before a caption: the
three pinned extensions (fold past twenty for `thirty`; a
possessive-insensitive entity match; a phatic-one flag) are each
T142-shape-testable but ride as caption RICHNESS, not preconditions. And
"insufficient evidence to choose" does not hold — the ride produced its
own numbers at all four cases. Any later extension is the founder's coin,
test-first, against the frozen three-word law.

## The ledger

- Wrote (all untracked, all new, none historical):
  `a24-review-results.json`, `a24-review-comparison.md`, `a24-report.md`,
  and the A24-named derived input `research-hold/a24-review-input.json`.
- No live request; no commit, no staging, no reset/clean/stash; the seven
  staged entries and all A22/A23 artifacts ride byte-untouched.
- The frozen harness, unmodified, re-ran at A24's close:
  **166/166 pass — HARNESS GREEN**.
- `A24 AUDIT COMPLETE`.
