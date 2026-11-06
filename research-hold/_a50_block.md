# ---------------- A50: the independence model (adds) ----------------
import independence as _ind50
def _c50(cid, chains, terms, rels=None, claims=None):
    return {"id": cid, "chains": chains, "terminals": terms,
            "relations": rels or [], "claims": claims or []}
def _t50(label, kind="work", status="COMPLETE", **kw):
    d = {"label": label, "kind": kind, "status": status}
    d.update(kw)
    return d
def _r50(rid, typ, a, b):
    return {"id": rid, "type": typ, "a": a, "b": b, "evidence": rid}
def _st50(r):
    return dict((k, v["status"]) for k, v in r["dimensions"].items())
def _keys50(x):
    if isinstance(x, dict):
        for k, v in x.items():
            yield k
            for y in _keys50(v):
                yield y
    elif isinstance(x, list):
        for v in x:
            for y in _keys50(v):
                yield y
def _raises50(fn):
    try:
        fn()
        return False
    except ValueError:
        return True

_C50 = {
 "c1": _c50("c1", {"A": {"terminals": ["a1"]}, "B": {"terminals": ["b1"]}},
            {"a1": _t50("Author A 2020"), "b1": _t50("Author B 2021")},
            [_r50("r1", "shares-edition", "a1", "b1")]),
 "c2": _c50("c2", {"A": {"terminals": ["a1"]}, "B": {"terminals": ["b1"]}},
            {"a1": _t50("Pub A", publisher="P1"),
             "b1": _t50("Pub B", publisher="P2")},
            [_r50("r1", "shared-editorial-control", "a1", "b1")]),
 "c3": _c50("c3", {"A": {"terminals": ["a1"]}, "B": {"terminals": ["b1"]}},
            {"a1": _t50("Inst A", institution="I1"),
             "b1": _t50("Inst B", institution="I2")},
            [_r50("r1", "shared-funder", "a1", "b1")]),
 "c4": _c50("c4", {"A": {"terminals": ["a1"]}, "B": {"terminals": ["b1"]}},
            {"a1": _t50("Report A"), "b1": _t50("Report B")},
            [_r50("r1", "same-observation", "a1", "b1")],
            [{"id": "k1", "text": "claim", "supports": ["A", "B"],
              "agreement": "AGREE"}]),
 "c5": _c50("c5", {"A": {"terminals": ["t1"]}, "B": {"terminals": ["t2"]}},
            {"t1": _t50("Translation 1", kind="translation"),
             "t2": _t50("Translation 2", kind="translation"),
             "e1": _t50("Earlier translation", kind="translation")},
            [_r50("r1", "translation-ancestor", "t1", "e1"),
             _r50("r2", "translation-ancestor", "t2", "e1")],
            [{"id": "k1", "text": "claim", "supports": ["A", "B"],
              "agreement": "AGREE"}]),
 "c6": _c50("c6", {"A": {"terminals": ["a1"]}, "B": {"terminals": ["b1"]}},
            {"a1": _t50("Scholar A"), "b1": _t50("Scholar B")},
            [_r50("r1", "same-primary-document", "a1", "b1"),
             _r50("r2", "independent-editorial", "a1", "b1")]),
}
_C50.update({
 "c7": _c50("c7", {"A": {"terminals": ["a1"]}, "B": {"terminals": ["b1"]}},
            {"a1": _t50("A"), "b1": _t50("B")}),
 "c8": _c50("c8", {"A": {"terminals": ["a1"]}, "B": {"terminals": ["b1"]}},
            {"a1": _t50("A"), "b1": _t50("B")},
            [_r50("r1", "shares-edition", "a1", "b1"),
             _r50("r2", "independent-underlying", "a1", "b1")]),
 "c9": _c50("c9", {"A": {"terminals": ["a1", "a2"]}, "B": {"terminals": ["b1"]}},
            {"a1": _t50("A1"), "a2": _t50("A2 partial", status="PARTIAL"),
             "b1": _t50("B1")},
            [], [{"id": "k1", "text": "claim", "supports": ["A", "B"],
                  "agreement": "AGREE"}]),
 "c10": _c50("c10", {"A": {"terminals": ["a1"]}, "B": {"terminals": ["b1"]}},
             {"a1": _t50("Wording one"), "b1": _t50("Wording two")},
             [_r50("r1", "derives-from", "a1", "b1")],
             [{"id": "k1", "text": "claim", "supports": ["A", "B"],
               "agreement": "AGREE"}]),
 "c11": _c50("c11", {"A": {"terminals": ["a1"]}, "B": {"terminals": ["b1"]},
                     "D": {"terminals": ["d1"]}},
             {"a1": _t50("A"), "b1": _t50("B"), "d1": _t50("D")},
             [_r50("r1", "shares-edition", "a1", "b1")],
             [{"id": "k1", "text": "claim", "supports": ["A", "B", "D"],
               "agreement": "AGREE"}]),
 "c12": _c50("c12", {"A": {"terminals": ["o1"]}, "B": {"terminals": ["o2"]}},
             {"o1": _t50("Observation 1", kind="observation"),
              "o2": _t50("Observation 2", kind="observation")},
             [_r50("r1", "independent-underlying", "o1", "o2"),
              _r50("r2", "independent-observation", "o1", "o2"),
              _r50("r3", "independent-editorial", "o1", "o2"),
              _r50("r4", "independent-institutional", "o1", "o2")],
             [{"id": "k1", "text": "claim", "supports": ["A", "B"],
               "agreement": "AGREE"}]),
 "cid": _c50("cid", {"A": {"terminals": ["same"]},
                     "B": {"terminals": ["same"]}},
             {"same": _t50("One work")}),
 "cunk": _c50("cunk", {"A": {"terminals": ["a1"]}, "B": {"terminals": ["b1"]}},
              {"a1": _t50("A"), "b1": _t50("B")},
              [_r50("r1", "unknown-derivation", "a1", "b1")]),
})
# the wording twins: identical structure, different prose
_C50["c10b"] = _c50("c10b", {"A": {"terminals": ["a1"]},
                             "B": {"terminals": ["b1"]}},
                    {"a1": _t50("Completely different sentence"),
                     "b1": _t50("Another phrasing entirely")},
                    [_r50("r1", "derives-from", "a1", "b1")],
                    [{"id": "k1", "text": "differently worded claim",
                      "supports": ["A", "B"], "agreement": "AGREE"}])
_R50 = dict((k, _ind50.assess(v)) for k, v in _C50.items())
_T203 = {
    "dimensions-separate": (
        _ind50.DIMENSIONS == ("attribution", "underlying", "editorial",
                              "institutional", "observational",
                              "corroboration")
        and _ind50.STATUSES == ("SUPPORTED", "CONTRADICTED", "UNKNOWN")
        and all(d in _R50["c1"]["dimensions"] for d in _ind50.DIMENSIONS)
        and all(_st50(_R50["c1"])[d] in _ind50.STATUSES
                for d in _ind50.DIMENSIONS)),
    "different-authors-same-source": (
        _st50(_R50["c1"])["attribution"] == "SUPPORTED"
        and _st50(_R50["c1"])["underlying"] == "CONTRADICTED"
        and _st50(_R50["c1"])["editorial"] == "UNKNOWN"
        and _st50(_R50["c1"])["institutional"] == "UNKNOWN"
        and _st50(_R50["c1"])["observational"] == "UNKNOWN"
        and _R50["c1"]["independent-evidence"] is False
        and _R50["c1"]["dependencies"][0]["type"] == "shares-edition"),
    "publisher-is-not-editorial": (
        _st50(_R50["c2"])["attribution"] == "SUPPORTED"
        and _st50(_R50["c2"])["editorial"] == "CONTRADICTED"
        and _st50(_R50["c2"])["underlying"] == "UNKNOWN"
        and _R50["c2"]["dimensions"]["editorial"]["evidence"]["contradicts"]
        == ["r1"]),
    "institution-is-not-institutional": (
        _st50(_R50["c3"])["institutional"] == "CONTRADICTED"
        and _st50(_R50["c3"])["editorial"] == "UNKNOWN"
        and _st50(_R50["c3"])["underlying"] == "UNKNOWN"),
    "same-observation-no-corroboration": (
        _st50(_R50["c4"])["observational"] == "CONTRADICTED"
        and _st50(_R50["c4"])["underlying"] == "CONTRADICTED"
        and _st50(_R50["c4"])["corroboration"] == "CONTRADICTED"
        and _R50["c4"]["independent-corroboration"] is False
        and _R50["c4"]["dimensions"]["corroboration"]["claims"]["k1"]
        ["status"] == "CONTRADICTED"),
    "translation-ancestor-is-one-line": (
        _st50(_R50["c5"])["underlying"] == "CONTRADICTED"
        and _R50["c5"]["dimensions"]["underlying"]["pairs"]["A|B"]
        ["evidence"]["contradicts"] == ["r1", "r2"]
        and len(_R50["c5"]["dependencies"]) == 2
        and _st50(_R50["c5"])["observational"] == "UNKNOWN"
        and _st50(_R50["c5"])["corroboration"] == "CONTRADICTED"),
    "same-document-independent-editorial": (
        _st50(_R50["c6"])["editorial"] == "SUPPORTED"
        and _st50(_R50["c6"])["underlying"] == "CONTRADICTED"
        and _st50(_R50["c6"])["observational"] == "CONTRADICTED"
        and _R50["c6"]["independent-evidence"] is False),
    "no-score-or-ladder": (
        not ({"score", "confidence", "weight", "ladder"}
             & set(_keys50(_R50["c1"])))
        and "independent-evidence" in _R50["c1"]
        and "independent-corroboration" in _R50["c1"]),
}
expect("T203 A50: THE SIX DIMENSIONS ARE CLASSIFIED SEPARATELY (no score, no "
       "ladder): different authors on one underlying source keep attribution "
       "SUPPORTED while underlying is CONTRADICTED and every other dimension "
       "stays UNKNOWN; different publishers under shared editorial control "
       "contradict EDITORIAL only; different institutions under a shared "
       "funder contradict INSTITUTIONAL only; two publications repeating one "
       "observation contradict observational AND corroboration (never "
       "awarded); two translations of one earlier translation are found as "
       "ONE material line by closure (evidence r1+r2) and still fail "
       "corroboration; two scholars on one primary document can be "
       "editorially independent (SUPPORTED) while underlying and "
       "observational are CONTRADICTED - research-process independence is not "
       "source independence; and no dimension carries a numeric score",
       _T203,
       why=lambda tr: ([] if all(tr.values()) else
                       [str(sorted(k for k, v in tr.items() if not v))]))

_T204 = {
    "no-information-stays-unknown": (
        _st50(_R50["c7"])["attribution"] == "SUPPORTED"
        and all(_st50(_R50["c7"])[d] == "UNKNOWN"
                for d in ("underlying", "editorial", "institutional",
                          "observational", "corroboration"))
        and _R50["c7"]["independent-evidence"] is False
        and len(_R50["c7"]["unresolved"]) == 5
        and len(_R50["c7"]["next-evidence"]) >= 5),
    "conflict-preserved": (
        _st50(_R50["c8"])["underlying"] == "UNKNOWN"
        and _R50["c8"]["dimensions"]["underlying"]["conflict"] is True
        and _R50["c8"]["dimensions"]["underlying"]["evidence"]["supports"]
        == ["r2"]
        and _R50["c8"]["dimensions"]["underlying"]["evidence"]["contradicts"]
        == ["r1"]),
    "partial-bibliography-no-promotion": (
        _st50(_R50["c9"])["attribution"] == "SUPPORTED"
        and _st50(_R50["c9"])["underlying"] == "UNKNOWN"
        and _st50(_R50["c9"])["corroboration"] == "UNKNOWN"
        and _R50["c9"]["independent-corroboration"] is False),
    "wording-never-independence": (
        _st50(_R50["c10"]) == _st50(_R50["c10b"])
        and _st50(_R50["c10"])["underlying"] == "CONTRADICTED"
        and _st50(_R50["c10"])["corroboration"] == "CONTRADICTED"
        and _R50["c10"]["dependencies"][0]["relation"] == "r1"),
    "one-common-source-does-not-collapse-all": (
        _R50["c11"]["dimensions"]["underlying"]["pairs"]["A|B"]["status"]
        == "CONTRADICTED"
        and _R50["c11"]["dimensions"]["underlying"]["pairs"]["A|D"]["status"]
        == "UNKNOWN"
        and _R50["c11"]["dimensions"]["underlying"]["pairs"]["B|D"]["status"]
        == "UNKNOWN"
        and len(_R50["c11"]["dependencies"]) == 1
        and _st50(_R50["c11"])["editorial"] == "UNKNOWN"
        and _st50(_R50["c11"])["corroboration"] == "CONTRADICTED"),
    "genuine-independent-observations": (
        all(_st50(_R50["c12"])[d] == "SUPPORTED"
            for d in _ind50.DIMENSIONS)
        and _R50["c12"]["independent-evidence"] is True
        and _R50["c12"]["independent-corroboration"] is True
        and _R50["c12"]["dimensions"]["corroboration"]["claims"]["k1"]
        ["status"] == "SUPPORTED"),
    "shared-terminal-is-shared-attribution": (
        _st50(_R50["cid"])["attribution"] == "CONTRADICTED"
        and _R50["cid"]["dimensions"]["attribution"]["label"]
        == "EXPLICIT-SHARED-ATTRIBUTION"
        and _st50(_R50["cid"])["underlying"] == "CONTRADICTED"),
    "unknown-derivation-never-promotes": (
        _st50(_R50["cunk"])["attribution"] == "SUPPORTED"
        and all(_st50(_R50["cunk"])[d] == "UNKNOWN"
                for d in ("underlying", "editorial", "institutional",
                          "observational", "corroboration"))
        and len(_R50["cunk"]["unknown-derivations"]) == 1
        and _R50["cunk"]["unknown-derivations"][0]["relation"] == "r1"),
    "invalid-relation-rejected": _raises50(
        lambda: _ind50.assess(_c50("bad", {"A": {"terminals": ["a"]}},
                                   {"a": _t50("A")},
                                   [_r50("r1", "made-up", "a", "b")]))),
}
expect("T204 A50: UNKNOWN IS TERMINAL, DEPENDENCY IS SCOPED, AND CONFLICT IS "
       "KEPT: no information leaves all five stronger dimensions UNKNOWN with "
       "concrete next-evidence hints; supporting and contradicting records "
       "for one pair yield UNKNOWN with conflict=True and BOTH lists exact "
       "(the support never leaks into the contradiction list); a PARTIAL "
       "bibliography promotes nothing; differently worded accounts of one "
       "shared source classify identically and fail corroboration; ONE common "
       "source among three chains contradicts only that pair (A|B) while the "
       "others stay UNKNOWN - the case is not collapsed into one; genuine "
       "independent observations with recorded provenance are the only shape "
       "that reaches SUPPORTED on every dimension including corroboration; a "
       "terminal shared by both chains is EXPLICIT-SHARED-ATTRIBUTION and "
       "shared material; an unknown-derivation is recorded but never promotes "
       "or demotes; and an invented relation type is rejected",
       _T204,
       why=lambda tr: ([] if all(tr.values()) else
                       [str(sorted(k for k, v in tr.items() if not v))]))

_F50 = json.loads(open("research-hold/a50-a49-case.json").read())
_R49_50 = _ind50.assess(_ind50.case_from_a49())
_L050 = web_research.LEDGER[0]
_R49_50B = _ind50.assess(_ind50.case_from_a49())
_L150 = web_research.LEDGER[0]
_EX49 = _ind50.explain(_R49_50)
_EX12 = _ind50.explain(_R50["c12"])
_T205 = {
    "fixture-matches-held-a49": (
        _F50["case"] == _ind50.case_from_a49()
        and _F50["source"]["sha256"]
        == hashlib.sha256(open("research-hold/a49-citation-replay.json",
                               "rb").read()).hexdigest()
        and _F50["source"]["a49-policy-digest"]
        == json.loads(open("research-hold/a49-citation-replay.json").read())
        ["policy-digest"]),
    "a49-attribution-diverse": (
        _st50(_R49_50)["attribution"] == "SUPPORTED"
        and _R49_50["dimensions"]["attribution"]["label"]
        == "DISTINCT-STATED-ATTRIBUTIONS"
        and _F50["expected"]["attribution"]["label"]
        == "DISTINCT-STATED-ATTRIBUTIONS"),
    "a49-never-promoted": (
        all(_st50(_R49_50)[d] == "UNKNOWN"
            for d in ("underlying", "editorial", "institutional",
                      "observational", "corroboration"))
        and _R49_50["independent-evidence"] is False
        and _R49_50["independent-corroboration"] is False
        and _R49_50["dependencies"] == []
        and _R49_50["unknown-derivations"] == []
        and _F50["expected"]["underlying"] == "UNKNOWN"
        and _F50["expected"]["corroboration"] == "UNKNOWN"),
    "a49-facts-preserved": (
        len(_F50["case"]["facts"]) == 7
        and any("Le 2010" in f for f in _F50["case"]["facts"])
        and any("NOT followed" in f for f in _F50["case"]["facts"])
        and any("No primary edition" in f for f in _F50["case"]["facts"])
        and _F50["case"]["terminals"]["c:wells"]["status"] == "COMPLETE"
        and _F50["case"]["terminals"]["c:earlier-translations"]["status"]
        == "UNRESOLVED"),
    "explain-distinguishes-the-three-words": (
        "different attributions: DISTINCT-STATED-ATTRIBUTIONS (attribution "
        "only; NOT independent evidence)" in _EX49
        and "independent evidence: NOT ESTABLISHED" in _EX49
        and "independent corroboration: NOT ESTABLISHED" in _EX49
        and "independent evidence: ESTABLISHED" not in _EX49
        and "dependencies: none documented" in _EX49),
    "explain-words-are-computed": (
        "independent evidence: ESTABLISHED" in _EX12
        and "independent corroboration: ESTABLISHED" in _EX12
        and "different attributions: DISTINCT-STATED-ATTRIBUTIONS" in _EX12),
    "zero-network-and-no-network-import": (
        _L050 == _L150
        and "import urllib" not in open("independence.py").read()
        and "import socket" not in open("independence.py").read()
        and "import http" not in open("independence.py").read()
        and "import requests" not in open("independence.py").read()
        and "urlopen" not in open("independence.py").read()),
    "history-whole": (
        _sig44("research-hold/a49-citation-replay.json", "a49-manifest.sha256")
        and _sig44("research-hold/a48-reference-read.json", "a48-manifest.sha256")
        and _sig44("research-hold/a47-provenance.json", "a47-manifest.sha256")
        and _sig44("research-hold/a46-compare.json", "a46-manifest.sha256")
        and _sig44("research-hold/a45-reclass.json", "a45-manifest.sha256")
        and _sig44("research-hold/a44-read.json", "a44-manifest.sha256")
        and _sig44("research-hold/a43-read.json", "a43-manifest.sha256")
        and _sig44("research-hold/a42-duel.json", "a42-manifest.sha256")),
    "config-untouched": (
        hashlib.sha256(open("config.json", "rb").read()).hexdigest()
        == "0b23f30ae0c89f61080796ef7fcf04196ca384f2855efb07826ee6fb27a931d0"),
    "charter-untouched": (loop.read_cfg().get("GENERAL_MAXTOK")
                          == stages.CONFIG.get("GENERAL_MAXTOK") == 1024),
}
expect("T205 A50: THE A49 REGRESSION REPRODUCES WITHOUT MANUFACTURING "
       "CORROBORATION (ZERO network - the LEDGER is unmoved): the fixture is "
       "byte-derived from the held A49 record (its sha and policy digest "
       "match) and equals a fresh case_from_a49(); W stays "
       "DISTINCT-STATED-ATTRIBUTIONS while underlying, editorial, "
       "institutional, observational and corroboration all stay UNKNOWN, with "
       "NO dependencies, NO promotion and independent evidence/corroboration "
       "NOT ESTABLISHED; the seven A49 facts are preserved (Le 2010 partial, "
       "the pointer NOT followed, no primary edition among W's entries); the "
       "explainer prints the three words SEPARATELY - attribution only; NOT "
       "independent evidence - and the words are COMPUTED (the genuine-"
       "observation case prints ESTABLISHED); the model imports no network "
       "module and the LEDGER is unmoved; every A42-A49 manifest still "
       "verifies, the config sha and the charter are untouched",
       _T205,
       why=lambda tr: ([] if all(tr.values()) else
                       [str(sorted(k for k, v in tr.items() if not v))]))
