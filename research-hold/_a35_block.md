
# ---------------- A35: the six, disposed (adds) ----------------------------
# T185 is the TABLE alone (synthetic records at run_one's shape, the real
# compare_stages under them - zero net); T186 replays the FINAL six at
# bytes (three re-runs + three originals; every pre-fix byte PRESERVED
# beside); T187 tries the CROSS-LAW at mini-synthetic sixes and demands
# the six's cross-words re-compute EXACTLY.
_T186 = json.loads(open("research-hold/a35-six-final.json").read())


def _art35(gap, one, two, **extra):
    a = {"gap": gap, "stage-1": one, "stage-2": two,
         "compare": research_eval.compare_stages(one, two, gap)}
    a.update(extra)
    return a


_R35 = {}
_R35["blocked"] = research_eval.dispose(_art35(
    "SUFFICIENT",
    _rec34(web={"ok": False, "results": 9, "gaps": ["socket-timeout"],
                "corroboration": {"read": 2, "origin_publishers": 2}}),
    _rec34()))["disposition"]
_S1 = _rec34(web={"ok": True, "results": 3, "gaps": [],
                  "corroboration": {"read": 1, "origin_publishers": 1}})
_EMPTY = _rec34(web={"ok": False, "results": 0, "gaps": ["search-empty"],
                     "corroboration": {"read": 0, "origin_publishers": 0}})
_R35["improved"] = research_eval.dispose(_art35(
    "SINGLE-ORIGIN", _S1,
    _rec34(web={"ok": True, "results": 5, "gaps": [],
                "corroboration": {"read": 3, "origin_publishers": 2}})))
_R35["empty-born"] = research_eval.dispose(_art35(
    "SINGLE-ORIGIN", _S1, _EMPTY))
_R35["no-site"] = research_eval.dispose(_art35(
    "NO-ORIGIN",
    _rec34(web={"ok": True, "results": 4, "gaps": [],
                "corroboration": {"read": 0, "origin_publishers": 0}}),
    _EMPTY))
_R35["site-also-empty"] = research_eval.dispose(_art35(
    "SINGLE-ORIGIN", _S1, _EMPTY, **{"stage-2b": {"web": {}}})).get("answer")
_R35["degraded"] = research_eval.dispose(_art35(
    "SUFFICIENT", _rec34(),
    _rec34(web={"ok": True, "results": 4, "gaps": [],
                "corroboration": {"read": 1, "origin_publishers": 2}}))
)["disposition"]
_R35["unresolved"] = research_eval.dispose(_art35(
    "NO-ORIGIN",
    _rec34(web={"ok": True, "results": 4, "gaps": [],
                "corroboration": {"read": 0, "origin_publishers": 0}}),
    _rec34(web={"ok": True, "results": 2, "gaps": [],
                "corroboration": {"read": 0, "origin_publishers": 0}}))
)["disposition"]
_R35["equival"] = research_eval.dispose(_art35(
    "SUFFICIENT", _rec34(), _rec34()))

expect("T185 THE DISPOSITION TABLE ALONE, AT SYNTHETIC RECORDS (the real "
       "compare_stages UNDER them, zero net): an infra lane-word (a word "
       "that is NOT honest emptiness) BLOCKS; a RISE in read-origins or "
       "voices is the ONLY route to IMPROVED; an EMPTY stage 2 is a "
       "RETRIEVAL-FAILURE whose answer-word SPOKE THREE TRUTHS by the "
       "bytes (FELL to the general road when a read stood at stage 1; the "
       "road FELL EVEN AFTER A SITE RETRY that came back empty (the "
       "demonstrated blocker); NO SITE to ask when the gap was NO-ORIGIN "
       "- A7's house shape, EA2's predicted form; and NOTHING-AT-ALL for "
       "the born-empty-without-a-net); SPOKEN stage-2 bytes that LOST "
       "footing DEGRADE; NO-ORIGIN at BOTH stages (bytes spoke, none "
       "readable) is UNRESOLVED; and SUFFICIENT-vs-SUFFICIENT with no "
       "movement needed is EQUIVALENT - a RESEARCH FINDING STANDING at "
       "two readings; the four FINDING-kinds fall FROM the disposition, "
       "never from a taste",
       _R35,
       why=lambda tr: ([] if (
           tr["blocked"] == "BLOCKED"
           and tr["improved"]["disposition"] == "IMPROVED"
           and tr["improved"]["finding"].startswith("RESEARCH FINDING")
           and "improvement-backed" in tr["improved"]["finding"]
           and tr["empty-born"]["disposition"] == "RETRIEVAL-FAILURE"
           and "fell to the general road" == tr["empty-born"]["answer"]
           and "SITE retry" in tr["site-also-empty"]
           and "EMPTY TOO" in tr["site-also-empty"]
           and tr["no-site"]["disposition"] == "RETRIEVAL-FAILURE"
           and "NO SITE to ask" in tr["no-site"]["answer"]
           and tr["degraded"] == "DEGRADED"
           and tr["unresolved"] == "UNRESOLVED"
           and tr["equival"]["disposition"] == "EQUIVALENT"
           and tr["equival"]["finding"]
           == "RESEARCH FINDING (stood at two readings)")
       else ["a table-leg moved wrong or an answer-word rang false"]))

_IDS35 = ["EA1", "EA2", "EA3", "EA4", "EA5", "EA6"]
_T186C = _T186["cycles"]
_T186D = _T186["disposed"]
_T186X = _T186["cross"]
_T186T = {
    "ids-doc-order": _T186["ids"] == _IDS35,
    "recomputed": all(research_eval.dispose(_T186C[i]) == _T186D[i]
                      for i in _IDS35),
    "labels-live": all(_T186C[i].get("label") == "live" for i in _IDS35),
    "impacted-rode-site": all("stage-2b" in _T186C[i]
                              for i in ("EA1", "EA5", "EA6")),
    "no-site-kept-bytes": (all("stage-2b" not in _T186C[i]
                               for i in ("EA2", "EA3", "EA4"))
                           and "NO SITE to ask"
                           in _T186D["EA2"]["answer"]
                           and "NO SITE to ask"
                           in _T186D["EA3"]["answer"]
                           and "AT ALL" in _T186D["EA4"]["answer"]),
    "grounded": _T186X["grounded-all"] is True and not _T186X["blocked"],
    "no-negative-eaten": _T186X["tally"] == dict(
        (w, sum(1 for i in _IDS35 if _T186D[i]["disposition"] == w))
        for w in {_T186D[i]["disposition"] for i in _IDS35}),
    "charter-untouched": (loop.read_cfg().get("GENERAL_MAXTOK")
                          == stages.CONFIG.get("GENERAL_MAXTOK") == 1024)}

expect("T186 THE FINAL SIX AT BYTES (three re-runs, three untouched "
       "originals - the PRE-FIX bytes PRESERVED beside them at "
       "a35-cycle-*.json): the doc's OWN order rode; every disposition "
       "RE-COMPUTES EXACTLY from the held bytes (the table is DETERMINED, "
       "not remembered); every record is label-live INSIDE (they touched "
       "the net); the THREE impacted cycles show the site-scoped leg "
       "beside the preserved empty bytes (stage-2b - the demonstration "
       "was never over-written); the three UNimpacted kept their bytes "
       "and their WORDS (EA2/EA3: NO SITE to ask - A7's house shape, the "
       "form EA2's A5 expect PREDICTED; EA4: nothing-at-all, the EXPECTED "
       "honest lane); NO run BLOCKED; every follow-up GROUNDED (the A22 "
       "read-back matched at all six); the tally EQUALS the per-cycle "
       "words re-counted (no aggregate eats a negative); and the charter "
       "is UNTOUCHED at file and mirror - six dozen net-rides and twelve "
       "door-legs wrote NO configuration word",
       _T186T,
       why=lambda tr: ([] if all(tr.values()) else
                       ["a held byte stopped re-computing, an order "
                        "strayed, a marker lied, or an aggregate ate a "
                        "negative"]))

_MIN35 = {
    "arts": {i: {"follow_query": "x", "question": "y",
                 "compare": {"query_ridden": "x"}} for i in "ABC"},
    "disps": {"A": {"disposition": "RETRIEVAL-FAILURE", "gap-1": "SUFFICIENT",
                    "gap-2": "SEARCH-EMPTY"},
              "B": {"disposition": "RETRIEVAL-FAILURE", "gap-1": "NO-ORIGIN",
                    "gap-2": "NO-ORIGIN"},
              "C": {"disposition": "EVIDENCE-GAP", "gap-1": "SINGLE-ORIGIN",
                    "gap-2": "SINGLE-ORIGIN"}}}
_MIN35B = {
    "arts": {i: {"follow_query": "x", "question": "y",
                 "compare": {"query_ridden": "x"}} for i in "AB"},
    "disps": {i: {"disposition": "EVIDENCE-GAP", "gap-1": "SINGLE-ORIGIN",
                  "gap-2": "SEARCH-EMPTY"} for i in "AB"}}
_T187 = {
    "singletons": research_eval.cross(_MIN35["arts"], _MIN35["disps"],
                                       ["A", "B", "C"])}
_T187["pair"] = research_eval.cross(_MIN35B["arts"], _MIN35B["disps"],
                                    ["A", "B"])
_T187["six-recomputes"] = (research_eval.cross(_T186C, _T186D, _IDS35)
                           == _T186X)
_T187["headline"] = {
    "no-improvement": "IMPROVED" not in _T186X["tally"],
    "tally": _T186X["tally"],
    "recurring": _T186X["recurring-gap"],
    "emptier": _T186X["emptier-stage"].startswith("stage-2")}

expect("T187 THE CROSS-LAW, LAWFULLY (mini-synthetic sixes first, then "
       "the real one re-COMPUTES EXACTLY): a SINGLETON gap does NOT "
       "recur (NONE-RECURRING printed, the singletons NAMED in the "
       "tallies); a class at TWO of the completed cycles DOES (the "
       "recurrence law is the >=2 the contract declared, and the "
       "empty-born-pair law TRIGS the reserve-fix word the SAME way the "
       "six TRIGGERED it at FIVE of six); and the REAL cross re-computes "
       "from the held bytes WORD FOR WORD - its headline at its true "
       "words: NO IMPROVED rode the six (the strategic word, printed at "
       "bytes: three EVIDENCE-GAP standing where the follow-up arrived "
       "and the single voice STOOD, three RETRIEVAL-FAILURE at the "
       "instrument's edge - none BLOCKED), and the recurring gap-CLASSES "
       "are the provider's house-only shape AND the single-read-origin "
       "shape - two halves of ONE stone (the single dominant site): a "
       "QUERY-CONSTRUCTION and SOURCE-SELECTION finding at the provider's "
       "edge, TENTATIVE as the contract warns, never a generalization "
       "beyond six",
       _T187,
       why=lambda tr: ([] if (
           tr["singletons"]["recurring-gap"] == ["NONE-RECURRING"]
           and tr["singletons"]["emptier-stage"].startswith("no stage")
           and tr["singletons"]["grounded-all"] is True
           and tr["pair"]["recurring-gap"] == ["SINGLE-ORIGIN"]
           and tr["pair"]["reserve-trigger"] == "FIX-TRIGGERED"
           and tr["six-recomputes"] is True
           and tr["headline"]["no-improvement"] is True
           and tr["headline"]["tally"] == {"EVIDENCE-GAP": 3,
                                           "RETRIEVAL-FAILURE": 3}
           and tr["headline"]["recurring"] == ["NO-ORIGIN",
                                               "SINGLE-ORIGIN"]
           and tr["headline"]["emptier"])
       else ["a singleton was called a pattern, the >=2 law moved, or "
             "the real cross stopped re-computing its own words"]))
