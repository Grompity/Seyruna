# ---------------- A44: the next HTML read, replayed (adds) ----------------
_P44 = json.loads(open("research-hold/a44-read.json").read())
_S44 = json.loads(open("research-hold/a35-six-final.json").read())["cycles"]
_sig44 = lambda p, man: (lambda want: want is not None and want ==
    hashlib.sha256(open(p, "rb").read()).hexdigest())(
        next((ln.split()[0] for ln in open(man)
              if ln.strip() and not ln.startswith("#")
              and ln.split()[1] == p), None))
def _policy44():
    import re
    txt = open("a44-contract.md").read()
    m = re.search(r"<!-- A44-POLICY -->(.*?)<!-- /A44-POLICY -->", txt, re.S)
    pol = json.loads(m.group(1))
    return (pol, hashlib.sha256(json.dumps(pol, sort_keys=True)
                                .encode()).hexdigest(), txt)
_L044 = web_research.LEDGER[0]
_POL44, _PDIG44, _CTXT44 = _policy44()
_ROWS44 = _P44["boundary"]["packet"]
_ROW44 = _P44["read"]["packet"]["results"][0]
_TXT44 = _ROW44.get("text") or ""
_PRIM44 = json.loads(open("research-hold/a36-read-EA1.json")
                     .read())["selection"]["primary"]
_LV44 = research_eval.levels36(_PRIM44, _P44["read"]["packet"])
_CO44 = web_research.corroboration({"results": [
    json.loads(open("research-hold/a42-duel.json").read())
    ["reads"]["results"][0], _ROW44]})
_AN44 = research_eval.answer42(None, [_P44["policy"]["candidate"]],
                               [_ROW44], "127.0.0.1")
_L144 = web_research.LEDGER[0]
_T441 = {
    "policy-frozen": (
        _PDIG44 == _P44["policy-digest"] and _PDIG44 in _CTXT44
        and _P44["policy"] == _POL44
        and _POL44["law"].startswith("A44-1")
        and _P44["label"] == "live"),
    "boundary-verified": (
        all(_P44["boundary"]["verification"].values())
        and _ROWS44["packet-digest-sha256"]
        == hashlib.sha256(json.dumps(
            json.loads(open("research-hold/a42-duel.json").read())
            ["search"]["rows-words"], sort_keys=True).encode()).hexdigest()
        and _P44["policy"]["candidate"]["row-1based"] == 4
        and _P44["policy"]["candidate"]["index-0based"] == 3
        and _P44["policy"]["candidate"]["url"]
        == "https://www.cs.colostate.edu/~malaiya/ashoka.html"
        and _P44["policy"]["candidate"]["publisher-normalized"]
        == web_research.publisher(_P44["policy"]["candidate"]["url"])
        == "colostate.edu"
        and _P44["boundary"]["candidate"]["candidate-represented"] is False
        and _P44["boundary"]["candidate"]["candidate-attempted-before"]
        is False),
    "contract-honored": (
        _P44["budget"]["searches"] == 0
        and _P44["budget"]["reads"] == 1
        and _P44["budget"]["retries"] == 0
        and _P44["budget"]["substitutions"] == 0
        and _P44["budget"]["fallbacks"] == 0
        and _P44["budget"]["read-calls"] == 1
        and _P44["budget"]["bodies-read"] == 1
        and len(_P44["read"]["packet"]["results"]) == 1
        and _ROW44["url"] == _P44["policy"]["candidate"]["url"]),
    "transport-answered": (
        _P44["read"]["transport"]["answered"] is True
        and _P44["read"]["transport"]["status"] == 200
        and _P44["read"]["transport"]["word"] == "opened"
        and _P44["read"]["wall-ms"] > 0),
    "content-arrived": (
        _P44["read"]["content"]["arrived"] is True
        and _P44["read"]["content"]["extracted-bytes"] == 1200
        and len(_TXT44) == 1200),
    "addressing-law-unmoved": (
        research_eval.answer42.__defaults__ == ("ashoka",)
        and "ashoka" not in _TXT44.lower()
        and "asoka" in _TXT44.lower()),
    "outcome-off-question-and-annotated": (
        _P44["read"]["outcome"] == "OFF-QUESTION"
        and "Asoka" in _P44["outcome-note"]["spelling"]
        and "NOT-USABLE" in _P44["outcome-note"]["spelling"]
        and "not-changed" in _P44["outcome-note"]),
    "answer-replays": (
        _AN44 == _P44["answer"]
        and _P44["answer"]["answer"] == "EVIDENCE-GAP"
        and _AN44["reads"][0]["usable"] is False
        and "ashoka" in _AN44["reads"][0]["why"]),
    "publisher-distinct": (
        _ROW44["publisher"] == "colostate.edu"
        and _PRIM44["publisher"] == "wikipedia.org"
        and _ROW44["publisher"] != _PRIM44["publisher"]),
    "corroboration-not-claimed": (
        _CO44 == _P44["corroboration-across-reads"]["counts"]
        and _CO44["read"] == 2
        and _CO44["origin_publishers"] == 2
        and _CO44["independence"] == "candidate"
        and _CO44["conflict"] == "unknown"
        and _P44["corroboration-across-reads"]["word"]
        .startswith("CANDIDATE at best")
        and _LV44 == _P44["levels"]
        and _P44["levels"]["verdict"] == "DIVERSITY-ONLY"),
    "metadata-limitation-recorded": (
        "NOT EXPOSED"
        in _P44["read"]["metadata-limitations"]["content-type"]
        and _P44["read"]["transport"]["final"].startswith("ABSENT")),
    "ea1-unchanged": (
        _P44["ea1-classification"]["a42"].startswith("PARTIAL")
        and _P44["ea1-classification"]["a43"].startswith("EVIDENCE-GAP")
        and _P44["ea1-classification"]["changed"] is False),
    "semantic-unknown": _P44["semantic-improvement"].startswith("UNKNOWN"),
    "dimensions-kept-separate": (
        len(_P44["dimensions"]) == 8
        and _P44["dimensions"]["semantic-improvement"]
        .startswith("UNKNOWN")),
    "replay-makes-no-network-call": _L044 == _L144,
    "history-whole": (
        _sig44("research-hold/a43-read.json", "a43-manifest.sha256")
        and _sig44("research-hold/a42-duel.json", "a42-manifest.sha256")
        and _sig44("research-hold/a41-duel.json", "a41-manifest.sha256")
        and _sig44("research-hold/a40-duel.json", "a40-manifest.sha256")
        and json.loads(open("research-hold/a37-probe.json").read())
        ["packets"]["EA1"]["a36-file-sha"]
        == hashlib.sha256(open("research-hold/a36-read-EA1.json",
                               "rb").read()).hexdigest()),
    "charter-untouched": (loop.read_cfg().get("GENERAL_MAXTOK")
                          == stages.CONFIG.get("GENERAL_MAXTOK")
                          == 1024)}
expect("T197 THE NEXT HTML READ AT ITS BYTES (ALL offline - ONE attempt "
       "was spent LIVE and the REPLAY spends NONE): the boundary was "
       "VERIFIED before the contract (the packet digest, row 4 at the "
       "ORIGINAL order, colostate.edu at the existing identity law, not "
       "represented among READ voices - A43's columbia ATTEMPT is not a "
       "representation) and the CONTRACT is the source (digest recomputed "
       "from its own block); EXACTLY ONE read rode (one url, one call, "
       "zero searches, zero retries, zero substitutions, zero fallbacks) "
       "and the TRANSPORT ANSWERED (200, 'opened') with 1200 extracted "
       "bytes; the ADDRESSING LAW was NOT TUNED (its literal default "
       "still 'ashoka') and it is EXACTLY the law that speaks the verdict "
       "- the page says 'Asoka' (a correct variant) and never 'Ashoka', "
       "so CONTENT ARRIVED and the frozen law says NOT-USABLE: OFF-QUESTION "
       "is printed AS ITS OWN WORD (outside the frozen categories) with "
       "BOTH facts kept, neither hiding the other; the answer map REPLAYS "
       "(EVIDENCE-GAP for the experiment) while A42's PARTIAL and A43's "
       "EVIDENCE-GAP stand byte-identical; the publisher is GENUINELY "
       "DISTINCT and the table now has TWO READ origin publishers - the "
       "independence word is 'candidate' and the ladder says 'unknown', so "
       "the levels word is DIVERSITY-ONLY and NOTHING claims corroboration; "
       "the missing kind word rides as a CAPABILITY LIMITATION (never "
       "fabricated, never repaired here), the eight dimensions ride "
       "separate, semantic improvement stays UNKNOWN BY LAW, the replay "
       "touches NO network, the HISTORY stands WHOLE (A43/A42/A41/A40 "
       "manifests, A36 at A37's stored word); and the charter rides "
       "UNTOUCHED at file AND mirror",
       _T441,
       why=lambda tr: ([] if all(tr.values()) else
                       [str(sorted(k for k, v in tr.items()
                                    if not v))]))
