# A44 contract - the next publisher-distinct HTML read (frozen before any byte)

## 1. The boundary, verified (all before this contract)
| fact | value |
| --- | --- |
| A42 artifact | `research-hold/a42-duel.json` sha256 `cceae0bc03bc55c694cec47a1f090487650cf2e9bdb67bd5b6e3a509eca99105` (re-signed at `a42-manifest.sha256`) |
| A43 artifact | `research-hold/a43-read.json` sha256 `555043274af127c3499d6607250b5080d8334ed29fe7d0db6db85b92f4b9e931` (re-signed at `a43-manifest.sha256`) |
| held packet | `search.rows-words`, 5 rows, ORIGINAL order preserved |
| packet digest | `21d2095af415c6f38f830f7e8064ed3ca1f8f71df63fc04476615c17dd2ab06a` (canonical JSON, `sort_keys=True`) |
| row 4 | `https://www.cs.colostate.edu/~malaiya/ashoka.html` |
| publisher | recorded `colostate.edu`; normalized `colostate.edu` at the EXISTING law |
| eligibility | url-bearing AND publisher != the instance house `127.0.0.1` -> eligible |
| represented among READ bytes | `wikipedia.org` ONLY (an attempt is not a representation: A43's `columbia.edu` was attempted and never read) |
| candidate status | `colostate.edu` is in NEITHER set and has never been attempted |
| expected format | HTML - an ADDRESS fact (`.html`); the held packet carries NO content-type |

## 2. The candidate (frozen)
- URL: `https://www.cs.colostate.edu/~malaiya/ashoka.html`
- Position: row **4** (1-based), index **3** in the original packet order.
- Publisher identity: `publisher(url)` = `colostate.edu` under the
  existing registrable-domain rule (no new normalization).
- The row's packet fields: url, publisher, lane, title-PRESENCE,
  snippet-PRESENCE. NO content is held for it; no byte of its response
  has been read by this line.

## 3. The policy (machine-replayable; frozen)
<!-- A44-POLICY -->
{
 "law": "A44-1 the next publisher-distinct HTML read - FROZEN BEFORE ANY BYTE",
 "packet": {
  "file": "research-hold/a42-duel.json",
  "artifact-sha256": "cceae0bc03bc55c694cec47a1f090487650cf2e9bdb67bd5b6e3a509eca99105",
  "packet-digest-sha256": "21d2095af415c6f38f830f7e8064ed3ca1f8f71df63fc04476615c17dd2ab06a",
  "rows": 5,
  "order": "original A42 packet order, preserved (never re-sorted)"
 },
 "candidate": {
  "url": "https://www.cs.colostate.edu/~malaiya/ashoka.html",
  "row-1based": 4,
  "index-0based": 3,
  "publisher-recorded": "colostate.edu",
  "publisher-normalized": "colostate.edu",
  "normalization-law": "publisher() = the registrable domain (last two labels; deep hosts collapse) - the existing identity rule, unchanged",
  "expected-format": "HTML (an ADDRESS fact: the path ends .html; the held packet carries NO content-type - the server's kind is the one read's own word)"
 },
 "reader": {
  "path": "web_research.reads(query, [url]) -> the A10 named road -> fetch(url) -> the road's guards -> extract()",
  "accepted-kinds": [
   "text/html",
   "application/xhtml+xml",
   "text/plain"
  ],
  "extract-cap-chars": 1200,
  "thin-floor-chars": 60
 },
 "eligibility": "A40 5 unchanged: the row carries a url AND publisher(url) != the instance's own house (127.0.0.1)",
 "represented-among-reads": {
  "set": [
   "wikipedia.org"
  ],
  "law": "REPRESENTED = a publisher with READ bytes (a row carrying a status) in the held reads; an ATTEMPT is not a representation",
  "columbia.edu": "ATTEMPTED at A43, never READ (wrong-kind, 0 bytes) - not represented",
  "candidate": "colostate.edu is in neither set and has never been attempted"
 },
 "budget": {
  "reads": 1,
  "searches": 0,
  "retries": 0,
  "substitutions": 0,
  "fallbacks": 0
 },
 "prohibitions": [
  "no PDF handling",
  "no content-type broadening",
  "no reader change to make the candidate succeed",
  "no production provider-config change",
  "no second candidate and no fallback",
  "no retry and no URL substitution"
 ],
 "outcome-categories": {
  "NO-RESPONSE": "a transport error word (timeout/unreachable/dns/malformed transport) - no HTTP answer arrived",
  "WRONG-KIND": "the server ANSWERED and the road refused the kind (wrong-kind:*); status/final discarded by the road's own branch -> ABSENT words",
  "ZERO-EXTRACTED": "the road OPENED (status) and extract() produced 0 chars",
  "THIN": "the road OPENED and extract() produced 1..59 chars (below the 60 floor) - a form-page/thin word, NOT usable",
  "USABLE": "opened AND extracted >= 60 chars AND publisher outside the house AND the bytes SPEAK the question ('ashoka' case-folded)",
  "OTHER-FAILURE": "an explicit road word outside the above (http-NNN, blocked-or-rate, too-big, read-failed, blocked:*, redirected-to-blocked)"
 },
 "metadata-to-preserve": {
  "status": "when the success face rides",
  "final": "ONLY when a redirect moved (else ABSENT, never invented)",
  "retrieved": "the success face's stamp",
  "extracted-bytes": "len(text) after extract()",
  "publisher": "publisher(url) at the existing law",
  "canon": "the road's canon word",
  "content-type": "NOT EXPOSED by the existing reader on ANY branch (fetch()'s kind is consumed by reads() and never recorded) - recorded as a CAPABILITY LIMITATION, never fabricated"
 },
 "corroboration-law": "a distinct publisher is NEVER corroboration by itself: the table's counts + independence ride, and 'candidate' needs >= 2 READ origin publishers AND the ladder's share (levels36 at the baseline primary)",
 "ea1-law": "A35's cycle disposition is NOT re-run; A42's PARTIAL and A43's EVIDENCE-GAP stand byte-identical; no claim about EA1's answer",
 "semantic-law": "UNKNOWN - no answer-leg rides (A40 7/8), declared before the bytes"
}
<!-- /A44-POLICY -->

Contract digest (sha256 of the canonical policy JSON, `sort_keys=True`):
`233def8238cc6c81560cee677292dc66ae1504c9d50c14cdbf7abec117163d16`

## 4. Budget and prohibitions
- Exactly **ONE** read attempt at exactly the frozen URL through the
  EXISTING HTML read path (`web_research.reads`).
- **ZERO** new searches; **ZERO** retries; **ZERO** URL substitutions;
  **ZERO** fallback candidates.
- **NO** PDF handling, **NO** content-type broadening, **NO** reader
  change to make this candidate succeed, **NO** production
  provider-config change.

## 5. Outcome categories (frozen) and metadata
- **NO-RESPONSE** - a transport error word; no HTTP answer arrived.
- **WRONG-KIND** - the server ANSWERED and the road refused the kind;
  the road's branch discards status/final -> those ride ABSENT/UNKNOWN,
  never zero.
- **ZERO-EXTRACTED** - opened (status) and 0 chars extracted.
- **THIN** - opened and 1..59 chars (below the 60 floor) - not usable.
- **USABLE** - opened AND >= 60 chars AND publisher outside the house
  AND the bytes SPEAK the question ("ashoka" case-folded).
- **OTHER-FAILURE** - an explicit road word outside the above
  (`http-NNN`, `blocked-or-rate`, `too-big`, `read-failed`, `blocked:*`,
  `redirected-to-blocked`).
- Metadata preserved: status (success face), final ONLY when a redirect
  moved, retrieved, extracted byte count, publisher, canon. Content-type
  is **NOT EXPOSED by the existing reader on any branch** - recorded as a
  CAPABILITY LIMITATION, never fabricated and never repaired in this
  experiment.

## 6. Interpretation laws (frozen)
- A distinct publisher is **NEVER** corroboration by itself: the table's
  counts + independence ride, and "candidate" needs >= 2 READ origin
  publishers AND the ladder's share (`levels36` at the A36 baseline
  primary).
- EA1's classification is **NOT** re-run: A42's PARTIAL and A43's
  EVIDENCE-GAP stand byte-identical; no claim about EA1's answer.
- Semantic improvement: **UNKNOWN** - no answer-leg rides.

## 7. Acceptance
A44 succeeds when the boundary and the contract are verified before the
read, exactly one attempt is accounted for, and the outcome is classified
honestly under the frozen categories - whichever category fires.
