# ---------------- A43: the publisher-distinct read, replayed (adds) --------
_P43 = json.loads(open("research-hold/a43-read.json").read())
_S43 = json.loads(open("research-hold/a35-six-final.json").read())["cycles"]
_sig43 = lambda p, man: (lambda want: want is not None and want ==
    hashlib.sha256(open(p, "rb").read()).hexdigest())(
        next((ln.split()[0] for ln in open(man)
              if ln.strip() and not ln.startswith("#")
              and ln.split()[1] == p), None))
def _policy43():
    """the policy AS the CONTRACT owns it: parsed from the frozen block and
    digested at the canonical JSON - the contract is the source, so the
    rule is replayable from the contract + the packet alone."""
    import re
    txt = open("a43-contract.md").read()
    m = re.search(r"<!-- A43-POLICY -->(.*?)<!-- /A43-POLICY -->", txt, re.S)
    pol = json.loads(m.group(1))
    return (pol, hashlib.sha256(json.dumps(pol, sort_keys=True)
                                .encode()).hexdigest(), txt)
_L043 = web_research.LEDGER[0]
_POL43, _PDIG43, _CTXT43 = _policy43()
_PK43 = _P43["packet"]["rows"]
_PK42 = _P42["search"]["rows-words"]
_FIRSTTWO43 = [r["url"] for r in _PK42
               if r.get("url")
               and web_research.publisher(r["url"]) != "127.0.0.1"][:2]
_PICK43 = research_eval.pick_distinct43(_PK43, _POL43["represented"],
                                        _POL43["house"])
_DUP43 = research_eval.pick_distinct43(
    [{"url": "https://en.wikipedia.org/wiki/A", "publisher": "wikipedia.org"},
     {"url": "https://en.wikipedia.org/wiki/B", "publisher": "wikipedia.org"},
     {"url": "https://x.example/y", "publisher": "x.example"}],
    ["wikipedia.org"], "h")
_NONE43 = research_eval.pick_distinct43(
    [{"url": "https://en.wikipedia.org/wiki/A", "publisher": "wikipedia.org"},
     {"url": "https://en.wikipedia.org/wiki/B", "publisher": "wikipedia.org"}],
    ["wikipedia.org"], "h")
_L143 = web_research.LEDGER[0]
_T431 = {
    "policy-frozen-and-owned": (
        _PDIG43 == _P43["policy-digest"] and _PDIG43 in _CTXT43
        and _P43["policy"] == _POL43
        and _P43["label"] == "live"
        and _POL43["law"].startswith("A43-1")),
    "packet-verified": (
        all(_P43["packet"]["verification"].values())
        and _P43["packet"]["artifact-sha256"]
        == hashlib.sha256(open("research-hold/a42-duel.json",
                               "rb").read()).hexdigest()
        and _P43["packet"]["packet-digest-sha256"]
        == hashlib.sha256(json.dumps(_PK42, sort_keys=True)
                          .encode()).hexdigest()),
    "content-blind-by-construction": (
        _P43["packet"]["candidate-content"].startswith("ABSENT")
        and not any(("text" in r or "body" in r or "content" in r)
                    for r in _PK43)
        and _P43["selection"]["no-content-consulted"] is True),
    "old-first-two-reproducible": (
        _FIRSTTWO43 == _P42["pick"]["urls"]
        and _P42["pick"]["urls"] == [_PK42[0]["url"], _PK42[1]["url"]]
        and _P42["answer"]["answer"] == "PARTIAL"),
    "distinct-rule-deterministic": (
        _PICK43["pick"] == _P43["selection"]["pick"]
        and _PICK43["position"] == _P43["selection"]["position-among-eligible"]
        and _PICK43["note"].startswith("the FIRST eligible row")),
    "duplicates-excluded": (
        _DUP43["pick"] == {"url": "https://x.example/y",
                           "publisher": "x.example"}
        and [s["skipped"] for s in _DUP43["skipped"]]
        == ["represented", "represented"]
        and [s["publisher"] for s in _P43["selection"]["skipped"]]
        == ["wikipedia.org", "wikipedia.org"]),
    "order-preserved": (
        [r["url"] for r in _PK43] == [r["url"] for r in _PK42]
        and _P43["selection"]["position-among-eligible"] == 2),
    "no-candidate-zero-reads": (
        _NONE43["pick"] is None
        and "zero reads" in _NONE43["note"].lower()
        and _P43["represented"]["alternative-reading"]["candidate-count"] == 0
        and "ZERO reads"
        in _P43["represented"]["alternative-reading"]["consequence"]),
    "exactly-one-read": (
        _P43["budget"]["read-events"] == 1
        and _P43["budget"]["search-events"] == 0
        and len(_P43["read"]["packet"]["results"]) == 1
        and _P43["read"]["packet"]["spent"]["calls"] == 1
        and _P43["read"]["packet"]["results"][0]["url"]
        == _P43["selection"]["pick"]["url"]),
    "read-accounting-honest": (
        _P43["read"]["packet"]["spent"]["fetch"] == 0
        and "BODIES READ" in _P43["read-accounting"]["fetch-word"]
        and _P43["read-accounting"]["attempts"].startswith("1")),
    "transport-vs-content": (
        _P43["read"]["transport"]["answered"] is True
        and _P43["read"]["content"]["arrived"] is False
        and _P43["read"]["transport"]["word"]
        == "wrong-kind:application/pdf"
        and _P43["read"]["content"]["bytes-extracted"] == 0),
    "success-is-not-corroboration": (
        _P43["corroboration-across-reads"]["counts"]["independence"]
        == "none"
        and _P43["corroboration-across-reads"]["word"]
        .startswith("NOT DEMONSTRATED")
        and web_research.corroboration({"results": [
            {"url": "https://a.example/x", "text": "Ashoka " * 30}]})
        ["independence"] == "none"),
    "missing-provenance-unknown": (
        ("status" not in _P43["read"]["packet"]["results"][0]
         and "final" not in _P43["read"]["packet"]["results"][0]
         and "text" not in _P43["read"]["packet"]["results"][0])
        and all(_P43["read"]["transport"][k].startswith("ABSENT")
                for k in ("status", "final", "retrieved"))),
    "levels-recorded": (
        _P43["levels"] == research_eval.levels36(
            json.loads(open("research-hold/a36-read-EA1.json")
                       .read())["selection"]["primary"],
            _P43["read"]["packet"])
        and _P43["levels"]["verdict"] == "MONOCULTURE-PERSISTS"
        and "wrong-kind" in _P43["levels"]["why"]
        and "RECORDED word" in _P43["levels"]["why"]),
    "answer-replays-and-ea1-unchanged": (
        research_eval.answer42(None, [_P43["selection"]["pick"]],
                               _P43["read"]["packet"]["results"],
                               "127.0.0.1") == _P43["answer"]
        and _P43["answer"]["answer"] == "EVIDENCE-GAP"
        and _P43["ea1-classification"]["changed"] is False
        and _P43["ea1-classification"]["a42-answer"].startswith("PARTIAL")),
    "corroboration-replays": (
        web_research.corroboration({"results": [
            _P42["reads"]["results"][0],
            _P43["read"]["packet"]["results"][0]]})
        == _P43["corroboration-across-reads"]["counts"]
        and _P43["corroboration-across-reads"]["counts"]["read"] == 1
        and _P43["corroboration-across-reads"]["counts"]
        ["origin_publishers"] == 1),
    "dimensions-kept-separate": (
        len(_P43["dimensions"]) == 8
        and all(len(v) == 2 for v in _P43["dimensions"].values())),
    "semantic-unknown": _P43["semantic-improvement"].startswith("UNKNOWN"),
    "replay-makes-no-network-call": _L043 == _L143,
    "history-whole": (
        _sig43("research-hold/a42-duel.json", "a42-manifest.sha256")
        and _sig43("research-hold/a41-duel.json", "a41-manifest.sha256")
        and _sig43("research-hold/a40-duel.json", "a40-manifest.sha256")
        and json.loads(open("research-hold/a37-probe.json").read())
        ["packets"]["EA1"]["a36-file-sha"]
        == hashlib.sha256(open("research-hold/a36-read-EA1.json",
                               "rb").read()).hexdigest()),
    "charter-untouched": (loop.read_cfg().get("GENERAL_MAXTOK")
                          == stages.CONFIG.get("GENERAL_MAXTOK")
                          == 1024)}
expect("T196 THE PUBLISHER-DISTINCT READ AT ITS BYTES (ALL offline - ONE "
       "source-read attempt was spent LIVE and the REPLAY spends NONE; a "
       "zero-count on the ROAD's fetch word is NOT a missed attempt): the "
       "policy is FROZEN IN THE CONTRACT'S OWN BLOCK (the digest recomputed "
       "at the canonical JSON, the contract the source - replayable from "
       "contract + packet alone) and it was declared BEFORE any candidate "
       "byte; the PACKET rides BYTE-VERIFIED (the A42 manifest's sha, the "
       "rows' own digest, the ORIGINAL order, and NO candidate content - "
       "selection could not see what was never stored); the OLD FIRST-TWO "
       "law still REPRODUCES (A42's pick and its PARTIAL answer ride "
       "UNTOUCHED - A43 is a new experiment, not a correction); the NEW "
       "rule is DETERMINISTIC (the two represented wikipedia.org rows ride "
       "'represented' and the FIRST distinct publisher wins by ORDER, no "
       "path/extension/quality/content consulted); a NO-CANDIDATE packet "
       "spends ZERO reads (the alternative reading's consequence printed, "
       "not taken); EXACTLY ONE read was authorized and spent (one url, "
       "one call, zero searches, no retry); TRANSPORT and CONTENT stand "
       "APART (the kind wall ANSWERED and the body did NOT arrive), the "
       "missing status/final/retrieved ride as ABSENT words and the "
       "success-word is NOT corroboration (the table says none at one READ "
       "publisher); the levels word rides the frozen table (a RECORDED "
       "road word, never a fallback), the answer word REPLAYS at the "
       "declared map (EVIDENCE-GAP for the experiment) while EA1's A42 "
       "classification stands UNCHANGED; the DIMENSIONS ride SEPARATE "
       "(eight, scoreless), semantic improvement stays UNKNOWN BY LAW, the "
       "replay touches NO network (the ledger unmoved), the HISTORY stands "
       "WHOLE (A42/A41/A40 re-sign at their OWN manifests, A36's witness at "
       "A37's stored word); and the charter rides UNTOUCHED at file AND "
       "mirror",
       _T431,
       why=lambda tr: ([] if all(tr.values()) else
                       [str(sorted(k for k, v in tr.items()
                                    if not v))]))
