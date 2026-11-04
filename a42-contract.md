# A42 contract - the controlled endpoint and the resumed EA1 duel

## 1. The frozen question and its bytes
EA1 rides its RECORD's bytes, not the mission's prose: b"Ashoka rock
edict" (no terminal dot). The duel asks the controlled instance ONCE;
the query bytes ride UNTOUCHED.

## 2. The held baseline (never re-felt, re-signed at the test)
- research-hold/a36-read-EA1.json (e73913779d41..) - the same-question
  measured READ witness: the held PRIMARY is W1 (en.wikipedia.org,
  publisher wikipedia.org) with its claim bytes.
- research-hold/a35-cycle-EA1.rerun.json (7c588f594bdb..) - the final
  EA1 cycle record.
- A40 (search-http-403 at the registered route) and A41
  (search-malformed at a documented public instance) ride as HISTORY -
  the two blocker records; neither is re-run, neither is reinterpreted.
- The closed ddg-ia stub family (A36 + A38 + A39) rides CLOSED - not
  re-opened by this sprint.

## 3. The deployment (chosen from the REAL environment, verified first)
- Environment, verified before any choice: macOS 14.5 arm64; Python
  3.11.0 (/usr/local/bin/python3); Docker ABSENT (checked, never
  assumed); PyPI 200 and GitHub 200; ports 8888/8080 free; 18 GiB free.
- Approach: the project's OWN source, a shallow clone pinned at commit
  cccbc9e158b0 (recorded), its runtime requirements in a venv OUTSIDE
  the repository, run with `python -m searx.webapp` and
  SEARXNG_SETTINGS_PATH pointing OUTSIDE the repository.
- Why not the alternatives (each checked, not assumed): Docker is
  absent on this host; PyPI's `searxng` 0.1.2 is a placeholder package,
  not the application; no public instance is available (A40's 403,
  A41's parse-death, A4's roster - HISTORY, not re-probed).
- The settings surface (recorded; the secret is generated locally and
  NEVER committed): use_default_settings true; bind_address
  127.0.0.1; port 8888; limiter false; public_instance false;
  image_proxy false; search.formats [html, json]; safe_search 0;
  instance_name "a42-controlled-duel".
- Exposure: LOOPBACK ONLY. No public bind, no TLS, no reverse proxy,
  no authentication surface, no admin value in the repository. The
  instance is SESSION-BOUND (no launchd/system service installed);
  that is declared, not hidden.
- The engine layer: the box aggregates its own default engines over
  this host's network. That is the box's WORK, not independent
  corroboration (see 10).

## 4. The integration (the ACTUAL reader, not the env)
- Verified before the window: config.json carries NEITHER
  SEARCH_PROVIDER NOR SEARCH_BASE (production rides the default
  ddg-ia), and SEARCH_BASE's only home is stages.CONFIG (A8 proved the
  environment is not its home).
- The window adds EXACTLY TWO WORDS to config.json:
  SEARCH_PROVIDER="searxng" and SEARCH_BASE="http://127.0.0.1:8888".
  Nothing else is touched. ASCENDED_SEARCH is POPPED in the run
  process and PROVEN absent, so provider_name() reads the CONFIG word
  (the mission's law: no assumption that the environment overrides).
- Isolation and restoration: the original config.json bytes are copied
  OUTSIDE the repository and sha256'd BEFORE the window; the window is
  restored in a `finally` BYTES-EXACT (never re-serialized), then
  verified: file sha == pre-sha, stages.CONFIG == the file (reload),
  provider_name() == "ddg-ia", SEARCH_BASE absent. Production ends as
  it began; if the deployment had failed, the same path restores it.

## 5. The protocol check (Phase 3; deployment face; ONE event)
Observed at 23:44 local, before this contract was written: GET
http://127.0.0.1:8888/search?q=wikipedia&format=json -> status 200,
content-type application/json, body 35672 bytes, JSON VALID (keys
answers, corrections, infoboxes, query, results, suggestions,
unresponsive_engines), results 33, first row https://www.wikipedia.org/
(engine brave), unresponsive engines: duckduckgo (CAPTCHA). The query
"wikipedia" is HARMLESS and is NOT the frozen EA1 bytes. This is
DEPLOYMENT evidence, not research evidence; it spends no research
budget and no research rule rode on it (it gated only the
reachable/unreachable branch of 3).

## 6. The duel (Phase 4; A40's frozen continuation, unchanged)
ONE search (search() rides it once) + AT MOST ONE reads call carrying
AT MOST the TWO first eligible urls; no retry, no second search, no
fan-out, no substitution. ELIGIBLE = the row carries a url AND
publisher(url) is not the instance's OWN house (provider_host at the
window). Lane/title/snippet presence gate NOTHING. A read row is USABLE
when: the road OPENED (status present, no error word) AND the extracted
bytes >= 60 (the road's own furniture floor) AND the publisher is
OUTSIDE the house AND the bytes SPEAK THE QUESTION ("ashoka"
case-folded). All four, at A40 6's words. Classes at the search face:
any search-* transport/parse word -> PROVIDER-UNAVAILABLE; the sole
"search-empty" -> SEARCH-EMPTY; rows present but none eligible ->
RESULTS-NO-USABLE-EVIDENCE.

## 7. The answer-words (declared BEFORE the duel's bytes)
The mission's four words, mapped deterministically at the DUEL's own
face (A35's cycle disposition is NOT re-run - the duel is not a cycle,
A40 7; no retrofit is possible):
- RETRIEVAL-FAILURE - the search face failed (a search-* word).
- EVIDENCE-GAP - the search spoke and NO usable read rode (no eligible
  row, or every rode read non-usable at 6's four conditions).
- PARTIAL - at least ONE usable read AND at least one rode read
  non-usable (including an allowance that could not be spent whole).
- EVIDENCE-BACKED - at least ONE usable read and EVERY rode read
  usable.
`answer42()` is the ONE pure mapper; it moves NO existing rule
(levels36 / dispose / candidate36 ride unmoved).

## 8. Semantic improvement
UNKNOWN BY LAW unless a BYTES-word moves the ANSWER itself; the duel
rides NO answer-leg (A40 7). Declared NOW, so no retrofit is possible.
Evidence arriving is NOT semantic improvement.

## 9. Budgets (declared)
- Deployment: 1 protocol request (spent; zero dollars; nothing
  purchased; no external account touched).
- Research: at most 1 search + at most 2 read lanes (2 fetch events),
  total at most 3 net events. No retries, no query broadening, no
  second search.
- The local box spends its OWN engine requests; that is its work, and
  it is recorded at the deployment face only.

## 10. What this record will NOT claim
No broad-web voice from one provider (n=1); no independence from a
hostname; no semantic movement without a bytes-witness; no causation;
no performance claim from one latency; the box's multi-engine
aggregation is not corroboration; tonight's loopback availability is
not a service commitment.

## 11. The exact restoration / stop path
- config.json: restore from the held backup bytes (path recorded),
  verified at file AND mirror (reload).
- the instance: kill the listener on 127.0.0.1:8888; venv, settings
  and clone live OUTSIDE the repository (paths recorded) and are never
  committed.
- Nothing is pushed.
