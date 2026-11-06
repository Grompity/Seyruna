# A48 contract - W reference-window provenance read (frozen before any network access)

## 1. The exact target
- **URL (verbatim from the held A46/A47 record):** `https://en.wikipedia.org/wiki/Edicts_of_Ashoka`
- **Why this window:** the held 1,200-char window ends mid-sentence at
  "that a comple…" and carries only `[1] [2] [3]`; MediaWiki renders the
  reference list further down the SAME page as the first
  `<ol class="references">`, whose items are numbered in display order -
  so item *i* is the target of displayed marker *[i]*. No request is
  needed to identify that structure, and none is made to discover it.

## 2. The frozen policy (machine-replayable)
<!-- A48-POLICY -->
{
 "law": "A48-1 reference-window provenance read of W - FROZEN BEFORE ANY NETWORK ACCESS",
 "url": "https://en.wikipedia.org/wiki/Edicts_of_Ashoka",
 "url-provenance": "copied verbatim from the held A46/A47 W record - NOT retyped",
 "why-this-window": {
  "fact": "the held 1200-char window ends mid-sentence at 'that a comple...' and contains only the markers [1][2][3]; the reference LIST is rendered further down the SAME page",
  "structure": "MediaWiki renders the reference list as the FIRST <ol class=\"references\"> whose <li> items are numbered in display order, so item i corresponds to the displayed marker [i]",
  "no-exploration": "the container and the item order are standard MediaWiki rendering; identifying them needs NO request, and no request is made to discover them"
 },
 "request": {
  "count": 1,
  "calls": 1,
  "path": "web_research.fetch(url) - the existing road (guards, kind law, body cap)",
  "searches": 0,
  "retries": 0,
  "substitutions": 0,
  "link-follows": 0,
  "redirects": "followed only as the road already follows them; a redirect is RECORDED, never followed to another content source by hand",
  "failure-honesty": "a transport failure is recorded as a failure, never as empty content"
 },
 "extraction": {
  "container": "the FIRST <ol class=\"references\"> ... </ol> block in the returned RAW HTML",
  "items": "split the container on <li ...>; item i (1-based) is the target of displayed marker [i]",
  "item-text": "web_research.extract(item_html, max_chars=20000, thin=0) - the EXISTING extractor; no new parser and no production change",
  "markers": "[1], [2], [3] only - no other marker is resolved in this sprint",
  "targets": "each li's id attribute is recorded VERBATIM; it is never resolved or navigated",
  "fields": "author / title / publisher / institution / date / edition / translator / URL are recorded ONLY where they literally appear in the extracted entry text",
  "completeness": "each entry is COMPLETE, PARTIAL or TRUNCATED against its own visible text - never reconstructed",
  "class": "PRIMARY (an edition/translation of the edicts themselves) / SECONDARY (scholarship about the history) / TERTIARY (reference-work summary) / UNCLASSIFIABLE - decided ONLY from the entry's own words",
  "failure": "if the container is absent or holds fewer than 3 items, each missing marker is recorded UNRESOLVED - no second request, no alternative source"
 },
 "preserve": {
  "body-file": "research-hold/a48-w-body.html (the exact returned bytes)",
  "body-digest": "sha256 at receipt, recorded before extraction",
  "extracted-file": "the extracted reference entries recorded VERBATIM in the observation artifact",
  "labels": "every word is a FRESH LIVE observation; the A42-A47 bytes are NOT reused as a substitute"
 },
 "comparison": {
  "classes": [
   "EXPLICIT-SHARED-REFERENCE",
   "EXPLICIT-RELATED-AUTHORITY",
   "POSSIBLE-SHARED-DERIVATION",
   "NO-VISIBLE-CONNECTION",
   "UNRESOLVED"
  ],
  "requirements": {
   "EXPLICIT-SHARED-REFERENCE": "a W reference entry and a C signal name the SAME work or the SAME author/translator, visibly",
   "EXPLICIT-RELATED-AUTHORITY": "a W entry and a C signal name authorities visibly related (e.g. one quotes what the other lists) but NOT the same work/person as source",
   "POSSIBLE-SHARED-DERIVATION": "the entries suggest a common underlying source without establishing it",
   "NO-VISIBLE-CONNECTION": "no W entry names any of C's signals",
   "UNRESOLVED": "W's entry is missing/truncated, or C's signal is unnamed, so no comparison is possible"
  },
  "c-only-signals": [
   "H.G. Wells",
   "Ven. S. Dhammika and 'the present rendering'",
   "'earlier translations' (unnamed)",
   "'Buddhist literature' (legend carrier)"
  ],
  "forbidden": [
   "shared author != proof all claims derive from that source",
   "different references != independent observation",
   "a domain difference is still not independence"
  ]
 },
 "ceiling": {
  "independence": "A48 CANNOT promote source independence to ESTABLISHED because a bibliography became visible",
  "four-propositions": [
   "publisher",
   "editorial",
   "source",
   "observational"
  ],
  "ladder": "DIVERSITY-ONLY unless previously declared requirements are satisfied; A46/A47 carry over"
 },
 "restoration": {
  "config": "NO production configuration or provider change is made; config.json sha256 recorded before and after",
  "pre-config-sha256": "0b23f30ae0c89f61080796ef7fcf04196ca384f2855efb07826ee6fb27a931d0",
  "env": "no environment variable is set or popped"
 },
 "budget": {
  "network-requests": 1,
  "fetch-calls": 1,
  "searches": 0,
  "retries": 0,
  "substitutions": 0,
  "link-follows": 0,
  "additional-reads": 0,
  "third-voice": 0
 },
 "acceptance": {
  "SUCCESS": "all three markers resolve to verbatim entries AND the body digest is preserved",
  "PARTIAL": "some markers resolve; the rest are recorded UNRESOLVED with the reason",
  "FAILED": "the request fails, or the container is absent/fewer than 3 items - recorded honestly, no retry"
 },
 "carry-over": {
  "a46": "UNCHANGED (2 AGREEMENT / 2 PARTIAL / 9 NO-MATCH)",
  "a47": "UNCHANGED (ATTRIBUTION-CHAIN-INCOMPLETE); A48 may only IMPROVE W's chain reconstruction",
  "ladder": "UNCHANGED - DIVERSITY-ONLY",
  "ea1": "UNCHANGED",
  "semantic": "UNKNOWN"
 },
 "prohibitions": [
  "no second request",
  "no following bibliography links",
  "no third-voice read",
  "no retrospective change to A42-A47",
  "no post-hoc rule change after seeing bytes",
  "no production configuration change",
  "no independence or corroboration promotion"
 ]
}
<!-- /A48-POLICY -->

Contract digest (sha256 of the canonical policy JSON, `sort_keys=True`):
`ad93895836a27e5efe6b03e334f7ef82b8f85690f8f05a5e341d8e9d0b4652ce`

## 3. Budget
**One** request, **one** URL, **one** call. Zero searches, zero
retries, zero substitutions, zero link-follows, zero third-voice reads.
Transport failure is a failure, never empty content.

## 4. Preservation
The exact returned bytes are written to `research-hold/a48-w-body.html`
and their sha256 recorded **before** extraction. A42-A47 bytes are never
reused as a substitute. Config sha256 is recorded before and after; no
environment variable is touched.

## 5. Acceptance
**SUCCESS**: `[1] [2] [3]` each resolve to a verbatim entry, body
digest preserved. **PARTIAL**: some resolve, the rest `UNRESOLVED`.
**FAILED**: request fails or the container is absent/too short - recorded
honestly, no retry.

## 6. Ceiling
A48 may improve W's chain reconstruction. It **cannot** promote source
independence to ESTABLISHED because a bibliography became visible.
Publisher, editorial, source and observational independence stay four
separate propositions; the ladder stays **DIVERSITY-ONLY** unless the
previously declared requirements are actually met.
