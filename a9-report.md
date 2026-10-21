# a9-report.md — A9: One Last Declared-User-Agent Probe

## State (inspected, not assumed)

Start HEAD `5febe1f` (A7) — unchanged by A8, and A9 moves it not at all.
The working tree held exactly A8's recorded shape: the founder's staged
reviewer bridge and modified-staged `opencode.json`, `Seyruna/` untracked,
A8's two untracked diagnostics (`a8-report.md`,
`research-hold/a8-probe-live.json`) present, the A8 bytes on disk matching
A8's report (two instances, two challenges, 200-at-`text/html`, 0.3 s each).
Baseline re-confirmed before the probe: **153/153 exit 0**; re-run after:
**153/153** (the rerun is the record line — no code moved, and none did).
`UA = "AscendedResearchBot/0.1 (self; A4 bounded research)"` — the house
request identity — read at the bytes before the experiment, as required.

## The one experiment

**Instance:** `libresearch.space` — one of A8's two walled instances; the
pick declared ARBITRARY (the identity law is not instance-specific).
**Fixed query:** `Ashoka rock edicts`. **Only the User-Agent moved:**

`Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (like Gecko) AscendedProbe/0.9 Safari/537.36`

— conventional in shape, TRUTHFUL by its own token (the probe declares
itself; the house does not masquerade). No cookies added, no rotation, no
challenge-solving, the same `Accept` (JSON-first), the same house context,
the same `MAX_BYTES`, a strict 10 s timeout, and `safe_target` weighing the
address before the road (`(True, None)`).

**Honesty of the count:** the experiment cost **two HTTP calls** — the first
response was captured with its status, type, and size but its BODY BYTES
WERE READ-THEN-DROPPED by a slip in the probe script itself (a double
`read` emptied the stream). The bytes are the observation §3 requires, so
the same request rode once more with the bytes kept. The slip is disclosed
as a slip: a re-sent AMBIGUOUS-200, not a retry of a refusal (the no-evasion
law stands). Had either call returned a refusal, the run would have
stopped then and there — it did not.

## The observation (facts first)

| field | value |
|---|---|
| timestamp | recorded in `research-hold/a9-probe-live.json` |
| instance | `libresearch.space` |
| query | `Ashoka rock edicts` (`format=json` asked) |
| User-Agent | the Mozilla-shaped string above (call 2, and call 1 identical) |
| HTTP | **200**, content-type **text/html** (not JSON), **7170 bytes**, **0.4 s** then **0.3 s** |
| body | `<!doctype html>… <title>Making sure you're not a bot!</title>` — the CHALLENGE, IDENTICAL page, IDENTICAL size to A8's |
| valid SearXNG JSON? | no — the JSON lane never opened |
| results / publishers | 0 / none (nothing to normalize) |

**The response is a bot challenge.** It is not valid SearXNG JSON and it is
not an ordinary results-page (the byte-shape distinguishes them; here the
title speaks). 403/429 did not appear; the wall is the polite shape: a
welcome 200 that declines to answer the format word.

## §4 or §5? The challenge-remains branch, stated as §5 says

§4's branch (valid JSON) did not open: no witness is claimed (a valid
search response alone would not be one anyway — and here there was not
even that). Per §5, recorded exactly in its words:

> the challenge remained… the default request identity **was not the sole
> demonstrated cause of the failure** — and no conclusion may reach that
> every SearXNG instance, or the whole provider market, is unavailable.

Two instances (A8) plus one (A9) — the same-second, byte-identical walls
read as shared instance-family middleware. **Which** property the wall keys
at is NOT established: cookies, TLS fingerprint, HTTP version, and a
JS-challenge posture were all untouched by law (the no-evasion list: no
CAPTCHA-solving, no spoof-auth, no rotation, no proxies). The probe's clean
claim is narrow and holds: **a bot-shaped UA and a browser-shaped UA are
answered the same way, so the house's request-identity is not the variable
that decides here.**

## Facts vs hypotheses (the report's own audit law)

- FACT (observed twice): 200 + `text/html` + the challenge title, 7170 bytes
  both times, sub-second, the same wall under both identities.
- FACT (design): nothing moved in code or tests (153/153 before and after —
  the actual rerun line, not a promise); A9's artifacts ride UNTRACKED for
  the founder's eye; nothing was staged, committed, stashed, or rewritten;
  CORAL unmoved.
- HYPOTHESIS (disclosed as such): the wall is instance-family default
  middleware (byte-identical pages, one second apart); the key property
  is still unknown (four candidate request-properties named, none touched).
- NOT concluded: that every instance walls; that the market is down; that
  any named property would have passed.

## The next milestone (the §5 recommendation, one step, not a strategy)

Stop probing public instances (§5's own direction: "a different retrieval
strategy rather than continuing public-instance probes") and move to a
**bounded named-origin read**: skip search entirely and FETCH a small,
NAMED set of public origins (≤2 pages, the A7 budget already fits), where
the publishers are distinct BY CONSTRUCTION and every house guard (size,
kind, private-address, redirect-reweigh) already applies. It is the
smallest road that can produce a genuine two-publisher READ — the thing
`candidate` actually requires — and it spends zero requests on a directory
that walls bots of every coat. The alternative flavor (a second bounded
query-shape at the working ddg-ia lane) rides behind it as the fallback if
the founder prefers to keep ONE provider word at the door. The GPT key and
the sentence-past-the-caption picker stay the founder's coins, unspent.

## A9 footprint, end to end

Two GETs, zero POSTs, zero retries-in-evasion, zero code lines moved, zero
commits; the single declared experiment answered its single declared
question: **the wall does not care who asks.**
