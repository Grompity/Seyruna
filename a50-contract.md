# A50 contract - the independence and corroboration model (frozen before implementation)

## 1. The problem
The system can already count cited terminals and can say
`DISTINCT-STATED-ATTRIBUTIONS`. It has no explicit model that keeps
**different attributions**, **independent evidence** and **independent
corroboration** apart, and no way to record a shared underlying source.
A50 adds that model as a PURE classifier over evidence records. It
retrieves nothing.

## 2. Dimensions
Six independent dimensions, each statused `SUPPORTED` / `CONTRADICTED` /
`UNKNOWN`, each with its own evidence requirement:

| dimension | question |
|---|---|
| attribution | are DIFFERENT named terminals visible? |
| underlying | are the underlying source materials demonstrably distinct? |
| editorial | were the works independently researched/assembled editorially? |
| institutional | are the source-production processes institutionally independent? |
| observational | do the sources derive from separate observations/records? |
| corroboration | do multiple chains independently support the same claim? |

There is **no ladder and no score**: establishing attribution diversity
promotes nothing else, and no dimension implies another.

## 3. Frozen policy (machine-replayable)
<!-- A50-POLICY -->
{
 "law": "A50-1 independence and corroboration model - FROZEN BEFORE IMPLEMENTATION",
 "scope": "a PURE, local, stdlib-only model over evidence records; it classifies, it never retrieves",
 "dimensions": {
  "attribution": {
   "question": "are DIFFERENT named attribution terminals visible?",
   "statuses": [
    "SUPPORTED",
    "CONTRADICTED",
    "UNKNOWN"
   ],
   "labels": {
    "SUPPORTED": "DISTINCT-STATED-ATTRIBUTIONS",
    "CONTRADICTED": "EXPLICIT-SHARED-ATTRIBUTION",
    "UNKNOWN": "UNKNOWN"
   },
   "sufficient": "at least two chains, each with at least one COMPLETE or PARTIAL named terminal, and the named terminal id sets are pairwise disjoint",
   "insufficient": [
    "different labels with the same id",
    "unnamed terminals",
    "a single chain"
   ],
   "contradicts": "a terminal id appears in two chains",
   "terminal": "UNKNOWN when any chain has no named terminal",
   "level": "attribution only - never evidence, never corroboration"
  },
  "underlying": {
   "question": "are the underlying source materials demonstrably distinct?",
   "sufficient": "an explicit independent-underlying record for every chain pair, or terminals that ARE distinct primary records with documented distinct provenance",
   "insufficient": [
    "different authors",
    "different citations",
    "different publishers",
    "different dates",
    "different wording",
    "different domains"
   ],
   "contradicts": "a documented material dependency path between the chains (shares-edition, translation-ancestor, derives-from, same-underlying-work, same-primary-document, same-dataset, same-observation)",
   "terminal": "UNKNOWN when nothing documents either way",
   "level": "chain pair"
  },
  "editorial": {
   "question": "were the works independently researched, selected, interpreted or assembled editorially?",
   "sufficient": "an explicit independent-editorial record",
   "insufficient": [
    "different publishers",
    "different imprints",
    "different author names"
   ],
   "contradicts": "a shared-editorial-control record",
   "terminal": "UNKNOWN when nothing documents either way",
   "level": "chain pair"
  },
  "institutional": {
   "question": "are the source-production processes institutionally independent?",
   "sufficient": "an explicit independent-institutional record",
   "insufficient": [
    "different institutional names",
    "different top-level domains"
   ],
   "contradicts": "a shared-funder, shared-commissioner or shared-institutional-control record",
   "terminal": "UNKNOWN when nothing documents either way",
   "level": "chain pair"
  },
  "observational": {
   "question": "do the sources derive from genuinely separate observations, records, measurements, witnesses or evidence-gathering processes?",
   "sufficient": "an explicit independent-observation record",
   "insufficient": [
    "different publications",
    "different retellings",
    "different wording"
   ],
   "contradicts": "a same-observation, same-primary-document or same-dataset record",
   "terminal": "UNKNOWN when nothing documents either way",
   "level": "chain pair"
  },
  "corroboration": {
   "question": "do multiple evidence chains independently support the same material claim?",
   "sufficient": "at least two chains support ONE declared claim with agreement AGREE, every pair is SUPPORTED on BOTH underlying and observational, and no dependency path links them",
   "insufficient": [
    "two authors",
    "two publications",
    "two publishers",
    "two citation lists",
    "different wording",
    "agreement alone",
    "a scholarly label",
    "age of a source"
   ],
   "contradicts": "a documented shared material/observation dependency between supporting chains, or a declared CONFLICT on the claim",
   "terminal": "UNKNOWN when the chain count, the shared claim, or the independence evidence is insufficient",
   "level": "claim"
  }
 },
 "statuses": [
  "SUPPORTED",
  "CONTRADICTED",
  "UNKNOWN"
 ],
 "relation-effects": {
  "shares-edition": {
   "underlying": "CONTRADICTED"
  },
  "translation-ancestor": {
   "underlying": "CONTRADICTED"
  },
  "derives-from": {
   "underlying": "CONTRADICTED"
  },
  "same-underlying-work": {
   "underlying": "CONTRADICTED"
  },
  "same-primary-document": {
   "underlying": "CONTRADICTED",
   "observational": "CONTRADICTED"
  },
  "same-dataset": {
   "underlying": "CONTRADICTED",
   "observational": "CONTRADICTED"
  },
  "same-observation": {
   "underlying": "CONTRADICTED",
   "observational": "CONTRADICTED"
  },
  "independent-underlying": {
   "underlying": "SUPPORTED"
  },
  "independent-editorial": {
   "editorial": "SUPPORTED"
  },
  "shared-editorial-control": {
   "editorial": "CONTRADICTED"
  },
  "independent-institutional": {
   "institutional": "SUPPORTED"
  },
  "shared-funder": {
   "institutional": "CONTRADICTED"
  },
  "shared-commissioner": {
   "institutional": "CONTRADICTED"
  },
  "shared-institutional-control": {
   "institutional": "CONTRADICTED"
  },
  "independent-observation": {
   "observational": "SUPPORTED"
  },
  "unknown-derivation": {
   "note": "recorded as an unknown; it never promotes or demotes"
  }
 },
 "dependency-closure": {
  "material": "the undirected graph over shares-edition, translation-ancestor, derives-from, same-underlying-work, same-primary-document, same-dataset, same-observation",
  "observation": "the undirected graph over same-primary-document, same-dataset, same-observation",
  "law": "two chains share material when any terminal of one and any terminal of the other are in one material component - so a shared ANCESTOR is found without a direct edge"
 },
 "promotion": {
  "no-single-ladder": "each dimension is classified independently; establishing one NEVER promotes another",
  "explicit-support": "SUPPORTED on underlying/editorial/institutional/observational requires an explicit independent-* record; absence of a discovered dependency is NOT independence",
  "conflict": "supporting and contradicting records for the same dimension/pair -> UNKNOWN with conflict=True and BOTH evidence lists preserved",
  "downgrade": "a newly recorded dependency demotes underlying (and observational when observation-level) to CONTRADICTED; another dimension's status is USUALLY untouched",
  "no-score": "no numeric confidence, no weighting, no aggregate score"
 },
 "unknown": "UNKNOWN is a terminal result; a missing relationship is NOT evidence that the relationship does not exist",
 "explain-contract": {
  "must-distinguish": [
   "DIFFERENT ATTRIBUTIONS",
   "INDEPENDENT EVIDENCE",
   "INDEPENDENT CORROBORATION"
  ],
  "independent-evidence": "underlying SUPPORTED and observational SUPPORTED",
  "independent-corroboration": "corroboration SUPPORTED",
  "forbidden": [
   "calling attribution diversity 'independent'",
   "calling agreement 'corroboration'",
   "printing a stronger word than the dimension status"
  ]
 },
 "a49-expectation": {
  "attribution": "SUPPORTED / DISTINCT-STATED-ATTRIBUTIONS",
  "underlying": "UNKNOWN",
  "editorial": "UNKNOWN",
  "institutional": "UNKNOWN",
  "observational": "UNKNOWN",
  "corroboration": "UNKNOWN",
  "independent-evidence": false,
  "independent-corroboration": false,
  "why": "W and C name disjoint terminals, but A49 recorded NO dependency either way, and no shared material claim exists to corroborate"
 },
 "non-goals": [
  "no network",
  "no retrieval",
  "no following the Le 2010 pointer",
  "no rewrite of A42-A49",
  "no change to web_research.corroboration or levels36",
  "no numeric score",
  "no schema migration of held records"
 ]
}
<!-- /A50-POLICY -->

Contract digest (sha256 of the canonical policy JSON, `sort_keys=True`):
`da981b94bdb7dc5fb7475c42872150fbb8aef5e3d53844af12a0a54794d1b01c`

## 4. The hard laws
1. A different author, citation, publisher, institution, date, domain or
   wording is **never** independence.
2. `SUPPORTED` on underlying/editorial/institutional/observational needs an
   **explicit** `independent-*` record. A missing dependency is not evidence
   of independence.
3. A documented dependency **contradicts** the dimension it bears on; it does
   not automatically falsify the other dimensions.
4. Shared ancestors are found by closure, so two translations of one earlier
   translation count as ONE source line, not two.
5. Corroboration needs two chains on the **same declared claim**, with
   underlying **and** observational SUPPORTED pairwise - agreement alone,
   wording alone, or count alone never suffices.
6. Conflicting evidence yields `UNKNOWN` with `conflict=True` and both
   evidence lists preserved.
7. `UNKNOWN` is a valid terminal result.

## 5. Integration
Narrowest point: a standalone `independence.py` (pure, stdlib-only) plus a
deterministic A49-derived fixture and a CLI for reports. No change to
`web_research.corroboration`, `levels36`, the pipeline, the held records, or
any historical classification. No network import, no retrieval, no model.

## 6. A49 expectation (frozen)
`DISTINCT-STATED-ATTRIBUTIONS` SUPPORTED; underlying, editorial,
institutional, observational and corroboration all `UNKNOWN`;
`independent-evidence = False`; `independent-corroboration = False`.
A48's FAILED acceptance and A49's five commits stay untouched.
