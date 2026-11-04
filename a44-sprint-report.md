# A44 - the next publisher-distinct HTML read, one attempt (closed 2026-11-04, from e25389e)

## The one line
The frozen row 4 from the held EA1 packet - `colostate.edu`, HTML - was
read **once**: the transport answered (HTTP 200, 614.5 ms) and **1200
characters of usable page text arrived**, substantively about Asoka's
edicts. The frozen A40 §6 addressing test, however, is a **literal**
substring test for "ashoka", and the page spells the name **"Asoka"**
(3 occurrences, 0 of "Ashoka"). So under the law as frozen the read is
**OFF-QUESTION / not usable**, while the content plainly arrived. That
discrepancy is the finding: the binding constraint at A44 was the
**addressing law's spelling sensitivity**, not the reader, not the
transport, and not the publisher's identity. Corroboration is still not
demonstrated (independence "candidate", ladder share "unknown");
EA1's classification is unchanged; semantic improvement is UNKNOWN.

## The eight required statements

1. **Was the selection correct?**
   **Yes, exactly.** The mission declared the candidate; the boundary
   check confirmed it against the held packet *before* anything was
   frozen: row **4** (index 3) in the original A42 order,
   `https://www.cs.colostate.edu/~malaiya/ashoka.html`, recorded
   publisher `colostate.edu`, normalized `colostate.edu` by the existing
   registrable-domain rule, eligible under A40 §5, and **not**
   represented among READ voices (`{wikipedia.org}`; A43's
   `columbia.edu` was an *attempt*, never a read). The packet digest
   `21d2095a…` and the A42/A43 artifact digests were verified against
   their manifests first. No ranking by quality, title, snippet or
   content was performed, and no candidate content was held at freeze
   time.

2. **Was the frozen contract honored?**
   **Yes.** One read attempt, one URL, one call; **zero** new searches,
   **zero** retries, **zero** substitutions, **zero** fallback
   candidates; no PDF handling, no content-type broadening, no reader
   change, no production provider-config change. `research_eval.py`,
   `web_research.py` and `stages.py` are **byte-identical** to their A43
   commits - this sprint required **zero production code motion**. The
   only code change is the appended offline test T197. Missing
   measurements ride as **absent**, never as zero; the reader's
   non-exposure of `content-type` on any branch is recorded as a
   **capability limitation**, not silently repaired mid-experiment.

3. **Did the transport respond?**
   **Yes.** The road's own word is `opened`: status **200**, 614.5 ms
   wall, 1200 bytes extracted (that number equals the extract cap, so the
   page is longer than what was kept - a known ceiling, not the page's
   length). `retrieved` is stamped; `final` is ABSENT because no
   redirect moved (it is never invented).

4. **Was usable content extracted?**
   **Content arrived: yes. Usable under the frozen law: no.** 1200
   characters of real page text arrived and it is on-topic - its first
   claim: *"King Asoka, the third monarch of the Indian Mauryan dynasty,
   has come to be regarded as one of the most exemplary rulers in world
   history…"*. The frozen A40 §6 addressing test asks whether the bytes
   SPEAK the question, implemented as the literal substring "ashoka"
   (case-folded). This source uses the equally standard spelling
   **"Asoka"**; the literal test therefore fails. The classification is
   recorded as its own word, **OFF-QUESTION**, because none of the six
   frozen categories names a ≥60-char extract that does not speak the
   question - and forcing it into USABLE would be weakening the law to
   buy a green, while forcing it into THIN would be false. Both facts are
   kept: *content arrived = yes*, *usable-at-the-frozen-law = no*.
   The law was **not** tuned after seeing the bytes.

5. **Was the publisher genuinely distinct under existing identity rules?**
   **Yes.** `publisher("https://www.cs.colostate.edu/~malaiya/ashoka.html")`
   = `colostate.edu` (the deep host collapses to the registrable domain),
   distinct from `wikipedia.org`. No new normalization was invented.

6. **Is independent corroboration demonstrated across the held reads?**
   **No.** The held reads now compose two genuinely distinct read
   publishers (wikipedia.org, colostate.edu): addresses 2, **read 2**,
   origin publishers **2**, independence **"candidate"**, conflict
   **"unknown"** - the shared-claim ladder spoke no share, so the levels
   table's verdict is **DIVERSITY-ONLY** ("a distinct origin stands READ;
   corroboration needs the SHARE the ladder did not speak"). A successful
   read is not corroboration, and a distinct hostname is not a second
   voice by itself. What A44 *does* add, modestly, is that diversity now
   holds at the **read** level (two publishers with bytes), not merely at
   selection as in A43.

7. **Does EA1's prior classification change?**
   **No.** A42's **PARTIAL** and A43's **EVIDENCE-GAP** stand
   byte-identical; A35's cycle disposition was not re-run. A44's own
   experiment answer word is **EVIDENCE-GAP** (no read usable at A40 §6's
   four conditions) - a fact about the experiment, not a revision of EA1.

8. **Is semantic improvement measurable?**
   **No - UNKNOWN by law.** There is no answer-leg. n = 1 read at one
   publisher. No performance or causation claim is made from 614.5 ms.

## What A44 actually demonstrated
- The **road works on real HTML**: HTTP 200, real page text, correct
  provenance, no kind wall this time. The A43 PDF wall was a *kind*
  limit, not a general reader failure - and that is now measured rather
  than assumed.
- The **addressing law is the binding constraint**: a genuinely relevant,
  correctly-spelled-in-a-standard-variant page fails a literal
  "ashoka" substring test. This is a **measurement-law limitation**, and
  it is the first finding in this line that is about *how we decide
  usability*, not about what the web returned.
- **Read-level publisher diversity now exists** (2 distinct read
  publishers), with corroboration still explicitly **not** demonstrated.

## What remains unknown
- Whether any held read *corroborates* another (requires a declared
  shared-claim law properly applied, not an identity proxy).
- Whether EA1's answer improves (no answer-leg).
- Whether other held candidates would pass the same addressing test - the
  law's blind spot may or may not be isolated to this source.
- Whether a spelling-aware addressing law would change the word for the
  **already held** A44 bytes - testable at **zero** new reads.

## The next justified experiment (from the observed result)
The observation points at the **law**, not the network, so the next
experiment is a **re-classification over already-held bytes**:
freeze a contract declaring a spelling-variant addressing law (at minimum
`ashoka` / `asoka`, declared *before* any replay), then re-derive the
answer word for A44's held read **with zero new network reads**. That
directly tests whether the addressing law - rather than retrieval - is
what withholds usable evidence, and it costs nothing.
Alternative, if the line instead wants more read voices: a **new** frozen
one-read contract for row 5 (`digitallylearn.com`, HTML) - never a
substitution inside A44. A PDF/text extraction capability remains a
separate, later contract.

## Verification (at committed bytes)
- `python3 tests.py` -> **197/197 pass - HARNESS GREEN** (T167-T196 whole,
  no existing assertion touched).
- Retrieval and integrity batteries: see closeout.
- Contract digest recomputed from its own `A44-POLICY` block:
  `233def8238cc6c81560cee677292dc66ae1504c9d50c14cdbf7abec117163d16`.
- A42/A43 artifacts byte-identical to their manifests;
  `config.json` unchanged (neither search word present).
- Manifest: 5 files, commits local only, tree clean, nothing pushed.
