# ---------------- A49: the preserved-body citation replay (adds) ----------------
_P49 = json.loads(open("research-hold/a49-citation-replay.json").read())
_B49 = open("research-hold/a48-w-body.html", "rb").read()
def _policy49():
    import re
    txt = open("a49-contract.md").read()
    m = re.search(r"<!-- A49-POLICY -->(.*?)<!-- /A49-POLICY -->", txt, re.S)
    pol = json.loads(m.group(1))
    return (pol, hashlib.sha256(json.dumps(pol, sort_keys=True)
                                .encode()).hexdigest(), txt)
def _sups49(html):
    import re
    out = []
    for m in re.finditer(r'<sup\b([^>]*)>(.*?)</sup>', html, re.S):
        attrs, inner = m.group(1), m.group(2)
        if "reference" not in attrs:
            continue
        a = re.search(r'<a\b([^>]*)>(.*?)</a>', inner, re.S)
        if not a:
            continue
        href = re.search(r'href="([^"]*)"', a.group(1))
        idm = re.search(r'id="([^"]*)"', attrs)
        out.append({"display": re.sub(r"<[^>]*>", "", a.group(2)).strip(),
                    "href": href.group(1) if href else None,
                    "sup-id": idm.group(1) if idm else None,
                    "pos": m.start()})
    return out
def _entry49(html, frag):
    import re
    import web_research as _wr
    m = re.search(r'id="' + re.escape(frag) + r'"', html)
    if not m:
        return None
    tag_start = html.rfind("<", 0, m.start())
    name = re.match(r'<([a-zA-Z0-9]+)', html[tag_start:]).group(1).lower()
    li_start = tag_start if name == "li" else html.rfind("<li", 0, m.start())
    li_end = html.find("</li>", m.start()) + 5
    raw = html[li_start:li_end]
    text = re.sub(r"\s+", " ", _wr.extract(raw, max_chars=20000, thin=0)).strip()
    return {"element": name, "li-start": li_start, "li-end": li_end,
            "raw": raw, "text": text}
_L049 = web_research.LEDGER[0]
_POL49, _PDIG49, _CTXT49 = _policy49()
_HTML49 = _B49.decode("utf-8", "replace")
_SUPS49 = _sups49(_HTML49)
_MAP49 = {}
for _k in ("1", "2", "3"):
    import re as _re
    _c = [s for s in _SUPS49 if _re.fullmatch(r"\[\s*" + _k + r"\s*\]", s["display"])]
    assert len(_c) == 1, (_k, len(_c))
    _e = _entry49(_HTML49, _c[0]["href"][1:])
    _MAP49[_k] = {"sup": _c[0], "entry": _e}
_L149 = web_research.LEDGER[0]
_T202 = {
    "policy-frozen": (
        _PDIG49 == _P49["policy-digest"] and _PDIG49 in _CTXT49
        and _P49["policy"] == _POL49
        and _PDIG49 == "6c278f264fc3c903f4b802d73a5d16f5f2406886d4d0fc3337265302ce7c766c"
        and _POL49["law"].startswith("A49-1")
        and _P49["label"] == "replay"
        and _P49["label-law"].lower().startswith("zero-network replay")),
    "input-verified": (
        len(_B49) == _P49["input"]["bytes"] == 925008
        and hashlib.sha256(_B49).hexdigest() == _P49["input"]["sha256"]
        == _P49["input"]["a48-recorded-sha256"]
        == "d45350ce045e5af55b0141f85099acac0ceea839b024e8c905bb986398546f8b"
        and _P49["input"]["digest-match"] is True),
    "zero-network": (
        _P49["zero-network"]["searches"] == 0
        and _P49["zero-network"]["fetches"] == 0
        and _P49["zero-network"]["network-requests"] == 0
        and _P49["zero-network"]["source-reads"] == 0
        and _P49["zero-network"]["link-follows"] == 0
        and _P49["zero-network"]["alternate-bodies"] == 0
        and _P49["zero-network"]["substitutions"] == 0
        and _P49["zero-network"]["ledger-before"] == 0
        and _P49["zero-network"]["ledger-after"] == 0),
    "mapping-replays-exactly": (
        all(_MAP49[k]["sup"]["href"] == _P49["mappings"][k]["sup"]["href"]
            and _MAP49[k]["sup"]["sup-id"] == _P49["mappings"][k]["sup"]["id"]
            and _MAP49[k]["sup"]["pos"] == _P49["mappings"][k]["sup"]["document-position"]
            and _MAP49[k]["entry"]["li-start"] == _P49["mappings"][k]["target"]["li-start"]
            and _MAP49[k]["entry"]["li-end"] == _P49["mappings"][k]["target"]["li-end"]
            and hashlib.sha256(_MAP49[k]["entry"]["raw"].encode()).hexdigest()
            == _P49["mappings"][k]["target"]["raw-sha256"]
            and _MAP49[k]["entry"]["text"] == _P49["mappings"][k]["entry-text"]
            and k in _P49["mappings"])
        for k in ("1", "2", "3")),
    "no-numeric-id-assumption": (
        _P49["mappings"]["1"]["sup"]["href"] == "#cite_note-FOOTNOTELe201030-1"
        and _P49["mappings"]["1"]["sup"]["href"] != "#cite_note-1"
        and _P49["mappings"]["1"]["target"]["fragment-id"] == "cite_note-FOOTNOTELe201030-1"
        and "NOT used" in _P49["structure"]["numeric-id-assumption"]),
    "acceptance-success": (
        _P49["acceptance"].startswith("SUCCESS")
        and "3 of 3" in _P49["acceptance"]
        and _P49["structure"]["candidates-per-marker"] == {"1": 1, "2": 1, "3": 1}),
    "bibliography-classified-from-own-words": (
        _P49["bibliographic"]["1"]["class"] == "UNCLEAR"
        and _P49["bibliographic"]["1"]["completeness"] == "PARTIAL"
        and _P49["bibliographic"]["2"]["class"] == "SECONDARY-SCHOLARSHIP"
        and _P49["bibliographic"]["2"]["completeness"] == "COMPLETE"
        and _P49["bibliographic"]["3"]["class"] == "SECONDARY-SCHOLARSHIP"
        and _P49["bibliographic"]["3"]["completeness"] == "COMPLETE"
        and _P49["bibliographic"]["3"]["isbn"] == "9788131711200"),
    "no-visible-connection-to-c": (
        len(_P49["comparisons"]) == 12
        and all(r["class"] == "NO-VISIBLE-CONNECTION" for r in _P49["comparisons"])
        and _P49["connection-summary"]["explicit-shared-reference"] == 0
        and _P49["connection-summary"]["possible-shared-derivation"] == 0
        and sum(1 for r in _P49["comparisons"]
                if r["entry-completeness"] != "COMPLETE") == 4
        and all(r["work-level"].startswith("UNRESOLVED")
                for r in _P49["comparisons"] if r["marker"] == "[1]")),
    "distinct-not-independence": (
        _P49["provenance"]["updated-class"] == "DISTINCT-STATED-ATTRIBUTIONS"
        and "DISJOINT" in _P49["provenance"]["why"]
        and "NOT independence" in _P49["provenance"]["no-independence"]
        and _P49["provenance"]["A47-unchanged"].startswith("A47's recorded class stands")
        and _P49["provenance"]["A48-unchanged"].startswith("A48's FAILED acceptance stands")
        and _P49["independence"]["assessment"] == "UNKNOWN"
        and _P49["independence"]["promoted"] is False
        and "UNDIFFERENTIATED" in _P49["independence"]["four-propositions"]),
    "carry-over-unchanged": (
        _P49["carry-over"]["a46"].startswith("UNCHANGED")
        and _P49["carry-over"]["a47"].startswith("UNCHANGED")
        and _P49["carry-over"]["a48"].startswith("UNCHANGED")
        and _P49["carry-over"]["ladder"].startswith("DIVERSITY-ONLY")
        and _P49["carry-over"]["semantic"].startswith("UNKNOWN")),
    "limits-recorded": (
        len(_P49["limitations"]) == 4
        and any("author-year footnote" in x for x in _P49["limitations"])),
    "replay-makes-no-network-call": _L049 == _L149,
    "history-whole": (
        _sig44("research-hold/a48-reference-read.json", "a48-manifest.sha256")
        and _sig44("research-hold/a47-provenance.json", "a47-manifest.sha256")
        and _sig44("research-hold/a46-compare.json", "a46-manifest.sha256")
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
expect("T202 A49: THE PRESERVED-BODY CITATION REPLAY (ZERO network - the LEDGER "
       "is unmoved before and after): the CONTRACT is the source (digest "
       "recomputed from its block) and it was committed BEFORE PARSING; the "
       "INPUT is A48's exact 925,008-byte body at its FULL recorded digest and "
       "the digests MATCH; the mapping follows the ACTUAL DOM - each marker's "
       "own superscript -> its LITERAL href -> the element carrying that exact "
       "fragment id -> its enclosing li - with NO id constructed from the "
       "marker number (marker [1] rides '#cite_note-FOOTNOTELe201030-1', which "
       "a '#cite_note-1' guess would have MISSED), all three resolving exactly "
       "as recorded (one candidate each, raw li HTML and normalized text "
       "replayed at their digests); acceptance is SUCCESS (3 of 3); the entries "
       "are classified ONLY from their own words (Le 2010 = PARTIAL/UNCLEAR "
       "author-year note; Olivelle 2024 and Singh 2008 = COMPLETE SECONDARY "
       "scholarship); NO connection to C's four signals is visible (12 rows, "
       "UNRESOLVED at work level for the PARTIAL [1]); the updated class is "
       "DISTINCT-STATED-ATTRIBUTIONS with DISJOINT named sets - explicitly NOT "
       "independence (UNKNOWN, not promoted, four propositions still "
       "undifferentiated); A47 and A48 stand UNCHANGED, the DIVERSITY-ONLY "
       "ladder carries over, the config sha is untouched, the HISTORY stands "
       "whole, and the charter rides UNTOUCHED at file AND mirror",
       _T202,
       why=lambda tr: ([] if all(tr.values()) else
                       [str(sorted(k for k, v in tr.items() if not v))]))
