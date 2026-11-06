# A48 - W reference-window provenance read, one request (closed 2026-11-06, from 0432e95)

## The one line
One fresh request to the exact frozen W URL **succeeded** (HTTP 200,
`text/html`, 925,008 bytes, no redirect, 860.3 ms), and the exact body is
preserved at `d45350ce…`. The **frozen extraction rule then missed**: the
first `<ol class="references">` on the page is a **notes group**
(`cite_note-71`, `-73`, `-118`, `-119`), not the main reference list, so
**none of `[1] [2] [3]` resolved**. That is a **window-selection defect**,
recorded as **FAILED** under the contract's own acceptance words - not a
transport failure, and not repaired with a second request. W's chain was
**not** improved; the provenance class stays
**ATTRIBUTION-CHAIN-INCOMPLETE**, independence stays **UNKNOWN**, and the
ladder stays **DIVERSITY-ONLY**.

## 1. Frozen contract
- Digest `ad938958…` (canonical policy JSON), commit `4ef34a0`,
  committed **before** any network access.
- It declared: the exact held URL; the first-references-container window;
  why it was expected to hold the targets; one request; acceptance
  SUCCESS/PARTIAL/FAILED; body preservation; comparison classes; and the
  independence ceiling.

## 2. Live request
| field | value |
| --- | --- |
| requests | **1** (fetch calls 1) |
| status | **200** |
| content type | `text/html` |
| final URL | identical to requested - **no redirect** |
| elapsed | 860.3 ms |
| ledger | 0 → 1 |
| searches / retries / substitutions / link-follows | 0 / 0 / 0 / 0 |

## 3. Retrieved bytes and window
- Body: **925,008 bytes**, sha256 `d45350ce045e5af55b0141f85099acac0ceea839b024e8c905bb986398546f8b`, preserved at `research-hold/a48-w-body.html`.
- Extraction rule (frozen): first `<ol class="references">`, items 1-3,
  each tag-stripped with the existing `extract(thin=0)`.
- Container found at raw offset **489386** (span 489386-493613), **4 items**.

## 4. Recovered targets
**None for `[1] [2] [3]`.** The frozen container is a notes group:

| item | li id | first words of the entry |
| --- | --- | --- |
| 1 | `cite_note-71` | "↑ Seems to refer to Tamil ruler Athiyaman. [70]" |
| 2 | `cite_note-73` | "↑ Kelalaputa is the Prakrit for Kerala. [71]" |
| 3 | `cite_note-118` | "↑ For example, according to Hultzsch, the first line of the First Edict at Shahbazgarhi…" |
| 4 | `cite_note-119` | "↑ For example Column IV, Line 89" |

Marker mapping: `1 → UNRESOLVED`, `2 → UNRESOLVED`, `3 → UNRESOLVED`
(the items' back-references point to `[70]`, `[71]`, … - not to
`[1] [2] [3]`). **Acceptance: FAILED (0 of 3).**

## 5. Source classes
**Not assignable.** The recovered entries are inline *notes*, not
bibliographic records, and assigning primary/secondary/tertiary to them
would be a category error. They are recorded as the frozen rule's output
and nothing more.

## 6. Proposed connections to C
**None can be proposed.** The comparison cargo is empty because no
`[1]-[3]` target was recovered; all three ride **UNRESOLVED**. The notes
mention **Hultzsch**, who is not one of C's signals (Wells; Dhammika/the
present rendering; "earlier translations"; "Buddhist literature") - so the
notes-versus-C reading is `NO-VISIBLE-CONNECTION`, explicitly **not** a
finding about W's cited sources.

## 7. Updated provenance classification
**`ATTRIBUTION-CHAIN-INCOMPLETE` - unchanged.** A48 did not improve W's
reconstruction; it *measured why* one plausible window rule fails on this
page (multiple reflist groups, notes first).

## 8. Independence and corroboration
Independence **UNKNOWN - not promoted**; a visible bibliography would not
have sufficed even had it been recovered, and none was. Publisher,
editorial, source and observational independence stay four separate,
undifferentiated propositions. A46's 2 AGREEMENT / 2 PARTIAL / 9 NO-MATCH
and A47's class stand unchanged; EA1 unchanged; semantic **UNKNOWN**.

## 9. Remaining unknowns
- The actual targets of `[1] [2] [3]` on the current page.
- Whether W cites Dhammika, Wells, or the "earlier translations" C names.
- Whether any shared derivation exists (still not shown, still not
  excluded).
- Whether the live page differs from the A42 snapshot (A48 is a *fresh*
  observation by design; it does not validate the old bytes).

## 10. Next justified experiment
A **zero-network replay over the preserved A48 body** under a **new
contract frozen before it**, with a corrected deterministic mapping: for
each marker `N`, locate the marker's own anchor
`<sup id="cite_ref-N">`, read its `href="#cite_note-…"` target id, and
extract exactly that `<li id="cite_note-…">` entry. This resolves the A48
uncertainty at **zero** network cost and cannot be accused of a post-hoc
rule change, because the corrected rule is declared in advance of its
replay. A third-voice read remains a separate, later decision.

## Verification
- `python3 tests.py` -> **201/201 pass - HARNESS GREEN** (T167-T200 whole).
- Retrieval exit 0, integrity 18/18, bridge 19/19, all `.py` compile.
- Contract digest recomputed from its block: `ad938958…`.
- A42-A47 artifacts byte-identical; `config.json` unchanged
  (`0b23f30a…`), no environment variable touched.
- Manifest: 6 files (including the preserved body) at committed bytes;
  local commits only; tracked tree clean; nothing pushed.
