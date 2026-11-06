# A49 - preserved-body citation replay (closed 2026-11-06, from c0d311d)

## The one line
The A48 window-selection defect is **repaired without a single network
call**: following the **actual DOM** - each marker's own superscript, its
literal `href`, the element bearing that exact fragment id, and that
element's enclosing `<li>` - all three of W's markers resolve. `[1]` is a
**partial** author-year footnote (`Le 2010, p. 30.`); `[2]` and `[3]` are
**complete** modern scholarly entries (Olivelle 2024; Singh 2008). **No W
entry names any of C's four signals.** The updated provenance class is
**DISTINCT-STATED-ATTRIBUTIONS**, which is explicitly **not** independence
- that stays **UNKNOWN**, and the ladder stays **DIVERSITY-ONLY**.

## 1. Contract
- Digest **`6c278f26…`** (canonical policy JSON), commit **`cf87585`**,
  committed **before** the body was parsed.
- It fixed the input path and full expected digest, the three markers with
  their A47 offsets, the DOM procedure, acceptance/failure words, the
  zero-network budget, and the preservation rules.

## 2. Verified input
- Path `research-hold/a48-w-body.html`, **925,008 bytes**.
- sha256 **`d45350ce045e5af55b0141f85099acac0ceea839b024e8c905bb986398546f8b`**
  - verified **before** parsing against A48's own recorded digest. Match.
- A48's result (acceptance **FAILED**) stands unchanged.

## 3. Zero network
Searches **0**, fetches **0**, requests **0**, source reads **0**,
link-follows **0**, alternate bodies **0**, substitutions **0**. The
reader's `LEDGER` is **0 before and 0 after** both the replay and its
offline test. The preserved body is the only input.

## 4. Marker → anchor → target

| marker | A47 offset | sup id (verbatim) | literal href | target id | target element | li span |
| --- | --- | --- | --- | --- | --- | --- |
| `[ 1 ]` | 453-458 | `cite_ref-FOOTNOTELe201030_1-0` (doc pos 146180) | `#cite_note-FOOTNOTELe201030-1` | `cite_note-FOOTNOTELe201030-1` | `<li>` | 496137-496675 |
| `[ 2 ]` | 926-931 | `cite_ref-2` (doc pos 147556) | `#cite_note-2` | `cite_note-2` | `<li>` | 496676-497672 |
| `[ 3 ]` | 1073-1078 | `cite_ref-3` (doc pos 147713) | `#cite_note-3` | `cite_note-3` | `<li>` | 497673-498623 |

Each marker had **exactly one** candidate superscript - no ambiguity. The
**numeric-id assumption is proven wrong**: `[1]`'s target is
`cite_note-FOOTNOTELe201030-1`, which no `#cite_note-1` construction would
have found. Raw `<li>` HTML is preserved verbatim in the artifact with its
own digest; normalized display text is kept **separate** from it.

## 5. Recovered entries (verbatim)

**`[1]`** - `↑ Le 2010 , p. 30.`
- Partial: author-year footnote. Its own text links onward to
  `#CITEREFLe2010` (recorded, **not followed** - outside the frozen step).
- Class: **UNCLEAR** (no title/work visible in the entry itself).

**`[2]`** - `↑ Olivelle, Patrick (2024). "Imperial ideology and religious
pluralism in the Asokan inscriptional corpus." Empires and Gods. The Role
of Religions in Imperial History . (Eds. Rüpke, Jörg & Biran, Michal &
Pines, Yuri, Berlim: Walter De Gruyter), p 27, https://archive.org/…`
- Complete. Explicit fields: author, year, chapter title, edited volume,
  editors, publisher, place, page, URL.
- Class: **SECONDARY-SCHOLARSHIP** (chapter in an edited scholarly volume).

**`[3]`** - `↑ Singh, Upinder (2008). A History of Ancient and Early
Medieval India: From the Stone Age to the 12th Century . Pearson Education
India. p. 351. ISBN 9788131711200 . Archived from the original on 2 July
2023…`
- Complete. Explicit fields: author, year, title, publisher, page, ISBN,
  archive and retrieval dates.
- Class: **SECONDARY-SCHOLARSHIP** (general history monograph).

## 6. Classes, from the entries' own words
| marker | completeness | class | basis |
| --- | --- | --- | --- |
| `[1]` | PARTIAL | UNCLEAR | author-year note only; work not in the entry |
| `[2]` | COMPLETE | SECONDARY-SCHOLARSHIP | scholarly chapter, named author/publisher/year |
| `[3]` | COMPLETE | SECONDARY-SCHOLARSHIP | history monograph, named author/publisher/year/ISBN |

No **primary edition/translation** of the edicts appears among the three.

## 7. Connections to C
C's preserved signals: **H.G. Wells**; **Dhammika / "the present
rendering"**; **"earlier translations"** (unnamed); **"Buddhist
literature"** (legend carrier).

All 12 marker × signal rows are **NO-VISIBLE-CONNECTION**. None of the
recovered entries contains "Wells", "Dhammika", "translat…" or
"Buddhist". For `[1]` the row is **NO-VISIBLE-CONNECTION on its visible
text only**, and its **work-level comparison is UNRESOLVED** because the
entry is partial: the full work is not visible.

**No connection is proposed**, because none is visible.

## 8. Updated provenance classification
**`DISTINCT-STATED-ATTRIBUTIONS`** - applied to the chain reconstruction
now in view, not retroactively to earlier records.
- W names accountable terminals: **Olivelle 2024**, **Singh 2008**, plus
  the partial **Le 2010** note.
- C names its own: **Dhammika**, **Wells**, unnamed **earlier
  translations**, **"Buddhist literature"**.
- The named sets are **disjoint**, and each chain is reconstructable to at
  least one named terminal - the frozen A47 requirement for DISTINCT.
- **A47 stands unchanged** for its own evidence (markers unresolved);
  **A48's FAILED acceptance stands** and is not rewritten. A49 improves the
  reconstruction, it does not edit history.

## 9. Independence and corroboration
**UNKNOWN - not promoted.** `DISTINCT` here means *different stated
attributions*, nothing more. It does **not** prove:
- that the works are editorially or institutionally independent;
- that they do not share underlying scholarship (both could draw on the
  same editions or the same earlier translations);
- independent **observation** of anything.

Publisher, editorial, source and observational independence remain four
separate, **undifferentiated** propositions. A46's 2 AGREEMENT / 2 PARTIAL
/ 9 NO-MATCH stand; EA1 stands; semantic improvement stays **UNKNOWN**
(no answer-level evaluation exists). Ladder: **DIVERSITY-ONLY**.

## 10. Remaining unknowns
- The full bibliography entry behind `[1]` (`#CITEREFLe2010`) - recorded,
  deliberately not followed.
- Whether W's and C's works share deeper derivation (common editions,
  common earlier translations) - not visible in either record.
- Whether the live page has drifted since A48's single snapshot.
- Whether a third voice would change anything (separate sprint, not taken).

## 11. Verification
- `python3 tests.py` -> **202/202 pass - HARNESS GREEN** (T167-T201 whole).
- Retrieval exit 0, integrity **18/18**, bridge **19/19**, all `.py` compile.
- Contract digest recomputed from its block: **`6c278f26…`**.
- A42-A48 artifacts byte-identical; `config.json` unchanged
  (`0b23f30a…`); no environment variable touched; **no network activity**.
- Manifest: 5 files at committed bytes (verified via `git show HEAD:`).
- Local commits only; tracked tree clean; **nothing pushed**.
