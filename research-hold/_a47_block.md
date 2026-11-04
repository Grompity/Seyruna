# ---------------- A47: provenance probe, replayed (adds) ----------------
_P47 = json.loads(open("research-hold/a47-provenance.json").read())
_A46 = json.loads(open("research-hold/a46-compare.json").read())
_W47 = json.loads(open("research-hold/a42-duel.json").read())["reads"]["results"][0]
_C47 = json.loads(open("research-hold/a44-read.json").read())["read"]["packet"]["results"][0]
def _policy47():
    import re
    txt = open("a47-contract.md").read()
    m = re.search(r"<!-- A47-POLICY -->(.*?)<!-- /A47-POLICY -->", txt, re.S)
    pol = json.loads(m.group(1))
    return (pol, hashlib.sha256(json.dumps(pol, sort_keys=True)
                                .encode()).hexdigest(), txt)
def _markers47(text, pol):
    import re
    return [m.group(0) for m in re.finditer(pol["extraction"]["citation-regex"], text)]
def _phrases47(text, pol):
    import re
    hits = []
    for ph in pol["extraction"]["phrase-list"]:
        for m in re.finditer(re.escape(ph), text, re.I):
            hits.append((ph, m.start()))
    return sorted(hits)
_L047 = web_research.LEDGER[0]
_POL47, _PDIG47, _CTXT47 = _policy47()
_WM47 = _markers47(_W47["text"], _POL47)
_CM47 = _markers47(_C47["text"], _POL47)
_WP47 = _phrases47(_W47["text"], _POL47)
_CP47 = _phrases47(_C47["text"], _POL47)
_SIG47 = _P47["signals"]["W"] + _P47["signals"]["C"]
_SRC47 = {"W": _W47["text"], "C": _C47["text"]}
def _sigok47():
    for s in _SIG47:
        a, b = s["offset"]
        if _SRC47[s["source"]][a:b] != s["excerpt"]:
            return False
    return True
_TRACE47 = {t["class"]: t["satisfied"] for t in
            _P47["classification"]["precedence-trace"]}
_L147 = web_research.LEDGER[0]
_T502 = {
    "policy-frozen": (
        _PDIG47 == _P47["policy-digest"] and _PDIG47 in _CTXT47
        and _P47["policy"] == _POL47
        and _PDIG47 == "d923a13ffa0f8d8f1a9f0d0e04c327c06a490a2610dea1adec714bba5622f5f4"
        and _POL47["law"].startswith("A47-1")),
    "same-held-windows": (
        _POL47["sources"]["W"]["text-sha256"]
        == hashlib.sha256(_W47["text"].encode()).hexdigest()
        == _A46["boundary"]["sources"]["W"]["text-sha256"]
        and _POL47["sources"]["C"]["text-sha256"]
        == hashlib.sha256(_C47["text"].encode()).hexdigest()
        == _A46["boundary"]["sources"]["C"]["text-sha256"]
        and len(_W47["text"]) == len(_C47["text"]) == 1200
        and _P47["boundary"]["extraction-cap"] == 1200),
    "deterministic-signals-replay": (
        _WM47 == ["[ 1 ]", "[ 2 ]", "[ 3 ]"]
        and _CM47 == []
        and len(_WP47) == 1 and _WP47[0][0] == "attributed to"
        and len(_CP47) == 6
        and {p for p, _ in _CP47} == {"has written", "preserved the legend",
                                      "based on", "earlier translations",
                                      "the compiler", "present rendering"}),
    "signals-verbatim-and-locatable": (
        _sigok47()
        and _P47["signals"]["counts"]["W"] == 4
        and _P47["signals"]["counts"]["C"] == 12
        and _P47["signals"]["counts"]["explicit"] == 16
        and _P47["signals"]["counts"]["inferred"] == 0),
    "classification-frozen-and-traced": (
        _P47["classification"]["class"] == "ATTRIBUTION-CHAIN-INCOMPLETE"
        and _TRACE47 == {"EXPLICIT-SHARED-ATTRIBUTION": False,
                         "POSSIBLE-SHARED-DERIVATION": False,
                         "ATTRIBUTION-CHAIN-INCOMPLETE": True,
                         "DISTINCT-STATED-ATTRIBUTIONS": False,
                         "UNKNOWN": False}
        and _P47["shared"]["named-authorities"] == []
        and _P47["chains"]["W"]["reconstructable"] is False
        and _P47["chains"]["C"]["reconstructable"] is True),
    "no-independence-promotion": (
        _P47["independence"]["assessment"] == "UNKNOWN"
        and _P47["independence"]["promoted"] is False
        and "UNDIFFERENTIATED and UNKNOWN" in _P47["independence"]["four-propositions"]),
    "a46-unchanged": (
        _P47["carry-over"]["a46"] == {"agreement": 2, "conflict": 0, "partial": 2,
                                      "indeterminate": 0, "no-match": 9,
                                      "status": "UNCHANGED - A47 does not re-run claim comparison and does not alter its counts"}
        and _A46["counts"]["agreement"] == 2 and _A46["counts"]["partial"] == 2
        and _A46["counts"]["no-match"] == 9),
    "ladder-unchanged": _P47["carry-over"]["ladder"].startswith("DIVERSITY-ONLY"),
    "ea1-unchanged": (
        _P47["carry-over"]["ea1"]["changed"] is False
        and _P47["carry-over"]["ea1"]["a42"].startswith("PARTIAL")
        and _P47["carry-over"]["ea1"]["a43"].startswith("EVIDENCE-GAP")
        and _P47["carry-over"]["ea1"]["a44"].startswith("EVIDENCE-GAP")),
    "semantic-unknown": _P47["carry-over"]["semantic"].startswith("UNKNOWN"),
    "zero-budget-and-replay-label": (
        all(_P47["budget"][k] == 0 for k in ("searches", "network-requests",
            "source-reads", "new-evidence", "pdf-work", "substitutions"))
        and _P47["label"] == "replay"
        and "ZERO searches" in _P47["label-law"]),
    "limitations-recorded": (
        len(_P47["limitations"]) == 5
        and any("1200-char" in x for x in _P47["limitations"])
        and any("analyst judgment" in x for x in _P47["limitations"])),
    "replay-makes-no-network-call": _L047 == _L147,
    "history-whole": (
        _sig44("research-hold/a46-compare.json", "a46-manifest.sha256")
        and _sig44("research-hold/a45-reclass.json", "a45-manifest.sha256")
        and _sig44("research-hold/a44-read.json", "a44-manifest.sha256")
        and _sig44("research-hold/a43-read.json", "a43-manifest.sha256")
        and _sig44("research-hold/a42-duel.json", "a42-manifest.sha256")
        and json.loads(open("research-hold/a37-probe.json").read())
        ["packets"]["EA1"]["a36-file-sha"]
        == hashlib.sha256(open("research-hold/a36-read-EA1.json",
                               "rb").read()).hexdigest()),
    "charter-untouched": (loop.read_cfg().get("GENERAL_MAXTOK")
                          == stages.CONFIG.get("GENERAL_MAXTOK") == 1024)}
expect("T200 HELD-SOURCE PROVENANCE PROBE AT ITS BYTES (ALL offline - ZERO "
       "searches, ZERO network, ZERO source reads, ZERO new evidence): the "
       "CONTRACT is the source (digest recomputed from its own block) and "
       "both windows are the SAME A46 bytes at their digests; the "
       "DETERMINISTIC signals replay exactly (W: three bare citation "
       "markers [1][2][3] and one 'attributed to' phrase; C: no markers and "
       "six closed-list phrase hits) and every analyst signal is VERBATIM "
       "and RE-LOCATABLE at its offset (16 signals, all EXPLICIT after the "
       "pre-commit amendment removed a mislabeled subject signal); the "
       "CLASSIFICATION is ATTRIBUTION-CHAIN-INCOMPLETE by the frozen "
       "precedence (shared attribution needs a shared NAME - W names none; "
       "possible shared derivation needs a visible connection - none is "
       "visible; distinct needs BOTH chains reconstructable - W's stops at "
       "unresolved markers; UNKNOWN is false because signals DO exist); NO "
       "named authority is shared; INDEPENDENCE stays UNKNOWN and is NOT "
       "promoted, with publisher/editorial/source/observational kept "
       "separate; A46's counts and the DIVERSITY-ONLY ladder are UNCHANGED "
       "and EA1's classification stands, semantic improvement UNKNOWN; the "
       "limitations (window caps, unresolved markers, unnamed translations, "
       "analyst judgment) ride recorded, the LEDGER is unmoved, the HISTORY "
       "stands whole (A46/A45/A44/A43/A42 manifests, A36 at A37's word), "
       "and the charter rides UNTOUCHED at file AND mirror",
       _T502,
       why=lambda tr: ([] if all(tr.values()) else
                       [str(sorted(k for k, v in tr.items() if not v))]))
