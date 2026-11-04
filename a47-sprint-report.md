# A47 - held-source provenance probe, offline (closed 2026-11-04, from b85c451)

## The one line
The two held windows are **provenance-asymmetric**. C states a visible chain:
a *present rendering* whose **compiler is Ven. S. Dhammika**, which is
**"based on earlier translations"**, quotes **H.G. Wells**, and names
**"Buddhist literature"** as the carrier of the conversion legend. W states
**three bare citation markers `[1] [2] [3]`** and **no named authority at
all** - its reference targets lie outside the 1,200-character window.
Because W's chain cannot be reconstructed, the frozen precedence yields
**ATTRIBUTION-CHAIN-INCOMPLETE**: no shared attribution can be shown, no
distinct attribution can be shown, and independence stays **UNKNOWN**.
A46's claim counts and the DIVERSITY-ONLY ladder are unchanged.

## Frozen extraction and classification rules
Committed before extraction (`d923a13f…`):
- **Signals** carry source, verbatim excerpt, offset, category and
  `nature` (EXPLICIT text vs INFERRED analyst relation). Six categories:
  citation marker; attribution phrase (closed list); named authority;
  named work/body; quotation; reliance statement. Citation markers are
  matched by regex `\[\s*\d+\s*\]`; phrases from a closed list of ten.
- **Subject exclusion:** the historical subject (Ashoka) is never counted
  as a source.
- **No invention:** incomplete markers are not expanded; links are not
  followed.
- **Truncation rule:** absence in a capped window is not evidence of
  absence.
- **Classification vocabulary** with pre-declared requirements and a
  precedence in which DISTINCT requires **both** chains reconstructable.
- **Ceiling:** independence can never be promoted to ESTABLISHED here.

## Exact signals and offsets
| id | src | category | excerpt | offset |
| --- | --- | --- | --- | --- |
| W-M1 | W | CITATION-MARKER | `[ 1 ]` | 453-458 |
| W-M2 | W | CITATION-MARKER | `[ 2 ]` | 926-931 |
| W-M3 | W | CITATION-MARKER | `[ 3 ]` | 1073-1078 |
| W-P6 | W | ATTRIBUTION-PHRASE | `attributed to` | 335-348 |
| C-A1 | C | NAMED-AUTHORITY | `The British historian H.G. Wells has written:` | 139-184 |
| C-A2 | C | QUOTATION | `Amidst the tens of thousands ... shines almost alone, a star.` | 186-332 |
| C-A3 | C | NAMED-WORK-OR-BODY | `Buddhist literature preserved the legend of this ruler` | 343-397 |
| C-A5 | C | NAMED-WORK-OR-BODY | `The present rendering of these edicts` | 818-855 |
| C-A4 | C | RELIANCE-STATEMENT | `based on earlier translations` | 857-886 |
| C-A6 | C | NAMED-AUTHORITY | `The Australian bhikkhu Ven. S. Dhammika, the compiler of the present work` | 1099-1172 |
| C-A7 | C | ATTRIBUTION-PHRASE | `preserved the legend` | 363-383 |
| + 6 closed-list phrase hits in C | | ATTRIBUTION-PHRASE | `has written`, `preserved the legend`, `based on`, `earlier translations`, `the compiler`, `present rendering` | various |

16 signals total (4 W, 12 C), all verbatim and re-locatable. One
pre-commit correction removed a signal that had misclassified the
*subject* as a named authority (annotation only; no chain or
classification changed).

## The visible chains
**W (wikipedia):** article text → `[1] [2] [3]` → **referents NOT VISIBLE**
(the window ends mid-sentence at "that a comple…"). The only attribution
phrase, "attributed to Emperor Ashoka…", concerns authorship of the
*edicts*, not the article's sourcing. **Chain unreconstructable.**

**C (colostate):** "the present rendering of these edicts" → compiler
**Ven. S. Dhammika** → **"earlier translations"** (unnamed) → quoted
authority **H.G. Wells**; plus **"Buddhist literature"** as carrier of the
legend. Missing links: translator/work unnamed; Dhammika's work title and
the Wells citation are outside the window; the sentence is cut after
"spiritual director…". **Chain partially reconstructable.**

## Shared or distinct
- **Shared named authorities/works: none.** W names no authority inside
  the window, so nothing can be shared.
- **Distinct stated attributions: not demonstrable** - the vocabulary
  requires *both* chains reconstructable, and W's is not.
- The asymmetry itself is the finding: the two windows do **not** provide
  comparable provenance.

## Classification
**`ATTRIBUTION-CHAIN-INCOMPLETE`** (frozen precedence: shared = no;
possible shared derivation = no visible connection; incomplete = yes;
distinct = no; unknown = no, because signals exist).

## Independence ceiling and ladder
Independence: **UNKNOWN, not promoted**. Distinct stated chains would not
have sufficed either; here even those are not visible. Publisher,
editorial, source and observational independence remain
**undifferentiated and unknown**. The corroboration ladder stays
**DIVERSITY-ONLY**. A46's 2 AGREEMENT / 2 PARTIAL / 9 NO-MATCH stands
unchanged; EA1 unchanged; semantic improvement **UNKNOWN**.

## The twelve required statements
1. **Held evidence verified - yes.** A42-A46 manifests at their own
   commits; all held artifacts disk==HEAD; both windows match A46's
   digests and 1,200-char cap.
2. **Contract frozen before analysis - yes** (`d923a13f…`, commit `0d27a93`).
3. **Every extracted signal** - 16, with offsets, in the table above and
   in `research-hold/a47-provenance.json`.
4. **W chain** - article → three markers → targets not visible;
   **unreconstructable**.
5. **C chain** - rendering → Dhammika → "earlier translations" → Wells;
   plus "Buddhist literature"; **partially reconstructable**.
6. **Shared named authorities** - **none**.
7. **Shared derivation suspected** - **no visible evidence**; not
   asserted, not excluded.
8. **Distinct stated chains visible** - **not demonstrable** (W's chain is
   incomplete).
9. **Genuine source independence established** - **no**, and this
   experiment cannot promote it.
10. **A46 claim-agreement findings change** - **no**.
11. **Corroboration ladder changes** - **no**; DIVERSITY-ONLY.
12. **What remains unknown because of truncation** - W's three reference
    targets; C's translator(s) and work title; whether the two texts share
    an underlying corpus; whether the agreements derive from shared
    scholarship.

## Next justified experiment
The blocker is W's invisible reference targets. The next justified
experiment is a **new frozen one-read contract** for a *different extract
window of the same W URL* (the reference-bearing region) - explicitly a
**new live observation**, declared before its bytes, with its own budget
and restoration path; it is *not* a replay and must not be treated as one.
Alternative: the third-voice row-5 read, which adds a source but does not
resolve W's chain. Until then, independence stays **UNKNOWN**.

## Verification
- `python3 tests.py` -> **200/200 pass - HARNESS GREEN** (T167-T199 whole).
- Retrieval exit 0, integrity 18/18, bridge 19/19, all `.py` compile.
- Contract digest recomputed from its block: `d923a13f…`.
- A42-A46 artifacts byte-identical; `config.json` unchanged.
- Manifest: 5 files at committed bytes; local commits only; tracked tree
  clean; nothing pushed.
