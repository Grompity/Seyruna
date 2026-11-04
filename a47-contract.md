# A47 contract - held-source provenance probe (frozen before extraction)

## 1. Evidence boundary, verified first
| source | file | url | publisher | chars | text sha256 |
| --- | --- | --- | --- | --- | --- |
| W | `research-hold/a42-duel.json` | `https://en.wikipedia.org/wiki/Edicts_of_Ashoka` | `wikipedia.org` | 1200 | `bbbdb36e195f0789ee749c048d7ba685eec32fee5324af7120ce042e39a37504` |
| C | `research-hold/a44-read.json` | `https://www.cs.colostate.edu/~malaiya/ashoka.html` | `colostate.edu` | 1200 | `07ba9f34fe08fceeb93d2e97fb81d7f936013ceebf18a4e1956c3c9a46033abc` |

A42-A46 manifests verify at their own commits (`cec50a7`, `e25389e`,
`6d3a4a3`, `850d945`, `b85c451`); the held artifacts are disk==HEAD; both
windows are the SAME 1,200-character extracts A46 compared. Label:
**REPLAY** - no new observation, no network, no reads.

## 2. The frozen policy (machine-replayable)
<!-- A47-POLICY -->
{
 "law": "A47-1 held-source provenance probe - FROZEN BEFORE PROVENANCE EXTRACTION",
 "label-law": "REPLAY over the two held windows; ZERO searches, ZERO network, ZERO reads, ZERO new evidence",
 "sources": {
  "W": {
   "name": "wikipedia",
   "file": "research-hold/a42-duel.json",
   "path": "reads.results[0]",
   "artifact-sha256": "cceae0bc03bc55c694cec47a1f090487650cf2e9bdb67bd5b6e3a509eca99105",
   "url": "https://en.wikipedia.org/wiki/Edicts_of_Ashoka",
   "publisher": "wikipedia.org",
   "status": 200,
   "text-sha256": "bbbdb36e195f0789ee749c048d7ba685eec32fee5324af7120ce042e39a37504",
   "chars": 1200,
   "extraction": "A42 road extract(), MAX_CHARS=1200 - the held text is TRUNCATED at the cap"
  },
  "C": {
   "name": "colostate",
   "file": "research-hold/a44-read.json",
   "path": "read.packet.results[0]",
   "artifact-sha256": "9d8de2c62015510eb5cde644a088d161689bc369b37bca2e76e3584db5b2ed18",
   "url": "https://www.cs.colostate.edu/~malaiya/ashoka.html",
   "publisher": "colostate.edu",
   "status": 200,
   "text-sha256": "07ba9f34fe08fceeb93d2e97fb81d7f936013ceebf18a4e1956c3c9a46033abc",
   "chars": 1200,
   "extraction": "A44 road extract(), MAX_CHARS=1200 - the held text is TRUNCATED at the cap"
  }
 },
 "extraction": {
  "units": "verbatim excerpts from the held windows only; every signal carries source id, exact excerpt, character offset, category and nature (EXPLICIT textual statement vs INFERRED analyst relation)",
  "categories": [
   "CITATION-MARKER - a bracketed reference number as it literally appears",
   "ATTRIBUTION-PHRASE - one of a CLOSED phrase list, matched case-insensitively",
   "NAMED-AUTHORITY - a person or institution the text explicitly names as a source, author, translator or authority (the historical SUBJECT is not a source and is excluded)",
   "NAMED-WORK-OR-BODY - a work or body of literature the text names (e.g. 'Buddhist literature', 'the present work')",
   "QUOTATION - a quoted passage presented with an attributing frame",
   "RELIANCE-STATEMENT - an explicit statement that the text rests on earlier translations or scholarship"
  ],
  "phrase-list": [
   "based on",
   "translated by",
   "according to",
   "quoted from",
   "has written",
   "attributed to",
   "the compiler",
   "earlier translations",
   "preserved the legend",
   "present rendering"
  ],
  "citation-regex": "\\[\\s*\\d+\\s*\\]",
  "explicit-vs-inferred": "EXPLICIT = the words are on the page verbatim; INFERRED = an analyst relation between signals (never presented as text)",
  "no-invention": "no bibliographic detail is invented and no incomplete marker is expanded using outside knowledge",
  "truncation-rule": "absence of an attribution in a TRUNCATED window is NOT evidence that no attribution exists",
  "subject-exclusion": "Ashoka/Asoka as the historical subject is NOT a named authority; only persons/institutions named as sources count"
 },
 "classification": {
  "vocabulary": [
   "EXPLICIT-SHARED-ATTRIBUTION",
   "POSSIBLE-SHARED-DERIVATION",
   "DISTINCT-STATED-ATTRIBUTIONS",
   "ATTRIBUTION-CHAIN-INCOMPLETE",
   "UNKNOWN"
  ],
  "requirements": {
   "EXPLICIT-SHARED-ATTRIBUTION": "the SAME named authority or named work appears in BOTH windows as a source",
   "POSSIBLE-SHARED-DERIVATION": "a visible connection exists (same named authority/work, or both explicitly state reliance on the same named body of translations) but it is insufficient to establish a common underlying evidence base",
   "DISTINCT-STATED-ATTRIBUTIONS": "BOTH windows explicitly name at least one accountable source/authority, the named sets are DISJOINT, and each chain is reconstructable to at least one named terminal; this does NOT prove independence",
   "ATTRIBUTION-CHAIN-INCOMPLETE": "at least one window's chain has a missing link (a marker without a visible referent, an unnamed translation or writer, or a truncation cutting an attribution), so neither shared nor distinct can be established",
   "UNKNOWN": "no provenance signal in either window"
  },
  "precedence": [
   "EXPLICIT-SHARED-ATTRIBUTION",
   "POSSIBLE-SHARED-DERIVATION",
   "ATTRIBUTION-CHAIN-INCOMPLETE",
   "DISTINCT-STATED-ATTRIBUTIONS",
   "UNKNOWN"
  ],
  "precedence-law": "the first satisfied class wins; DISTINCT requires BOTH chains reconstructable, so an incomplete chain outranks it",
  "forbidden-inferences": [
   "different citation numbers do not mean different sources",
   "different intermediary sources do not prove independent underlying evidence",
   "a common translator or historian is a provenance connection, not proof that every claim derives from that person",
   "different publishers do not establish source independence"
  ]
 },
 "ceiling": {
  "independence": "this experiment CANNOT promote independence to ESTABLISHED",
  "strongest-negative": "evidence suggesting shared derivation (POSSIBLE-SHARED-DERIVATION)",
  "strongest-positive": "distinct stated attribution chains (DISTINCT-STATED-ATTRIBUTIONS) - actual independence remains UNKNOWN",
  "four-separate-propositions": [
   "publisher independence",
   "editorial independence",
   "source independence",
   "independent observation of the historical facts"
  ]
 },
 "carry-over": {
  "a46-claims": "UNCHANGED - A46's 2 AGREEMENT / 2 PARTIAL / 9 NO-MATCH stands; A47 does not re-run it",
  "ladder": "UNCHANGED - DIVERSITY-ONLY stands unless the A46 claim layer AND independence both support otherwise; A47 cannot supply independence",
  "ea1": "UNCHANGED - A42 PARTIAL, A43 EVIDENCE-GAP, A44 EVIDENCE-GAP",
  "semantic": "UNKNOWN - no answer-leg"
 },
 "budget": {
  "searches": 0,
  "network-requests": 0,
  "source-reads": 0,
  "new-evidence": 0,
  "pdf-work": 0,
  "substitutions": 0
 },
 "prohibitions": [
  "no following citation links",
  "no external lookup",
  "no new evidence",
  "no modification of A42-A46 artifacts or manifests",
  "no change to A46's comparison methodology",
  "no production code change beyond a narrowly scoped offline test",
  "no independence promotion"
 ]
}
<!-- /A47-POLICY -->

Contract digest (sha256 of the canonical policy JSON, `sort_keys=True`):
`d923a13ffa0f8d8f1a9f0d0e04c327c06a490a2610dea1adec714bba5622f5f4`

## 3. The two layers
- **EXPLICIT**: verbatim signals on the page (markers, phrases, names,
  quotations) with offsets.
- **INFERRED**: analyst relations between signals, recorded as such and
  never quoted as text.
- **Never**: bibliographic invention, marker expansion, link-following,
  independence promotion.

## 4. Independence ceiling
The strongest negative word this experiment may emit is
**POSSIBLE-SHARED-DERIVATION**; the strongest positive is
**DISTINCT-STATED-ATTRIBUTIONS** with independence still **UNKNOWN**.
Publisher, editorial, source and observational independence are four
different propositions and are never collapsed.

## 5. Acceptance
A47 succeeds when every digest verifies, this contract's digest verifies
before extraction, every signal is verbatim and re-locatable, the visible
chains are printed with their missing links, and the classification stays
inside the frozen vocabulary and precedence - whichever class fires.
