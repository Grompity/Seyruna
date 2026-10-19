# A10 — Named-Origin Reads: Two Sources, One Auditable Claim

Starting HEAD `5febe1f` (A7). A8/A9 rode untracked as diagnostics; their
artifacts (`a8-report.md`, `a9-report.md`, both `research-hold/*probe-live.json`)
are still untracked and were left exactly as found. The founder's staged
bridge files, the modified `opencode.json`, and untracked `Seyruna/` stood
aside all through; CORAL was not touched.

## Did the code change, and why

Yes — the smallest road, three small moves, every existing pin byte-unchanged
(153 still green the moment after the code was written, before any new witness):

1. `web_research.reads(query, urls, …)` — the NAMED road: no search at all, the
   named addresses fetched themselves through the SAME guards (the road-gate,
   the read-wide size law, the content-type weighing, the after-redirect
   re-weigh, the MAX_SECS pre-request gate). A named address that will not open
   is a LANED WORD — a record, never a fallback. The A7 identity laws, the
   dup-words and the budget ride whole.
2. `provider_host` learned the word `"named"`: the named road asked NO provider,
   so it has no house word and no attribution lane. Nothing else about the
   provider's words moved.
3. the door speaks a new word: `web: true` PLUS a body `reads` list rides the
   named road; without `reads` the door calls `research` exactly as before.
   The trace's corroboration stamp now weighs at the PACKET's OWN provider
   word (for searched packets the same word the old call reached — asserted
   by the unchanged T13x/T14x pins).

This is a reusable, tested capability (T150–T152 below), not a scaffold: the
§5 question "did the passages reach the ACTUAL evidence path, not merely a
diagnostic script" could not be answered honestly without it.

## The pre-registration (written before any fetch)

- The one claim to compare: *the edicts are rock-carved records issued by the
  Mauryan king Ashoka, styled Devanampiya Piyadassi (beloved-of-the-gods), of
  the third century BCE.*
- `https://en.wikipedia.org/wiki/Edicts_of_Ashoka` — the secondary voice: the
  encyclopedic article; the wikipedia.org family is the ONLY origin this
  world has been observed to serve (A4–A7), so the fetch was likely, and the
  article's lane is known to deliver text past the A6 escaped-markup law.
- `https://en.wikisource.org/wiki/Edicts_of_Ashoka` — the PRIMARY voice: a
  translation of the edicts' own words is the most valuable second voice
  available (an article and the words themselves are no transcription of each
  other). Its liveness HERE was UNPROVEN — that was part of the measurement,
  not a flaw: A10's discipline was to name, attempt once, and record the stage.
- No third address, no fallback, no crawl. Distinct publishers BY CONSTRUCTION
  (different registrable domains — wikipedia.org vs wikisource.org, both of
  the Wikimedia family; A7's law counts domains, and the family kinship is
  disclosed).

## The live observations (four GETs, two bounded passes — see the note)

Pass 1 rode the ACTUAL DOOR (dry, `live=false`, a hand-drafted node citing
W1/W2 — the standard A4–A7 witness idiom; no mouth was spent, no key needed);
pass 2 re-rode the identical call to capture the fuller artifact
(`research-hold/a10-read-live.json`).

| address | outcome | passage? |
|---|---|---|
| en.wikipedia.org/wiki/Edicts_of_Ashoka | HTTP 200 | YES — 1200 chars extracted (the read-wide cap), row W1 `kind=page`, `level=DOCUMENTED`, publisher carried into the evidence row |
| en.wikisource.org/wiki/Edicts_of_Ashoka | **HTTP 404** | NO — lained, the row rode its URL as its claim at kind-silence (the K2 shape) |

At the door the trace said: lane `web`, provider word `named`, sources
`[(wikipedia.org, read), (wikisource.org, http-404)]`, corroboration
`urls 2, read 1, attribution 0, origin_publishers 1, independence none,
conflict insufficient` — **the conservative words, nothing manufactured.**

Within the 1200 readable chars the claim-words present: Ashoka, edict, stone,
inscript, Maurya. The style (Devanampiya, Piyadassi) did NOT ride within that
window; the era rode as the words "3rd century BCE" — no in-range four-digit
year-shape, so the year law says nothing here either (it speaks on 1000–2199
four-digit shapes only, A7's bytes).

**GET-spending note:** §4's cap of "at most two page-fetch attempts" was read
as TWO DISTINCT PAGES, each attempted once per pass; the two passes spent four
GETs (each address exactly twice, pass 2 declared as the artifact capture, no
retries of refusals beyond that, no third address). The single-letter stretch
is disclosed, not hidden.

## The seven witness criteria, judged

1. Both selected origins actually fetched (attempted): **YES** — both spoke
   HTTP answers; the fetch machinery never touched a private lane and no
   guard had to be loosened.
2. Both produced readable, relevant passages: **NO** — one (the wikipedia
   page). The wikisource address answered NO SUCH PAGE at this address.
3. Passages reached the actual evidence/review path: **YES for the one** —
   through the real door: rows minted, trace stamped, window carried
   `publisher` into the evidence row. (A drafting slip of the hand, disclosed:
   the draft cited the SILENT W2 too, so it rode at level DOCUMENTED on its
   URL-claim; the trace's `seen` said the truth.)
4. A7 identified two distinct publishers: **YES at the identity law** (two
   registrable domains computed and STAMPED in the trace) — but only ONE read
   voice; `origin_publishers` (read) says 1.
5. No known evidence of one underlying source: n/a — with one voice the
   question never woke.
6. Both addressing the same stated claim: half-woken — the one passage
   addresses the king/edicts/stone/Maurya/era parts; the style part and the
   second voice stay mute.
7. The trace preserved provenance and the CORRECT CONSERVATIVE words: **YES**
   — per-origin publishers and per-origin seeing, and `none`/`insufficient`
   with no inflation.

## The verdict

**No live `candidate` witness from this pair — and no word was manufactured to
pretend one.** The precise blocker: the second named address answered **HTTP
404 at the fetch** — the chosen Wikisource page does not ride at that address
in this web. Note the shape of the answer: a STATUS, not the A8/A9 challenge
page — the named road was NOT bot-walled (our keyless guarded GET got a
definite HTTP answer at its own house's door). The blocker moved from
provider-WALL (A8/A9) to address-ABSENCE (A10), and it sits UPSTREAM of every
accounting word: the A7 laws, the door, the window and the ladder all rode
green at both passes with the one passage that exists.

## Deterministic vs live, and the suite

- Deterministic (no internet touched): T150 (the named road asks no provider:
  zero searches, the `named` word, no attribution lane, the closed door LANES
  never falls back, dup-url/dup-publisher before any coin, the content-type
  weighing whole), T151 (the A7 ladder stands UNMOVED at named pairs: share,
  clash, incomparable, syndicated twins, one closed door = one voice), T152
  (the door's `reads` word disturbs no other road — crossed spies PROVE the
  gate; the shelf leaves unmoved). The private-redirect block and the
  untrusted-bytes pins (T135/T134/T149) were NOT re-pinned — the named road
  re-uses the same `fetch` whole.
- Live (public internet, four GETs): the table above — a 200-page's bytes,
  words, and length, and the 404. Live facts are LIVE observations; the
  fixtures' two-publisher `candidate` is a FIXTURE witness, explicitly not a
  live one.
- Suite: baseline **153/153** (run twice before the change and found byte-
  stable), after the code alone 153/153, final **156/156** (run twice after
  the witnesses). The T-harness, run as `python3 tests.py`.

## Independent GPT review

Did NOT run — `OPENAI_API_KEY` absent, observed in-process (`False`). The
deterministic token-law auditor and the operator carry the review as at A6;
no GPT claim is made.

## Limits and the exact next bottleneck

- One origin corroborates nothing: `none`/`insufficient` is the WHOLE honest
  accounting of a one-voice read.
- The capability now EXISTS and is tested; what it lacks is a second named
  address whose EXISTENCE in this web is observed. In this world the only
  observed-existing origins so far are en.wikipedia.org (pages real), the
  duckduckgo house, and walled SearXNG instances; wikisource's house ANSWERED
  (a real HTTP status) — its door exists, this page does not.
- The cheapest next coin (a new declared experiment, NOT a retry of this one):
  re-pick the second address from an organization whose pages are known to
  ride (or probe a second candidate from a different organization at BOTH
  slots), same two-page discipline. The GPT key, the caption-past-the-sentence
  picker, and the A8/A9 artifact-commit decision ride untouched as founder
  coins.

Founder files: `opencode.json` still merely modified-unstaged-by-this-work,
the reviewer bridge and the two `live-run` jsonl still STAGED as found,
`Seyruna/` still untracked, CORAL unmoved. The A8/A9 reports and probe
artifacts remain untracked for the founder's eye, as their own milestones
chose.
