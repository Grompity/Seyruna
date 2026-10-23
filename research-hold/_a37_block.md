
# ---------------- A37: the six-packet measurement (adds) -------------------
_P37 = json.loads(open("research-hold/a37-probe.json").read())
_F37 = {i: _P37["packets"][i]["classification"] for i in _P37["packets"]}
_T190 = {
    "forms-recompute": all(research_eval.classify37(
        json.loads(open("research-hold/a35-six-final.json").read())
        ["cycles"][i])["form"] == _F37[i]["form"]
        for i in ("EA2", "EA3", "EA4", "EA5", "EA6")),
    "causes-distinct": (_F37["EA4"]["form"] == "NO-ROWS-AT-ALL"
                        and _F37["EA2"]["form"]
                        == _F37["EA3"]["form"]
                        == "NO-READ-ROW-ROWS-PRESENT"
                        and _F37["EA4"]["rows"] == 0
                        and _F37["EA2"]["rows"] == 3),
    "the-frozen-word-HOLDS": all(
        _F37[i]["why"].startswith("NO-PRIMARY-READ")
        for i in ("EA2", "EA3", "EA4")),
    "twins": all(_F37[i]["form"] == "NO-ELIGIBLE-PROBE-ROW"
                 and _F37[i]["eligible"] is False
                 for i in ("EA5", "EA6")),
    "stub-forms-UNUNIFORM": ("/c/" in _F37["EA5"]["probe-row-url"]
                             and "/c/" not in
                             _F37["EA6"]["probe-row-url"]),
    "network-at-the-words": (_P37["reads-used"] == 0
                             and _P37["searches-used"] == 0
                             and _P37["budget"]["reads-at-most"] == 5
                             and _P37["claim-check"] is True),
    "ea1-rides-as-is": (_P37["packets"]["EA1"]["a36-read-AS-IS"]["verdict"]
                        == "MONOCULTURE-PERSISTS"
                        and hashlib.sha256(
                            open("research-hold/a36-read-EA1.json",
                                 "rb").read()).hexdigest()
                        == _P37["packets"]["EA1"]["a36-file-sha"]),
    "charter-untouched": (loop.read_cfg().get("GENERAL_MAXTOK")
                         == stages.CONFIG.get("GENERAL_MAXTOK") == 1024)}

expect("T190 THE SIX-PACKET MEASUREMENT AT ITS BYTES (a replay, zero live - "
       "and the ACTUAL run spent ZERO of its five-read budget, so the "
       "replay and the record need NO restating): every form RE-COMPUTES "
       "from the frozen selector (the law UNMOVED); the two no-primary "
       "causes STAND APART at the records' own rows (EA4's ZERO rows "
       "against EA2/EA3's three - the A36 word HOLDS over both, A37's "
       "forms DISTINGUISH, the code moved NOTHING), the twins (EA5/EA6) "
       "print NO-ELIGIBLE-PROBE-ROW - EA1's shape at FIVE of six packets, "
       "the monoculture's THIRD independent witness - and the stubs are "
       "not even UNIFORM in FORM (EA5 rides A36's /c/ form, EA6 a BARE "
       "path: A36's measured word stays ANCHORED to its one address and "
       "is NOT to be smeared across six - the PROVIDER-LIMITED law at "
       "work at the record's own bytes); the network words EQUAL the "
       "truth (reads 0 of 5, searches 0 - the budget the sprint DECLINED "
       "to spend is PRINTED as declined, not hidden); EA1's A36 read "
       "rides AS-IS (its verdict at the held word, its file digest "
       "recomputed - the companion was never re-felt); and the charter is "
       "UNTOUCHED at file AND mirror - a whole measurement wrote NO "
       "network and NO configuration word",
       _T190,
       why=lambda tr: ([] if all(tr.values()) else
                       ["a form stopped re-computing, a cause blurred, "
                        "the twins misrode, the network words lied, or "
                        "the companion got re-felt"]))
