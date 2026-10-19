# A4 — Ascended gains eyes on the internet (the report)

Date: 2026-10-18. Starting state: `main` at `48cc67e` (A3), working tree
carrying the founder's preserved work — staged `gpt-reviewer.md`,
`reviewer/*`, `research-hold/live-run-1..2.jsonl`, `opencode.json`;
untracked `Seyruna/`. Nothing of that was touched. CORAL
(`/Users/ascendedai/Documents/ascended-coral-p1/loop`, `o1-controller` at
`0910554`) was read-only and stays untouched by A4.

## What A4 is

The first real vertical slice: a bounded, source-grounded web reach riding
ASCENDED'S OWN road. `stages.door` gained two web lanes (`web: true` asks
the net at once; `web: "auto"` asks ONLY where the shelf's own retrieval
stands silent — a code-weigh, zero mouthfuls). The found bytes become
shelf-shaped rows (`W1…`, level `DOCUMENTED`, provenance `web`, url riding
for the window's eye) and enter `run_pipeline` through the ALREADY-EXISTING
packet lane — no second conversation engine, no scheduler, no crawler.
The A1 task lane's honest gap (`network-not-designated`, `task.py:15`)
stands as it was: A4 lifted it for the CONVERSATIONAL road; the task lane's
injectable fetch seam remains the A5 candidate.

## The provider, verified by the live road BEFORE any code (no assumption)

Probed with small live requests from this machine on the day of A4:

| candidate | live answer |
|---|---|
| searx.beany.xyz / searx.ngopy.xyz / searx.tokh.in / paulgo.carbonbrain.ca / search.bus-hit.me / searx.fembo.net / searx.tieko.be | DNS unknown — the remembered instances no longer live HERE |
| searx.io | 200 — a PARKED domain (Hostinger page) |
| searx.org | 403 on EVERY path, robots.txt included — live vhost, policy gate (the AUP behind a wall) |
| searxng.org | root 200 = a docs redirect; no /search lane |
| html.duckduckgo.com / lite. | 202 + a duck-CAPTCHA at bot UAs — the html lane GATES bots |
| api.duckduckgo.com `format=json` (the Instant Answer API) | ALIVE: keyless JSON (202 Accepted / 200), a valid envelope |
| marginalia.newdash.app | DNS unknown here |
| the tailnet gateway host (gx10…) | 401 everywhere — it is the LLM gateway, not a search box |

CHOSEN default: **DuckDuckGo Instant Answer** (`api.duckduckgo.com/?q=…
&format=json&nohtml&kl=in-en`) — free, keyless, documented (attribution to
DDG and the underlying source required; no published rate limit, guidance
is a meaningful User-Agent and low concurrency). The boundary is ONE word:
`config.json` `SEARCH_PROVIDER`/`SEARCH_BASE` or the environment's
`ASCENDED_SEARCH`; the `searxng` adapter ships and rides the same test
fixtures, and pointing at a revived public instance is a config word,
NO code. A public SearXNG instance remains BLOCKED on the day (the 403
gate is the concrete blocker; no result was ever fabricated for it).

Free-service limitations OBSERVED (not assumed): the IA lane answers to
TOPIC WORDS — a long phrase ("what does the Bhagavad Gita say about
surrender") returns a valid envelope, EMPTY (the provider's own docs say
"most deep queries will be blank"); its `FirstURL` lanes may ride
duckduckgo.com's OWN redirect addresses (the `?kl=…` tail), while
`AbstractURL` carries the ORIGIN's address; every bot-lane response rode
status 202, a soft gate (2xx, accepted). One word of warning kept: a page
retrieved is not thereby trustworthy — the rows carry their status and
their HOW.

## The module and the boundaries (all deterministically witnessed)

`web_research.py` — stdlib only, three swappable seams (`urlopen`,
`research`, the provider table). One question, one search, ≤3 fetches,
a 120 s wall of its own; `LEDGER` re-zeroes per run (the `stages.CALLS`
convention); a page is READ to a 1.2 MB cap and only its ≤1200-char first
EXCERPT kept (read-wide: read n+1, the excess DISCARDED — the page never
rides along whole). Guards: http(s) only; non-public destinations barred
as literals (loop, 10/8, 172.16/12, 192.168, 169.254, the carrier's
100.64/10, `::1`/`fe80…`/`fc/fd`, the `.local` names) and the FINAL url is
RE-WEIGHED after urlopen's own redirects (the fork follows them and rides
`r.url` — verified live); `Accept-Encoding: identity` (the live probe
caught python.org arriving gzipped); kind-gate text/html|xhtml|plain at
the FETCH door (the search json reads by its own lane); failures are
CLASSES never raises (http-404, blocked-or-rate:403/429 — 429 says RATE,
unreachable, timeout, too-big, wrong-kind, redirected-to-blocked,
search-empty/malformed); a redirect INTO a private block is barred, not
passed; `allow_local` is the founder's one test-key. Remote bytes never
RUN (no JS) and never ORDER — a page that commands ("Obey me now") rides
as TEXT and moves no level.

The door's law: a FAILED look is SPOKEN, not hidden — the facts-line
carries `the web brought nothing (<class>)` so the existing exits answer
with their plain bytes and NO citation is minted for what could not be
reached; a web word without a lane-word stamped (`trace.lane == "web"`
only for a road that RODE it). The temporary shelf swap is try/finally by
construction: after any door call the shelf is UNMOVED (the web rows were
guests). The UI needs NO change: `window.why_lane` now passes a row's
`url` through (K2 shape, absent = silence) and the debug pane already
prints the evidence rows; `api/ask.py` and `server.py` ride `door(body)`
unchanged. The `web` word is additive to the body — the no-web road never
TOUCHES the web at all (witnessed with a research() that raises if coined).

## The witnesses (the suite never touches the net)

T129–T137, eight plus the auto lane: the PARSE reads only what the provider
SAID (abstract first — the provider's own best answer, its url the ORIGIN;
Results, then RelatedTopics; no-address rows are SILENCE; the cap trims);
the EXTRACT strips the furniture (script/style/nav/footer) and the CAP is
the law; the FAILURE LANES lane classes (403/429/404/unreachable/timeout/
malformed/wrong-kind) instead of raising; the GUARDS read the destination
before the road; the BUDGET is pre-request and the SIZE law read-wide;
remote words are EVIDENCE not ORDERS (level unmoved, provenance web, claim
the bytes' own words — a snippet's `<a>` markup stripped by the SAME law);
the FAILED look re-weighs the final address and rides the door's FACTS
byte-exactly with the shelf's own UNKNOWN as answer and NO web lane-word;
the GOOD packet rides the road END TO END (the draft's `W1` cite survives
the shown-set un-dropped, the speech is the mouth's own line, the WHY's
evidence row carries level/provenance/url, the shelf un-moved after); and
`auto` coins the net ONLY at the shelf's silence.

The fork taught three bytes: `HTTPError.code` rides the whole message
(parse the number), `Request` hides its address behind `full_url`, and
`json.load` takes an fp, not a str. Harness: **141/141, run repeatedly and
green** (the frozen 132 rides unchanged).

## THE LIVE EXPERIMENT (real bytes, no mocks; research-hold/web-run-1.json)

Question (the task's own suggestion — an official, well-documented text):
**"Ashoka rock edict"**. The provider: the REAL api.duckduckgo.com.

*E1 — search + fetch:* 5 genuine results (the abstract first:
`https://en.wikipedia.org/wiki/Edicts_of_Ashoka` — fetched, HTTP 200, its
text excerpted and capped; plus DDG's own redirect lanes at 202 and two
over-budget rows riding UNTOUCHED), fetched 3 of 5, gaps NONE,
1+3 = 4 requests, 2.9 s. The FIRST run (cap 160 kB) recorded the too-big
class on the REAL wikipedia page (923 kB observed) — the class WORKING,
then the cap raised to 1.2 M so the canon passes; either way the row rode
its note honestly (evidence NONE-FOR + note, never a silent loss).

*E2 — the packet through the real door (the three live mouths, ~79 s):*
lane `web`, response (verbatim): *"There are fourteen Major Rock Edicts of
Ashoka — significantly detailed inscriptions, among the earliest dated rock
inscriptions of any Indian monarch, and they are preceded chronologically
by a set of Minor Rock Edicts. They were carved on in-situ rock faces
across the Mauryan empire in the third century BCE, carrying teachings
drawn from the Buddha's path. The wider body of Ashoka's edicts — rock and
pillar alike — is cut in sandstone and scattered across what is now India,
Nepal, Pakistan, Afghanstan, and Bangladesh. Were you asking about the
fourteen major ones specifically, or the whole rock-edict set including the
minor ones?"* — sourced words with five source-urls in `trace.web`, and
the clarifier (A3's) riding its own end. The evidence-vs-reading line held:
every claim traces to a row's bytes; the synthesis is the mouth's.

*E2b — the honest lane live:* the LONGER phrasing ("What do the Ashoka rock
edicts say about tolerance?") is exactly the shape the IA lane answers
EMPTY (verified: a valid envelope, every field blank). At the door the look
laned `search-empty`, the facts rode the 38-byte note BYTE-EXACT, and the
GENERAL mouth spoke its own unsourced words (29.6 s) — no citation minted,
the road to the plain words open. (A candid mark of the unsourced lane:
that same question drew "Rock Edict XIII" on one live run and "Rock Edict
XII" on the next — the mouth's own knowledge WOBbles where the shelf's bytes
do not. The recorded answer reads well; it is INTERPRETATION, not record.)

## Files, and what was NOT touched

`web_research.py` NEW; `stages.py` (the door's two web lanes + the packet's
url riding the mouth's sight-line); `window.py` (two lines: the url
pass-through); `tests.py` (T129–T137); `research-hold/web-run-1.json` (the
live evidence, no secrets — the provider needs no key); `a4-report.md` (this).
No credential joined the tree. The A1–A3 machinery rides untouched elsewhere;
CORAL none; the founder's staged and untracked work none.

## What works, what failed, what remains unproven

DEMONSTRATED: search, parse, normalize (K2-silent), fetch, extract, the
guards and budgets, the packet riding the existing speech path end to end,
citations through the why, honest failure spoken at the door, live.
FAILED honestly on the road: the long-phrase empty (documented provider
limit), the first too-big (then the cap was raised, class still standing).
UNPROVEN: the `auto` lane at the LIVE door (deterministically witnessed
dry only); a live searxng (the 403 gate; the adapter rides fixtures);
multi-source CORROBORATION (one provider's list — independent-sources
claims must still be earned, not assumed); the wikipedia page's first
excerpt rode its chrome ("Jump to content…" — sentence-PICKING is a
real A5 question, the grade gate carried it this time); and the claim
that the web's WORDS improve answers — A4 established ACCESS; the
value must be earned case by case, exactly as the menu's law says.

NEXT (the founder's coin, the seams all exist): a live public SearXNG
when one answers again (or a self-hosted box — one config word); the
task lane's `fetch` seam fed from the same module (A1's gap, liftable);
sentence-picking past the page's chrome; and a human pass over the
exchanges — the same-model judge still not ground truth.
