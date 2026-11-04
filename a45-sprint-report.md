# A45 - spelling-aware addressing reclassification, offline (closed 2026-11-04, from 6d3a4a3)

## The one line
Under a law frozen before its own application, the held A44 bytes -
**unchanged, byte-for-byte** - address the question: the complete-token
rule recognises **`Asoka` three times** and `ashoka` never, so the
addressing test flips from **FAIL (literal substring)** to **PASS
(declared variants)**, and the reclassification word flips from
**EVIDENCE-GAP** to **EVIDENCE-BACKED**. A44's recorded OFF-QUESTION /
EVIDENCE-GAP is **not rewritten**: it is the *original* law's word over
the same bytes and it stands beside the new one. Nothing else moves -
publisher diversity, corroboration, EA1's classification and semantic
improvement are all exactly as A44 left them. Zero searches, zero
network, zero source reads.

## The two laws, side by side
| | original (A44) | new (A45) |
| --- | --- | --- |
| implementation | `'ashoka' in text.lower()` - literal substring | complete ASCII-letter tokens, case-folded, closed list |
| variants | `ashoka` | `ashoka`, `asoka` |
| `ashoka` hits | 0 | 0 |
| `asoka` hits | (substring: 3, but irrelevant to the rule) | 3 |
| matched surfaces | - | `Asoka`, `Asoka`, `Asoka` (the third is the possessive `Asoka's`, matched by its head token) |
| addressing | **FAIL** | **PASS** |
| experiment word | **EVIDENCE-GAP** | **EVIDENCE-BACKED** |

The implementing code of the new law is a **narrowly scoped test-only
addition** inside T198; `research_eval.py`, `web_research.py` and
`stages.py` are untouched (the original `answer42` default is
**proven unmoved** by the test). No production code changed.

## The nine required statements

1. **Held evidence and digest verified - yes.** A44's manifest verifies
   5/5 at disk **and** at `HEAD`; the artifact digest
   `9d8de2c6…`, the read-row digest `f65805a6…`, the text digest
   `07ba9f34…` and the 1200-char length all recompute against the held
   record; the bytes are the recorded `colostate.edu` read at HTTP 200.
2. **The new law was frozen before reclassification - yes.** Contract
   digest `387bd6a1…` (canonical policy JSON) was committed as `cdbf5dc`
   *before* the token application. Honest caveat: the substring counts
   `3 / 0` were already public in A44's record before A45 existed; what
   A45 froze first is the token-boundary law, the surface inventory and
   the classification word.
3. **The spelling-aware rule matched - yes.** Complete-token matches:
   `asoka` **3**, `ashoka` **0**. All three surfaces are `Asoka`,
   including the possessive `Asoka's` (its head token `Asoka` matches;
   the trailing `s` is a separate token by the declared rule).
4. **The new rule changes the experiment-level addressing classification
   - yes.** Addressing flips to PASS and the experiment word flips to
   EVIDENCE-BACKED, because the read still satisfies A40 §6's other
   conditions (status 200, ≥60 chars, publisher outside the house).
   A44's own record is **not** rewritten.
5. **Does this show a generalizable spelling-law improvement - no.** One
   page, one spelling pair, one closed variant list. T198 proves the
   *semantics* (e.g. `Asokan`/`Ashokan` deliberately do **not** match),
   not generality. No claim is made that the variant list is complete,
   or that other sources would behave the same.
6. **Publisher diversity changes - no.** No new bytes were read, so the
   read population is identical to A44's (2 read publishers,
   `wikipedia.org` and `colostate.edu`).
7. **Independent corroboration demonstrated - no.** The table is
   recomputed and **equals A44's**: independence `candidate`, ladder
   `unknown`, levels **DIVERSITY-ONLY**. A spelling match is not
   corroboration, and an addressing-positive word is not a truth or
   relevance claim.
8. **EA1's classification changes - no.** A42 PARTIAL, A43
   EVIDENCE-GAP, A44 EVIDENCE-GAP all stand byte-identical; A45's
   EVIDENCE-BACKED is a **replay-level** word about the addressing law,
   not a revision of EA1.
9. **Semantic improvement measurable - no, UNKNOWN.** No answer-leg;
   one held page; no performance claim.

## Does the new law fix the demonstrated false negative?
**Yes, narrowly.** A44's only blocking failure was the literal spelling
test: the bytes named the subject as `Asoka`, a standard variant. Under
the frozen complete-token law that specific false negative disappears
(addressing PASS). What it does **not** fix: whether the source's claims
are true, whether it is independent of the other read, whether the
extract cap hides qualifying text, or whether other spellings
(`Ashokan`, `Piyadasi`) should ever count - those are separate questions
and are not claimed here.

## What remains unknown
- Whether any held read *corroborates* another; the ladder still speaks
  `unknown`.
- Whether EA1's answer improves; no answer-leg.
- Whether the variant list is adequate beyond this page.
- Whether the extract cap (1200 chars) truncated content that would
  change any count - all counts are counts **within the window**.

## Next justified experiment
The evidence line now has two read voices and an addressing-positive
law; the binding constraint is **corroboration**, not addressing. The
next justified experiment is the one A43/A44 already pointed at: a
**declared shared-claim comparison** between the two *held* reads
(wikipedia + colostate), frozen before it runs and computed **offline
over held bytes with zero new reads** - specifying, in advance, what
counts as a shared claim (a token/phrase overlap law, its floor, and its
ceiling), so the ladder's `unknown` is tested by a declared instrument
rather than inferred. Only after that would a fresh **one-read**
contract for row 5 (`digitallylearn.com`) add a third voice.

## Verification
- `python3 tests.py` -> **198/198 pass - HARNESS GREEN** (T167-T197
  whole, no existing assertion touched).
- Retrieval and integrity batteries: see closeout.
- Contract digest recomputed from its block: `387bd6a1…`.
- A42/A43/A44 artifacts byte-identical; `config.json` unchanged.
- Manifest: 5 files at committed bytes; local commits only; tracked tree
  clean; nothing pushed.
