# ---------------- A45: spelling-aware reclassification, replayed (adds) ----------------
_P45 = json.loads(open("research-hold/a45-reclass.json").read())
_A44 = json.loads(open("research-hold/a44-read.json").read())
_ROW45 = _A44["read"]["packet"]["results"][0]
_TXT45 = _ROW45["text"]
def _policy45():
    import re
    txt = open("a45-contract.md").read()
    m = re.search(r"<!-- A45-POLICY -->(.*?)<!-- /A45-POLICY -->", txt, re.S)
    pol = json.loads(m.group(1))
    return (pol, hashlib.sha256(json.dumps(pol, sort_keys=True)
                                .encode()).hexdigest(), txt)
def _addressing45(text, variants):
    import re
    counts = {v: 0 for v in variants}
    surfaces = {v: [] for v in variants}
    for m in re.finditer(r"[A-Za-z]+", text):
        low = m.group(0).lower()
        if low in counts:
            counts[low] += 1
            surfaces[low].append(m.group(0))
    return {"addressed": any(counts.values()), "counts": counts,
            "surfaces": surfaces}
_L045 = web_research.LEDGER[0]
_POL45, _PDIG45, _CTXT45 = _policy45()
_R45 = _addressing45(_TXT45, _POL45["new-rule"]["variants"])
_ORIG45 = research_eval.answer42(None, [{"url": _ROW45["url"]}], [_ROW45],
                                 "127.0.0.1")
_PRIM45 = json.loads(open("research-hold/a36-read-EA1.json")
                     .read())["selection"]["primary"]
_LV45 = research_eval.levels36(_PRIM45, _A44["read"]["packet"])
_CO45 = web_research.corroboration({"results": [
    json.loads(open("research-hold/a42-duel.json").read())
    ["reads"]["results"][0], _ROW45]})
_L145 = web_research.LEDGER[0]
_T481 = {
    "policy-frozen": (
        _PDIG45 == _P45["policy-digest"] and _PDIG45 in _CTXT45
        and _P45["policy"] == _POL45
        and _PDIG45 == "387bd6a16f634d6df723dade4ada12145e87c89027e316e2c61d37fbb31af96c"
        and _POL45["law"].startswith("A45-1")),
    "evidence-verified": (
        _P45["evidence"]["artifact-sha256"]
        == hashlib.sha256(open("research-hold/a44-read.json", "rb").read())
        .hexdigest()
        and _P45["evidence"]["row-sha256"]
        == hashlib.sha256(json.dumps(_ROW45, sort_keys=True).encode())
        .hexdigest()
        and _P45["evidence"]["text-sha256"]
        == hashlib.sha256(_TXT45.encode()).hexdigest()
        and _P45["evidence"]["text-chars"] == len(_TXT45) == 1200
        and _P45["evidence"]["url"] == _ROW45["url"]
        and _P45["evidence"]["publisher"] == "colostate.edu"
        and _P45["evidence"]["status"] == 200),
    "original-law-unmoved-and-still-fails": (
        research_eval.answer42.__defaults__ == ("ashoka",)
        and "ashoka" in _ORIG45["reads"][0]["why"]
        and _ORIG45["answer"] == "EVIDENCE-GAP"
        == _A44["answer"]["answer"]
        == _P45["original-law"]["answer"]
        and _P45["original-law"]["a44-recorded"] == "EVIDENCE-GAP"
        == _A44["answer"]["answer"]
        and _A44["read"]["outcome"] == "OFF-QUESTION"
        and _P45["evidence"]["a44-outcome"] == "OFF-QUESTION"),
    "variant-list-closed": _POL45["new-rule"]["variants"] == ["ashoka", "asoka"],
    "new-law-replays": (
        _R45["counts"] == _P45["new-law"]["counts"]
        == {"ashoka": 0, "asoka": 3}
        and _R45["surfaces"] == _P45["new-law"]["surfaces"]
        == {"ashoka": [], "asoka": ["Asoka", "Asoka", "Asoka"]}
        and _R45["addressed"] == _P45["new-law"]["addressed"] is True
        and _P45["new-law"]["addressing"] == "PASS"
        and _P45["new-law"]["matched-variants"] == ["asoka"]),
    "complete-token-semantics-proven": (
        _addressing45("Asokan and Ashokan and asoka's and Asoka-2", ["ashoka", "asoka"])
        ["counts"] == {"ashoka": 0, "asoka": 2}
        and _addressing45("Asokan Ashokan", ["ashoka", "asoka"])["addressed"] is False),
    "classification-flips-only-addressing": (
        _P45["comparison"]["identical-bytes"] is True
        and _P45["comparison"]["original"]["answer"] == "EVIDENCE-GAP"
        and _P45["comparison"]["new"]["answer"] == "EVIDENCE-BACKED"
        and _P45["comparison"]["flips-addressing"] is True
        and _P45["new-law"]["usable"] is True
        and len(_TXT45) >= 60 and _ROW45["publisher"] != "127.0.0.1"),
    "corroboration-and-diversity-unmoved": (
        _CO45 == _P45["unchanged"]["corroboration"]
        == _A44["corroboration-across-reads"]["counts"]
        and _CO45["read"] == 2 and _CO45["origin_publishers"] == 2
        and _CO45["independence"] == "candidate"
        and _CO45["conflict"] == "unknown"
        and _LV45 == _P45["unchanged"]["levels"] == _A44["levels"]
        and _LV45["verdict"] == "DIVERSITY-ONLY"
        and _P45["unchanged"]["corroboration-word"].startswith("NOT DEMONSTRATED")),
    "ea1-unchanged": (
        _P45["unchanged"]["ea1"]["changed"] is False
        and _P45["unchanged"]["ea1"]["a42"].startswith("PARTIAL")
        and _P45["unchanged"]["ea1"]["a43"].startswith("EVIDENCE-GAP")
        and _P45["unchanged"]["ea1"]["a44"].startswith("EVIDENCE-GAP")),
    "semantic-unknown": (
        _P45["unchanged"]["semantic-improvement"].startswith("UNKNOWN")),
    "zero-budget-and-replay-label": (
        _P45["budget"]["searches"] == 0
        and _P45["budget"]["network-requests"] == 0
        and _P45["budget"]["source-reads"] == 0
        and _P45["budget"]["substitutions"] == 0
        and _P45["budget"]["ledger-before"] == _P45["budget"]["ledger-after"] == 0
        and _P45["label"] == "replay"
        and "NO new observation" in _P45["label-law"]),
    "limitations-recorded": (
        len(_P45["limitations"]) == 5
        and any("CAP" in x for x in _P45["limitations"])
        and any("ASCII" in x for x in _P45["limitations"])
        and any("one page" in x for x in _P45["limitations"])),
    "replay-makes-no-network-call": _L045 == _L145,
    "history-whole": (
        _sig44("research-hold/a44-read.json", "a44-manifest.sha256")
        and _sig44("research-hold/a43-read.json", "a43-manifest.sha256")
        and _sig44("research-hold/a42-duel.json", "a42-manifest.sha256")
        and json.loads(open("research-hold/a37-probe.json").read())
        ["packets"]["EA1"]["a36-file-sha"]
        == hashlib.sha256(open("research-hold/a36-read-EA1.json",
                               "rb").read()).hexdigest()),
    "charter-untouched": (loop.read_cfg().get("GENERAL_MAXTOK")
                          == stages.CONFIG.get("GENERAL_MAXTOK") == 1024)}
expect("T198 SPELLING-AWARE RECLASSIFICATION AT ITS BYTES (ALL offline - ZERO "
       "searches, ZERO network, ZERO source reads; the bytes are A44's ONE "
       "LIVE read and the REPLAY spends none): the CONTRACT is the source "
       "(digest recomputed from its own block) and it was frozen BEFORE its "
       "application; the held evidence VERIFIES at artifact/row/text digests; "
       "the ORIGINAL law is proven UNMOVED and still FAILS over the SAME "
       "bytes (literal 'ashoka', zero hits) so A44's OFF-QUESTION / "
       "EVIDENCE-GAP stands byte-identical; the NEW closed law (ashoka, "
       "asoka as COMPLETE ASCII tokens) REPLAYS exactly - 'asoka' 3, "
       "'ashoka' 0, surfaces 'Asoka' x3 - and its complete-token semantics "
       "are proven on the tricky cases ('Asokan'/'Ashokan' do NOT match, a "
       "possessive DOES); the addressing word FLIPS to PASS and the "
       "read-level word to EVIDENCE-BACKED while the ORIGINAL word rides "
       "beside it unchanged - two laws, identical bytes, neither rewriting "
       "the other; the publisher table and the ladder are UNMOVED (2 read "
       "publishers, independence 'candidate', conflict 'unknown', "
       "DIVERSITY-ONLY) so a spelling match claims NO corroboration and NO "
       "publisher diversity change; EA1's classification stands, semantic "
       "improvement stays UNKNOWN, the limitations (extract cap, ASCII "
       "tokenizer, adjective exclusion, one page) ride recorded, the LEDGER "
       "is unmoved, the HISTORY stands whole (A44/A43/A42 manifests, A36 at "
       "A37's word), and the charter rides UNTOUCHED at file AND mirror",
       _T481,
       why=lambda tr: ([] if all(tr.values()) else
                       [str(sorted(k for k, v in tr.items()
                                    if not v))]))
