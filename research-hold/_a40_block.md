
# ---------------- A40: the duel's blocker, replayed (adds) -----------------
_P40 = json.loads(open("research-hold/a40-duel.json").read())
_S40 = json.loads(open("research-hold/a35-six-final.json").read())["cycles"]
_sig40 = lambda p, man: (lambda want: want is not None and want ==
    hashlib.sha256(open(p, "rb").read()).hexdigest())(
        next((ln.split()[0] for ln in open(man)
              if ln.strip() and not ln.startswith("#")
              and ln.split()[1] == p), None))
_T401 = {
    "budget-honest": (_P40["budget"]["search-events"] == 1
                       and _P40["budget"]["read-events"] == 0
                       and "no retry" in _P40["budget"]["declared"]
                       and _P40["search"]["calls-on-ledger"] == 1
                       and _P40["search"]["gap"] == "search-http-403"),
    "unavailable-not-empty": (_P40["class"] == "PROVIDER-UNAVAILABLE"
                              and _P40["class"] != "SEARCH-EMPTY"),
    "no-fabricated-evidence": (_P40["class"] != "USABLE-RESULTS"
                               and _P40["levels-per-read"] == []
                               and _P40["corroboration-table"]
                               == {"absent": "no reads rode"}),
    "class-rederives": (lambda g: ("SEARCH-EMPTY" if g == "search-empty"
                                   else "PROVIDER-UNAVAILABLE" if g
                                   else "NO-GAP"))(
                                       _P40["search"]["gap"])
                        == _P40["class"],
    "absences-consistent": (_P40["search"]["rows"] == 0
                            and _P40["search"]["rows-words"] == []
                            and _P40["eligible"] == []
                            and _P40["reads"]
                            == "NOT-SPENT (class stopped the line first)"),
    "provenance-rides-as-words": (len(_P40["search"]
                                      ["absent-fields-recorded"]) >= 2
                                  and _P40["blocker"]["no-substitution"]
                                  is True
                                  and _P40["blocker"]["no-silent-retry"]
                                  is True),
    "eligibility-un-evaluated": (_P40["eligible-rule"]
                                 .startswith("UN-EVALUATED")),
    "question-frozen": (_P40["question-bytes"]
                        == _S40["EA1"]["question"]),
    "fork-follows-class": _P40["fork"].startswith("LIVE LINE STOPS"),
    "history-whole": (
        _sig40("research-hold/a35-cycle-EA1.rerun.json",
               "a35-manifest.sha256")
        and _sig40("research-hold/a38-probe.json",
                    "a38-manifest.sha256")
        and json.loads(open("research-hold/a37-probe.json").read())
        ["packets"]["EA1"]["a36-file-sha"]
        == hashlib.sha256(open("research-hold/a36-read-EA1.json",
                               "rb").read()).hexdigest()),
    "charter-untouched": (loop.read_cfg().get("GENERAL_MAXTOK")
                          == stages.CONFIG.get("GENERAL_MAXTOK")
                          == 1024)}
expect("T193 THE DUEL'S BLOCKER AT ITS BYTES (ALL offline - the replay "
       "touches NO net and the WHOLE live line rode at the ONE declared "
       "event): a 403 is UNAVAILABLE and NOT mislabelled EMPTY (the two "
       "classes STAND APART at the gap-word ALONE - the road's own law, "
       "REPLAYED here at the stored word); NOTHING was FABRICATED to fill "
       "the stop (no levels word, corroboration rides its ABSENT word, "
       "the reads print NOT-SPENT - an UNRUN road speaks NO evidence); "
       "the ABSENCES ride CONSISTENT (zero rows speak with the gap's own "
       "voice, the rows-words list is EMPTY, the eligible list EMPTY and "
       "printed UN-EVALUATED - an UNRUN selection is NOT a FAILED one); "
       "the MISSING PROVENANCE rides AS WORDS (the success face's silent "
       "status, headers, the derived publishers - never zeros) and the "
       "BLOCKER prints its no-substitution and no-silent-retry laws; the "
       "FORK FOLLOWS the class at the FROZEN mapping (the LIVE line "
       "STOPS, the CLOSED ddg-ia branch owes the duel NOTHING); the "
       "frozen QUESTION rides BYTE-EXACT to the record's own bytes (no "
       "outcome could bend it); the HISTORY stands WHOLE (A35/A38's "
       "records re-sign at their OWN manifests, A36's witness at A37's "
       "stored word); and the charter rides UNTOUCHED at file AND mirror "
       "- the env-home word that pointed the duel is GONE with its "
       "process, and config.json was NEVER touched",
       _T401,
       why=lambda tr: ([] if all(tr.values()) else
                       [str(sorted(k for k, v in tr.items()
                                    if not v))]))
