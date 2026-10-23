
# ---------------- A41: the resume, replayed (adds) -------------------------
_P41 = json.loads(open("research-hold/a41-duel.json").read())
_A8 = json.loads(open("research-hold/a8-probe-live.json").read())
_S41 = json.loads(open("research-hold/a35-six-final.json").read())["cycles"]
_sig41 = lambda p, man: (lambda want: want is not None and want ==
    hashlib.sha256(open(p, "rb").read()).hexdigest())(
        next((ln.split()[0] for ln in open(man)
              if ln.strip() and not ln.startswith("#")
              and ln.split()[1] == p), None))
def _iso41():
    stages.CONFIG["SEARCH_BASE"] = "https://baresearch.org"
    try:
        with_base = web_research.search_url(
            "searxng", "Ashoka rock edict", 5)
    finally:
        stages.CONFIG.pop("SEARCH_BASE", None)
    after = web_research.search_url("searxng", "Ashoka rock edict", 5)
    return (with_base.startswith("https://baresearch.org/search?q=")
            and after == ("http://searx.org/search?q=Ashoka+rock+edict"
                          "&format=json")
            and "SEARCH_BASE" not in stages.CONFIG
            and "SEARCH_BASE" not in open("config.json").read())
_T411 = {
    "budget-honest": ("no retry" in _P41["budget"]["declared"]
                      and "no fan-out" in _P41["budget"]["declared"]
                      and _P41["budget"]["search-events"] == 1
                      and _P41["budget"]["read-events"] == 0
                      and _P41["search"]["calls-on-ledger"] == 1
                      and _P41["search"]["gap"] == "search-malformed"),
    "class-rederives": (lambda g: ("SEARCH-EMPTY" if g == "search-empty"
                                   else "PROVIDER-UNAVAILABLE" if g
                                   else "NO-GAP"))(
                                       _P41["search"]["gap"])
                        == _P41["class"],
    "parse-death-is-not-empty": (_P41["search"]["gap"]
                                 != "search-empty"
                                 and _P41["class"]
                                 == "PROVIDER-UNAVAILABLE"
                                 and _P41["search"]["rows"] == 0),
    "no-fabricated-evidence": (_P41["levels-per-read"] == []
                               and _P41["corroboration-table"]
                               == {"absent": "no reads rode"}
                               and isinstance(_P41["reads"], str)
                               and _P41["eligible"] == []
                               and _P41["eligible-rule"]
                               .startswith("DERIVED")),
    "isolation-proven-and-restored": (_iso41()
                                      and _P41["isolation-proof"]
                                      ["derived-url"].startswith(
                                          "https://baresearch.org/"
                                          "search?q=")
                                      and _P41["isolation-proof"]
                                      ["restored-registered"] is True),
    "query-frozen": _P41["question-bytes"] == _S41["EA1"]["question"],
    "history-held-at-bytes": (_P41["pick"]["A8-history-word"] == {
        "http": _A8["instances"][0]["http"],
        "content-type": _A8["instances"][0]["content-type"],
        "lane-at-house": _A8["instances"][0]["at-house-lane"],
        "verdict": _A8["instances"][0]["verdict"]}),
    "fork-follows-class": _P41["fork"].startswith(
        "the STOP at the lane-word"),
    "history-whole": (
        _sig41("research-hold/a40-duel.json", "a40-manifest.sha256")
        and _sig41("research-hold/a38-probe.json",
                    "a38-manifest.sha256")
        and json.loads(open("research-hold/a40-duel.json").read())
        ["search"]["gap"] == "search-http-403"
        and json.loads(open("research-hold/a40-duel.json").read())
        ["class"] == "PROVIDER-UNAVAILABLE"
        and json.loads(open("research-hold/a37-probe.json").read())
        ["packets"]["EA1"]["a36-file-sha"]
        == hashlib.sha256(open("research-hold/a36-read-EA1.json",
                               "rb").read()).hexdigest()),
    "charter-untouched": (loop.read_cfg().get("GENERAL_MAXTOK")
                          == stages.CONFIG.get("GENERAL_MAXTOK")
                          == 1024)}
expect("T194 THE RESUME AT ITS BYTES (ALL offline - one EVENT was spent "
       "LIVE, the REPLAY spends NONE): today's word at the documented "
       "lane is the PARSE-DEATH lane-word (search-malformed) and the "
       "frozen law RE-DERIVES PROVIDER-UNAVAILABLE from the gap-word "
       "ALONE - a PARSE-death is NOT an empty search and a 200 with a "
       "FORM for a body is NOT a search (rows ZERO with the gap's voice "
       "ATTACHED, never silence-turned-zero); NOTHING was FABRICATED "
       "into the stop (no levels word, corroboration at its ABSENT word, "
       "the reads NOT-SPENT, the eligibility DERIVED-from-zero and NOT a "
       "failed SELECTION - the A40 ABSENCE discipline RIDES again); the "
       "OVERRIDE is PROVEN IN THE TEST'S OWN PROCESS (the base RIDE the "
       "template, the REMOVAL restores the REGISTERED url BYTE-IDENTICAL, "
       "the word GONE from the CONFIG-DICT, the config FILE STILL "
       "carries NEITHER word - isolation PROVEN, restoration PROVEN, the "
       "file UN-TAKEN); the frozen QUESTION rides BYTE-EXACT to the "
       "RECORD; the A8 HISTORY rides HELD at the ARTIFACT's OWN bytes "
       "(the two blockers, yesterdays' 403 and today's PARSE-death, ride "
       "SEPARATE and NEITHER clobbers the OTHER; A40's record re-signs at "
       "its OWN manifest); the FORK FOLLOWS the class (the STOP - no "
       "second instance, no fan-out, no rotating pool); and the charter "
       "rides UNTOUCHED at file AND mirror",
       _T411,
       why=lambda tr: ([] if all(tr.values()) else
                       [str(sorted(k for k, v in tr.items()
                                    if not v))]))
