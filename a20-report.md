# A20 — the live evaluation of the A15→A19 stack (diagnostic; nothing changed, nothing committed)

Start and end HEAD `fbdf227` (read, not assumed) with the A18+A19 stack
present in the working tree exactly as delivered (three ` M` files,
+229/−15). No commit, no staging, no reset/stash/clean, no deploy, no
production change, no source or test change, no CORAL change. **Zero
retries spent, zero errors, provider word `ddg-ia` (no keys, no
credentials, no config values exposed).**

## Run configuration, and the §2 preflight question, answered at bytes

**The frozen doc** (`research-eval.json`, EA-0.1): six FROZEN questions
— running `main` verbatim would spend the live run on all six, and
A20's mandate is two; **the runner's query question:** `run_one`'s door
body is `{question, web}` (research_eval.py:64) — **no query field** —
so per the §'s command the runner was NOT modified and the faithful
invocation is the runner's own per-case unit `run_one(qtext, live=True,
caps)` with the document's caps (`max_calls_per_question 8`,
`max_secs_per_question 240`). Consequence, disclosed: for both cases the
search query RODE AS THE QUESTION (case A's question IS the
previously-successful two-word name; case B's is the previously-empty
sentence — each the same bytes its predecessor turn used); the human-
readable line was produced through the SAME `status_word` selector the
print uses (the selector is pure; mirroring main's print is a read, not
a change). Baseline suite before anything: **163/163 — HARNESS GREEN**.

**Artifact, no obstacle:** the driver wrote a fresh
`research-hold/a20-eval-live.json` (unique name; envelope carries
`eval: a20-diagnostic`, date, provider, caps, mode, and the two full
`run_one` records). `main`'s fixed `a5-eval-live.json` was NOT run and
NOT overwritten; A13/A16 records ride untouched.

## Case A — the previously-successful research-shaped query (69.9 s, 3 model calls)

Question and search query both `"Ashoka rock edict"` (the faithful
`run_one` shape, above). Search: 200-class lane, **5 results, gaps
empty**; web-phase spend `search 1, fetch 2`; corroboration `{urls: 5,
read: 1, attribution: 4, origin_publishers: 1}`, `independence: none`.
Fetch outcomes at the rows: **W1 READ** (`wikipedia.org`, page, note
`http 200 (capped)` — the A-era bytes-cap, at bytes), W2 fetched
snippet (note `http 202`), W3–W5 `not-fetched:dup-publisher` snippets.
Read windows: **one**, distinct read publishers: **one**; snippet/
attribution rows: **four**. **Recorded status, exact:**
`carried by: wikipedia.org (read)`; **printed status:** the same bytes,
selected by `status_word` (`| status: carried by: wikipedia.org (read)`);
**the artifact holds the same value** (verified by re-reading the
written file). The answer is a RECITATION — it opens with the house's
own caution phrase (not a claim), then recites the read window's
infobox bytes, and finishes with the three stubs' own sentences.

## Case B — the previously-problematic sentence (31.9 s, 2 model calls)

Question and query both the A13.4 sentence. Search: **successful EMPTY
— third live sighting of A13.1's law on these exact words at three
different milestones and HEADs** (`results 0, gaps ['search-empty'],
indep word: unknown`); fetch 0; all corroboration counts 0. Lane
`general`, **recorded status, exact:** `general knowledge, not verified
this turn (the web brought nothing (search-empty))` — the A19
emptiness-side compound, live at the real path; printed identical;
artifact holds it. The answer is pure prior-knowledge speech (duty
lists, officers of dhamma, the royal kitchen) from a turn that read
NOTHING — and the word says exactly that, at the record, at the line,
and in the file.

## Claim-level audit (same-family operator reading — independent human fact-check PENDING)

**Case A** (classes as the § names them; citation membership ≠
entailment, applied):
- Infobox bytes (pillar at Lauriya Araraj; sandstone; "3rd century
  BCE"; "present location" list) — **supported by the actually-read
  window W1** (the answer's bytes sit in W1's claim verbatim) —
  **unclear/human-review:** the recited infobox's referent thinned
  (the location list belongs to the LAURIYA PILLAR, not to all the
  edicts), and the mangled "3rd" rides as-spoken.
- "More than thirty inscriptions… Mauryan… 268 to 232 BCE" —
  **supported by the READ window W1** (its own tail bytes).
- Delhi-edicts sentence — **present only in a snippet (W4, unfetched
  attribution row)**. "Carved in-situ or on pillars" — **snippet
  (W3)**. "14 separate major Edicts… preceded by the Minor Rock
  Edicts" — **snippet (W5)** — the headline number again rides an
  attribution row, not the read origin (A13.3's finding, re-met, no
  drift). Nothing contradicted by retrieved evidence.

**Case B**: every material claim (lived ethic; the duty list; turn from
war; officers of dhamma; sects and orders; the household; animal
slaughter cut back / the royal kitchen) is **not established by
evidence retrieved during this turn** — nothing was retrieved — and
none contradicted (nothing stood to contradict). Whether they are TRUE
of the record is the human fact-check, pending; the system's own
status word correctly declines to claim verification for this turn.

## What this run demonstrated; what remains unverified; the one next step

**Demonstrated (live, at the record, the print, and the file):** the
A18 propagation and the A19 presentation work in a fresh evaluation on
BOTH lanes the system can currently produce — the read-origin lane
and the emptiness lane; the words are byte-identical across
door-record, printed line, and artifact; the lane-laws (A13.1's shape
law; A15's fold shapes) held at a third live sighting; A19's FAILURE
word (`research failed (X)`) rode NO live traffic here (no failed
search occurred) and stands only at its deterministic pins plus A16's
dry seam ride. **Remains unverified:** the human fact-check of both
answers' real-world truth (same-family audit only); the failure arm's
LIVE appearance (the second family's name still stands behind any
`candidate`); the `query`-separation live ride (the runner carries no
query word — A15's feature stays unexercised at the runner);
claim-level entailment remains the human's, never the word's.

**The single highest-value next engineering step:** **commit the
A18+A19 stack with the A19 report (the A17 pattern) — A20 has now
verified the propagation and the presentation live on both producible
lanes.** The standing design coins (the runner's `query` body word,
the caption-past-the-sentence picker, the mouth asked to speak the
word) remain unspent, unfired, and unforced.

## State preservation, re-confirmed at the close

Seven founder-staged entries still staged and byte-exact (the index
never touched by a diagnostic); the three A18/A19 ` M` files still
unstaged and byte-unchanged by the run; `Seyruna/` and CORAL outside
the modification scope, untouched; A8–A19 reports and every A8–A16
`research-hold` artifact ride untracked as ever; the suite baseline
163/163 stands (no code moved, no reason to re-run mid-run — the close
battery re-ran it green, below).
