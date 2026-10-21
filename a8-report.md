# a8-report.md — A8: First Live Witness (bounded provider experiment)

## The state (start, and end — verified not assumed)

Start HEAD `5febe1f` (A7) on `main`; working tree exactly the founder's
shape: staged reviewer bridge (`gpt-reviewer.md`, `reviewer/reviewer_*.py`,
`selftest.py`), modified-staged `opencode.json`, two `live-run-*.jsonl`,
untracked `Seyruna/`. Test baseline confirmed before the experiment:
**153/153 exit 0**. Config mechanism read at the bytes, not from memory:
`provider_name()` rides `ASCENDED_SEARCH` env → `stages.CONFIG["SEARCH_
PROVIDER"]` → default; the provider BASE rides **only** `config.json`'s
`SEARCH_BASE` (no env home exists today) — relevant to §5, unused today.

## The experiment (bounded by law: one request per instance, no retries,
no fan-out, no rotating pool)

The documented directory (`https://searx.space/`, read through the house's
own `fetch` — guards, caps, timeout) answered with 200 and, in its own
bytes, **exactly two instance URLs** beside a 69-online-instance health
table: **baresearch.org** and **libresearch.space**. The selection (§3's
"at most two") was therefore FORCED by the directory itself — both were
probed, one JSON search each for the fixed stable-fact query
**"Ashoka rock edicts"**, strict 10 s timeout, house cap/UA/context:

| endpoint | HTTP | content-type | body | secs | outcome |
|---|---|---|---|---|---|
| baresearch.org/search?…format=json | 200 | **text/html** (JSON asked) | *"Making sure you're not a bot!"* | 0.3 | CHALLENGE — stop |
| libresearch.space/search?…format=json | 200 | **text/html** (JSON asked) | *same challenge, same second* | 0.3 | CHALLENGE — stop |

Through the house path both lane as `search-malformed` (`json.loads` over
the challenge page) — A7/A4's design kept whole at the live edge: **a laned
class, zero fabricated sources**. The two walls, one second apart and
byte-identical in shape, read as shared middleware at the instances' default
posture, not two independent refusals — disclosed, not concluded. The
A4-era memory of instances (DNS-dead/parked/403-behind-an-AUP) is
consistent: today's instance family answers a *polite* wall (200 + HTML)
where A4's met a loud one (403). Raw bytes ride
`research-hold/a8-probe-live.json` (held, live-observed, distinct from the
synthetic fixtures).

## The witness, criterion by criterion (§4, pre-defined)

| # | criterion | status |
|---|---|---|
| 1 | real live search response from the configured provider | **FAILS at the entry** — an HTTP answer arrived (200), but no SEARCH response: JSON was requested, a bot-challenge HTML came |
| 2 | ≥2 distinct publishers after A7 normalization | unreachable (no results parsed) |
| 3 | both publishers' passages FETCHED and READ | unreachable |
| 4 | both passages supplied through the existing evidence pipeline | unreachable |
| 5 | relevance to one clear claim | unreachable |
| 6 | A7 accounting labels honestly; bytes-agreement ≠ entailment | not exercised (no evidence to label) |
| 7 | trace makes identities and kinds inspectable | not exercised (lane-word only) |

**The blocking pipeline stage is exact: `search()`'s network boundary — the
request was ACCEPTED (200) and the response DECLINED to be JSON, upstream
of `results_from`, upstream of the A7 picker, upstream of every fetch,
upstream of every accounting word.** No partial-success shape (independent
results, failed fetches) arose: the road stopped before results existed.
The door run (§6) was conditional on a working endpoint; none worked, so
the door did not ride the searxng road — and it will not be reported as if
it had.

## The verdict, against the pre-set bar (no redefinition)

**Honest blocker (the second branch of "done").** No live `candidate`
witness was produced; the reason is a real HTTP outcome (200-at-a-challenge
at each instance, 0.3 s each, no retry burned) at a precisely named stage.
What A7's report *predicted* as a possibility — "if the public instances
prove as dead as A4 found them, the blocker belongs to the provider
market" — is now observed from the inside: the instances are ALIVE (they
answer in 0.3 s) and the JSON lane is WALLED for an unknown bot. The
accounting layer was never reached, and A8 does not pretend it was tested.

## Numbers, files, safety

- Tests: baseline **153/153** → final **153/153** (no code moved; the run is
  the evidence line, not a change).
- **No code change and no commit were made** — §7's own instruction: an
  experiment that yields only diagnostic evidence leaves it as a report
  and earns no ceremonial commit. The two A8 artifacts
  (`a8-report.md`, `research-hold/a8-probe-live.json`) ride UNTRACKED in
  the tree, the exact way the founder's bridge rode A1–A5, until the
  founder reviews them (a future commit may fold them in whatever shape
  he prefers — A6/A7 precedent: a real change carries its report in).
- The GPT reviewer **did not run** (`OPENAI_API_KEY` still absent; no
  output observed; the claim is the absence, not a substitute).
- Founder-owned staged files untouched (nothing staged, unstaged, or
  committed today); `Seyruna/` untracked as found; CORAL unmoved
  (`0910554`); no reset/clean/stash/rewrite; no credential read or written;
  total live footprint: 5 GETs (3 directory inspections — one tripped a
  too-small probe cap and the `too-big` word rode, no retry — + 2 probes),
  zero POSTs, zero retries.

## Recommended next action (the smallest move)

**One declared UA experiment — a NEW experiment, not a retry of this
one:** a single request to ONE instance carrying a browser-ish
`User-Agent` (SearXNG's bot-wall is UA/behavior-shaped; the house's is
`AscendedResearchBot/0.1`, and §3's law rightly forbade wearing that as a
retry today). If the wall still stands, the keyless-multi-source blocker
is the provider market's and gets written as such, and the road forks
toward the founder's other coins (the GPT key; or the A4-noted lane that
lifts the A1 task-lane `fetch` seam). If the wall falls, A8's seven
criteria get their full check at the door with `SEARCH_BASE` (and, if the
founder wants env-only play, the one-line `ASCENDED_SEARCH_BASE` home in
`search_url` — the one code change A8 did NOT need and therefore did not
make, per its own law).

## Founder-facing summary

**Live-observed:** both instances listed by the official directory are
alive and fast but answer the house's bot at the JSON lane with a
bot-challenge page (200 + HTML, 0.3 s each, one pass each).
**Deterministic:** nothing moved — 153/153 before and after; the challenge
lanes through the existing `search-malformed` class exactly as the A4/A7
laws designed (no raise, no fabricated source).
**Claimed:** the blocker is provider-shape, precisely located upstream of
every A7 organ; a candidate witness is a declared-UA request away.
**Not claimed:** no door turn on the new provider, no GPT review, no test
delta, no `candidate` word earned, and no instance-market conclusion from
n=2 beyond "the wall is there".
