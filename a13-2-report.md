# A13.2 — Historical Query Boundary Probe (one search, the exact A5 word)

## State and bounds honored

HEAD `9c352bd` (unchanged through A13.2 — the probe is a run, not a
change); the founder's seven staged entries (bridge set + `opencode.json`)
as found, `Seyruna/` and the A8–A13 artifacts untracked, CORAL unmoved;
no reset, clean, stash, staging, or commit; the supported road
(`web_research.research`, the runner's own web-phase call) with its normal
guards; **exactly one search attempt, no retries, no extra controls.**
The A13.1 report and the A5 live record were inspected first: the exact
word `Ashoka rock edict` carried `results: 5, gaps: []` there — five rows,
of which the historical bytes show ONE fetched wikipedia page (`http 200`,
the capped-truncation marker) and FOUR duckduckgo.com stubs (two at a
curious `http 202` note, two noteless).

## What the one probe returned (raw: `research-hold/a13-2-probe-live.json`)

Provider `ddg-ia`, its configured default, `RESULTS_N = 5`. Outcome:
**`ok: True`, FIVE results, `gaps: []`**, spent `{search: 1, fetch: 2,
calls: 3}`, wall 2.4 s — no failure class, no empty set, no raise (and the
lane distinguishes a raise from an emptiness by words, never by
exception). The transport truth the supported layer exposes is exactly
this: lane words, the per-row `note` for fetched rows, and the ledger —
no raw status or content-type is exposed for the un-fetched rows, and none
is inferred.

Row by row, at the table's words (the evidence-table shape, mapped through
`to_rows`, pure, no extra GET):

| row | kind | level | evidence | publisher | note | usable passage? |
|---|---|---|---|---|---|---|
| W1 | page | DOCUMENTED | PRESENT | wikipedia.org | `http 200 (capped)` | **YES** — the Edicts_of_Ashoka page, read, its first passage minted |
| W2 | snippet | DOCUMENTED | (none) | duckduckgo.com | `http 202` | no — fetched, furniture-only bytes (the A12 emptiness shape) |
| W3 | snippet | DOCUMENTED | NONE-FOR | duckduckgo.com | `not-fetched:dup-publisher` | no |
| W4 | snippet | DOCUMENTED | NONE-FOR | duckduckgo.com | `not-fetched:dup-publisher` | no |
| W5 | snippet | DOCUMENTED | NONE-FOR | duckduckgo.com | `not-fetched:dup-publisher` | no |

The corroboration words the packet earns: `urls 5, read 1, attribution 4,
origin_publishers 1, independence none, conflict insufficient` — A7's law
riding EXACTLY as designed: the four house-lane stubs weighed as
ATTRIBUTION, not origins; the one true origin (wikipedia) stands voiceless
against itself; no word inflated.

## The comparison the milestone asked for

- **Against A5's historical record:** identical shape and set — same page,
  same four stubs, the same `202` curiosity, same count. Five-for-five,
  the lane did NOT narrow since A5's day.
- **Against A13.1:** the open question — "did the lane narrow, or was
  name-shape always the law?" — resolves to the second: the law is
  **name-shape with a tolerance**, and the three-word `Ashoka rock edict`
  (which A13.1's own bytes could not predict either way) rides green. The
  five-keyword pile and the twenty-word sentence remain the empty shapes;
  a two-word name (`Magna Carta`) rode green at A13.1's context probes.

## What this establishes, what remains unknown

**Establishes:** the current lane answers the historical word at full
strength; one readable, provenance-carrying passage (`W1`, page-level,
`PRESENT`) reaches the evidence table through the real `to_rows` with
publisher, kind, level, and the truncation marker intact; the house-stub
rows are correctly weighed as attribution (not corroboration), and the
picker spent exactly two coins — one origin page, one at the house's own
porch (which came back furniture-only, the A12 emptiness word at a `202`
status, disclosed and not hidden) — before spending NONE on the three
dup-publisher stubs, A7's law at bytes.

**Unknown:** what the `202` at the house's stub-door means (a queue? an
as-accepted stub page? — not exposed, not guessed); whether a sentence
carrying the SAME name-shape ("Ashoka rock edict"-sized) would also ride
(the empty shapes were a five-keyword pile and a full question — a
short name-bearing sentence is the gap in the evidence); and, as ever at
this lane, the raw status/content-type of the un-fetched rows.

## The one next step, per the §'s first branch (results returned)

They DID progress to usable, provenance-preserving evidence at the table
— so the single justified next step is the last unridden mile: **ride the
ACTUAL door once (dry or live mouth, the A13-era call) with this very
green word, and see the ANSWER it speaks with a real read passage on the
shelf** — the first end-to-end turn (lane green → fetch → rows → trace →
speech) this lane has been given since the A5 day, and the one that turns
"results exist" into "answers ride them."

## Kept apart: the tests

The deterministic suite rides **158/158** (run at the close; no code moved
— A13.2 touched no application bytes). Suite-status and experiment-finding
reported apart, as ever. The GPT key stays absent (`OPENAI_API_KEY`
inspected); the two A13.2 files (`a13-2-report.md`,
`research-hold/a13-2-probe-live.json`) ride untracked per command. Final
HEAD `9c352bd`.
