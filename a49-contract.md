# A49 contract - preserved-body citation replay (frozen before parsing)

## 1. Input
`research-hold/a48-w-body.html` - **925,008 bytes**, sha256
`d45350ce045e5af55b0141f85099acac0ceea839b024e8c905bb986398546f8b` (A48's own recorded digest). A48's result is **not** changed
retrospectively; this sprint only replays over its preserved bytes.

## 2. Markers
| marker | number | A47 offset | A47 signal |
| --- | --- | --- | --- |
| `[ 1 ]` | 1 | [453, 458] | `W-M1` |
| `[ 2 ]` | 2 | [926, 931] | `W-M2` |
| `[ 3 ]` | 3 | [1073, 1078] | `W-M3` |

## 3. The frozen policy (machine-replayable)
<!-- A49-POLICY -->
{
 "law": "A49-1 preserved-body citation replay - FROZEN BEFORE PARSING",
 "label-law": "ZERO-network REPLAY over A48's preserved body; NOT a fresh observation and NOT new source evidence",
 "input": {
  "path": "research-hold/a48-w-body.html",
  "bytes": 925008,
  "sha256": "d45350ce045e5af55b0141f85099acac0ceea839b024e8c905bb986398546f8b",
  "source": "A48's ONE live request (label live) - preserved byte-for-byte"
 },
 "markers": [
  {
   "marker": "[ 1 ]",
   "number": 1,
   "a47-offset": [
    453,
    458
   ],
   "a47-source": "A47 W signal W-M1"
  },
  {
   "marker": "[ 2 ]",
   "number": 2,
   "a47-offset": [
    926,
    931
   ],
   "a47-source": "A47 W signal W-M2"
  },
  {
   "marker": "[ 3 ]",
   "number": 3,
   "a47-offset": [
    1073,
    1078
   ],
   "a47-source": "A47 W signal W-M3"
  }
 ],
 "structure": {
  "step-1": "parse EVERY forward citation superscript: <sup ... class=...reference...> containing an anchor",
  "step-2": "read each anchor's DISPLAYED text and parse its number from the bracketed digits; NEVER construct or assume an id such as cite_ref-1 or cite_note-1",
  "step-3": "candidates for marker k = sups whose displayed number == k; exactly ONE -> proceed; ZERO or MORE THAN ONE -> UNRESOLVED, ambiguity preserved (never pick the most useful-looking entry)",
  "step-4": "read the anchor's literal href; resolve ONLY a same-document fragment ('#id'); a non-fragment/external href -> UNRESOLVED",
  "step-5": "locate the element carrying that exact id; absent -> UNRESOLVED; present -> take its enclosing <li> entry (the element itself when it IS an li, else the nearest enclosing li)",
  "step-6": "record the RAW <li> HTML and a NORMALIZED display text SEPARATELY; tag stripping must not silently discard bibliographic detail",
  "cross-check": "document order and the A47 marker order are recorded as a cross-check but are NEVER used to break a tie",
  "no-numbering-assumption": "the mapper follows hrefs; it does not build '#cite_note-<k>' from k"
 },
 "record": [
  "marker text",
  "A47 offset",
  "minimal verbatim anchor HTML",
  "anchor id attribute (verbatim)",
  "literal href",
  "target fragment id",
  "target element type",
  "raw <li> HTML",
  "normalized entry text",
  "byte offset of the target in the preserved body",
  "explicit bibliographic fields ONLY where literally present",
  "completeness: COMPLETE / PARTIAL / TRUNCATED against the entry's own text"
 ],
 "source-classes": {
  "rules": [
   "PRIMARY-EDITION: the entry explicitly presents an edition/translation of the inscriptions themselves",
   "SECONDARY-SCHOLARSHIP: a book/article about the history, with author and publication context",
   "TERTIARY-REFERENCE: an encyclopedia/reference-work summary",
   "UNCLEAR: a reference is present but its class cannot be decided from its own text",
   "UNRESOLVED: no entry recovered"
  ]
 },
 "comparison": {
  "c-signals": [
   "H.G. Wells",
   "Ven. S. Dhammika / 'the present rendering'",
   "'earlier translations' (unnamed)",
   "'Buddhist literature' (legend carrier)"
  ],
  "classes": [
   "EXPLICIT-SHARED-REFERENCE",
   "EXPLICIT-RELATED-AUTHORITY",
   "POSSIBLE-SHARED-DERIVATION",
   "NO-VISIBLE-CONNECTION",
   "UNRESOLVED"
  ],
  "laws": [
   "a shared author/work is an ATTRIBUTION connection - NOT proof that all claims derive from it",
   "different references are NOT independent observation",
   "a domain difference is NEVER independence"
  ]
 },
 "acceptance": {
  "SUCCESS": "all three markers resolve through the actual DOM relationship",
  "PARTIAL": "some resolve; the rest UNRESOLVED with the reason",
  "FAILED": "none resolves or the digest mismatches (then STOP, no substitute body)"
 },
 "budget": {
  "searches": 0,
  "fetches": 0,
  "network-requests": 0,
  "source-reads": 0,
  "link-follows": 0,
  "alternate-bodies": 0,
  "substitutions": 0
 },
 "preservation": {
  "modifies": [],
  "why": "A42-A48 artifacts are immutable; A48's result is NOT changed retrospectively",
  "digest-check": "the body must hash to the FULL recorded digest BEFORE parsing; mismatch = STOP"
 },
 "ceiling": {
  "independence": "UNKNOWN stays UNKNOWN; recovering bibliography does NOT establish source or observational independence",
  "four-propositions": [
   "publisher",
   "editorial",
   "source",
   "observational"
  ],
  "ladder": "DIVERSITY-ONLY unless previously declared requirements are independently satisfied"
 },
 "carry-over": {
  "a46": "UNCHANGED",
  "a47": "UNCHANGED",
  "a48": "UNCHANGED (its FAILED acceptance stands)",
  "ea1": "UNCHANGED",
  "semantic": "UNKNOWN"
 },
 "prohibitions": [
  "no fetch",
  "no search",
  "no request",
  "no link-following",
  "no alternate body",
  "no live fallback",
  "no new source read",
  "no retrospective change to A48",
  "no promotion of independence or corroboration"
 ]
}
<!-- /A49-POLICY -->

Contract digest (sha256 of the canonical policy JSON, `sort_keys=True`):
`6c278f264fc3c903f4b802d73a5d16f5f2406886d4d0fc3337265302ce7c766c`

## 4. Budget
Zero searches, zero fetches, zero requests, zero source reads, zero
link-follows, zero alternate bodies, zero substitutions. If the digest
mismatches, **STOP** - no substitute copy, no reconstruction, no fetch.

## 5. Acceptance
**SUCCESS**: all three markers resolve through the actual DOM
relationship. **PARTIAL**: some resolve, the rest UNRESOLVED with the
reason. **FAILED**: none resolves. An unresolved marker is an acceptable
result.

## 6. Ceiling
A49 may improve W's visible attribution chain. It **cannot** establish
source or observational independence, and it does not touch A48's word or
the DIVERSITY-ONLY ladder.
