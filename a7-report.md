# a7-report.md — A7: Independent Sources, Corroboration & Conflict

## The state (start and end, verified not assumed)

Start HEAD `b3a7ecf` (A6) on `main`; baseline **148/148 exit 0** confirmed
twice before any edit; the founder's staged set (`gpt-reviewer.md`,
`reviewer/reviewer_*.py`, `reviewer/selftest.py`, two `live-run-*.jsonl`,
modified `opencode.json`) and untracked `Seyruna/` rode exactly as found and
will ride after; CORAL (`0910554`, `o1-controller`) untouched; no A4/A5/A6
artifact was rewritten. The final HEAD is the single A7 commit that carries
this report (the six paths below; the A1→A6 chain below it rides untouched,
and all six milestones remain unpushed until the founder says otherwise).

## What changed, and why (the §2 verdict first)

**The live probe (6 bounded calls, no retries, before any code):** the
default keyless provider (ddg-ia) today often returns a doc whose text
lanes ride **present-but-empty** (a Type-"D" disambiguation doc emptied
AbstractText, Definition, DefinitionURL, DefinitionSource and Answer at
once, leaving only nine RelatedTopics stubs — ALL riding the provider's
own house). The `Definition`/`DefinitionWord` lane — the one lane that can
carry a genuinely different second publisher from ONE search — rode empty
all probe day. Verdict, said straight: **the retrieval path CAN show more
than one publisher (abstract-origin + definition-origin are two distinct
origins in one response), and A7 now reads both and accounts them apart —
but this provider, on these days, mostly hands one origin voice at most,
plus house attribution.** The machinery was built to the shape of that
truth, not to a hope: no crawler, no second request, no fabricated
diversity.

**The changes (five files, all in the existing seams):**

1. `web_research.publisher(target)` — the ORIGIN'S identity: registrable
   domain of the host (two labels, three at the `bbc.co.uk` shape).
   `en.wikipedia.org` and `de.wikipedia.org` are ONE voice — A5's host-set
   counted them as TWO (the inflation A7 removes). Direction chosen on
   purpose: the laws UNDER-count (may hide an independence), never
   OVER-count (never invent one).
2. `web_research.canon_url(url)` — the address without its tracking
   clothes: fragment falls, the `utm_*` family and a NAMED list of
   click-ids fall; a meaning-bearing param (`?action=edit`) rides; a PATH
   never collapses. An unnamed param rides too (over-split at worst).
3. **The picker** in `research()`: coins ride PUBLISHERS, not the first N
   addresses. A clothed twin is `dup-url` before any coin moves; a second
   page of an already-READ publisher is `dup-publisher` (the spare coin
   reaches a voice BEHIND — where A4's first-N law wasted it); the house's
   stub still spends a coin and still reads as attribution (A5 whole); a
   failed look is NOT a voice (the publisher may try again); the cap still
   STOPS without a word (T133's law adopted whole); and the lineage
   (`publisher`, `canon`) rides every walked row — including the dup-words
   (a duplicate can be SPOKEN because the identity survived).
4. **The Definition lane** joins `results_from` (second only to the
   abstract; silence when empty — K2 whole; no address, no row) and its
   rows speak the kind word `abstract` (the origin's own words — A5's P3
   set, the lane-set moved, the law not relaxed).
5. **The corroboration word-ladder** replaces A5's blanket `unknown`:
   `insufficient` (fewer than two origin voices READ — nothing to weigh;
   EA4's truth, which the blanket word hid), `unknown` (voices read, the
   bytes share no year-shape to compare — a stated limit; the shelf's
   DISAGREEMENT lanes remain the contradiction-home), `bytes-share` (two
   READ publishers share a year-shaped number — bytes agree; **agreement
   of bytes is not entailment: two independent sources can both be
   wrong** — A5's law kept whole), `bytes-clash-possible` (disjoint years
   — the disagreement KEPT, never averaged, never CHOSEN — both rows ride
   the shown set; two pages may also merely speak different facts, hence
   `-possible`). New companions: `publishers_seen` (voices the provider
   spoke, weighed or not), `duplication` (the picker's dup-words counted),
   `syndicated-possible` (IDENTICAL bytes at two publishers — detected,
   never assumed).
6. **The audit path** (the §D): the door's `trace["web"]` now stamps the
   compact `corroboration` dict beside a `sources` list where every source
   says its `publisher`, its `lane`, and HOW it was seen (`read` /
   failure-class / `skipped:dup-*` / `bytes-not-read`) — no page-body
   dumped. `window.why_lane` passes `publisher` into the evidence row;
   `research_eval` carries it into the eval rows. Identity survives the
   pipeline to the review output.

## Tests — synthetic evidence (153/153; the five new witnesses)

| # | A7 requirement | Witness | Outcome |
|---|---|---|---|
| 1 | two distinct publishers, one claim | T147/T148 (`candidate` at two READ) | ok |
| 2 | two URLs, one publisher = NOT two sources | T145+T148 (`none` at one publisher) | ok |
| 3 | snippet + fetched page, one URL = one source | T147 (`dup-*` words; row speaks it) | ok |
| 4 | tracking-parameter dedup | T145 (cloth == bare), T147 (`dup-url`) | ok |
| 5 | conflicting passages stay VISIBLY conflicting | T148 (`bytes-clash-possible`; BOTH rows ride) | ok |
| 6 | one supporter never called corroborated | T148 (`insufficient` + `none`) | ok |
| 7 | empty/malformed/failed stays honest | T146 (empty lanes = silence; no invented address) | ok |
| 8 | no-web and auto intact | T149 (spy raises uncoined) + frozen T137/T140 | ok |
| 9 | identity survives to the evidence/review output | T149 (`publisher` through window+door+trace) | ok |
| 10 | instructions in fetched bytes stay data | T149 ("Read me well" rides DOCUMENTED, no order) | ok |

Two A4/A5 pins moved **with disclosure** (the only edits to frozen tests):
T133's synthetic search now rides TWO publishers (its words — "TWO coins,
the rest UNTOUCHED" — hold verbatim; what changed is that the two coins
now demonstrably ride two voices); T139's pinned dict grew the three
companions and its `conflict` word moved `unknown → insufficient` where
fewer than two voices were read (the counts it pinned are unchanged). The
frozen A3 baseline (T01–T128) rode untouched.

## Live observed (the smoke — six frozen EA questions, search road only,
ZERO mouthfuls, one pass no retries, 8.9 s total; `research-hold/a7-smoke-live.json`)

| Q | ok | rows | independence | conflict | the day-shape |
|---|---|---|---|---|---|
| EA1 | ✓ | 5 | none | insufficient | one origin voice READ (wiki); house lanes around it |
| EA2 | ✓ | 3 | unknown | insufficient | attribution-only (A5's shape REPRODUCED — bytes not in hand) |
| EA3 | ✓ | 3 | unknown | insufficient | stubs rode (the Type-"D" day-form); no origin READ |
| EA4 | ✗ | 0 | unknown | insufficient | `search-empty` — the honest empty REPRODUCED, nothing minted |
| EA5 | ✓ | 5 | none | insufficient | one origin voice READ |
| EA6 | ✓ | 3 | none | insufficient | one origin voice READ |

Every `conflict` word reads `insufficient` — and that is the milestone's
honest headline, not a failure of it: **today's default provider never
handed two READ origins to weigh**, so `candidate` still has NO live
witness (the A5 finding REPRODUCED and sharpened: the barrier is the
provider's shape, not the accounting). No failures beyond the provider's
own empties; the probe additionally observed DAY-DRIFT (the same query
answered with full lanes in the smoke minutes apart from an empty-lane
probe) — provider flakiness, said, not smoothed. A4↔A5↔A7 comparability
holds only at the lanes' words (the answers' words rode a search-only
road — zero mouths); no claim of smarter answers is made on this evidence.

## What was NOT claimed

- **No independent GPT review occurred** (the bridge's `OPENAI_API_KEY`
  remains absent; the deterministic law + the disclosed operator carry the
  review — not an independent model, and not renamed as one).
- No paid API, no new account, no secret touched: stdlib only.
- No conflict was ever PROVEN — the ladder's two fire-words end in
  `-possible`/`bytes-` on purpose; source agreement stays apart from claim
  entailment; two sources can both be wrong.
- Syndication is DETECTED only at identical bytes; a reworded syndicated
  twin still reads as two (over-count direction there, stated).
- Unlisted second-level shapes underccunt (a `metro.tokyo.jp` reads
  `tokyo.jp`); IDNA hosts read apart, not merged; the tracking list is
  NAMED (an unnamed param rides the canon).

## Safety kept

Six paths in the one commit: `web_research.py`, `stages.py`, `window.py`,
`research_eval.py`, `tests.py`, `research-hold/a7-smoke-live.json`, plus
this report — the founder's staged files rode IN the index exactly as
found (never staged, unstaged, or committed), `Seyruna/` untracked as
found, CORAL unmoved, no reset/clean/stash/rewrite, nothing of A1–A6
refactored.

## The single best next milestone (and why)

**Give `candidate` its first live witness: try the SECOND provider word
(searxng — one config word, already shipped and fixture-tested) against a
live public instance, strict timeouts, bounded attempts, no AUP-mystery
retries.** Rationale: A7 built the multi-source machinery to the shape of
the evidence and *proved where the barrier sits* — it is the provider's
one-voice shape, not the accounting, not the budget, not the guards. Green
tests do not make an answer more accurate (§5's own warning); the next
measurement that could move that claim is the SAME bounded road pointed at
a provider that can actually hand two publishers — and if the public
instances prove as dead as A4 found them, that is a KEYLESS-MULTI-SOURCE
blocker belonging to the provider market, reported as such, and the
sentence-picker and the GPT key stay the founder's coins.
