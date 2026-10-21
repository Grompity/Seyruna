# Sprint A29 — the speed seam, the mumble's lane, and the de-pinned bridge

## Commits and exact files
- Implementation: `stages.py` (the call seam's thinking word; the three seam caps;
  the synthesize lanes; the trace's `synth_note`), `config.json` (the words
  `GRADE_MAXTOK: 1200`, `AUDIT_MAXTOK: 1200`, `SYNTH_MAXTOK: 3000` - every one
  under the global `MAXTOK: 4096`), `evaluator.py` (the counted witness
  learns the seam word), `tests.py` (T168/T169/T170; the `_Mouth` double
  learns the word).
- Bridge: `reviewer/selftest.py` (two era-pinned checks de-pinned).
- Evidence: `research-hold/_a29_probe.py` (the measurement script - a probe,
  `_`-prefixed like its A28 kin), `research-hold/a29-before.json`,
  `research-hold/a29-after.json` (retained results), this report,
  `a29-manifest.sha256`.

## Root causes
1. **The latency.** The endpoint's THINKING mode is the whole floor: the grade
   prompt costs 19-25s with thinking and **2.4s without it** (valid array,
   finish=stop, the same measured minute). `max_tokens` caps thinking+content
   together and the CONTENT RIDES BEHIND the thinking bytes - a cap inside
   the thinking truncates the content away entirely (finish=length with an
   empty content: the fast-but-fell-back trap). So a smaller cap alone buys
   NOTHING (the thinking still runs); the provider-specific word
   (`chat_template_kwargs: {"enable_thinking": false}`) is the lever. The two
   mechanical mouths (grade, audit) speak it; the voice seam (synthesize)
   KEEPS its thinking and got only its own cap (3000, a tail bound).
2. **The raw raise at the synthesis boundary.** `grab_json` raises ValueError
   when the mouth answers prose; grade and audit had caught it for ages
   (grade-fell-back; the audit's silent `pass`), synthesize did not - it had
   a lane for the EMPTY completion only (the A-era two blips). The prose
   A28 witnessed live (twice, the Tao-Te-Ching sentence) now LANES: the road
   is the empty-completion's own (no nodes -> `blocked` -> the shelf's plain
   render), the bounded head rides the trace as `synth_note`
   (`synth-mumble: ...`), the two blank shapes are named apart
   (`synth-truncated` when the cap cut it, `synth-empty` when the mouth
   really said nothing), an array of non-dict rows is a malformed contract
   TOO (yesterday a raw TypeError at the next boundary), and the dead
   mouth's word (`[MOUTH ERROR...`) STILL RAISES - T125's eval-address
   law UNMOVED, its why-clauses byte-identical.
3. **The bridge's two reds.** Both checks were pinned to an era's bytes: one
   wanted the word `opencode.json` in the UNCOMMITTED diff (the tree
   committed; the era ended), one wanted the word `baseline` inside the LAST
   THREE log one-liners (the window moved on). The repairs assert the
   permanent shapes: the diff speaks the tree's truth (a real hunk or the
   honest nothing-word); the log answers N asks with N lines.
4. **The test doubles.** `tests._Mouth` and `evaluator._Counted` wrap the
   call seam's signature; the seam gained a word so they learned it. T125's
   and T167's assertions rode unchanged.

## Latency: before and after (same script, same question, one run each)
- The raw sweep (thinking ON at BOTH timestamps - the probe measures the
  endpoint, not the seams): grade@4096 24.8s -> 32.1s; the endpoint's own
  variance is ~30%, and it eats any single-sample whole-total claim.
- The deterministic shape probe (the same prompt bytes, the same minute):
  thinking ON 19.0s vs thinking OFF 2.4s, valid array; a cap at 700 lands
  finish=length with EMPTY content (the behind-the-thinking proof).
- The end-to-end door (live, both timestamps): total 23.9s -> 20.0s;
  grade 4.6s -> 1.4s (-70%), audit 8.8s -> 1.1s (-87%), synthesize 10.5s ->
  17.4s (the voice's own variance, the floor now it owns). The two mechanical
  seams' delta (5-8x, twice witnessed) is far outside the endpoint's noise;
  the whole-total delta (16% on this sample) is NOT a defensible claim at
  n=1 - the road's floor is now one synthesize thought, and that is the
  next sprint's number to move.
- The task road (2ms, zero mouths) and the shelf/general road (15.3s at A28,
  one THINKING general mouth) rode as the A28 witnesses recorded them.
  NOTE: the general road speaks NO seam word today (unchanged bytes) -
  the A28 road's cost is untouched by design; a next-sprint candidate.

## Live observations vs deterministic replay
- Two A29 LIVE door runs (the before/after probes) completed - no raw raise,
  no mumble drawn this time (the provider was in an array mood twice; the
  A28 mumble was witnessed 2x2). The after-run's node render is real.
- The mumble's lane is proven by DETERMINISTIC REPLAY of A28's live bytes
  (T169's first shape is the recorded sentence, verbatim) - replay, not a
  new live observation, and labelled so.
- The synthesis timeout shape at the probe's first run rode as A28 left it.

## The gates as found at the close
- Harness: **170/170 - GREEN** (167 rode in + 3 new), also green THROUGH the
  bridge (`reviewer_run_tests`).
- Retrieval battery: green. Integrity battery: **18/18**.
- Bridge selftest: **19/19 - BRIDGE GREEN** (first time this repo has shown
  that word since the bridge was written; the GPT reviewer leg is NOT part
  of the count - it rides keyless-parked, disclosed, unfunded).
- Manifest: `a29-manifest.sha256` digests this sprint's four artifacts.

## Remaining blockers
- The GPT reviewer leg: OPENAI_API_KEY absent; recorded unavailable, no
  paid service provisioned on its behalf.
- The whole-road floor is now the single synthesize thinking call
  (10-17s, wide variance). Two open questions the bytes cannot answer yet:
  does the voice hold its law with `enable_thinking` off (a cheap A/B at
  the T-seam? - it would collapse the last big floor), or does the voice
  need the thinking it costs?
- The general (shelf-silent) road still pays the full thinking cost - the
  seam word was scoped to the three pipeline seams by evidence, not by
  the road's economics.

## The highest-value next target
The synthesize seam itself: A/B its voice with thinking off at the real
door (two or three live runs, the node renders weighed by the T-laws, not
by taste), and either collapse the floor or MEASURE the voice's price of
thinking into the config as a chosen word. The shelf-silent general road
is the same word's second address.
