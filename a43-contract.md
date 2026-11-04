# A43 contract - the publisher-distinct selection (frozen before any candidate content)

## 1. The held packet (verified, not re-fetched)
- File `research-hold/a42-duel.json`, artifact sha256
  `cceae0bc03bc55c694cec47a1f090487650cf2e9bdb67bd5b6e3a509eca99105`
  == the a42 manifest's line (re-verified at the test).
- The result packet is `search.rows-words` (5 rows, original order
  preserved, never re-sorted).
- Packet digest (sha256 of the canonical JSON of those rows,
  `sort_keys=True`): `21d2095af415c6f38f830f7e8064ed3ca1f8f71df63fc04476615c17dd2ab06a`.
- The packet carries NO candidate content: each row is url, publisher,
  lane, title-PRESENCE, snippet-PRESENCE. The three unspent candidates'
  bytes have never been fetched or held. Selection cannot read what was
  never stored.
- NO search rides in A43. Question, provider, endpoint and environment
  are frozen at A42's. This sprint reads, it does not search.

## 2. The voices already represented (derivation, before content)
- `wikipedia.org`: the A36 held primary
  (`research-hold/a36-read-EA1.json` `selection.primary`) AND A42's
  opened read row (status present).
- The instance house `127.0.0.1` is excluded by the ELIGIBILITY rule,
  never counted as evidence (A7: the house is the ABSENCE of a voice).
- `duckduckgo.com` is ddg-ia's house, not a voice (A7), and does not
  appear in this packet.
- Therefore `represented = ["wikipedia.org"]`.

## 3. The policy (frozen; replayable from this contract + the packet alone)
<!-- A43-POLICY -->
{
 "law": "A43-1 publisher-distinct selection - FROZEN BEFORE ANY CANDIDATE CONTENT IS SEEN",
 "packet": {
  "file": "research-hold/a42-duel.json",
  "artifact-sha256": "cceae0bc03bc55c694cec47a1f090487650cf2e9bdb67bd5b6e3a509eca99105",
  "packet-digest-sha256": "21d2095af415c6f38f830f7e8064ed3ca1f8f71df63fc04476615c17dd2ab06a",
  "rows": 5,
  "order": "original A42 packet order (the provider's own); preserved, never re-sorted"
 },
 "house": "127.0.0.1",
 "eligibility": "A40 5 unchanged: the row carries a url AND publisher(url) != the instance's own house",
 "represented": [
  "wikipedia.org"
 ],
 "represented-derivation": {
  "a36-held-primary": "wikipedia.org (research-hold/a36-read-EA1.json selection.primary)",
  "a42-opened-read": "wikipedia.org (research-hold/a42-duel.json reads.results[0], status present)",
  "house-not-evidence": "A7: the house is the ABSENCE of a voice - excluded by ELIGIBILITY, never counted as represented evidence",
  "ddg-ia-house": "duckduckgo.com is not a voice (A7) and does not appear in this packet"
 },
 "order-rule": "pick = the FIRST eligible row, in original packet order, whose publisher is NOT in represented; every earlier eligible row rides a skipped word 'represented', in order; no later row is consulted once a pick stands",
 "no-skip-law": "an inconvenient candidate is NEVER passed over for a more promising one: the rule reads NO path, extension, title, snippet, quality, or eventual content",
 "content-blind": "the held packet carries NO candidate content (each row has url, publisher, lane, title-PRESENCE, snippet-PRESENCE only) - selection cannot see what was never stored; the unspent candidates' bytes have never been fetched or held",
 "alternative-reading": "if 'represented' were read as 'any publisher present anywhere in the packet', the candidate set would be EMPTY and zero reads would spend; that reading is recorded and NOT taken - the mission names the three other publishers as the UNSPENT candidates this experiment is about, so 'represented' is read as REPRESENTED IN THE EVIDENCE (the voices already read and held)",
 "budget": {
  "searches": 0,
  "reads": 1,
  "retries": 0,
  "substitutions": 0
 }
}
<!-- /A43-POLICY -->

Policy digest (sha256 of the canonical policy JSON, `sort_keys=True`):
`937e131b4e6f1ddf097857dfe8adca0859eceaca686e92ae2cf4ffb7bbbf2bfd`

Disambiguation, declared BEFORE any byte: "publishers already
represented in the EA1 evidence packet" is read as REPRESENTED IN THE
EVIDENCE (the voices already read and held). The alternative reading
("any publisher present anywhere in the packet") would empty the
candidate set and spend ZERO reads; it is recorded and NOT taken,
because the mission names the three unread publishers as the candidates
the experiment is about. Both consequences are printed here.

## 4. Budget
Exactly ONE new source-read attempt: one `reads()` call carrying exactly
the picked url. No searches, no retries, no substitutions, no extra
reads. If no candidate qualifies, ZERO reads spend.

## 5. Outcome classes (frozen before the read)
- TRANSPORT and CONTENT are SEPARATE words: an HTTP answer is not
  content; a content-type wall is not a transport failure.
- The road's own words ride as they come: an error word is a RECORD,
  never a fallback. A `wrong-kind` word means the transport ANSWERED
  with a kind the road will not read - and the road's `wrong-kind`
  branch discards status/final/body, so those fields ride ABSENT /
  UNKNOWN, never zero.
- USABLE evidence = A40 6 unchanged: opened (status, no error) AND
  extracted >= 60 chars AND publisher outside the house AND the bytes
  SPEAK the question ("ashoka" case-folded), with the claim TRACEABLE
  to the url's own bytes.
- Answer word (experiment level) = `answer42(None, [pick], read_rows,
  house)` - the A42-declared map, unchanged.
- Corroboration = the existing table's words only: counts +
  independence. A distinct publisher alone is NEVER corroboration; a
  "candidate" requires >= 2 READ origin publishers AND the ladder must
  SPEAK (`levels36` at the baseline primary). Diversity without shared
  claims is DIVERSITY ONLY.
- EA1's A35 cycle classification is NOT re-run: no cycle rides in A43;
  A42's PARTIAL stands. A43 changes no prior classification and claims
  no change to EA1's answer.
- Semantic improvement: UNKNOWN by law (no answer-leg). Declared now.

## 6. Integrity
- A42 and every earlier record stay byte-identical (re-signed at their
  manifests in the tests).
- No production config change is required (nothing searches; the read
  is a plain named read at the existing guards).
- Missing provenance rides as ABSENT / UNKNOWN words, never zeros.
- The record is `research-hold/a43-read.json`; tests T196; one clean
  commit series; nothing pushed.

## 7. Acceptance
A43 succeeds when the rule is frozen before reading, the single
authorized read is accounted for, and the evidence is classified
honestly - whichever way the read comes back.
