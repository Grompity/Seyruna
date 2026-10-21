# A11 — First Live Two-Publisher Witness

Starting HEAD `26c6f63` (A10). Final HEAD: **`26c6f63` — unchanged.**
A11 was diagnostic-only: the live experiment revealed no defect in the
machinery (its verdict below), so per A10's rule (no ceremonial commit) this
report and `research-hold/a11-read-live.json` ride UNTRACKED for the
founder's eye, as A8/A9's did. Founder state byte-exact throughout: the
staged reviewer bridge and its two `live-run` jsonl, `opencode.json`
modified-staged, `Seyruna/` untracked, CORAL unmoved.

## The one experiment, bounded

Question (the milestone's): what do the historical sources establish about
Ashoka's use of edicts to communicate royal policy? The single compared
claim, pre-registered before any fetch: *Ashoka, Mauryan emperor of the
third century BCE, communicated royal policy through edicts inscribed on
rock.*

Road: `web_research.reads` (A10's named road) invoked THROUGH THE ACTUAL
DOOR (`web:true` + the `reads` list, dry, a hand-drafted node citing W1/W2 —
the A4–A10 witness idiom; no mouth spent, no key needed). Two pure
pass-through recorders watched the fetches and the packet; zero behavior
added; both stood down after.

GET ledger — **exactly two, one per address, no retries, no fallback, no
third address**:

| address | outcome | the exact stage |
|---|---|---|
| `en.wikipedia.org/wiki/Edicts_of_Ashoka` | HTTP 200 | read — 1200 chars through the extract law (the same bytes as A10: same window, same road) |
| `www.britannica.com/biography/Ashoka-Indian-emperor` | **HTTP 403** | lained `blocked-or-rate:403` at the FETCH — the house's own door refused; no extract ran |

`spent: {search 0, fetch 1, calls 2}` — the named road asked no provider
and wasted no coin, as the A10 law requires. Wall-clock 1.1 s.

## What the readable window actually says (no invented excerpts)

The scan words are substring-hits, disclosed for sloppiness (Sandstone
matches "stone"); this is an operator's word-scan, never a law-word:

- wikipedia.org window — present: `edict`, `inscription`, `stone`,
  **`policy`**, **`dharma`**, `emperor`, `ashoka`, `maurya`, `3rd century`.
  Absent: `proclam`, `rock` (as that word), `king`, the style words
  (Devanampiya/Piyadassi — outside the read window). **The window carries
  the claim on BOTH its sides**: the edicts/inscriptions/stone side AND,
  within these same 1200 chars, the words `policy` and `dharma` — A10's
  scan simply never asked for them (the bytes are the bytes; only the
  question changed). No in-range four-digit year-shape, so the A7 year law
  stays silent — the era rides as the WORDS "3rd century BCE".
- britannica.com — silent (403). No passage, no words; its evidence row
  rode its URL as its claim at kind-silence (the K2 shape). Disclosed
  drafting slip of the hand, as at A10: the draft cited W2 too, so it rode
  level DOCUMENTED on that URL-claim while the trace told the truth.

## The trace's own words (the auditable record)

lane `web`, provider word `named`, sources
`[(wikipedia.org, read), (britannica.com, blocked-or-rate:403)]` —
the per-source `seen` word for britannica IS the lane word itself.
corroboration `urls 2, read 1, attribution 0, origin_publishers 1,
independence none, conflict insufficient, publishers_seen 2, duplication 0`.
Every origin, publisher, passage kind and per-origin `seen` preserved end
to end; the shelf left unmoved (dry idiom).

## The witness standard, criterion by criterion

1. Both pages fetched AND readable: **NO** — one read, one refused (403).
2. Passages through the real evidence/review path: **YES for the one that
   spoke** — the actual door minted it (W1 `page` row), the window carried
   `publisher`, the trace stamped.
3. Publisher identity distinct and preserved end-to-end: **YES at the
   identity law and the stamp** — two registrable domains computed and
   traced — but ONE read voice.
4. Same specific claim (not mere topic): **half-woken** — the wikipedia
   side speaks the claim on both its sides (edicts-in-stone AND policy);
   the britannica side never arrived to be weighed.
5. Evidence supports the claim on BOTH sides: **fails** — one side silent.
6. No shared underlying source invalidating independence: n/a — with one
   voice the question never woke (no gram-overlap was computable; no two
   windows existed to overlap).
7. Trace preserves origins, publishers, kinds, `seen`: **YES** (printed
   above; the conservative words, nothing manufactured).

## The verdict

**No genuine live `candidate` yet.** The precise blocker, at its exact
stage: **the second named address answered HTTP 403 AT THE FETCH** — an
access refusal at britannica's own door (the A4 law word
`blocked-or-rate:403`, and note the law does not claim WHICH reason: its
own word admits rate or refusal; this shape reads as AUP/gate, the house's
policy, not Ascended's defect). The blocker's lineage across the trio:
A8/A9 a challenge PAGE at a provider's search road (identity-independent);
A10 a definite ABSENCE of the named page (404); A11 a definite REFUSAL at
the named house's door (403) — each time UPSTREAM of every A7 accounting
word, and each time the machinery rode green on whatever bytes existed,
with zero guard loosened, zero manufactured word. A10's own recommendation
had said the pair must come from an origin whose *servability* is observed
— wikipedia is; britannica now joins SearXNG in the refused column, at a
different stage (its page-level wall came at the page itself, not at a
search endpoint).

## Deterministic vs live, tests, review

- Deterministic suite UNTOUCHED: baseline 156/156 (green before, re-confirmed
  green at the end); no code changed, so no new fixtures were owed — and the
  A10 T150 already pins this very shape (a closed door LANES as a record and
  the other passage rides; independence none + insufficient) at a fixture —
  A11's contribution is that the SAME words were now witnessed on REAL bytes
  at a REAL refusal, through the real door.
- Live facts (the table above): four of them real observations — a 200 page's
  bytes, a 403, the lane-words, the 1.1-second wall. Nothing in the artifact
  is a fixture, nothing a fabricated excerpt.
- GPT review: did NOT run — `OPENAI_API_KEY` absent, inspected in the process
  environment, not assumed.

## Limitations and the exact next bottleneck (the founder's coin, one line)

One origin corroborates nothing; `none`/`insufficient` is the whole honest
accounting. The named road is proven ready; what it lacks is a SECOND
NAMED ADDRESS THAT BOTH ANSWERS AND EXISTS in this web — the two known
servable shapes so far are the wikipedia family (200s) and refused doors
(SearXNG's wall at search, britannica's 403 at the page). The smallest next
declared experiment: probe a THIRD family's servability at a single named
page-level GET first - two wikipedia-family addresses would be ONE voice
under the A7 law, so the second address must earn its slot - and only
then spend a two-address pair. Stopping here as the milestone commands:
no A12, no provider-discovery campaign.
