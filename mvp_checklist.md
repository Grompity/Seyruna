# mvp_checklist.md — pre-code checklist (the build order's §12 paper)

*(the door = one route over the existing spine; the window = one
renderer over the existing trace. Nothing else is added. Everything
below names bytes, not intentions.)*

## 1. FILES TO TOUCH
- `server.py` — one POST route (`/ask`) + one import of stages. The
  static Handler survives untouched beneath it.
- `window.py` — NEW, the window: one pure function over a trace dict.
- `mvp.html` — NEW, the ugly desk page (one box, one line, the answer,
  one fold). The landing page is not the desk.
- `tests.py` — append exactly TWO witnesses (T56/T57), ordered by the
  door/window's new failure modes, inserted before the run loop.
- After the runs (records): a new section appended to `five-visible.md`
  (originals sacred), and this file's report half.

## 2. FILES NOT TO TOUCH
`stages.py` (the spine — the door WRAPS it; it is already the
pipeline), `proto.py` (the CLI exemplar stands), `shelf.jsonl`
(FROZEN for the build — §5), `rule_pack.json` / `config.json`
(RP-0.2, endpoint/model/key unchanged), `voice_brief.md`, the law files
(constitution, architecture, golden-set), `integrity_battery.py`,
`projection.py`, `mutate_*.py`, and the landing shell (`index.html`,
`css/`, `js/`).

## 3. ENTRY POINT
POST `/ask`, same origin, synchronous, one request at a time. Body:
`{"question": "...", "facts": "..."}` with `facts` optional (the
seeker's own context line). `stages` at import auto-loads the shelf
(`SHELF = _load_shelf()`) — the door needs NO init of its own. The
route runs `run_pipeline(question, facts, live=True)` — no packet:
the product always rides the retrieval lane.

## 4. INPUT/OUTPUT CONTRACT
200 with `{"response": ..., "why": ..., "trace": ...}`. `response` is
`trace["response"]` verbatim (the UI never re-renders speech). Bad or
missing body → 4xx JSON with an `error` key — never a laundered
default, never an invented sentence.

## 5. TRACE CONTRACT (the verbatim bytes, from run_pipeline)
`versions` (…build "proto-0.1") · `retrieval` (the shown ids) ·
`lane` ("packet" only when a packet was given — never in product
traffic) · **early return**: when the shown set is EMPTY and no draft,
the trace is ONLY {versions, retrieval, fires:["RP-10"],
unknown:true, response:P["unknown_plain"]} — the mouth is never
called at the empty lane; `P["unknown_plain"]` is frozen RULE-PACK
DATA. Full shape: `frame` (factors/indicators/human) · `analysis` ·
`draft[]` (node, cites, verbs, level, reading, notes, cite_dropped,
lineage) · `fires` · `observations` · `blocked` · `caution_appended` ·
`audit_findings` · `repair_ops` · `required_content` ({text, rule
"RP-02", survives_to_speech} when appended) · `response`. The
disposition-A arm: when blocked, `response` is REPLACED by
`plain_render(ids)` — the lane's printout, recorded.

## 6. WINDOW CONTRACT
Six questions, each answerable from RECORDED bytes only, each line
tagged with the key it came from:
- EVIDENCE ← `retrieval` × the shelf's rows (claim, level,
  kind-WHEN-PRESENT — absent is silence, edges).
- DISTINCTION ← the shown records' `kind`/`level` fields (data, not
  the window's opinion).
- DISAGREEMENT ← edges BETWEEN shown records, plus the RP-13-family
  observations when fired.
- UNCERTAINTY ← `unknown` (the exit), `observations`, `caution_appended`,
  `required_content` when present.
- SYNTHESIS ← each `draft[].lineage` label + its `cites` (SOURCE vs
  SYNTHESIS vs UNSOURCED — the field the seven validated, now shown
  where a human eye first reads it).
- BOUNDARY ← `blocked` (why the plain lane spoke), `fires`,
  `audit_findings`, `repair_ops` — the machine's RECORDED refusals and
  repairs, in order.
LAWS: display the law's outputs, add no claim; the window may NOT read
the response text to find reasons (no reading-back); it must tolerate
the EARLY-RETURN shape (missing keys); it is an inspect — the trace
votes nothing, so the window gates nothing.

## 7. TEST COMMANDS
Floor, all five green before anything else is trusted:
`.venv/bin/python3 tests.py` · `mutate_test.py` · `mutate_kind.py` ·
`integrity_battery.py` · `projection.py`
Product, live (the funnel IS the product): one curl POST as the door's
first breath; then one urllib script — the five verbatim + ONE probe
POST (an out-of-shelf question — the empty lane's first HEARING,
ordered by the accepted spec, not a new battery).

## 8. THE FIVE, AS THE RECORD HOLDS THEM
Questions verbatim from `five-visible.md` (the owners' red lines = the
FAIL-IF lines there). FACTS bytes from the deck (`round1-log.md` card
blocks); C5's facts = the founder's repaired verbatim (§M — "so no
mouth may re-invent it"). No new expectations after seeing output (§7).

## 9. ACCEPTANCE
(1) the five responses arrive verbatim through the door; (2) the five
FAIL-IFs: shapes reported, verdicts reserved to the owner's First
Seeker seat; (3) regression floor prints its counts from the run,
bumped by EXACTLY the two authorized witnesses (55→57), nothing else
moved; (4) empty-lane: "met" or "not met by the five", plus the probe's
verbatim; (5) the five tests (USEFUL / HONEST / INSPECTABLE /
SELF-STANDING / NON-DEPENDENT) reported as structure — the owner reads
them; (6) nothing built that the letter did not order: no state, no
memory, no second reasoning system, no aesthetic act.

## 10. THE ONE FACT FOUND WHILE LOOKING (logged, no action taken)
The empty lane is CODE-side: RP-10's short-circuit answers with
`unknown_plain` and never calls the funnel mouth. The letter's
"unheard voice" at the funnel will therefore hear the MACHINE's fixed
lawful sentence, not a model's — the probe will say so, and the
classification (if any) follows the hearing, never precedes it.
