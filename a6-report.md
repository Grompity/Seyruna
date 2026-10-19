# a6-report.md — A6: The Second Brain (independent adversarial review)

## Where the road stood (the §1 recover, kept exact)

HEAD at the start was `640fcd8` (A5) on `main`; five unpushed milestone commits
(A1 `a4f204f` → A5) behind none. The founder's staged reviewer files
(`gpt-reviewer.md`, `reviewer/reviewer_ask.py`, `reviewer/reviewer_mcp.py`,
`reviewer/selftest.py`), the two `research-hold/live-run-*.jsonl`, the modified
`opencode.json`, and the untracked `Seyruna/` rode as found — A6 touched none
of them and unstaged none of them. CORAL (`0910554`, `o1-controller`) rode
untouched. Baseline before any edit: `python3 tests.py` **144/144 twice, exit
0, ~0.3 s** (the frozen harness; `-m unittest` is vacuous here). Missing
artifacts: none — every A4/A5 report and byte-file the brief named was on the
shelf, so no judgment had to be marked unreviewable for absence.

## What the second brain ACTUALLY was (the §2 answer, told straight)

The bridge the founder staged is real and inspected: `reviewer_ask.py` is a
Responses-API leg (default `gpt-6-astra`, keyless-free `OPENAI_API_KEY` env
gate, value never printed) and its standing orders (`gpt-reviewer.md`) name
the loop *Qwen builds, GPT reviews, Founder decides*. The answering mouth is
`RadixArk/Qwen3.8-Flash-Next-NVFP4` (config's `MODEL`) — so the bridge's
reviewer is a genuinely DIFFERENT FAMILY, which is what independence needs.
But **`OPENAI_API_KEY` is ABSENT** on the day, and the leg "waits for the
key" by its own law: **model independence is DESIGNED and BLOCKED (one named
env word), not proven, and A6 did not fake it.** What actually reviewed A6
was (i) the **deterministic token-law** (`review.py` — machine, re-runnable:
`python3 review.py`, zero net, zero mouths) and (ii) the **disclosed operator
— the same hand that wrote the code**, wearing the bridge's temperament
(source-report vs interpretation vs synthesis; UNKNOWN may be correct; a
citation is not a pass). `review.py`'s independence word says all of this in
code, and T143 pins both lanes (BLOCKED today; READY — still NOT PROVEN — with
a key).

## The protocol rode FIRST (RRV-0.1)

`review-protocol.json` was written **before any status was assigned**, and
its schema bites (T141: nine measures are the spine; six claim-statuses, four
verdicts — PASS / FAIL / UNREVIEWABLE / N/A; the nine measures stand APART —
no single score). The claim-lists per answer are the operator's extraction
(a judgment, disclosed); every support-check is the machine's token-law over
**the experiment's own bytes** (the artifact's row-claims — `packet_text`'s
law: what the mouth saw is the record's ground, never a today-page).

## The artifact and the machine's finding

`research-hold/a6-review-1.json` (AR-0.1; the machine pass beside it:
`a6-machine.json`) carries per case: the query, the real answer, the exact
rows-bytes with kind (page/snippet) and work, the claim-by-claim status, the
nine measures, missing evidence, and WHO reviewed. The token-law — digits
with a spelled-number table (fourteen and 14 are ONE claim), capitalized
proper forms, against the rows — found **absent signatures: NONE across all
six answers.** Read that with its humility: tokens-present is not entailment
(the machine can only FLAG absence); its verdict words are exactly three, and
for a signature-free sentence it STANDS ASIDE (`token-free`) rather than
passing it — the self-grading sin in a new coat.

## The adversarial audit, case by case (the §4 pass, assume-the-answer-is-wrong)

- **EA1** — every important claim rides (`14`/fourteen, `earliest dated`,
  `Minor Rock Edicts`, the five locations via the caption lane): PASS, with
  one named PARTIALLY: "content CENTERS ON the teachings of Buddha"
  generalizes W4's DELHI-subset words to the whole — the mouth's mild move,
  not a contradiction. **The new damage the attack found:** the support rode
  W1's CLAIM — and that claim was a caption DROWNING in escaped markup
  (`&lt;b id="mwCw">…"}'>…`): the site serves markup already escaped, so the
  real-tag saw (`<[^>]*>`) saw nothing, and A5's extraction exposed the
  shavings in the bytes the mouth waded. This is the report's one
  reproducible MACHINERY failure (the bridge's classification word), and
  EA5's W1 shows the same lane (its claim rode the TEMPLE-IMAGE caption) —
  two live observations, not a one-day ghost.
- **EA2** — attacked from both sides and it HELD: the `15` rides the snippet
  verbatim, and the day-reading is licensed by the byte's OWN preposition
  ("on 15…" — the trap tried: the digits could have been a cut "1215"; "on"
  says day). "The record cuts off there, so I can't tell you the month" is a
  TRUE statement about the byte — the mouth's knowledge was present and
  NOT SPENT. A5's operator word REPRODUCED under the token-law; this is the
  exemplar case of appropriate uncertainty.
- **EA3** — the claim stated is DIRECT (W1 verbatim: "Krishna is a major
  divinity in Hinduism"). The gap is not the claim's: THREE referents rode
  (deity, emperor, mantra) and ONE was spoken as THE subject with the
  referent-set unmentioned — an OMISSION, not an error, and what the seeker
  MEANT is UNREVIEWABLE-BY-THESE-BYTES. A5's PARTIAL word stands, now sharp.
- **EA4** — the machine called its one sentence `token-free` and stood aside,
  correctly: "We don't know — that is an answer, not a failure" is the ROAD's
  word, not a claim about the world. Failure-honesty PASS: `search-empty`
  spoken, NO web lane-word stamped, nothing minted. REPRODUCED exactly.
- **EA5** — the definition rode W1 verbatim, and so did the etymology
  ("The encounter of a teacher and a disciple…" — the FULL untruncated
  artifact bytes carry it; A5's own record had hidden this behind a print
  truncation). PASS end to end; its note is the caption-lane note again.
- **EA6** — attacked hardest: "the Anguttara Nikaya (3.65)" looked like the
  mouth's book-knowledge, but the BYTES carry "(3.65)" verbatim — A5's word
  REPRODUCED, no false precision. The gap is now SHARP and RETRIEVAL-SHAPED:
  the page's claim-lane (its caption) carried POLYGLOT NAMES (Bengali,
  Burmese, Thai gloss lanes), NOT readings — so "what the suttas MEAN across
  the traditions" is UNREVIEWABLE-BY-THESE-BYTES, not denied, and the
  answer's convergence stands UNTESTED (one origin family; corroboration said
  none/unknown for all six, never `candidate` — the provider's shape, said by
  `web_research.corroboration`, deterministic).

## The ONE intervention (the §6 experiment, bounded)

- FAILURE (new, reproducible, actionable): the escaped-markup shavings in
  page-kind claims — every claim A6 must AUDIT rides them.
- PROPOSAL: one clause in `web_research.extract` — cut escaped spans and
  their residue-runs (`"}'>` = three-or-more of quote-brace-angle-quote);
  multi-script bytes ride untouched. PREDICTION: EA1's re-run claim reads as
  caption prose, the answer not worse, other lanes unbent.
- BEFORE the witness rode, a standalone probe CAUGHT the trap: the live bytes
  close almostEVERY escape with a REAL `>` (only the `<` is escaped), so a
  `&lt;…&gt;` law matched NOTHING — the span now closes at a real `>` OR at
  `&gt;`. The probe caught what a hopeful witness would have blessed.
- PRESERVED first: the A5 bytes rode on as the benchmark (`a5-eval-live.json`
  untouched by design — the re-run rode `run_one` inline and wrote its OWN
  file); the original answer-words ride beside the new ones in
  `research-hold/a6-ea1-rerun.json`.
- RERUN (EA1 only — the affected case, one bounded door turn, comparable
  conditions, 71.1 s, 3 mouths, web stamped): the claim reads
  "Edicts of Ashoka — A Major Pillar Edict … Material Sandstone — Created
  3rd century BCE — Present location Nepal …" — **prose, no shavings**.
  The answer got RICHER (dates, counts) and the token-law AUDITED the
  re-run ITSELF: clean of absent signatures (268/232/30 all ride the bytes —
  knowledge spent was byte-knowledge, not memory). No regressions anywhere:
  T130–T140 rode untouched.
- VERDICT: **KEEP** — the improvement is MEASURED at the claim-shape (the
  target the intervention aimed at); at the answer-words it rides
  INCONCLUSIVE-FAVOURABLE (provider lanes rotate day to day, and that is
  said, not smoothed). The deterministic fixture T144 — copying the live
  shape — is what PROVES the clause; today's clean bytes match it.

## Witnesses and the suite (the §7 law kept)

T141 (the protocol is DATA and its schema bites), T142 (the token-law speaks
THREE humble words and no fourth: folds fourteen→14, flags a fabricated
1215 and a place the bytes lack, STANDS ASIDE at signature-free prose, and
names WHICH ROW of WHICH KIND supports — tokens-present is support POSSIBLE,
never support THAT IT IS), T143 (the independence word tells the truth it can
tell: BLOCKED now by one NAMED env var; READY — still unproven — with a key;
the FAMILIES named apart so no model is called independent of itself by a
prose accident), T144 (the clause keeps its hands off the prose: caption and
definition SURVIVE, shavings DIE, a pure-gunk half-escape yields nothing,
T134's snippet lane rides UNTOUCHED). Suite: **147/147** with the review
witnesses, **148/148** with the clause's witness; two clean runs before the
commit, one after (below). No ordinary test touched the net or a mouth; no
review endpoint failed (the GPT leg was never CALLED — its absence was
recorded, not papered over, and it stands un-retried per the no-retry-storm
law).

## What remains, told straight

- The GPT leg's LIVE judgement is UNPROVEN (the key is one env word — the
  blocker is CONCRETE, not philosophical). With a key, one bounded call per
  case is the road; A6 did not manufacture its verdict.
- Every PARTIAL weight in the artifact is OPERATOR weight, disclosed; the
  token-law's CLEAN word is WEAK by design (presence ≠ entailment); a
  contradiction a passage resolves by TONE remains outside the machine.
- Independence beyond one origin family still rides none/unknown for all
  six — the provider's shape, and the `candidate` word still has no live
  witness. The multi-voice provider behind the one-word boundary remains
  the founder's coin (unchanged from A5).
- The claim-lane still rides the CAPTION FIRST (EA1, EA5): the clause made
  the caption READABLE; picking the DEFINITION SENTENCE past it remains
  open, and A6 left it open ON PURPOSE (one narrow intervention was the
  law; the caption now at least speaks cleanly).
- The founder's files rode exactly as found; nothing in this phase moved
  `stages.py`, `window.py`, or the door; the eight A6 paths commit as ONE
  path-limited commit, and the five prior milestones keep their bytes
  (A4's report already marked the A1 task-lane `fetch` seam liftable; the
  A5 auto-proof and eval stay as they were — A6 added no new policy).

## The commit

Eight paths, nothing else: `review-protocol.json`, `review.py`,
`research-hold/a6-review-1.json`, `research-hold/a6-machine.json`,
`research-hold/a6-ea1-rerun.json`, `web_research.py`, `tests.py`,
`a6-report.md`.
