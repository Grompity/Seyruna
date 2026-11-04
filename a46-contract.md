# A46 contract - held-source claim comparison (frozen before content analysis)

## 1. Evidence boundary, verified first
| source | file | url | publisher | status | chars | text sha256 |
| --- | --- | --- | --- | --- | --- | --- |
| W (wikipedia) | `research-hold/a42-duel.json` | `https://en.wikipedia.org/wiki/Edicts_of_Ashoka` | `wikipedia.org` | 200 | 1200 | `bbbdb36e195f0789ee749c048d7ba685eec32fee5324af7120ce042e39a37504` |
| C (colostate) | `research-hold/a44-read.json` | `https://www.cs.colostate.edu/~malaiya/ashoka.html` | `colostate.edu` | 200 | 1200 | `07ba9f34fe08fceeb93d2e97fb81d7f936013ceebf18a4e1956c3c9a46033abc` |

Historical manifests verify at their OWN commits: a42 @ `cec50a7`,
a43 @ `e25389e`, a44 @ `6d3a4a3`, a45 @ `850d945` (all entries). The
held JSON artifacts are disk==HEAD. Both texts are **truncated at the
road's 1200-character extract cap** - every count and claim below is a
statement about the HELD WINDOW only, never about the whole page.

Label: **REPLAY** - A46 adds no new observation; zero network, zero
reads, zero new evidence.

## 2. The frozen policy (machine-replayable)
<!-- A46-POLICY -->
{
 "law": "A46-1 held-source claim comparison - FROZEN BEFORE CONTENT ANALYSIS",
 "label-law": "REPLAY over the two held reads; A46 adds NO new observation, NO read, NO network",
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
 "normalization": {
  "unicode": "NFKC on a COPY for comparison only; original bytes and offsets preserved separately",
  "case": "str.casefold() after NFKC",
  "token-regex": "[^\\W_]+",
  "punctuation": "every character not matched by the token regex is a boundary (apostrophes, hyphens, commas, periods, digits stay attached only inside a token run)",
  "numbers": "retained verbatim as tokens; never stripped, never converted",
  "stopword-policy": "a CLOSED list is removed from the CONTENT stream only; negations (no, not, never, none, nor, without, cannot) and hedges/qualifiers (may, might, could, reportedly, according, about, likely) are NEVER removed",
  "stopword-list": [
   "a",
   "an",
   "and",
   "are",
   "as",
   "at",
   "be",
   "been",
   "but",
   "by",
   "for",
   "from",
   "had",
   "has",
   "have",
   "he",
   "her",
   "his",
   "i",
   "in",
   "into",
   "is",
   "it",
   "its",
   "of",
   "on",
   "or",
   "she",
   "that",
   "the",
   "their",
   "them",
   "they",
   "this",
   "to",
   "was",
   "were",
   "which",
   "who",
   "will",
   "with",
   "you",
   "your",
   "we",
   "our",
   "us"
  ],
  "variant-map": {
   "ashoka": "ashoka",
   "asoka": "ashoka"
  },
  "variant-law": "both surface forms map to the canonical token 'ashoka' on BOTH sides symmetrically; the surface forms are still counted separately for the record",
  "phrases": "bigrams (n=2) and trigrams (n=3) over the CONTENT-token stream in original order",
  "duplicates": "both TYPE-level (unique) and MULTISET counts are reported everywhere"
 },
 "overlap": {
  "shared-tokens-type": "|A intersect B| over unique content tokens",
  "shared-tokens-multiset": "sum over tokens of min(count_A, count_B)",
  "proportions": "type-share of A, type-share of B, multiset-share of A, multiset-share of B",
  "jaccard": "|A intersect B| / |A union B| (types)",
  "dice": "2|A intersect B| / (|A| + |B|) (types)",
  "overlap-coefficient": "|A intersect B| / min(|A|, |B|) (types)",
  "phrase-counts": "shared unique bigrams and trigrams, with shares of each source's unique n-grams",
  "floor": "if shared unique content tokens < 10 the measurement is INSUFFICIENT-SIGNAL: raw counts only, NO similarity adjective is emitted",
  "saturation": "no score, however high, moves the word beyond TEXTUAL-SIMILARITY - similarity is not corroboration",
  "topic-terms": [
   "ashoka",
   "edict",
   "edicts",
   "rock",
   "rocks",
   "pillar",
   "pillars",
   "inscription",
   "inscriptions",
   "maurya",
   "mauryan",
   "emperor",
   "empire",
   "king",
   "kings",
   "buddhist",
   "buddhism",
   "dhamma",
   "dharma",
   "reign",
   "century",
   "bce",
   "ce",
   "india",
   "indian"
  ],
  "topic-inflation": "token overlap is recomputed with topic terms removed and BOTH results are reported, so common historical terminology cannot silently inflate the headline",
  "denominators": "every score is printed with its numerator and denominator"
 },
 "claims": {
  "unit": "a clause-level factual proposition EXPLICITLY present in the held excerpt",
  "fields": [
   "id",
   "proposition",
   "excerpt (verbatim)",
   "source",
   "offset (start,end in the held text)",
   "entities",
   "dates-quantities-qualifications",
   "negation-or-uncertainty",
   "status"
  ],
  "status-values": [
   "CLAIM",
   "NON-CLAIM",
   "AMBIGUOUS"
  ],
  "rules": [
   "no external knowledge, memory or other sources",
   "no inference beyond the excerpt",
   "no upgrading a vague description into a precise claim",
   "every excerpt must be re-locatable: text[offset_start:offset_end] == excerpt",
   "if no clear proposition -> NON-CLAIM or AMBIGUOUS, never forced"
  ],
  "judgment-law": "claim extraction is ANALYST JUDGMENT and is recorded as such; the deterministic layer is normalization + overlap only. Judgments are auditable (verbatim excerpt + offset), not presented as deterministic facts"
 },
 "comparison": {
  "outcomes": [
   "AGREEMENT",
   "CONFLICT",
   "PARTIAL",
   "INDETERMINATE",
   "NO-MATCH"
  ],
  "material-equivalence": "same subject AND predicate AND the same material qualifiers (entity identity, date/quantity value, polarity) within the held excerpts; a paraphrase that preserves all of these is equivalent",
  "incompatibility": "same subject and predicate with a contradictory value, polarity or attribution - not merely a different emphasis",
  "PARTIAL": "shared subject/predicate but a material detail differs OR is unsupported on one side",
  "INDETERMINATE": "a comparable subject exists but the held excerpts are too thin to decide",
  "NO-MATCH": "no comparable proposition was identified in the other source",
  "rule": "shared names or terminology alone NEVER constitute AGREEMENT; the proposition must match"
 },
 "corroboration": {
  "conditions": [
   "1. two publishers with readable content",
   "2. similar language (textual similarity measured)",
   "3. equivalent factual claims (claim layer)",
   "4. genuine independence in origin"
  ],
  "independence-law": "different registrable domains are NOT independence; independence is UNKNOWN unless provenance in the held bytes establishes it",
  "ladder-disposition": "DIVERSITY-ONLY stands unless condition 3 holds AND condition 4 is established; otherwise the word stays DIVERSITY-ONLY or drops to TEXTUAL-SIMILARITY / CLAIM-PARTIAL, never 'corroborated'"
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
  "no fetching anything",
  "no gap-filling",
  "no new evidence",
  "no post-hoc rule adjustment",
  "no threshold chosen after the result",
  "no promotion of DIVERSITY-ONLY to corroboration",
  "no modification of A42-A45 artifacts or manifests",
  "no production code change beyond a narrowly scoped offline test"
 ]
}
<!-- /A46-POLICY -->

Contract digest (sha256 of the canonical policy JSON, `sort_keys=True`):
`cef965bf784ec22010dec93cdc68582a96a6fe05ec2ceb6f338d896ee1bf796b`

## 3. What this can and cannot output
- **Layer 1 (deterministic):** token / n-gram overlap with raw counts and
  denominators - word **TEXTUAL-SIMILARITY** only.
- **Layer 2 (analyst judgment, auditable):** claim extraction and
  comparison - every excerpt re-locatable by offset.
- **Never:** corroboration from similarity, from publisher diversity, or
  from shared terminology. Independence is UNKNOWN unless provenance
  establishes it.

## 4. Acceptance
A46 succeeds when every digest verifies, this contract's digest verifies
before analysis, both layers run exactly as frozen, every comparison
carries verbatim excerpts from both sides, and the ladder keeps its
frozen words - whichever result the evidence yields.
