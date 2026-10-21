# A14 — Research Path Design Review (design-only; no code moved)

HEAD `9c352bd`, tree as the A-series left it (founder's seven staged
entries byte-for-byte, all A-era artifacts untracked, `Seyruna/` and CORAL
unmoved, nothing staged, committed, deployed). Suite green at the open:
**158/158**. No live search was run for this review; the findings below are
all at bytes already on disk.

## Current-state findings, tied to code and records

1. **The question IS the search query** (stages.py ~885: `pkt =
   web_research.research(q)` with `q = body["question"]`) — there is no
   separate query field, which is why A13.3 had to make the *word* be the
   question to ride green (its record names the deviation).
2. **The provider's lane answers topic-NAMES, not word-counts.** A13: eight
   sentences, eight `search-empty`. A13.1: the keyword twin died too (the
   hypothesis falsified by its own test); single- and two-word names lived.
   A13.2: the exact three-word historical `Ashoka rock edict` returned the
   full five-row set — the law is *name-shape with a small tolerance*;
   four-to-nine-word forms all lained empty (A13.4's live record). **A
   shorter query is NOT the fix** — a keywords-pile is still an empty
   shape; a NAME core is what the lane answers.
3. **The empty fold is exact at bytes** (stages.py ~893-899: the folded
   phrase *"the web brought nothing (…)"* rides the facts; no web stamp) —
   but A13.4 established at a live turn that the phrase never reaches the
   SPEECH: the mouth spoke a flat, confident 726-char telling of a turn
   that had read nothing.
4. **The general road already files its own status, comprehensively**
   (stages.py ~715-725): at a general turn the trace stamps `lane:
   general`, `lineage: "UNSOURCED"` (the EXISTING word), `unknown: True`,
   and `fires: ["GENERAL:UNSOURCED", …]` — the STATUS IS ALREADY COMPUTED;
   it simply stops at the trace.
5. **Read vs attribution is weighed exactly and silently** (A7's
   corroboration law at web_research ~455-487: attribution counts the
   provider's own house rows; independence counts only READ origins).
   A13.3's record is the live proof: the headline claim ("14 separate,
   significantly detailed") rode the provider's attribution SNIPPETS,
   `read 1, attribution 4` said the truth — and the answer's words did not
   say it.
6. **A12's law holds the failed/empty/label rows honest at the TABLE**
   (level tracks kind; provenance-only rows ride the enum's own UNKNOWN) —
   the table's words are right; the gap A13 exposed is that the table's
   words stop at the table (and the trace), not the speech.
7. **The mouth adds its own risk** (A13's Q8: a garbage delivery raised at
   the A3 guard; one bounded re-run rode) — any design that ADDS model
   calls adds instances of that risk; the caps are pre-request and would
   bound it.

## Design A — the question and the query, separated

**Where generated:** in `stages.door`'s web branch only (the one place
search is ridden — `web_research` needs to know nothing about who asked),
reading an optional body key: **`body["query"]`** (absent ⇒ query == the
question, the byte-unchanged today-road).

**Model call or deterministic?** **Deterministic first** — and honest about
what A13.1/2 actually license: the generator must return a *name-core*,
not a pile. The minimal law: take the question, drop leading
question-words and punctuation, and keep **at most the first short
name-phrase (2-3 words max, names and head-nouns only)** — e.g.
`What do Ashoka's rock edicts say about dhamma?` → `Ashoka rock edicts`
(NOT the four-keyword pile, which the lane has not been shown to answer).
A model-generated variant may exist behind the existing mouth road (the
door's mouths are already capped and audited), but it is NOT required
and it buys an extra Q8-shaped event per turn — a founder coin, not the
proposal's spine.

**The question stays the question:** the door never replaces `q` — the
query is an extra, parallel word; the mouth's road and the shelf speak to
the ORIGINAL words (A13.4's answer is proof the door's speech never needs
the query at all).

**Generation failure rides a LANED WORD, not a shrug:** a deterministic
generator that cannot carve a name (empty or longer-than-law result)
emits `query-none` and the door **falls back to the question itself** as
the search string — today's exact shape (A13.4's emptiness is the
no-loss floor, and the fold phrase already speaks it). A model variant
that returns bytes-not-JSON raises like A13's Q8 — the no-retry law
unchanged.

**No silent intent-change:** the trace gains one stamped word,
`trace["web"]["query"]`, beside the question — inspectable at the record
exactly as A13's records make every other word inspectable. The risk of
drift is then not trusted, it is SHOWN.

**Tested without inventing results:** fixtures at the door with a
recording search-spy (the A10/T152 idiom): (a) with `query` present, the
spy sees the QUERY and not the question; (b) the trace speaks the query
word; (c) with `query` absent, the spy sees the question — byte-identical
to today's calls. No fake results needed: the assertions are about the
STRING SENT, which is the whole design A.

## Design B — user-visible evidence honesty, at the smallest word

The status is already computed (finding 4): the proposal is therefore
**DISPLAY, not prose, and not a mouth**: `window.py` already builds the
shown record with a per-row levels/kinds distinction table — the
minimal change is to carry the ALREADY-STAMPED trace words into the
shown presentation: one status word chosen by deterministic law from the
turn's own bytes —

| turn's own words | shown status word (deterministic, no mouth) |
|---|---|
| packet read ≥1 origin | `carried by: <publisher(s)> (read)` |
| rows present, none read | `provider words only; no origin read` (the A13.3 disclosure-shape, computed from the corroboration words already in the trace) |
| empty fold (`search-empty` in the facts) | `the web brought nothing (search-empty)` — the house's OWN phrase, shown rather than folded away |
| `lineage: UNSOURCED` stamped | `general knowledge, not verified this turn` |

The ANSWER TEXT itself stays untouched (no refusal-by-design, no new
mouth, no new flake instance): the status rides beside the speech as the
record's word — the same shape the A6 review made for claims (a
machine-word under the speech, not a re-voicing of it). **Helpfulness is
preserved because nothing is subtracted from the telling; honesty is
preserved because a reader of the RECORD cannot mistake recall for
report** (A13.4's named weakness), and the A13.3 subtlety (a headline
carried by attribution-words) reaches the reader through row two of the
same table. If the founder later prefers the status IN the sentence, that
is prompt-tuning territory — explicitly not this proposal (non-goal:
tuning).

Claim-level attribution (each clause to its row) is the big-road
alternative — the proposal takes the STATUS-WORD road because it needs
no parser, no prompt change, and no model.

## Design C — the verification plan, split where the split is real

| # | case | mechanism | outcome expected |
|---|---|---|---|
| 1 | search yields usable evidence | door fixture + canned packet (page + stubs) | rows mint, `read ≥1`, status word names the READ publisher(s) |
| 2 | search returns empty | canned `gaps:["search-empty"]` | no web stamp, fold phrase shown as the status word, lane word rides |
| 3 | results exist, fetches fail | canned all-error packet | rows ride kind-silence + `NONE-FOR` + lane-word notes; A12's `UNKNOWN` levels; status word: `provider words only; no origin read` |
| 4 | a readable source supports only part of an answer | A13.3-shaped record audited claim-by-claim | code asserts rows/levels/words; **the claim-to-window match itself is model-quality — human review**, same-family labeled |
| 5 | attribution snippets are not independent read origins | canned multi-house-stub packet | `attribution` counts them, `origin_publishers` does not; independence stays `none` on one origin (A7's law, one new fixture at the door) |
| 6 | the answer communicates the right evidence status | the four status-shapes above as fixtures | the right word chosen from the right packet-shape — **automatable**; whether the word HELPS the reader — human review |

Automatable: 1, 2, 3, 5, and 6's WORD-CHOICE half (five deterministic
fixtures, the T-series idiom — call them T159+ when the coin is spent).
Human-review territory: 4 (claim-vs-window truth is the mouth's craft)
and 6's USEFULNESS half (does a reader understand the word) — plus the
standing truth that the mouth's own road can only be judged, never
asserted.

## Proposal, in one line, and its cost

**The smallest safe change:** an OPTIONAL `query` word at the door
(deterministic name-core derivation, trace-stamped, laned-word failure
that cannot go below today's no-loss floor) **plus** a deterministic
evidence-STATUS WORD displayed beside every answer from the words the
trace already stamps. **Files likely touched when spent:** `stages.py`
(the door's web branch reads the word and stamps it), `web_research.py`
(at most `research(query, …)`'s caller-side use — the function itself
already takes any string), `window.py` (one status word in the shown
record), `tests.py` (the five fixtures). No config, no new files, no
provider change. **Costs:** zero new model calls, zero new latency, zero
new resources for the proposal as drawn; the optional model-querier (a
coin, not the spine) would add one capped mouthful and one Q8-shaped
event-chance per turn.

## Risks, open questions, non-goals

- **Risk, query-shaped:** a deterministic stripper that builds a
  keywords-PILE where the lane wants a NAME (A13.1's law says short is not
  enough) — guarded by the 2-3-word name-phrase cap and shown, not
  trusted, at `trace["web"]["query"]`.
- **Risk, display-shaped:** a status word beside the speech may read as
  bureaucracy and be ignored — the same fate any `note` field has; the
  mitigation (nudge the mouth to speak it) is tuning, deliberately not
  taken here.
- **Open questions:** the lane's exact sentence-tolerance (the five-word
  `What do Ashoka's edicts say?` probe, unspent since A13.4); whether a
  real second-family name would ride green (the one `candidate`-witness
  coin, unspent); whether a model-made querier is worth a mouth at all.
- **Explicit non-goals:** provider swap; claim-level citations in prose;
  re-benchmarking against A13's eight (that baseline stands at its own
  record); any tuning against these very questions; any commit.

## State at delivery

Final HEAD `9c352bd` (unchanged by A14 — a review moves no bytes); the
tree as found plus this one untracked file; founder entries, `Seyruna/`,
CORAL, and every research artifact exactly as found; suite-status at the
open was 158/158, kept apart from design all along; the GPT key inspected
absent (a review written by the same brain that built the road, disclosed,
not independent). Stopping at the recommendation: spend the two coins
above or name the next probe — the review adds no code, no tuning, no
deployment, and no commit.
