# A13 — Ascended Answer-Quality Benchmark (BM-0.1, eight fresh questions)

## State and protection

Starting HEAD `9c352bd` (A12), branch main; the tree was already as the
A-series left it (the founder's staged bridge set and `opencode.json`
staged; `Seyruna/` and the A8–A12 artifacts untracked). A13 changed **no
production code** — an evaluation milestone keeps its hands off the answer
path. The deterministic suite still rides **158/158** (re-run at the close;
suite-truth and answer-quality-truth are kept separate throughout). CORAL
unmoved, nothing deployed.

## The entry point, the configuration, the web

The supported unit is `research_eval.run_one(question, live, caps)` — the
very function `main()` loops over: the real `research()` (search, fetches,
kinds, corroboration words) then the SAME real door the conversation rides,
`live=True`, `web:True`. No parallel answer path was invented. Recorded
configuration: provider `ddg-ia`; model `RadixArk/Qwen3.8-Flash-Next-NVFP4`;
caps `{max_calls_per_question: 8, max_secs_per_question: 240}` (the fixture's
own, pre-request as the house's law).

**Web-enabled actually ran — and its finding is the milestone's sharpest
fact.** The provider answered all eight searches (~0.4-0.7 s each) and said
`search-empty` to EVERY one: the ddg-ia RelatedTopics lane serves the
A-era's keyword-shaped words (the EA six rode it green) but returns NOTHING
for whole-sentence questions. All eight answers therefore rode the door's
non-web roads (three `general`, five interpretive/shelf), the web's
emptiness recorded each time, no answer claimed a web pedigree, and **the
corroboration/independence machinery was NOT exercised by this sample** —
named plainly below as the sample's limitation.

**Q8's first try stopped at a recorded MODEL event**: the mouth delivered
bytes-not-JSON (`r识 C+Z2 Sfr...`) and the A3 guard (stages.py:318, "the
MODEL event stays the model's; the uncaught raise was") raised — no retry
storm, exactly as designed. §4's discipline permitted one bounded re-run;
it rode true (Zhuangzi's butterfly, 2 calls, 38 s) and the failure record
rides the artifact beside it.

## Baseline — what is actually preserved (nothing invented)

BM-0.1 exists (`benchmark.json`, ten fictionalized A3 cases) with two live
records (`bench-baseline-live.json`, `bench-candidate-live.json`) whose
answers ride inside scripted `turns` with A3's own `checks` — real, but not
comparable case-for-case with these eight fresh sentences. A5's EA-0.1 run
preserved six terse frozen questions WITH responses; A6 preserved one EA1
re-run. **None is these eight exact words** — so this run stands as a
**NEW BASELINE**, explicitly not an improvement over an unobserved past.

## The eight, and what each actually said (full bytes in the artifact)

Raw records: `research-hold/a13-eval-live.json` — per question: the web
record ("THE BYTES THE MOUTH SAW"), lane, model_calls, code, response,
secs; caps and provider in the header.

- **Q1 (general, 2 calls, 60 s)** — the run's richest: a three-part split of
  what the inscriptions DIRECTLY establish (geographic spread as evidence,
  Rock Edict XIII's Hellenistic kings as a datable anchor, the Kalinga
  turning-point, dhamma as an ethical code, the dhamma-mahamatras), what
  they DO NOT establish (one-sided royal self-presentation, reception,
  economy, succession, "the dating... still debated"), and later
  interpretations (Ashokavadana/Divyavadana, the Mahavamsa, nationalist
  projections — "the edicts themselves do not settle that").
- **Q2 (shelf, 2 calls)** — "related, not an answer": the very sameness
  being asked about is the move the record flags as interpretive; "what's
  lost in the flattening is the texts' own disagreement."
- **Q3 (shelf, 3 calls)** — one thread named (Mark 12:29-31, the two
  greatest commandments, Mark as earliest gospel) and the rest STATES as
  outside the record: the Buddhist side, the comparison, the historical
  link.
- **Q4 (shelf, 2 calls)** — the run's best two-sidedness: FOR convergence,
  Tao Te Ching 48's diminishing doing and Newton's Opticks refraction ("one
  source, many angles"); AGAINST, the mind-precedes/neti-neti meeting is
  "our part of the sentence, not the texts'" — and the refraction picture
  cuts both ways: "the separation is real."
- **Q5 (shelf, 2 calls, 28 s)** — "We don't know - that is an answer, not a
  failure." The unknown test answered IN the system's own idiom.
- **Q6 (general, 2 calls)** — the false premise CAUGHT and refused:
  mainstream historians have NOT proved the trip; the Gospels and Paul say
  nothing of it; the whole theory rests on Notovich's 1894 Saint-Issa
  manuscript report — no accepted primary source settles where he studied
  "because the trip itself is not established."
- **Q7 (general, 2 calls)** — the system spoke **A12's own doctrine in its
  own words**: 403 = "access, not truth"; 200-without-passage = "reachable
  yet silent... absence of a passage here is not proof the claim is false";
  "that third result is the only one that can support a documented claim."
- **Q8 (shelf, 2 calls, re-run)** — chose a telling over a clarifier:
  Zhuangzi's butterfly, "he called that not-knowing the transformation of
  things... the moment the dream and the waker trade places, and you let
  them." (Interpretive; flagged.)

## Scores — 0/1/2 per applicable criterion, N/A where inapplicable

The scorer ran in the SAME model family as the answerer (RadixArk/Qwen3.8
spoke; Qwen3.8-family scored) — **same-family scoring, disclosed, NOT
independent validation**. Flags mark interpretive judgments for human
review.

| Q | (1) support | (2) provenance | (3) uncertainty | (4) fair-repr | (5) false-premise | (6) helpful | (7) evidence-integrity |
|---|---|---|---|---|---|---|---|
| Q1 | 1 — claims are recall-shaped and structurally self-marked, but no per-claim pedigree; a human fact-check is owed (FLAG: is the split accurate?) | 1 — the trace says general (none read) yet the text rides ~20 named things with no visible read/recall mark | 2 — explicit establish / do-not-establish / interpretation split; dating named as debated | N/A | N/A | 2 — all three asks answered richly | 2 — the empty web supported nothing |
| Q2 | 2 — no flat claim made; named texts stay shelf-records | 2 — "the one note says" names its record | 2 — the sameness itself flagged interpretive | 1 — protects the disagreement but defers naming it (FLAG) | N/A | 1 — honest deferral; insight delivered, the ask not fully answered | 2 — related rows kept below an answer's rank |
| Q3 | 2 — one cited thread; the rest named as outside the record, not invented | 2 — names the record and its limits | 2 — what sits outside is stated | 1 — flattens nothing, represents only one side (FLAG) | N/A | 1 — one of four asks served | 2 — as above |
| Q4 | 2 — both cases rest on named shelf-texts | 2 — "on records 5 and 6" guard-note | 2 — the meeting-point is "our part of the sentence" | 2 — genuine disagreement preserved BOTH ways ("the separation is real") | N/A | 2 — strongest of the run | 2 |
| Q5 | 2 — claims only the record's state, self-identified | 2 — the not-knowing is about the records | 2 — the answer IS the unknown, in the system's idiom | N/A | N/A | 2 — the unknown-information ask met cleanly | 2 |
| Q6 | 2 — the premise challenged with named recall-sources | 2 — names its grounds (Gospels, Paul, Notovich 1894) | 2 — "shaky", "unreliable or lost", not settled | N/A | 2 — the designed catch: premise refused, not swallowed | 2 | 2 |
| Q7 | 2 — pure doctrine-recital; every word matches A12's fixed bytes | N/A — no external provenance at issue | 2 — the access/truth line drawn exactly | N/A | N/A (premise true) | 2 — the three-way split delivered correctly | 2 — the system's own integrity law spoken true |
| Q8 | 2 — attribution named, told "in his telling" | 2 — Zhuangzi named at recall, no read-fake | 2 — "not-knowing" carried AS the content | N/A | N/A | 1 — a clarifier was warranted and a telling rode instead (FLAG) | 2 |

**Aggregates (applicable-only denominators):** (1) 15/8 ≈ 1.9 · (2) 13/7 ≈
1.9 · (3) 16/8 = 2.0 · (4) 4/3 ≈ 1.3 · (5) 2/1 = 2.0 · (6) 13/8 ≈ 1.6 · (7)
16/8 = 2.0. **Overall 79/43 ≈ 1.84 of 2** across 43 applicable slots; 13
slots N/A and never forced. Per-question aggregates: Q1 1.6, Q2 1.67, Q3
1.67, Q4 2.0, Q5 2.0, Q6 2.0, Q7 2.0, Q8 1.8.

## What the sample does and does not show

- **A success the design earned:** Q7 is the strongest evidence that
  Ascended's designed qualities reach its speech — the system recited its
  OWN A12 evidence-integrity law (403 = access not truth; empty-200 = silent
  not false; only a readable passage supports DOCUMENTED) with the exact
  right distinctions, in ordinary words. Q6's false-premise catch and Q5's
  not-knowing idiom are the other two designed behaviors visibly present.
- **A weakness the sample names at itself:** whole-sentence seeker-words do
  not move the configured web lane AT ALL (eight for eight `search-empty`) —
  so in this sample the corroboration/provenance machinery stood unused and
  the provenance scores measure honesty-about-emptiness, not provenance
  WORK. Whether the sentences are too long for ddg-ia's lane or the lane has
  changed shape is UNRESOLVED — A6/A7's keyword words rode it green days
  ago; a one-bounded-query probe (a keyword twin of any of these eight)
  settles it.
- **Can be concluded:** the door's uncertainty idiom, deferral honesty,
  false-premise refusal, and its own doctrine-in-speech are REAL at bytes
  and repeat (Q2's/Q3's/Q4's "related, not an answer" pattern fired on
  three different questions without flattening or fabbing). **Cannot be
  concluded:** factual correctness of the general-road claims (Q1's
  Kandahar-to-Karnataka spread, Notovich's date — no read source stood
  behind them here), anything about two-publisher corroboration on sentence
  words (the lane was empty), and ANY of this as independent review — the
  scorer shares the answerer's family.
- **One live flake, priced:** one mouth-event in eight (Q8 try 1) — the
  guard raised, one bounded re-run rode true.

## GPT review, founder state, and the recommendation

GPT review did **NOT** run: `OPENAI_API_KEY` absent, inspected in the
process environment, not assumed. The founder's staged set,
`opencode.json`, `Seyruna/`, the A8–A12 artifacts, and CORAL are byte-for-
byte as found — `git status` at the close shows the SAME staged entries,
plus only A13's two untracked artifacts (`a13-report.md`,
`research-hold/a13-eval-live.json`), no tracked file touched, no commit
made (§ "diagnostic-only... do not commit").

**Recommendation for the next milestone (the founder's coin, one line):**
a bounded query-shape diagnostic — re-run one or two of these eight with
the SAME words at keyword shape at the web lane (a probe, not a
re-benchmark, not a tuning) — because the milestone's own bytes say the
answers are carrying the designed distinctions at the door while the
provider's lane will not carry the seeker's sentences.
