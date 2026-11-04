# A43 - publisher-distinct selection, frozen and spent once (closed 2026-11-03, from cec50a7)

## The one line
The frozen publisher-distinct rule selected the FIRST eligible row whose
publisher was not already represented in EA1's evidence - row 3,
`columbia.edu` - and the single authorized read met the road's KIND
WALL: the server answered `application/pdf`, the road refuses non-HTML
kinds by its own law, so the transport ANSWERED and **zero bytes**
arrived. No new usable evidence, no corroboration, EA1 unchanged,
semantic UNKNOWN. The SELECTION law is now measured as deterministic
and content-blind; the diversity question stays open because the bytes
never arrived.

## The eight required statements
1. **Selected result, and why the frozen rule selected it.**
   `https://projects.mcah.columbia.edu/indianart/pdf/asoka_thapar.pdf`
   (publisher `columbia.edu`). The policy excludes represented
   publishers (`{wikipedia.org}`), keeps A40's eligibility unchanged
   (url-bearing, publisher != the instance house `127.0.0.1`), and takes
   the FIRST remaining row in the ORIGINAL packet order. Rows 1-2 rode
   the word `represented`; row 3 wins by ORDER alone. The rule reads no
   path, extension, title, snippet, quality or content.
2. **Was the source successfully retrieved?**
   The TRANSPORT answered - the road's own word `wrong-kind:application/pdf`
   is read from the response headers, so an HTTP answer arrived. The
   road's `wrong-kind` branch discards status/final/body, so
   status/final/retrieved ride **ABSENT (unknown), never zero**. The
   road's `fetch` word is 0 because it counts BODIES READ; the attempt
   rides `calls: 1`.
3. **Did usable, relevant content arrive?**
   **No.** Zero bytes were extracted. The content-type wall is a road
   law, not a content judgment; the PDF was never parsed, so nothing can
   be said about what it would have said.
4. **Was the publisher genuinely distinct under existing identity rules?**
   **Yes.** `publisher()` is the registrable domain: the deep host
   `projects.mcah.columbia.edu` normalizes to `columbia.edu`, which is
   distinct from `wikipedia.org`. No new normalization was invented.
5. **Was independent corroboration demonstrated?**
   **No.** Across the held reads (A42's wikipedia row + A43's columbia
   row): addresses 2, **read 1**, origin publishers **1**,
   independence **none**, conflict `insufficient`, publishers seen 2.
   A distinct publisher alone is never corroboration; no bytes arrived
   to share the ladder with the baseline.
6. **Did EA1's answer classification change?**
   **No.** A42's PARTIAL stands byte-identical; A35's cycle disposition
   is not re-run (no cycle rides in A43). The experiment's own word is
   EVIDENCE-GAP. No claim is made about EA1's answer.
7. **Semantic improvement: TRUE, FALSE, or UNKNOWN?**
   **UNKNOWN** - the duel rides no answer-leg (A40 7/8); declared before
   the bytes, no retrofit possible.
8. **The exact budget spent and the verification results.**
   Searches **0**; reads **1** (one `reads` call, one url, one attempt,
   zero bodies read); retries **0**; substitutions **0**; no extra read.
   Verification: the packet's artifact sha equals the A42 manifest's
   line (`cceae0bc..`); the packet digest is `21d2095a..`; the original
   row order is preserved; the held packet carries NO candidate content;
   the policy digest `937e131b..` recomputes from the contract's own
   block; T196 replays everything offline with the LEDGER unmoved; A42,
   A41 and A40 re-sign at their own manifests and A36's witness at
   A37's stored word; harness **196/196**, retrieval exit 0, integrity
   18/18, bridge 19/19, all compile; manifest 6/6 at committed bytes;
   clean tree; nothing pushed.

## What A43 establishes, and what it does not
- **Establishes:** the publisher-distinct rule is deterministic,
  order-preserving, duplicate-excluding, content-blind (the held packet
  literally has no candidate bytes) and replayable from the contract +
  the packet alone; it picked the first distinct candidate without
  consulting content; the single read is accounted for to the attempt.
- **Does not establish:** that a distinct publisher yields usable
  evidence. The first distinct candidate sits outside the road's
  readable kinds. Diversity at the SELECTION level is not diversity at
  the EVIDENCE level.
- **The wall is precise:** not a fetch failure, not a content judgment,
  not search unavailability - a KIND wall at a real HTTP answer. It is
  a road limit to be named, not a source to be blamed.
- **On the frozen levels word:** the table returns
  MONOCULTURE-PERSISTS for a recorded non-infra road word; its `why`
  carries the real meaning ("a fact about THIS address"). That word is
  NOT a claim that columbia.edu belongs to a monoculture; the plain
  dimension word is "no bytes arrived; nothing corroborated".

## The disambiguation, declared before the read
"Publishers already represented in the EA1 evidence packet" is read as
REPRESENTED IN THE EVIDENCE (the voices already read and held:
`wikipedia.org`). The alternative reading - any publisher present
anywhere in the packet - would empty the candidate set and spend ZERO
reads; it is recorded in the contract and the artifact, and NOT taken,
because the mission names the three unread publishers as the candidates
this experiment is about.

## The gates (run, not copied)
Harness **196/196 HARNESS GREEN** (T167-T195 whole; T196 is ALL offline
- the policy frozen in the contract's own block and digested, the
packet byte-verified with no candidate content, the OLD first-two law
reproduced and A42 untouched, the NEW rule deterministic with the two
represented rows skipped and the first distinct publisher winning by
order, the no-candidate packet spending zero reads, EXACTLY one
authorized read, the dup lanes excluded, transport kept apart from
content, the missing provenance kept as ABSENT words, success NOT
treated as corroboration, the levels word re-derived at the baseline
primary, the answer map replayed, EA1's classification unchanged, the
eight dimensions separate, semantic UNKNOWN, the ledger unmoved, and
the history whole). Retrieval GREEN (exit 0), integrity 18/18, bridge
19/19 BRIDGE GREEN, all compile. The manifest (6 files, including
`research_eval.py` - the one code motion is the declared pure
`pick_distinct43`; the roads, templates and registry are untouched)
re-verified at COMMITTED bytes. Clean tree; nothing pushed.

Two honest notes on process: one test assertion's case-sensitivity was
corrected at draft time before the green run (the function's
no-candidate note is lowercase) - no substantive assertion changed; and
one ACCOUNTING field (`read-accounting`) was added to the artifact at
bytes before any commit, clarifying that the road's `fetch` word counts
bodies, not attempts - no measurement, word or class changed.

## The next decision (two honest options, no silent substitution)
1. **Read the NEXT distinct publisher** - `colostate.edu` (row 4, an
   HTML page) - under a NEW one-read contract that declares its rule
   BEFORE its bytes (e.g. "the first unrepresented row after the
   already-selected one"). That is the natural continuation of this
   line, but it must be its own frozen sprint: spending it today would
   be a substitution after the fact.
2. **Add a read KIND** (PDF text extraction) as a capability with its
   own contract, if the product wants PDFs to count as evidence.

A43 measured the SELECTION, not the voice. The second voice rides
un-shown - and now with a sharper map of where it can hide.
