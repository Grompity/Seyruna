# A42 - the controlled endpoint, deployed and questioned (closed 2026-11-03, from 709cb45)

## The one line: the box was BUILT, the road OPENED, and the pick was the BASELINE'S OWN VOICE
The controlled SearXNG instance was deployed on this host (loopback
only), proven at the real JSON endpoint, wired through the ACTUAL config
reader, and questioned ONCE at the frozen EA1 bytes. The search lane
SPOKE for the first time in this line's searxng history: 5 rows, gap
None, one ledger call, 1350 ms. The frozen eligibility law passed all
five; the frozen pick (the FIRST TWO eligible, content-blind) landed on
TWO wikipedia.org rows - and the first of them is the BASELINE's own held
primary address (en.wikipedia.org/wiki/Edicts_of_Ashoka). The road's own
dup-publisher law then spent ONE of the two read lanes, so the allowance
could not be spent whole: 1 fetch, 200, 1200 extracted chars, the bytes
SPEAK the question; the second lane rode its `dup-publisher` word. The
levels table re-derives **MONOCULTURE-PERSISTS** ("the voice repeats");
corroboration's counts say **none** (1 read, 1 publisher, no
independence word); the declared answer-word is **PARTIAL**; semantic
improvement is **UNKNOWN**.

## The deployment (verified environment, smallest viable, no assumption)
- Environment, verified first: macOS 14.5 arm64; Python 3.11.0; Docker
  **absent** (checked, never assumed); PyPI 200 and GitHub 200; ports
  8888/8080 free; 18 GiB free.
- Approach: the project's OWN source, shallow clone pinned at
  `cccbc9e158b0ac3bb2158e9841a647a5bec57b57` (2026-11-02), its runtime
  requirements in a venv OUTSIDE the repo, run as
  `python -m searx.webapp` with `SEARXNG_SETTINGS_PATH` OUTSIDE the
  repo.
- Two deployment defects were met and worked around WITHOUT touching the
  repo: `pip install -e .` dies in build isolation (`msgspec`), and
  `python searx/webapp.py` puts the script's own directory first on
  `sys.path` (`ModuleNotFoundError: No module named 'searx'`); the
  module entry with the repo root on the path is the one that stands.
- Settings (surface recorded; the secret was generated locally and is
  NOT in this record and NOT in the repo): `use_default_settings: true`;
  `bind_address: 127.0.0.1`; `port: 8888`; `limiter: false`;
  `public_instance: false`; `image_proxy: false`; `search.formats:
  [html, json]`; `safe_search: 0`; instance name `a42-controlled-duel`.
- Exposure: LOOPBACK ONLY - no public bind, no TLS, no reverse proxy,
  no auth surface. The listener line recorded at the artifact's bytes:
  `TCP 127.0.0.1:8888 (LISTEN)`. The instance is SESSION-BOUND: no
  launchd/system service was installed, so tonight's availability is not
  a service commitment.
- Protocol check (deployment face, ONE harmless request, spent before
  the duel and not part of its budget): `GET
  http://127.0.0.1:8888/search?q=wikipedia&format=json` ->
  **200**, `application/json`, 35672 bytes, JSON VALID, **33 results**,
  first row `https://www.wikipedia.org/`. Engines that ANSWERED:
  `brave`, `google cse`; `duckduckgo` rode CAPTCHA. That engine-distress
  word is the BOX's aggregation fact, not corroboration.

## The integration (the config reader, proven; the env proven absent)
- Before the window, config.json carried NEITHER `SEARCH_PROVIDER` NOR
  `SEARCH_BASE` (verified: production rides the default ddg-ia).
- The window added EXACTLY the two words: `SEARCH_PROVIDER="searxng"`,
  `SEARCH_BASE="http://127.0.0.1:8888"`. `ASCENDED_SEARCH` was popped
  in-process and PROVEN absent, so `provider_name()` read the CONFIG
  word; the derived route was exactly
  `http://127.0.0.1:8888/search?q=Ashoka+rock+edict&format=json`.
- Restoration: the pre-window bytes were held OUTSIDE the repo and
  restored BYTE-EXACT in a `finally` (never re-serialized):
  pre-sha256 `0b23f30ae0c89f61080796ef7fcf04196ca384f2855efb07826ee6fb27a931d0`
  equals today's file; the mirror reloads clean; `provider_name()` is
  `ddg-ia` again; neither word is in the file. Production ends as it
  began. That is also the exact restoration path had the deployment
  failed.

## The duel (frozen law, unchanged; one search, one reads call)
- Search: `Ashoka rock edict` (record bytes, no dot), 2026-11-03T23:47:51,
  1350.1 ms, gap **None**, **5 rows** (all lane `result`), ledger 1.
- Rows in the provider's own packet order: wikipedia.org x2
  (`Edicts_of_Ashoka`, `Major_Rock_Edicts`), columbia.edu (a PDF),
  colostate.edu, digitallylearn.com. Titles and snippets present; they
  gated NOTHING.
- Eligibility (A40 5): all five carried a url with a publisher outside
  the instance house (`127.0.0.1`). Pick = the first two, content-blind
  -> both wikipedia.org; three eligible rows rode UNSPENT beyond the
  allowance.
- Named road: ONE `reads` call with those two urls -> 1 fetch, 943.6 ms.
  Row 1: status 200, extracted 1200 chars (the cap), the bytes SPEAK the
  question, publisher wikipedia.org. Row 2: `skipped: dup-publisher` -
  the A7 dup-lane, a LAWFUL word, not a missed budget and not a retry.
- Levels (A40 7: at the BASELINE's held primary, the A36 witness):
  **MONOCULTURE-PERSISTS** for both lanes - the first is literally a
  REPEAT of the primary's publisher; the second never opened. The
  primary IS the pick's first address.
- Corroboration (the table's own words): urls 2, **read 1**,
  attribution 0, **origin publishers 1**, independence **none**,
  conflict `insufficient`, publishers seen 1, duplication 1.
- Answer-word (declared before the bytes, contract 7): **PARTIAL** -
  one usable read of the authorized two, the second unspent by the dup
  law.
- Semantic improvement: **UNKNOWN** - the duel rides no answer-leg, so
  no bytes-word can move the ANSWER itself; declared before the bytes,
  no retrofit possible.

## What MOVED, what did NOT (the words the bytes allow, no more)
- MOVED: availability at a controlled endpoint. A40 died at a 403 gate
  and A41 at parse-death; both ever SPOKE ZERO rows. Tonight a real JSON
  search returned five usable rows and a real page opened with bytes
  that speak the question. That is a genuine end-to-end advance of the
  integration.
- DID NOT MOVE: independence. The strongest pick the frozen rule allows
  landed on ONE publisher, and that publisher is the baseline's own.
  Monoculture persists at the SELECTION, measured - not assumed.
- The row set DID contain three other publishers (columbia.edu,
  colostate.edu, digitallylearn.com). They rode UNSPENT because the
  frozen rule is content-blind and takes the first two. That is a fact
  about the row set and the RULE, NOT a reason to re-run today: changing
  the pick after the outcome would be the very retrofit the law forbids.
  The rule question is a NEXT contract, not an amendment to this one.
- NOT CLAIMED: that the web has a second voice (n=1 provider); that a
  distinct hostname is a voice; that anything moved semantically; any
  causation; any performance claim from one latency; that the box's
  multi-engine aggregation is corroboration; that tonight's loopback box
  is a durable service.

## Acceptance (the mission's own A/B/C, said plainly)
- A (end-to-end success) is MET for the INTEGRATION: deploy -> protocol
  -> config-reader -> duel -> restore, all proven.
- The RESEARCH outcome is the C-shaped finding: backend up, research
  weak - one voice, no independence word, PARTIAL, semantic UNKNOWN.
  Reporting it as "success" without that second half would be the lie
  the charter exists to prevent.

## The gates (run, not copied)
Harness **195/195 HARNESS GREEN** (T167-T194 whole; T195 is ALL offline
- the loopback-only posture, the protocol-check words at the deployment
  face, the config-as-reader window and its byte-exact restoration, the
  search's five rows and the frozen two-pick, the dup-lane word, the
  answer42 truth table and the record's own replay, the levels table
  re-derived at the baseline primary, corroboration's counts, the A40/A41
  manifests and A36's witness whole, semantic UNKNOWN, the charter
  untouched); retrieval GREEN (exit 0), integrity 18/18, bridge 19/19
  BRIDGE GREEN, all compile; the manifest (6 files, INCLUDING
  `research_eval.py` - the one code motion is the declared pure
  `answer42`, nothing else in the roads moved) re-verified at COMMITTED
  bytes; clean tree; NOTHING pushed.

## The precise next decision (a RULE question, not another probe)
The controlled box stands as a measured capability, but it is
session-bound. Two honest next moves, both above this sprint's pay
grade: (1) PERSIST the box (a service/launcher decision - operator
action, not an agent's silent change), so `SEARCH_BASE` can point at a
durable endpoint; and/or (2) a NEW contract for the PICK: if the
product wants a second voice as a REQUIREMENT, the rule must prefer a
publisher-distinct row by a declared law - and that rule must be frozen
BEFORE its bytes, exactly as this one was. The second voice is not
refuted tonight; it was not SHOWN, because the frozen rule spent its
second lane on a repeat.

## Reproduce (enough specificity to run it again)
1. `git clone --depth 1 https://github.com/searxng/searxng && git -C
   searxng checkout cccbc9e158b0ac3bb2158e9841a647a5bec57b57`
2. `python3 -m venv venv && venv/bin/pip install -r requirements.txt`
3. `settings.yml` (outside the repo): the surface above, plus
   `server.secret_key: <generated locally>`.
4. `SEARXNG_SETTINGS_PATH=<abs>/settings.yml python -m searx.webapp`
5. Probe: `curl 'http://127.0.0.1:8888/search?q=wikipedia&format=json'`.
6. The duel: set the two config words (backup the bytes first), run the
   frozen EA1 search + one `reads` call of the first two eligible urls,
   classify at A40 5/6 and the contract's answer map, restore the bytes.
