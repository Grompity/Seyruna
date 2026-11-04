# A45 contract - spelling-aware addressing reclassification (frozen before its own application)

## 1. The held evidence, verified first
| fact | value |
| --- | --- |
| file | `research-hold/a44-read.json` |
| artifact sha256 | `9d8de2c62015510eb5cde644a088d161689bc369b37bca2e76e3584db5b2ed18` (owned by `a44-manifest.sha256`, verified at DISK and HEAD) |
| read row sha256 | `f65805a615754cb706c990fe3e66281fe330bd751e3903113c869ae6f9f1a704` (canonical JSON) |
| text sha256 | `07ba9f34fe08fceeb93d2e97fb81d7f936013ceebf18a4e1956c3c9a46033abc` |
| text length | 1200 chars (the extract CAP - the page is longer; all counts are counts WITHIN this window) |
| url | `https://www.cs.colostate.edu/~malaiya/ashoka.html` |
| publisher / status | `colostate.edu` / 200 |
| A44 outcome / answer | `OFF-QUESTION` / `EVIDENCE-GAP` |
| A44 policy digest | `233def8238cc6c81560cee677292dc66ae1504c9d50c14cdbf7abec117163d16` |
| label law | the bytes are A44's ONE LIVE read; **A45 adds NO new observation** - any A45 word is a REPLAY |

## 2. The original rule (unchanged, not re-run in production)
`research_eval.answer42`'s addressing test is a case-folded **literal
substring** test for `ashoka` (its `speak` default). On A44's bytes it
FAILS: `ashoka` occurs 0 times while the page spells `Asoka`. A44's
recorded classification therefore stands: **OFF-QUESTION /
EVIDENCE-GAP**, byte-identical and never rewritten here.

## 3. The new law (frozen; machine-replayable)
<!-- A45-POLICY -->
{
 "law": "A45-1 spelling-aware addressing reclassification - FROZEN BEFORE ITS OWN APPLICATION",
 "evidence": {
  "file": "research-hold/a44-read.json",
  "artifact-sha256": "9d8de2c62015510eb5cde644a088d161689bc369b37bca2e76e3584db5b2ed18",
  "row-sha256": "f65805a615754cb706c990fe3e66281fe330bd751e3903113c869ae6f9f1a704",
  "text-sha256": "07ba9f34fe08fceeb93d2e97fb81d7f936013ceebf18a4e1956c3c9a46033abc",
  "text-chars": 1200,
  "url": "https://www.cs.colostate.edu/~malaiya/ashoka.html",
  "publisher": "colostate.edu",
  "status": 200,
  "a44-outcome": "OFF-QUESTION",
  "a44-answer": "EVIDENCE-GAP",
  "a44-policy-digest": "233def8238cc6c81560cee677292dc66ae1504c9d50c14cdbf7abec117163d16",
  "label": "A44's ONE LIVE read - A45 adds NO new observation; any A45 word is a REPLAY over held bytes"
 },
 "original-rule": {
  "where": "research_eval.answer42 -> _usable42 -> the addressing test",
  "implementation": "'ashoka' as a case-folded LITERAL SUBSTRING of the extracted text (answer42's speak default, unchanged, proven by its __defaults__)",
  "a44-observed": "FAILS - 'ashoka' occurs 0 times; the page spells 'Asoka'"
 },
 "new-rule": {
  "name": "addressing45",
  "variants": [
   "ashoka",
   "asoka"
  ],
  "variant-expansion": "FORBIDDEN - the list is closed at freeze time",
  "tokenization": "tokens = maximal runs of ASCII letters [A-Za-z]+ (re.findall(r'[A-Za-z]+', text)); every other character is a BOUNDARY",
  "case": "comparison on token.lower() (ASCII case-fold); the SURFACE spelling is recorded exactly as it appears, never rewritten",
  "punctuation": "a boundary: 'Asoka.' -> token 'Asoka'; 'Asoka,' -> 'Asoka'",
  "possessives": "the apostrophe is a boundary: \"Asoka's\" -> tokens 'Asoka', 's' -> MATCHES via its head token; recorded with that fact",
  "hyphen-and-digits": "boundaries: 'Asoka-2' -> 'Asoka', '2'",
  "complete-tokens-only": "a variant matches ONLY a whole token: 'Asokan', 'Ashokan', 'asokas' do NOT match (deliberate: no substring false positives)",
  "non-ascii": "a non-ASCII letter is a boundary; if the held text carries any, the affected tokens are recorded as a limitation rather than normalized",
  "no-normalization": "no rewriting, transliteration, stemming or diacritic folding of the held text"
 },
 "output-fields": {
  "addressed": "bool - at least one variant matched at least one complete token",
  "counts": "per variant, complete-token matches in the held text",
  "surfaces": "per variant, the exact observed token spellings (with repetitions listed in order of appearance)",
  "contexts": "for each match, a bounded surrounding window of the ORIGINAL bytes",
  "usable": "status present AND >= 60 chars AND publisher != the instance house AND addressed",
  "experiment-answer": "A42's four-word vocabulary reused verbatim: no usable read -> EVIDENCE-GAP; any usable read -> EVIDENCE-BACKED (a read-level word, NOT a corroboration word and NOT a claim about the source's truth)",
  "comparison": "the original-rule word recomputed beside the new-rule word over IDENTICAL bytes"
 },
 "budget": {
  "searches": 0,
  "network-requests": 0,
  "source-reads": 0,
  "substitutions": 0,
  "additional-evidence": 0,
  "pdf-work": 0
 },
 "prohibitions": [
  "no fetching the URL again",
  "no adding candidates or evidence",
  "no production configuration or provider change",
  "no rewriting A44's record, report, manifest or classification",
  "no variant-list expansion after seeing the result",
  "no claim of corroboration from an addressing result",
  "no claim of generalizable spelling-law improvement from ONE page"
 ],
 "corroboration-law": "UNCHANGED and NOT recomputed from this experiment: the held reads' table stands as A44 recorded it; a spelling match is not corroboration",
 "ea1-law": "UNCHANGED - A42 PARTIAL, A43 EVIDENCE-GAP, A44 experiment EVIDENCE-GAP stand byte-identical",
 "semantic-law": "UNKNOWN - no answer-leg rides"
}
<!-- /A45-POLICY -->

Contract digest (sha256 of the canonical policy JSON, `sort_keys=True`):
`387bd6a16f634d6df723dade4ada12145e87c89027e316e2c61d37fbb31af96c`

## 4. Matching semantics in one paragraph
Extract complete tokens as maximal ASCII-letter runs; compare each token,
case-folded, against the closed variant list `["ashoka", "asoka"]`.
Punctuation, apostrophes, hyphens and digits are boundaries, so
`Asoka's` matches via `Asoka` and `Asoka-2` via `Asoka`, while `Asokan`
and `Ashokan` do **not** match. Surface spellings are recorded exactly;
the held bytes are never rewritten, normalized or transliterated.

## 5. Budget and prohibitions
Zero searches, zero network requests, zero source reads, zero
substitutions, zero additional evidence, no PDF work, no provider or
configuration change, no rewriting of A42/A43/A44 artifacts or
manifests, no expansion of the variant list after seeing the result.

## 6. Interpretation laws
- An addressing-positive result is **not** a truth, relevance or
  corroboration claim: it says the held bytes NAME the subject under a
  declared token law.
- No generality claim: one page, one spelling pair.
- Corroboration and EA1's classification are **not recomputed** here;
  they stand as A44 recorded them.
- Semantic improvement stays **UNKNOWN** (no answer-leg).

## 7. Acceptance
A45 succeeds when the evidence digest verifies, this contract's digest
verifies before application, the reclassification is computed offline
from the held bytes under the frozen law, both laws are reported side by
side over identical bytes, and no prohibition is crossed - whichever
result the law yields.
