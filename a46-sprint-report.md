# A46 - held-source claim comparison, offline (closed 2026-11-04, from 850d945)

## The one line
Across the two **held 1,200-character windows**, the deterministic overlap
layer finds **20 shared content types out of 101/103** (Jaccard 0.109) -
and that headline is **topic-inflated**: with the declared historical
topic terms removed it falls to **11 of 85/90** (Jaccard 0.067). The
claim layer finds **2 AGREEMENT**, **2 PARTIAL**, **0 CONFLICT** and **9
NO-MATCH** over 13 rows. The agreements are real but thin: both texts say
the edicts are **stone inscriptions on pillars**, and both place Ashoka
as a **Mauryan ruler**. Independence is **UNKNOWN** - different domains
are not independence - so the ladder stays **DIVERSITY-ONLY**: this is
**CLAIM-AGREEMENT with unknown independence**, explicitly **not**
corroboration. EA1 is unchanged; semantic improvement is UNKNOWN.

## The frozen methodology
Frozen in `a46-contract.md` (policy digest `cef965bf…`) **before** either
text was read for comparison:
- **Normalization:** NFKC on a copy, casefold, Unicode letter/digit
  tokens (`[^\W_]+`), every other character a boundary, numbers retained,
  a **closed 46-word stopword list** that never removes negations or
  hedges, `ashoka`/`asoka` mapped symmetrically, bigrams (n=2) and
  trigrams (n=3) over the content-token stream, type **and** multiset
  counts.
- **Overlap:** shared types and multiset, per-source shares, Jaccard,
  Dice, overlap coefficient, n-gram counts, a declared floor of **10**
  shared unique content tokens, a saturation law (nothing exceeds
  TEXTUAL-SIMILARITY), and a **with/without topic-terms** pair.
- **Claims:** analyst-judgment layer; every claim carries a verbatim
  excerpt and an offset that re-locates it exactly; no external
  knowledge; no upgrading vagueness.
- **Comparison:** AGREEMENT / CONFLICT / PARTIAL / INDETERMINATE /
  NO-MATCH with definitions declared in advance.
- **Corroboration:** four conditions; independence UNKNOWN unless
  provenance establishes it.

## Exact lexical-overlap measurements
| measure | all content | minus topic terms |
| --- | --- | --- |
| unique content types (W / C) | 101 / 103 | 85 / 90 |
| shared unique types | **20** | **11** |
| type share of W / of C | 0.1980 / 0.1942 | 0.1294 / 0.1222 |
| shared multiset tokens | 24 | 11 |
| multiset share of W / of C | 0.1890 / 0.2017 | 0.1170 / 0.1111 |
| Jaccard (types) | **0.1087** | **0.0671** |
| Dice (types) | 0.1961 | 0.1257 |
| overlap coefficient | 0.1980 | 0.1294 |
| shared bigrams (unique) | 2 / 125 / 117 | 2 |
| shared trigrams (unique) | **0** / 125 / 117 | 1 |

Shared bigrams are `ashoka s` (both texts' possessive *Ashoka's/Asoka's*)
and `pakistan afghanistan` (both country lists). Zero shared trigrams in
the full stream. Floor (10) is met; the word this layer may emit is
**TEXTUAL-SIMILARITY** only.

## Extracted claims (full table in `research-hold/a46-compare.json`)
- **W (wikipedia): 11 claims** - caption findspot/material/date; >30
  stone inscriptions on pillars/boulders/cave walls; attribution to
  Emperor Ashoka of the Mauryan Empire; reign 268-232 BCE; dispersion
  across India/Bangladesh/Nepal/Afghanistan/Pakistan; first tangible
  evidence of Buddhism; earliest written and datable texts from India;
  stone preservation; Vedic oral transmission; the expression
  *Dhamma Lipi*; the edicts describe the policy on dhamma.
- **C (colostate): 8 claims** - Asoka third Mauryan monarch and
  exemplary ruler; Wells's praise; the Buddhist *legend* of conversion
  (explicitly marked legend); records of the reign were lacking; 19th-
  century discovery of many edicts in India/Nepal/Pakistan/Afghanistan;
  inscribed on rocks and pillars, proclaiming reforms/policies/advice;
  the rendering is based on earlier translations; the compiler's
  identity (**AMBIGUOUS** - cut by the cap, excluded from comparison).
- Every excerpt is verbatim and re-locatable: `text[offset[0]:offset[1]]
  == excerpt` for all 19.

## Claim comparison results
| outcome | count | rows |
| --- | --- | --- |
| **AGREEMENT** | **2** | X1 stone medium (W-01↔C-06); X2 Ashoka/Mauryan identity (W-02↔C-01) |
| **CONFLICT** | **0** | - |
| **PARTIAL** | **2** | X3 geography (W-04↔C-05: Bangladesh only in W; 19th-c date only in C); X4 what the edicts convey (W-10↔C-06: different formulations, W truncated) |
| **INDETERMINATE** | **0** | - |
| **NO-MATCH** | **9** | X5-X13: reign dates, Buddhism-evidence, earliest-texts, stone preservation, Vedic transmission, Dhamma Lipi, caption metadata, Wells praise, rendering provenance |

**7 distinct claims have a real counterpart** (W-01, W-02, W-04, W-10,
C-01, C-05, C-06); 16 claims were examined in some row; 1 is AMBIGUOUS.

## Independence assessment
**UNKNOWN.** A registrable-domain difference is not independence. The
held windows show W citing references `[1]-[3]` and C quoting H.G. Wells
while describing a rendering "based on earlier translations". Both are
secondary/tertiary texts; nothing in the held bytes establishes
independent origin, and no external lookup is permitted. Condition 4 of
the corroboration standard is **not established**.

## Corroboration ladder disposition
**DIVERSITY-ONLY - unchanged.** Conditions: two readable publishers (yes);
similar language (moderate, topic-dominated); equivalent claims (2
AGREEMENT + 2 PARTIAL); genuine independence (**UNKNOWN**). The
claim-level observation is recorded as **CLAIM-AGREEMENT (2) with
independence UNKNOWN** - it is **not** corroboration and **not** a ladder
promotion. No threshold was chosen after the result; the floor was frozen
at 10.

## The eleven required statements
1. **Both held sources and digests verified - yes.** a42/a43/a44/a45
   manifests verify at their own commits; both artifacts are disk==HEAD;
   both texts match their recorded digests and are 1200-char extracts.
2. **Comparison contract frozen before analysis - yes** (`cef965bf…`,
   committed `46e15e8`).
3. **Lexical overlap** - reported above: 20/101/103 (Jaccard 0.109);
   11/85/90 without topic terms (Jaccard 0.067).
4. **Claims extracted** - W: 11; C: 8 (7 CLAIM + 1 AMBIGUOUS).
5. **Comparable claims** - 7 distinct with a real counterpart.
6. **Counts** - 2 agreement, 0 conflict, 2 partial, 0 indeterminate,
   9 no-match, 13 rows.
7. **Specific propositions supported by both** - two: the edicts are
   stone inscriptions on pillars; Ashoka was a ruler of the Mauryan
   polity. Both are broad, and neither is a contested detail.
8. **Independence** - **UNKNOWN** (see above).
9. **Ladder change** - **none**; DIVERSITY-ONLY stands.
10. **EA1's answer/classification** - unchanged (A42 PARTIAL, A43
    EVIDENCE-GAP, A44 EVIDENCE-GAP).
11. **Semantic improvement** - **UNKNOWN** (no answer-leg).

## What remains unknown
- Whether the sources are genuinely independent (provenance not in the
  held windows).
- Whether the full pages contain more comparable claims - both windows
  are capped at 1200 chars.
- Whether the two agreements reflect shared underlying scholarship (both
  cite prior work) rather than independent observation.
- Whether EA1's answer improves; no answer-leg.

## Next justified experiment
The binding constraint is now **provenance**, not overlap or addressing.
The next justified experiment is a **declared provenance probe over the
already-held bytes**: freeze, before running it, a rule that extracts
citation/reference markers and attribution phrases from each held window
(W's `[1]-[3]` markers; C's "based on earlier translations" and the
Wells quotation), and classify what each text *says about its own
sources* - offline, zero reads. That can only move independence from
UNKNOWN to "shared-derivation suspected" or "still unknown"; it cannot
manufacture independence. A fresh one-read contract for row 5 would add a
third voice but not resolve independence either.

## Verification
- `python3 tests.py` -> **199/199 pass - HARNESS GREEN** (T167-T198 whole).
- Retrieval exit 0, integrity 18/18, bridge 19/19, all `.py` compile.
- Contract digest recomputed from its block: `cef965bf…`.
- A42-A45 artifacts byte-identical; `config.json` unchanged.
- Manifest: 5 files at committed bytes; local commits only; tracked tree
  clean; nothing pushed.
