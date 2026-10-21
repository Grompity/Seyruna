
# ---------------- A34: the duel decided, the cycle climbed (adds) ----------
# Part 1's tests are the DUEL's own replay (the held two-chain bytes + the
# comparison TABLE at synthetic supports); Part 2's are the CYCLE's law at
# the system's OWN frozen words (EA4's search-empty, A7's no-origin, the
# A15 carried-by class) and the live cycle's replay. T182's name carries
# the ACTUAL live result (the table's own words) so the reader sees the
# duel was RUN, not merely reasoned.
import research_eval

_T182 = {}
_CMP34 = json.loads(open("research-hold/a34-compare.json").read())["compare"]
_A34A = _CMP34["A"]
_A34B = _CMP34["B"]
# the synthetic TABLE (five faces of the supports + the B-win route):
_FA34 = {"proposal": {"proposal": "PROPOSED", "candidate": 20},
         "application_verified": True,
         "decision": {"decision": "ROLLBACK",
                      "rationale": ["the road left its lane (x)",
                                    "the cap cut the road's mouth "
                                    "(finish=length, REPORTED)"]},
         "after": [{"finish": "length", "completion_tokens": 20,
                    "wall_ms": 1500, "max_tokens": 20}]}
_KA34 = {"proposal": {"proposal": "PROPOSED", "candidate": 30},
         "application_verified": True,
         "decision": {"decision": "APPLIES-HOLDS", "rationale": []},
         "after": [{"finish": "stop", "completion_tokens": 28,
                    "wall_ms": 2900, "max_tokens": 30}]}
_RA34 = {"proposal": {"proposal": "NO-PROPOSAL", "why": "not a count"},
         "decision": {"decision": "ROLLBACK", "rationale": ["x"]},
         "after": []}
_T182["table"] = {
    "A-stands": loop.compare(dict(_KA34), dict(_FA34))["decision"],
    "B-wins": loop.compare(dict(_FA34), dict(_KA34))["decision"],
    "both-kept": loop.compare(dict(_KA34), dict(_KA34))["decision"],
    "both-cut": loop.compare(dict(_FA34), dict(_FA34))["decision"],
    "no-proposal": loop.compare(dict(_RA34), dict(_FA34))["decision"]}
# the LIVE chains re-compared at bytes (a replay of the DUEL itself):
_T182["live"] = {
    "verdict": loop.compare(_A34A, _A34B)["decision"],
    "recorded": _CMP34["decision"],
    "A-roads-at-cand": all(r["max_tokens"] == _A34A["proposal"]["candidate"]
                            for r in _A34A["after"]),
    "B-roads-at-cand": all(r["max_tokens"] == _A34B["proposal"]["candidate"]
                            for r in _A34B["after"]),
    "A-cut": all(r["finish"] == "length" and r["completion_tokens"]
                 == _A34A["proposal"]["candidate"] for r in _A34A["after"]),
    "B-cut": all(r["finish"] == "length" and r["completion_tokens"]
                 == _A34B["proposal"]["candidate"] for r in _A34B["after"]),
    "candidates-differ": (_A34A["proposal"]["candidate"]
                          != _A34B["proposal"]["candidate"]),
    "final-safe": (loop.effective_word(loop.read_cfg(), "GENERAL_MAXTOK")
                   == 1024)}

expect("T182 THE DUEL REPLAYS AND THE TABLE COVERS EVERY FACE (synthetic "
       "supports + the held live chains): the table speaks A33-1-HELD when "
       "A completed where B cut, the ONE route to a B-win (A34-B-HELD), "
       "A33-1-SAFER-SUPPORTED at BOTH kept (both complete; the tighter "
       "bound is the safer) AND at both cut (equal correctness, harder "
       "tail-bounds), NEITHER-JUSTIFIED when a leg never proposed; and the "
       "LIVE pair re-compares AT BYTES to the RECORDED verdict (the "
       "sprint's ACTUAL outcome, the table's own words: BOTH CUT - so "
       "A33-1 stands SAFER-SUPPORTED and the safe production 1024 rides "
       "UNTOUCHED - the mission's own retain-the-safe-config outcome); "
       "every after-record of BOTH chains speaks its road-word AT its own "
       "candidate and a REPORTED length AT its candidate EXACTLY (the "
       "halved bound cut TOO - the road has yet to speak an object under "
       "half its own need); and the two candidates DIFFER by the law "
       "(looser at every trusted count) - the formulas were never twins",
       _T182,
       why=lambda tr: ([] if (
           tr["table"]["A-stands"] == "A33-1-HELD"
           and tr["table"]["B-wins"] == "A34-B-HELD"
           and tr["table"]["both-kept"] == "A33-1-SAFER-SUPPORTED"
           and tr["table"]["both-cut"] == "A33-1-SAFER-SUPPORTED"
           and tr["table"]["no-proposal"] == "NEITHER-JUSTIFIED"
           and tr["live"]["verdict"] == tr["live"]["recorded"]
           in ("A33-1-SAFER-SUPPORTED", "A33-1-HELD", "A34-B-HELD")
           and tr["live"]["A-roads-at-cand"] and tr["live"]["B-roads-at-cand"]
           and tr["live"]["A-cut"] and tr["live"]["B-cut"]
           and tr["live"]["candidates-differ"]
           and tr["live"]["final-safe"] is True)
       else ["the table missed a face, the live pair stopped re-comparing, "
             "a road-word strayed from its candidate, or the safe word "
             "moved"]))

_CYC34 = json.loads(open("research-hold/a34-cycle-live.json").read())


def _rec34(**over):
    """a RECORD shaped like run_one's own (the classes ride the SYSTEM's "
    frozen words - EA4's search-empty, A7's read-zero, A15's carried-by)"""
    r = {"web": {"ok": True, "results": 5, "gaps": [],
                 "corroboration": {"read": 3, "origin_publishers": 2,
                                   "attribution": 0}},
          "door": {"evidence_status": "carried by: x.org (read)",
                   "response": "R"}, "question": "Q?"}
    r.update(over)
    return r


_T183 = {}
_T183["gaps"] = {
    "fail": research_eval.gap_word(_rec34(web={"ok": False, "results": 9,
                                              "gaps": ["socket-timeout"],
                                              "corroboration": {
                                                  "read": 2,
                                                  "origin_publishers": 2}})),
    "empty": research_eval.gap_word(_rec34(web={"ok": False, "results": 0,
                                               "gaps": ["search-empty"],
                                               "corroboration": {
                                                   "read": 0,
                                                   "origin_publishers": 0}})),
    "no-origin": research_eval.gap_word(_rec34(
        web={"ok": True, "results": 4, "gaps": [],
             "corroboration": {"read": 0, "origin_publishers": 0,
                               "attribution": 1}})),
    "single": research_eval.gap_word(_rec34(
        web={"ok": True, "results": 3, "gaps": [],
             "corroboration": {"read": 1, "origin_publishers": 1,
                               "attribution": 0}})),
    "sufficient": research_eval.gap_word(_rec34())}
_T183["queries"] = {
    "empty-is-definition": research_eval.follow_query(
        "SEARCH-EMPTY", _rec34()),
    "named-origin-speaks": research_eval.follow_query(
        "SINGLE-ORIGIN", _rec34(web={"ok": True, "results": 1, "gaps": [],
                                     "corroboration": {"read": 1,
                                                       "origin_publishers": 1,
                                                       "attribution": 0},
                                     "rows": [{"publisher": "x.org",
                                               "url": "http://x.org/a"}]})),
    "no-name-uses-host": research_eval.follow_query(
        "NO-ORIGIN", _rec34(web={"ok": True, "results": 1, "gaps": [],
                                 "corroboration": {"read": 0,
                                                   "origin_publishers": 0,
                                                   "attribution": 1},
                                 "rows": [{"publisher": None,
                                           "url": "http://h.org/a"}]})),
    "sufficient-is-breadth": research_eval.follow_query("SUFFICIENT",
                                                       _rec34())}
_C1 = _rec34(web={"ok": True, "results": 3, "gaps": [],
                  "corroboration": {"read": 1, "origin_publishers": 1,
                                    "attribution": 0}})
_C2 = _rec34(web={"ok": True, "results": 5, "gaps": [],
                  "corroboration": {"read": 2, "origin_publishers": 2,
                                    "attribution": 0}})
_T183["improves"] = {
    "read-rises": research_eval.compare_stages(_C1, _C2, "SINGLE-ORIGIN"),
    "no-move": research_eval.compare_stages(
        _rec34(), _rec34(), "SUFFICIENT"),
    "status-moves": research_eval.compare_stages(
        _rec34(door={"evidence_status": "no origin read (rows unweighed)",
                     "response": "R1"}),
        _rec34(door={"evidence_status": "carried by: y.org (read)",
                      "response": "R1"}), "SUFFICIENT")}
_T183["failed-leg"] = research_eval.compare_stages(
    _C1, _rec34(web={"ok": False, "results": 0, "gaps": ["search-empty"],
                     "corroboration": {"read": 0, "origin_publishers": 0},
                     "query": "Q? definition"}), "SINGLE-ORIGIN")

expect("T183 THE CYCLE'S LAW AT THE SYSTEM'S OWN FROZEN WORDS (synthetic "
       "records in the run_one SHAPE - EA4's search-empty, A7's "
       "read-zero, A15's carried-by class - never invented words): the "
       "five gap classes fall EXACTLY as A19/A28's laws read (the lane "
       "WORD decides; emptiness is ITS OWN honest class, not a failure; a "
       "non-empty failure lane rides FIRST; read-ZERO is NO-ORIGIN before "
       "the single-voice count; SUFFICIENT last); the follow-ups take the "
       "RECORD'S OWN words (a named publisher SPEAKS; an UNNAMED row "
       "contributes its HOST, the record's bytes, not a guess; emptiness "
       "asks for a DEFINITION; sufficiency tests BREADTH and says so); the "
       "improvement rubric moves ONLY on its declared legs (read-origins "
       "RISING; an A15 word CROSSING from un-read to carried-by; and "
       "NOTHING moves when nothing moved - SUFFICIENT-vs-SUFFICIENT prints "
       "NO-MATERIAL-IMPROVEMENT as the valid finding it is); and a FAILED "
       "second leg is a FINDING, not a crash (the query's bytes ride, the "
       "read-count DROPS, the A15 word tells, improved is FALSE at the "
       "words - no exception, no rescue, no spin)",
       _T183,
       why=lambda tr: ([] if (
           tr["gaps"] == {"fail": "RETRIEVAL-FAIL", "empty": "SEARCH-EMPTY",
                           "no-origin": "NO-ORIGIN",
                           "single": "SINGLE-ORIGIN",
                           "sufficient": "SUFFICIENT"}
           and tr["queries"]["empty-is-definition"] == "Q? definition"
           and tr["queries"]["named-origin-speaks"] == "x.org Q?"
           and tr["queries"]["no-name-uses-host"] == "h.org Q?"
           and tr["queries"]["sufficient-is-breadth"] == "Q? in summary"
           and tr["improves"]["read-rises"]["improved"] is True
           and any("rose" in w or "voices" in w
                   for w in tr["improves"]["read-rises"]["why"])
           and tr["improves"]["no-move"]["improved"] is False
           and any("VALID finding" in w
                   for w in tr["improves"]["no-move"]["why"])
           and tr["improves"]["status-moves"]["improved"] is True
           and any("READ origin" in w
                   for w in tr["improves"]["status-moves"]["why"])
           and tr["failed-leg"]["improved"] is False
           and tr["failed-leg"]["query_ridden"] == "Q? definition"
           and tr["failed-leg"]["changed"]["read"] == [1, 0])
       else ["a class fell wrong, a follow-up spoke from a coat instead of "
             "the record, or the rubric moved on an undeclared leg"]))

_CMP34 = _CYC34["compare"]
_T184 = {
    "labels-live": (all(_CYC34.get(k, {}).get("label") == "live"
                        for k in ("stage-1", "stage-2"))
                    and _CYC34.get("label") == "live"),
    "gap-honest": _CYC34["gap"] in research_eval.GAPS,
    "born-not-hardcoded": (_CYC34["follow_query"] != _CYC34["question"]
                           and _CMP34["query_ridden"]
                           == _CYC34["follow_query"]),
    "stage1-read": (_CYC34["stage-1"]["web"]["corroboration"]["read"],
                    _CYC34["stage-1"]["web"]["corroboration"]
                    ["origin_publishers"]),
    "improved-word": _CMP34["improved"],
    "charter-untouched": (loop.read_cfg().get("GENERAL_MAXTOK")
                          == stages.CONFIG.get("GENERAL_MAXTOK") == 1024),
    "gate-words": all((s.get("door") or {}).get("evidence_status")
                      is not None for s in
                      (_CYC34["stage-1"], _CYC34["stage-2"]))}

expect("T184 THE LIVE CYCLE, AT ITS BYTES AND AT ITS TRUE WORD (replay, "
       "zero live calls): BOTH stages are label-live INSIDE (they touched "
       "the net - a replay could not say so); the gap word rides the "
       "declared class; the follow-up was BORNT (different bytes than the "
       "question, and the packet's OWN query word says the recorded bytes "
       "were the bytes RIDDEN - the A22 rail read back, never "
       "reconstructed); stage one SPOKE its counts at the A7/A15 words and "
       "the cycle's own lane (the web lane rode); the IMPROVEMENT says its "
       "TRUE WORD at the held bytes - and A34's cycle found NONE: the "
       "gap-born follow-up (the record's OWN publisher at its head) went "
       "search-empty, a VALID finding printed as one, NO spin; the charter "
       "is UNTOUCHED at file and mirror (research is RESEARCH - the cycle "
       "wrote no word); and BOTH stages spoke an A15 evidence_status (the "
       "A18 verbatim law - absent would be ABSENCE, never a stronger "
       "claim). One honest cycle; no autonomy claimed",
       _T184,
       why=lambda tr: ([] if (
           tr["labels-live"] and tr["gap-honest"]
           and tr["born-not-hardcoded"]
           and tr["stage1-read"][0] == 1 and tr["stage1-read"][1] == 1
           and tr["improved-word"] is False
           and tr["charter-untouched"] is True and tr["gate-words"])
       else ["a label lied, the gap spoke a word off the list, the "
             "follow-up was not born of the bytes, the counts moved, the "
             "improvement word rang false, or the charter felt the cycle"]))

