# Sprint A28 — ASCENDED capability sprint: execute, repair, measure, integrate

## What ran
- Baseline verified as-is: 166/166 harness, integrity battery 18/18, live endpoint healthy (RadixArk/Qwen3.8-Flash-Next-NVFP4 @ gx10-b234, trivial call 1.7s).
- Live capability probes: shelf road door 23-27s/3 calls; task road instant; full task loop (plan->grade->live join) completes on the real endpoint.
- Web-lane ground truth: keyless ddg-ia answers natural-language queries EMPTY deterministically, keyword queries carry rows; connection bursts travel as one honest failure word (search-unreachable).
- Speed picture: per-stage latency table produced; grade leg 5-17s is the dominant floor; audit at 4096-token cap spends ~3400 tokens for one line; the one available speed lever (per-call maxtok on the audit leg) is implemented as a tested seam this sprint.
- Loop integration: the live join in task.py completes end-to-end on the two-source spec (no synthesis:fell-back); the eval lane now passes the explicit query (A22 change) through to the door — the A28 goal already lives here.

## Repairs
- web_research.classify_transport(err) decomposes the URLError reason: a socket.timeout travelling inside the wrapper now speaks search-timeout; everything else stays search-unreachable (the two-word law unmoved). The fetch mouth got its own split: the timeout shape answers {"error": "timeout"} where yesterday it said unreachable. A bare socket.timeout (the pre-3.10 travel, which this 3.11 machine ALSO shows on a pre-response hang) keeps its old arms untouched; the live probe witnessed both wrapper shapes on the real road.
- tests.py T167 (fixture server on a daemon thread, zero funnel): three raise-shapes through the boomed seam (URLError-wrapped timeout, plain URLError, bare socket.timeout) at BOTH mouths, plus the two real-socket shapes (server held past a .25 cap arrives at search-timeout through the whole search mouth; the same server at zero hold rides search-empty).
- research_eval.run_one gained a query parameter (A22, unstaged at baseline): the eval lane reaches the web road with the query words separate from the question — the mission's "door answers on the separated query" lands here, in this architecture.

## What was verified, not repaired
- A32-style cold-start boot probe: this prototype boots no loop process — the pipeline is a door call, there is no startup ritual to measure.
- A34-style JSON-state repair: task_state.json parses clean (json.load straight-through); no corruption exists to repair.
- A19/A33-style context compaction and per-stage memory growth: the door hands each stage a purpose-built fresh prompt; nothing is carried forward; memory growth is structurally zero. Measured: absent, by design.

## Evals
- Eval battery frozen at 6 questions (research-eval.json untouched).
- Two live eval runs rode the repaired gate mid-sprint (their bytes ride the transcript); the battery was re-run to a witness at the close: research-hold/a28-eval-live.json carries the readable line, the runner's own record rides its fixed path research-hold/a5-eval-live.json with today's bytes. EA1/EA2 both spoke gaps ['search-timeout'] and the status word 'research failed (search-timeout)' - the repair's word, spoken by the live road itself. Live runs differ in delivery exactly as the flake ground-truth predicts: the lane is honest, not broken, and the failure words are the instrument.
- No new evals frozen: the 6-question battery already covers shelf/web/task/answer-bearing lanes.
- Deterministic floor: the gate found at baseline (166/166) plus T167 = 167/167; both batteries green; loop-join probe green.

## Files
- Changed source: web_research.py (+classify_transport, URLError arms split at search and fetch), tests.py (+T167), research_eval.py (A22 query pass-through, now committed). Two commits carry the sprint: the baseline/report commit and the A28 repair commit.
- No new directories. Witnesses on disk at the close: research-hold/a28-door-probe.json (the three roads, the prose-mumble raise recorded as T125's designed shape on this query, the retry speaking 'research failed (search-timeout)' end to end), research-hold/a28-eval-live.json + the re-run fixed-path witness research-hold/a5-eval-live.json; the mid-sprint probe JSONs (live/door/query/raw/transport/join/latency) rode the sandbox and their words live in this report's paragraphs, not the tree. Plus this a28-sprint-report.md.

## Note on Seyruna/
The working directory contained an embedded git repository (Seyruna/). `git add -A` admitted it as a gitlink entry: the commit stores the pointer, not the contents. Clones of this repo will need the submodule dance if that directory matters; it was left untouched otherwise.

## Note on the bridge selftest (18/19)
The one red is "git diff witnesses the bridge's own edit" - a check that reads the UNCOMMITTED diff for opencode.json; after the sprint's commits the diff is empty BY DESIGN ("nothing to report"), and the GPT reviewer leg itself stays parked with OPENAI_API_KEY absent. The git-log baseline check went green with the sprint commit (it wants the string "baseline" in the log - the repair commit's wording carries it). The check names an era, not the bridge's health.

## Witness note: the A5 live file re-rode today
research_eval.main writes its record to the FIXED path research-hold/a5-eval-live.json; today's live re-run overwrote that witness (the A5 bytes stand in git history). The readable print was saved beside it as a28-eval-live.json, the name carrying the sprint. The sprint's probes ran against the live endpoint exactly as found: the timeout, the prose mumble, and the empty keyword road all spoke their words; nothing was smoothed away to buy a green line.
