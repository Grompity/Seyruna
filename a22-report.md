# A22 — separate the retrieval query from the question, at the runner (implementation + adversarial audit + controlled live evaluation; uncommitted)

Starting HEAD `1c7a74c` (read at preflight, not assumed); ending HEAD
`1c7a74c` — **no commit, no staging** (no `add -A`, no reset, no stash, no
clean, no amend, no history touch, no deploy). The A22 work rides as
UNSTAGED working-tree changes to two tracked files plus new UNTRACKED
reports/artifacts; the seven founder-staged entries are byte-exact and
still staged (the index untouched); `Seyruna/` (nested repo), `Paper
Website/`, CORAL and the Eshkol investigation were not touched.

## Exact files changed, and why

- **`research_eval.py`** — the A15 door word SPENT at the runner (the coin
  the A19 and A20 reports named unspent). `run_one` gained a fourth,
  OPTIONAL, trailing parameter `query=None` (existing callers — main's loop,
  A20's driver idiom — ride byte-compatible):
  (a) the query rides the SEARCH alone (`rquery or qtext`, the door's own
  `or q` shape adopted whole); (b) the QUESTION rides the record, the
  door-body and the pipeline's road BYTE-FOR-BYTE, never overwritten;
  (c) the door-body gains the A15 `"query"` key ONLY where a query was
  spoken (no key, no claim, where none rode); (d) two TRUTHFUL RECORDS: the
  eval record's `web` block gains `"query": pk.get("query")` (the packet's
  OWN word — what ACTUALLY rode; in the fallback case it speaks the
  question's bytes, inspectable, not assumed), and the door-record gains
  `"query": (tr.get("web") or {}).get("query")` (the A15 trace stamp verbatim,
  a `tr.get` in the A18 idiom — on a fold the key rides as ABSENCE (`None`)
  beside `web_stamped False`, never promoted; the over-budget branch, which
  never calls the door, stays sparse with no query key); (e) malformed input
  is guarded at the runner (not a string, empty, all-space → the fallback
  road, the door never sees the garbage, no raise); (f) `main` passes
  `q.get("query")` — the frozen EA-0.1 fixture carries NO query word, so
  main's six questions ride today's road byte-exact; (g) the readable print
  line gained `| query:` (nothing pins the print; serialization byte-
  undisturbed). NO rewriting, NO extra model call, NO new provider
  behavior, NO touch of the evidence-status or promotion POLICY.
- **`tests.py`** — three new witnesses at the tail (T164–T166), A-era seam
  idiom: canned packets canned, a recording door-spy, the real
  `to_rows`/`corroboration` on canned bytes, and a raising seam
  (`_boom22`) left standing so the suite stays net-free past them. No prior
  expectation MOVED — T159/T160/T161/T162/T163 ride byte-unchanged (T161's
  pinned key-set holds because the query key is conditional on a spoken
  query).
- New UNTRACKED artifacts (the §'s deliverables): this report,
  `a22-eval-design.md`, `research-eval-a22.json` (EA-A22.0.1 — the frozen
  cases/queries, written BEFORE the run), and six clearly-named
  `research-hold/a22-*.json` (the probe, the machine-readable envelope,
  four per-case raw records). Nothing historical moved.

## Tests — exact commands and results

- `.venv/bin/python3 -B tests.py` — baseline entering A22 **163/163 —
  HARNESS GREEN**; after the implementation splice **166/166 — HARNESS
  GREEN**; at the close **166/166 — HARNESS GREEN**. (The harness is one
  frozen file; the focused A22 witnesses are T164–T166, all green within
  the full rides.)
- `.venv/bin/python3 -B retrieval_battery.py` and
  `.venv/bin/python3 -B integrity_battery.py` — both rode; integrity
  **18/18** at both rides; every witness line printed `ok`; the batteries'
  named-boundaries tails are their own designed verdicts (no red).

## The three new witnesses, in one line each

- **T164** — the runner separates and tells the truth: no-query rides
  exactly today's road (T161's two-key body and seven-key record byte-
  undisturbed; the fallback spoken at the packet's word); an explicit
  query reaches the search (the spy HEARS the query), rides the door-body
  beside the UNTOUCHED question, and lands byte-exact in BOTH records
  (`web.query` from the packet's word, `door.query` from the trace's stamp
  verbatim; exactly one additive key); the A19 selector still says the
  record's word; the JSON round-trips. Separation is not support.
- **T165** — the query word moves neither the status law nor the old
  shapes: the fold's shape rides the query key as ABSENCE (`None`) with
  `web_stamped False` (never promoted to the caller's bytes), the compound
  word rides VERBATIM, the selector says it unmoved; search-only still
  grows no door record (yet its `web.query` still names the query that
  rode) and says NO-DOOR; the over-budget lane stays sparse (the door
  CALLED ZERO TIMES at the query road — the branch coins no door word);
  A18/A19 propagation and selection byte-UNMOVED.
- **T166** — degenerate words ride the fallback, not a crash: `""`,
  `"   "`, and `5` each send the QUESTION's bytes to the search, leave the
  body two-key and the door-record seven-key (the garbage never reaches
  the door), and raise nothing; the frozen A5 fixture (read through the
  runner's own loader) carries no query word at any question, so main's
  road is today's road byte-exact.

## Adversarial regression audit (Phase 2) — every case at deterministic fixtures

| failure case | classification | where the witness rides |
|---|---|---|
| search returns NO results | correctly handled | A19 T163's emptiness arm; live C3/C4: the fold phrase + compound word; A22 adds the truthful ABSENCE at `door.query` (T165) while `web.query` still names what rode |
| search FAILS (HTTP/provider) | correctly handled | A19 T163's `research failed (search-http-503)`; T165 proves the shape unmoved by the query word. Known limitation inherited: the FAILED arm's LIVE sighting is still NONE (the A20 word stands; today's run had no failed search) |
| results but NO readable evidence | correctly handled (A12/T153 level/kind law; A15's INCONCLUSIVE/provider-words-only arms T159–T161); untouched by A22 |
| readable evidence IRRELEVANT | known limitation (predates A22): the status word speaks READ, not ABOUT — no machine weighs aboutness; A22 neither worsens it nor claims it fixed |
| evidence CONFLICTING | known limitation, honestly laned: `conflict` rides at the packet (observed `"insufficient"` at C1/C2); resolution stays UNRESOLVED (EA3's expectation), no new claim |
| answer rides UNRELATED SHELF CONTEXT | uncovered (by design): live 6-gram check — C2's response shares ZERO six-grams with the READ window, its three hits are SNIPPET-only (A13.3's headline-numbers-on-snippets finding, RE-MET on the separated road); the machinery's job (speak what rode) did its job — claim-level entailment remains the human's, PENDING |
| record lacks STATUS or QUERY metadata | correctly handled: absent words ride as ABSENCE/absence-words (T161/T162; T165), never a lean toward verified |
| explicit query MALFORMED | correctly handled (T166): the runner guards; the door's OWN A15 road stays byte-frozen (T160) — no scope creep |

**No actual regression was observed** — twice 166/166, no prior pin moved,
no evidence-status or promotion POLICY changed (nothing was tuned to make
a test pass; the only added key is the §'s required record of the actual
query). One disclosed asymmetry: the record's `web.query` rides ALWAYS
(it is the truth of the eval's OWN search), while the door-record's
`door.query` rides ONLY where a query was spoken — deliberate, so existing
readers of the A20-shaped record see no new word where none rode.

## The controlled live evaluation (Phases 3–4) — it RAN, and why it could

It ran because Phases 1–2 passed at fixtures and the runner's existing
road supports the comparison safely: the §-blessed A20 invocation idiom
(`run_one(qtext, live, caps)` per case, caps verbatim from the frozen doc)
now carries the 4th argument — `main` was NOT ridden, so the fixed
`a5-eval-live.json`/`a5-eval-search.json` bytes did not move, and no
historical artifact moved (`a20-eval-live.json` included). A search-level
LIVENESS PROBE rode first (an out-of-fixture word `dhamma`: empty,
`search-empty` in 0.6 s — emptiness is DATA; a laned FAILURE would have
VOIDED the comparison) and was written as its own artifact.

The law held: 4 cases (the cap), ONE attempt each (4 of 8), retride
reserved for runtime errors — and NO retride was spent (zero raises, zero
errors; two emptinesses are lane-words, not errors). No unbounded retries.
Total wall-clock 175.1 s, provider `ddg-ia` throughout, no key words
printed.

| | C1 (retitled green) | C2 (separated query, green SENTENCE-question) | C3 (nonsense, same-bytes query) | C4 (the control, no query word) |
|---|---|---|---|---|
| elapsed | 53.2 s | 61.2 s | 30.0 s | 30.2 s |
| results / gaps | 5 / `[]` | 5 / `[]` | 0 / `[search-empty]` | 0 / `[search-empty]` |
| readable evidence | 1 READ page (`wikipedia.org`) + 4 snippet/attribution | same shape | none (emptiness) | none (emptiness) |
| status word (verbatim, all three homes) | `carried by: wikipedia.org (read)` | `carried by: wikipedia.org (read)` | `general knowledge, not verified this turn (the web brought nothing (search-empty))` | same compound word |
| actual query, at the record | `Edicts of Ashoka` (= spoken; ≠ question) | `Ashoka rock edict` (= spoken; ≠ question) | `Zzzyx plingworth` (= spoken = question bytes, SPEAKEN not fallback) | the question's OWN bytes (the fallback SPOKEN at the packet) |
| door-query (trace stamp) | `Edicts of Ashoka` + web-stamped | `Ashoka rock edict` + web-stamped | `None` (the A22 abstinence, with web-stamped False) | NO KEY at all (no word spoken) |
| model calls | 3 ≤ 8 | 3 ≤ 8 | 2 ≤ 8 | 2 ≤ 8 |

All four frozen mechanical criteria (M1–M4, `a22-eval-design.md`) hold for
every case at the WRITTEN artifacts. The A15/A19 lane laws held live: the
two green turns' answers are RECITATIONS carried by the read page, the
two emptiness turns minted no citation, and NOTHING reached a promotion
it never earned. The same-family review stands (the GPT key absent — no
independent model judged the child); a plausible answer is nowhere called
a supported one.

## Phase 5 — the explicit answers

1. **Query separation worked mechanically?** Yes — three dry witnesses and
   four live cases, byte-exact at both roads and both records.
2. **Did the intended query actually reach retrieval?** Yes — the door-spy
   HEARD the query (T164); live, the packet's own recorded query equals the
   spoken bytes, the trace stamp repeats it, and the door's own web leg
   turned GREEN at the separated query for C2 while the SENTENCE-question
   alone (C4, same minutes, same provider) came back EMPTY.
3. **Evidence quality?** IMPROVED for the separated case (C2's query road
   carried 5 results with a read window where the bare sentence has now
   emptied FOUR live sightings: A13.1, A13.4, A20, C4); UNCHANGED for C1/C3
   (their lanes held); no case worsened. Counted, not judged: the
   improvement is at the RETRIEVAL axis, and n=1 per case on one
   provider-day.
4. **Answers better supported by readable evidence?** Not claimable:
   C2's response shares NO six-grams with the read window (3 snippet-only
   hits — A13.3's shape re-met); C1's partly rides the read window (4
   hits) and partly the snippets (6) — the A20 finding again. The
   machinery's support-disclosure improved (the words now name carriers
   AND the query); the claims' entailment is still the human's, PENDING.
5. **Status reporting truthful?** Yes — verbatim at record, line and file
   on all four; the emptiness compound rode both emptiness turns; the
   failure arm rode no live traffic (as at A20 — still deterministic-pinned
   only); the A22 word never leaned toward verified.
6. **Regressions?** None observed: suite twice 166/166 (entered 163/163),
   prior pins unmoved, policies untouched, A20/A5/A13 bytes unmoved, and
   `git diff --name-only` shows the seven founder entries clean.
7. **Supported conclusions:** the A15 door word now rides END-TO-END at the
   eval road; the record SAYS what rode (both fallback and separated, both
   modes); degenerate queries fall back without crashing or reaching the
   door; on one provider-day the two-word-name query carried evidence
   where the sentence-question did not — observed, not proof of
   generalization; the A18/A19 propagation and selection survive the new
   road at the live byte.
8. **Unknowns:** the real-world truth of C1/C2's answers (human fact-check
   pending); day-to-day drift (single provider-day, RESULTS_N=5 cap,
   `ddg-ia` only); whether an independent reviewer agrees (GPT key absent);
   the failure arm's live sighting (still none); claim entailment itself.
9. **Is A23 justified?** Yes, narrowly, at whatever the founder picks from
   what this run RE-MET rather than invented: (a) the snippet-vs-read
   dependence at the mouth (A13.3's coin — the response bytes rode the
   provider's index words, not the read window), or (b) a drift-stability
   ride of the SAME frozen bytes on a later day (the design anticipated
   it; no tuning), or (c) the A19/A20 `indep`-adjacent print tuning — a
   one-field coin, not an architecture change. This § did not begin it.

## State, at the close

HEAD unchanged (`1c7a74c`); the seven founder-staged entries byte-exact
and staged, with NOTHING unstaged beneath them; the A22 diff surface is
exactly `research_eval.py` (+35/−5) and `tests.py`
(+193, additions only); every historical report and `research-hold/*`
artifact rides untracked exactly as found; `Seyruna/`, `Paper Website/`,
CORAL and Eshkol untouched; no dependency added; no deploy; no production
touch. **Status: A22 COMPLETE.**
