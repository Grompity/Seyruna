# A18 — the runner carries the door's word (implementation; uncommitted by command)

Starting HEAD `fbdf227` (read at preflight, not assumed); ending HEAD
`fbdf227` — **no commit, no staging** (the §'s hold: a commit rides on a
later, explicit authorization). No reset, no stash, no clean, no history
touch, no `add -A`, no deploy.

## Exact files changed

- **`research_eval.py`** — ONE key added to `run_one`'s door-record, plus
  a four-line comment: `"evidence_status": tr.get("evidence_status")`.
  A `tr.get` — the door's own word, verbatim, never reconstructed from
  answer prose, never independently inferred.
- **`tests.py`** — one new witness, **T161**, at the file's tail (the
  A-era seam idiom: canned packets, a recording door-spy, the real
  `to_rows`/`corroboration` on the canned bytes, and a raising spy left
  on the net seam so the suite stays net-free past T161).
- The present report, untracked for the founder's review (the standing
  precedent for non-real-change milestones).

## The data path, before and after

**Before:** the door stamped `trace["evidence_status"]` (A15) and the
window passed it into the shown `why` — but `run_one` picked
`{code, lane, retrieval, response, model_calls, web_stamped}` into its
door-record and the EVAL record (the JSON that `main` writes to
`research-hold/a5-eval-live.json`) carried no status word at all — the
A16 report named exactly this projection gap. **After:** the same six
keys plus the door's word verbatim; a trace with no word (a pre-A15
shape) rides it as ABSENCE — the key present, the value `None`, never
silently promoted to something verified; the over-budget lane (the
branch that never calls the door) stays sparse exactly as built — the
house's own precedent that an absent word rides as absence, and T161
proves no status key and no raise there; the search-only mode still
grows no door record at all (today's behavior, byte-exact).

## Artifact/schema compatibility — the actual inspection, not a guess

`run_one`'s record has **no schema/version field** (it carries `eval`,
`mode`, `provider`, `caps`, `date`, `review` at `main`'s envelope — no
version to bump); `main` serializes with `json.dumps(rec, indent=1)`
(an additive key rides for free); `main`'s print line picks FIXED keys
through `(d or {}).get(...)` — immune to the addition; **nothing in
`tests.py` or `reviewer/*` calls `run_one` at all** (grep at bytes — the
A18 witness is the first); historical artifacts (`a5-eval-live.json`
lineage, `a13-eval-live.json`) are hand-read files, additive-compatible
by the same facts. **No schema/version adjustment was needed, and
nothing historical was rewritten** to force uniformity.

## Tests added — T161 — and the §'s five requirements, mapped

1. a real status rides the runner's result VERBATIM (and the projection
   is EXACTLY the built seven-key set — the old keys byte-undisturbed);
   2. the A13.4 fold-shape keeps its compound word (`general knowledge,
   not verified this turn (the web brought nothing (search-empty))`)
   WITH `web_stamped` False — emptiness and unverified spoken apart in
   the eval record itself; 3. a missing word rides as absence — key
   present, value `None`, no crash, no silent promotion; 4. the question
   rode byte-identical into the door (`{"question": …, "web": True}` seen
   verbatim by the spy — the body-shape undisturbed), and the answer
   rides the record untouched; 5. `json.loads(json.dumps(rec))`
   round-trips, mirroring `main`'s own serialization. The fold-shape's
   word is a CANNED value in a fixture — the door's live production of
   that same compound is A16's observed fact, not re-claimed here.

**Full suite, exact:** **161/161 — HARNESS GREEN** (T161 green at its
first ride; baseline was 160/161-less at preflight on the same HEAD).

## Model calls and network

**Zero.** The witness patched the search seam (`web_research.research`)
and the door seam (`stages.door`); the real `to_rows`, `corroboration`,
and `run_one` ran on canned bytes. No live request, no mouth, no
deployment, no production change, no CORAL change.

## State confirmations (final battery at delivery)

HEAD `fbdf227` unmoved; the seven founder-staged entries (
`gpt-reviewer.md`, `opencode.json`, both `live-run` JSONLs, all three
`reviewer/*`) still staged and byte-exact (the index untouched by this
milestone); `Seyruna/` (nested repo at `9230080`/main, read-only probe)
and CORAL (`0910554`, `o1-controller`, outside this workspace's git)
unmodified; the A8–A14 artifacts ride untracked as ever; the two
modified files (`research_eval.py`, `tests.py`) carry UNSTAGED
working-tree changes only.

## Limitations and follow-up coins (all unfired, none forced)

- `main`'s human-readable print line does not yet SELECT the word (the
  record carries it; the print stays byte-compatible) — adding
  `| status: ...` is a founder's word, unspent.
- The runner's door-body still pins the query to the question (no
  `query` word) — A15's separation remains the runner's own unspent
  coin, untouched by mandate.
- A live eval run (the a5 document's questions) would now WRITE the word
  into `a5-eval-live.json` — predicted, not claimed (no live probe this
  milestone's kind).
- The `research failed (x)` word-class at the fold branch remains the
  named one-conditional.
- **Status propagated is not claims verified:** the word says the
  TURN's evidence state; whether the answer's individual claims are
  true remains the human review's, and the reviewing model here is
  same-family (`OPENAI_API_KEY` absent throughout).

**Demonstrated by the deterministic suite:** the propagation itself —
verbatim carry, absent-as-absence, sparse-lane and search-only
compatibility, round-trip serialization. **Left to live operation:**
the word's appearance in a fresh `a5-eval-live.json`, and every
answer-quality claim (the A13/A16 records stand as the live witnesses,
byte-unchanged).
