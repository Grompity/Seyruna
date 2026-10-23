
# ---------------- A38: three stubs at the named road (adds) ----------------
_P38 = json.loads(open("research-hold/a38-probe.json").read())
_S38 = json.loads(open("research-hold/a35-six-final.json").read())["cycles"]
_row38 = lambda pid: next(
    x for x in _S38[pid]["stage-1"]["web"]["rows"]
    if x.get("id") == _P38["targets"][pid]["target"]["row-id"])
_lv38 = lambda pid: research_eval.levels36(
    research_eval.candidate36(_S38[pid]).get("primary")
    or {"publisher": None},
    {"results": [{"text": "", "status":
                   _P38["targets"][pid]["read"]["status"]}]})
_T191 = {
    "budget-honest": (_P38["budget-declared"]
                       == {"attempts": 3, "searches": 0}
                       and _P38["attempts"] == 3
                       and _P38["reads-used"] == 3
                       and _P38["searches-used"] == 0),
    "digests-recompute": all(
        _P38["targets"][i]["target"]["packet-digest-sha256"]
        == hashlib.sha256(json.dumps(_S38[i]["stage-1"],
                                     sort_keys=True).encode()).hexdigest()
        for i in ("EA5", "EA6", "EA2")),
    "rows-are-rows": all(_row38(i)["url"]
                         == _P38["targets"][i]["target"]["url"]
                         for i in ("EA5", "EA6", "EA2")),
    "law-row-pinned": (_P38["targets"]["EA2"]["target"]["row-id"]
                       == _S38["EA2"]["stage-1"]["web"]["rows"][0]["id"]),
    "every-echo-shaped": all(
        _P38["targets"][i]["read"]["status"] == 202
        and _P38["targets"][i]["read"]["error"] is None
        and _P38["targets"][i]["read"]["bytes"] == 0
        and _P38["targets"][i]["read"]["redirect"] is True
        and "?q=" in _P38["targets"][i]["read"]["final"]
        and _P38["targets"][i]["read"]["final-host"]
            == _P38["targets"][i]["target"]["row-publisher"]
            == web_research.provider_host()
        for i in ("EA5", "EA6", "EA2")),
    "usability-words-replay": all(
        _P38["targets"][i]["usability"].startswith("EMPTY")
        for i in ("EA5", "EA6", "EA2")),
    "levels-replay": all(_lv38(i)["verdict"]
                         == _P38["targets"][i]["verdict"]
                         and _lv38(i)["why"]
                         == _P38["targets"][i]["levels"]["why"]
                         for i in ("EA5", "EA6", "EA2")),
    "lineage-words-held": all(
        _P38["targets"][i]["target"]["row-stage-1-words"]
        == {"kind": "snippet", "note": "http 202", "evidence": None}
        for i in ("EA5", "EA6", "EA2")),
    "shapes-at-bytes": ("/c/" in _P38["targets"]["EA5"]["target"]["url"]
                        and "/c/" not in
                        _P38["targets"]["EA6"]["target"]["url"]
                        and "/c/" not in
                        _P38["targets"]["EA2"]["target"]["url"]),
    "prior-evidence-whole": (
        hashlib.sha256(open("research-hold/a36-read-EA1.json",
                            "rb").read()).hexdigest()
        == json.loads(open("research-hold/a37-probe.json").read())
        ["packets"]["EA1"]["a36-file-sha"]
        and json.loads(open("research-hold/a37-probe.json").read())
        ["claim-check"] is True),
    "charter-untouched": (loop.read_cfg().get("GENERAL_MAXTOK")
                          == stages.CONFIG.get("GENERAL_MAXTOK")
                          == 1024)}
expect("T191 THE THREE STUBS AT THE NAMED ROAD (live reads, replayed at "
       "the held bytes, the net UNTOUCHED by this test): the budget was "
       "DECLARED 3 attempts and ZERO searches and the ACTIVITY EQUALS "
       "the words (reads-used 3, searches-used 0); every packet digest "
       "RE-COMPUTES from the immutable record and every target row "
       "STANDS as an existing row of its packet at its exact url (the "
       "EA2 pick rides the PREDECLARED law - first row at packet order, "
       "pinned W1); all three addresses speak the SAME SHAPE (202, a "
       "REDIRECT to the provider's own ?q= echo, ZERO bytes, the HOUSE "
       "word at BOTH ends - the self-echo at three fresh addresses, "
       "A36's word now STANDING at FOUR, the A36 fix's final-word "
       "PROVEN at every one); the usability words and the FROZEN "
       "levels-table RE-COMPUTE exactly from the held bytes (a replay, "
       "the table UNMOVED); the stage-1 lineage word (touched, no bytes) "
       "rides HELD and UNSMOOTHED; the address-forms name themselves at "
       "the BYTES (the /c/ once, the bare path twice); the PRIOR "
       "evidence is WHOLE (A36's witness re-signs, A37's claim-check "
       "rides TRUE); and the charter is UNTOUCHED at file AND mirror",
       _T191,
       why=lambda tr: ([] if all(tr.values()) else
                       [str(sorted(k for k, v in tr.items()
                                    if not v))]))
