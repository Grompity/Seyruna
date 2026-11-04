# ---------------- A42: the controlled endpoint, replayed (adds) -----------
_P42 = json.loads(open("research-hold/a42-duel.json").read())
_S42 = json.loads(open("research-hold/a35-six-final.json").read())["cycles"]
_sig42 = lambda p, man: (lambda want: want is not None and want ==
    hashlib.sha256(open(p, "rb").read()).hexdigest())(
        next((ln.split()[0] for ln in open(man)
              if ln.strip() and not ln.startswith("#")
              and ln.split()[1] == p), None))
def _replay42():
    """the duel's pure replays at the RECORDED words: the levels table at
    the BASELINE's held primary, corroboration's own counts, and the
    derived route - the instance's house FORCED in-process and REMOVED in
    a finally (A41's isolation idiom; the file is never touched)."""
    stages.CONFIG["SEARCH_BASE"] = "http://127.0.0.1:8888"
    try:
        primary = json.loads(open("research-hold/a36-read-EA1.json")
                             .read())["selection"]["primary"]
        lv = [dict({"url": r.get("url")},
                   **research_eval.levels36(primary, {"results": [r]}))
              for r in _P42["reads"]["results"]]
        cor = web_research.corroboration(_P42["reads"])
        url = web_research.search_url("searxng", "Ashoka rock edict", 5)
    finally:
        stages.CONFIG.pop("SEARCH_BASE", None)
    return {"levels": lv, "corroboration": cor, "url": url,
            "clean": ("SEARCH_BASE" not in stages.CONFIG
                      and "SEARCH_BASE" not in open("config.json").read())}
_R42 = _replay42()
_T421 = {
    "mapper-truth-table": (
        research_eval.answer42("search-http-403", [], [],
                               "h")["answer"] == "RETRIEVAL-FAILURE"
        and research_eval.answer42(None, [], [], "h")["answer"]
        == "EVIDENCE-GAP"
        and research_eval.answer42(None, [{"url": "https://a.example/x"}],
                                   [], "h")["answer"] == "EVIDENCE-GAP"
        and research_eval.answer42(None, [{"url": "https://a.example/x"}],
            [{"url": "https://a.example/x", "publisher": "example.com",
              "status": 200, "text": "Ashoka " * 20},
             {"url": "https://b.example/y", "publisher": "example.com",
              "status": 200, "text": "Ashoka " * 20}], "h")["answer"]
        == "EVIDENCE-BACKED"
        and research_eval.answer42(None, [{"url": "https://a.example/x"}],
            [{"url": "https://a.example/x", "publisher": "example.com",
              "status": 200, "text": "Ashoka " * 20},
             {"url": "https://b.example/y", "publisher": "example.com",
              "status": 200, "text": "thin"}], "h")["answer"]
        == "PARTIAL"),
    "mapper-gates": (
        research_eval.answer42(None, [{"url": "https://a.example/x"}],
            [{"url": "https://a.example/x", "publisher": "h",
              "status": 200, "text": "Ashoka " * 20}], "h")["answer"]
        == "EVIDENCE-GAP"
        and research_eval.answer42(None, [{"url": "https://a.example/x"}],
            [{"url": "https://a.example/x", "publisher": "example.com",
              "status": 200, "text": "no word here " * 20}], "h")["answer"]
        == "EVIDENCE-GAP"
        and research_eval.answer42(None, [{"url": "https://a.example/x"}],
            [{"url": "https://a.example/x", "publisher": "example.com",
              "error": "timed out"}], "h")["answer"] == "EVIDENCE-GAP"),
    "label-live": _P42["label"] == "live",
    "question-frozen": _P42["question-bytes"] == _S42["EA1"]["question"],
    "loopback-only": (
        _P42["deployment"]["surface"]["bind_address"] == "127.0.0.1"
        and _P42["deployment"]["surface"]["port"] == 8888
        and any("127.0.0.1:8888" in ln and "LISTEN" in ln
                for ln in _P42["deployment"]["listener"])
        and not any("0.0.0.0" in ln
                    for ln in _P42["deployment"]["listener"])),
    "no-public-posture": (
        _P42["deployment"]["surface"]["public_instance"] is False
        and _P42["deployment"]["surface"]["limiter"] is False
        and _P42["deployment"]["surface"]["image_proxy"] is False
        and "LOOPBACK ONLY" in _P42["deployment"]["exposure"]),
    "settings-outside-repo": (
        _P42["deployment"]["settings"]["outside-repo"] is True
        and not _P42["deployment"]["settings"]["path"].startswith(
            stages.BASE_DIR)),
    "commit-pinned": (
        len(_P42["deployment"]["clone"]["commit"]) == 40
        and all(c in "0123456789abcdef"
                for c in _P42["deployment"]["clone"]["commit"])),
    "no-secret-key": ("secret_key" not in json.dumps(_P42)
                      and _P42["deployment"]["settings"]["secret"]
                      .startswith("generated locally")),
    "protocol-200": (
        _P42["protocol-check"]["status"] == 200
        and _P42["protocol-check"]["content-type"] == "application/json"
        and _P42["protocol-check"]["json-valid"] is True
        and _P42["protocol-check"]["bytes"] > 0),
    "protocol-rows": (_P42["protocol-check"]["results"] == 33
                      and _P42["protocol-check"]["results"] > 0
                      and _P42["protocol-check"]["first-row"]
                      == "https://www.wikipedia.org/"),
    "protocol-harmless": (
        _P42["protocol-check"]["query"].startswith("wikipedia")
        and _P42["question-bytes"] != "wikipedia"
        and _P42["protocol-check"]["request"]
        == "GET http://127.0.0.1:8888/search?q=wikipedia&format=json"),
    "protocol-deployment-face": _P42["protocol-check"]["face"]
                                .startswith("DEPLOYMENT"),
    "window-words": (
        set(_P42["config-window"]["words-set"])
        == {"SEARCH_PROVIDER", "SEARCH_BASE"}
        and _P42["config-window"]["words-set"]["SEARCH_PROVIDER"]
        == "searxng"
        and _P42["config-window"]["words-set"]["SEARCH_BASE"]
        == "http://127.0.0.1:8888"),
    "window-from-config": (
        _P42["config-window"]["provider-resolved"] == "searxng"
        and _P42["config-window"]["env-ASCENDED_SEARCH-before"] == "absent"
        and all(v is None for v in
                _P42["config-window"]["mirror-before"].values())),
    "derived-url-exact": (
        _P42["config-window"]["derived-search-url"]
        == "http://127.0.0.1:8888/search?q=Ashoka+rock+edict&format=json"
        and _R42["url"] == _P42["config-window"]["derived-search-url"]),
    "restoration-bytes-exact": (
        _P42["restoration"]["equals-pre-sha"] is True
        and _P42["restoration"]["pre-sha256"]
        == hashlib.sha256(open("config.json", "rb").read()).hexdigest()),
    "restoration-mirror-clean": (
        _P42["restoration"]["mirror-SEARCH_BASE"] is None
        and _P42["restoration"]["mirror-SEARCH_PROVIDER"] is None
        and _P42["restoration"]["provider-after"] == "ddg-ia"
        and _P42["restoration"]["env-ASCENDED_SEARCH-after"] is None),
    "config-carries-neither": (
        "SEARCH_BASE" not in open("config.json").read()
        and "SEARCH_PROVIDER" not in open("config.json").read()),
    "search-spoke": (_P42["search"]["gap"] is None
                     and _P42["search"]["rows"] == 5
                     and _P42["search"]["calls-on-ledger"] == 1
                     and _P42["search"]["ms"] > 0),
    "rows-words-consistent": (
        len(_P42["search"]["rows-words"]) == _P42["search"]["rows"]
        and all(web_research.publisher(w["url"]) == w["publisher"]
                and w["lane"] == "result"
                for w in _P42["search"]["rows-words"])),
    "eligible-outside-house": (
        len(_P42["eligible"]) == _P42["search"]["rows"]
        and all(e["publisher"] != "127.0.0.1"
                for e in _P42["eligible"])),
    "pick-first-two": (
        len(_P42["pick"]["urls"]) == 2
        and _P42["pick"]["urls"]
        == [e["url"] for e in _P42["eligible"][:2]]),
    "reads-one-call": (
        _P42["reads"]["spent"]["calls"] == 1
        and _P42["reads"]["spent"]["fetch"] == 1
        and _P42["reads"]["spent"]["search"] == 0
        and [r["url"] for r in _P42["reads"]["results"]]
        == _P42["pick"]["urls"]),
    "dup-lane-word": (
        _P42["reads"]["results"][1].get("skipped") == "dup-publisher"
        and _P42["reads"]["results"][0].get("status") == 200
        and len(_P42["reads"]["results"][0].get("text") or "") >= 60),
    "budget-honest": (
        _P42["budget"]["search-events"] == 1
        and _P42["budget"]["read-events"] == 1
        and _P42["budget"]["fetches"] == 1
        and "no retry" in _P42["budget"]["declared"]),
    "answer-replays": (
        research_eval.answer42(None, _P42["eligible"],
                               _P42["reads"]["results"], "127.0.0.1")
        == _P42["answer"]
        and _P42["answer"]["answer"] == "PARTIAL"),
    "levels-replay": (_R42["levels"] == _P42["levels-per-read"]
                      and all(l["verdict"] == "MONOCULTURE-PERSISTS"
                              for l in _P42["levels-per-read"])),
    "levels-at-the-baseline-primary": (
        _P42["levels-primary"]["url"] == _P42["eligible"][0]["url"]
        and "REPEATING publisher"
        in _P42["levels-per-read"][0]["why"]),
    "corroboration-replay": (
        _R42["corroboration"] == _P42["corroboration-table"]
        and _P42["corroboration-table"]["independence"] == "none"
        and _P42["corroboration-table"]["origin_publishers"] == 1
        and _P42["corroboration-table"]["read"] == 1),
    "replay-isolation": _R42["clean"],
    "history-whole": (
        _sig42("research-hold/a40-duel.json", "a40-manifest.sha256")
        and _sig42("research-hold/a41-duel.json", "a41-manifest.sha256")
        and json.loads(open("research-hold/a37-probe.json").read())
        ["packets"]["EA1"]["a36-file-sha"]
        == hashlib.sha256(open("research-hold/a36-read-EA1.json",
                               "rb").read()).hexdigest()),
    "semantic-unknown": _P42["semantic-improvement"].startswith("UNKNOWN"),
    "limits-printed": (len(_P42["limits"]) >= 5
                       and any("n=1" in l for l in _P42["limits"])),
    "charter-untouched": (loop.read_cfg().get("GENERAL_MAXTOK")
                          == stages.CONFIG.get("GENERAL_MAXTOK")
                          == 1024)}
expect("T195 THE CONTROLLED ENDPOINT AT ITS BYTES (ALL offline - the ONE "
       "research search and the ONE reads call were spent LIVE and held; "
       "the REPLAY spends NONE): the instance is LOOPBACK ONLY (the "
       "127.0.0.1 bind, the listener line, no public posture, the "
       "settings OUTSIDE the repo, the commit PINNED, no secret word in "
       "the record); the protocol check's words ride as DEPLOYMENT "
       "evidence (200, application/json, 33 rows, the HARMLESS query - "
       "not research evidence, not the frozen bytes); the CONFIG was the "
       "integration point and the ENV was ABSENT (the window's TWO "
       "words, the mirror's before-nulls, the derived url at the bytes; "
       "the reader PROVEN, never assumed) and the WINDOW stands RESTORED "
       "BYTE-EXACT (pre-sha == today's file, the mirror clean, provider "
       "back to ddg-ia, the file carrying NEITHER word); the search "
       "SPOKE (five rows, gap None, one ledger call) and the pick rode "
       "the FROZEN law (the first two eligible, content-blind) - and the "
       "road's OWN dup-publisher law spent ONE of the two lanes (a "
       "REPEAT is not a second voice); the LEVELS re-derive at the "
       "baseline's held PRIMARY (MONOCULTURE-PERSISTS - the voice "
       "repeats, the first pick IS the baseline's own address), "
       "corroboration's counts say NONE (one read, one publisher, no "
       "independence word), and the ANSWER word REPLAYS at the declared "
       "map (PARTIAL - one usable, one lane unspent); semantic "
       "improvement rides UNKNOWN BY LAW (no answer-leg, declared before "
       "the bytes); the HISTORY stands WHOLE (A40/A41 re-sign at their "
       "OWN manifests, A36's witness at A37's stored word); and the "
       "charter rides UNTOUCHED at file AND mirror",
       _T421,
       why=lambda tr: ([] if all(tr.values()) else
                       [str(sorted(k for k, v in tr.items()
                                    if not v))]))
