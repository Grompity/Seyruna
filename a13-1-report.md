# A13.1 — Isolating the Empty-Search Failure

## State before the probes

HEAD `9c352bd` (A12), main; the tree exactly as A13 left it — founder's
staged bridge set and `opencode.json` staged, `Seyruna/` and the A8–A13
artifacts untracked, CORAL unmoved, **no reset, no clean, no stash, no
staging, no commit, no deploy, no code touched** (the probe is a run, not a
change). The A13 report and the provider's bytes were read first: the
supported lane is `search(query)` — a LANED WORD for every failure class
(`search-http-*`, `search-unreachable`, `search-timeout`,
`search-malformed`, `search-too-big`, `search-empty`) and a raise that
never travels — with `research()` the runner's own supported web-phase
call (the `--search` mode rides it). Probes were ridden at `research()`:
the narrowest supported layer that exercises the real provider end to
end. HTTP status and content-type are **not exposed** at this layer — the
lane word is (recorded as such below, not guessed over).

## The four attempts (the two required, then two bounded context probes — three searches total were budgeted as "no retry storm", and nothing was retried)

Configuration identical throughout: provider `ddg-ia`, the config's default
base, `RESULTS_N = 5`. Raw bytes: `research-hold/a13-1-probe-live.json`.

| attempt | query | outcome | results | spent |
|---|---|---|---|---|
| required 1 | `What do Ashoka's surviving edicts tell us about his rule and his concept of dhamma?` | `search-empty` | 0 | search 1, fetch 0, 0.5 s |
| required 2 | `Ashoka rock edicts inscriptions dhamma Maurya` | **`search-empty`** | 0 | search 1, fetch 0, 0.4 s |
| context 3 | `Ashoka` (the A7-smoke-era shape, one word) | no gap | **2** RelatedTopics rows (duckduckgo.com stubs, `related` lane — attribution rows, as A7's law says) | search 1, fetch 0 |
| context 4 | `Magna Carta` (a plain control topic) | no gap | **3** stubs | search 1, fetch 0 |

Transport was fast and clean for every attempt (~0.4-0.5 s); nothing
raised; nothing retried; zero fetch coins moved (the picker spent none
where rows existed, A7's law intact). The door was NOT re-ridden — this
probe isolates the search lane, not the mouths; no extra work beyond each
`research()` call's own was performed (recorded in `spent`).

## Answers, in the §'s own order

1. **Did the keyword twin behave differently?** **No — and that IS the
   result.** The twin went empty exactly like the sentence. The
   A13.1 hypothesis — "the lane answers keywords but not NL questions" —
   is **FALSIFIED by its own test**: the keyword shape it names as the
   working one was empty too.
2. **Did either return a usable result?** Neither of the two required
   queries. But the two bounded context probes answer the REAL question
   the falsification raises: single-word `Ashoka` still returns stubs, and
   so does a plain control topic — the lane is ALIVE and still serving.
3. **What this establishes / leaves unknown.** Established, at bytes this
   hour: the lane's RelatedTopics service answers topic-SHAPED queries one
   and two words deep (`Ashoka` two rows, `Magna Carta` three), and as of
   this hour empties on longer keyword-piles and sentences with `[]
   RelatedTopics` on a clean fast response.
   The A-series' green history was NOT all one-word: A5's own live bytes
   gave FIVE results for the three-word `Ashoka rock edict` and three for
   the two-word `Kalama Sutta`. The lane answers when the query wears the
   shape of a TOPIC NAME — one, two, and on A5's day even three words — and
   empties at a keywords-pile or a sentence. Unknown, disclosed: the
   raw HTTP status/content-type (not exposed at the supported layer — the
   "200 json with empty RelatedTopics" reading is inferred from the clean
   fast `search-empty` lane word, no exception class behind it); whether A5's
   green three-word `Ashoka rock edict` would ride green TODAY (not
   re-ridden here); locale (`kl=in-en`)
   sensitivity; and whether the service is merely having a quieter hour.
4. **Query sensitivity, provider limitation, network, or inconclusive?**
   **Not network** (fast clean lanes throughout, controls green in the same
   minutes). **Not the A13.1 version of query sensitivity** (the twin fell
   too). It is a **provider-shape limitation** — the lane now answers only
   one-word topics — which is ALSO the sharpest query-sensitivity fact yet
   established: the service's notion of a "query" is a topic NAME, not a
   question and not a search-string. A13's aggregate reading ("the lane
   answers keyword-shaped words") needs its own correction: the shape that
   works is *name-shape* — five keywords died while a two-word name lived;
   the law is topic-shape, with a length tolerance that A5's bytes once
   stretched to three words.
5. **The one next step justified by these bytes** (not taken here): a
   single bounded probe at the EXACT words A5's live bytes saw green —
   `Ashoka rock edict` — at the same supported layer: it sits exactly on
   the line today's bytes drew (name-shape short green; keyword-piles and
   sentences empty) and one run says whether the lane NARROWED since A5's
   day or whether name-shape was always the law. A fix, a
   provider change, and any re-benchmark all stay the founder's coins.

## Verification, kept apart from the probe's findings

Deterministic suite untouched by A13.1 and green at the close:
**158/158** (one run; suite-truth and experiment-truth reported apart). The
protected state stands: the staged bridge set and `opencode.json` as found,
`Seyruna/` and the A8–A12 artifacts untracked, and A13.1's two new files
(`a13-1-report.md`, `research-hold/a13-1-probe-live.json`) untracked per the
milestone's command. The GPT key remains absent (`OPENAI_API_KEY`
inspected, false). The transport/results/evidence three-way is respected
throughout: a fast clean 200-shaped GET is NOT a search result, and neither
is it evidence — and here, this hour, five of five multi-word words got
nothing at all.
