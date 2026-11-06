# ---------------- A48: the W reference-window read, replayed (adds) ----------------
_P48 = json.loads(open("research-hold/a48-reference-read.json").read())
_B48 = open("research-hold/a48-w-body.html", "rb").read()
def _policy48():
    import re
    txt = open("a48-contract.md").read()
    m = re.search(r"<!-- A48-POLICY -->(.*?)<!-- /A48-POLICY -->", txt, re.S)
    pol = json.loads(m.group(1))
    return (pol, hashlib.sha256(json.dumps(pol, sort_keys=True)
                                .encode()).hexdigest(), txt)
def _container48(html):
    import re
    m = re.search(r'<ol[^>]*class="[^"]*\breferences\b[^"]*"[^>]*>', html)
    if not m:
        return None
    depth = 0; end = None
    for tag in re.finditer(r'<(/?)ol\b[^>]*>', html[m.start():]):
        depth += 1 if tag.group(1) == "" else -1
        if depth == 0:
            end = m.start() + tag.end(); break
    return (m.start(), end)
def _items48(html, span, n=3):
    import re
    cont = html[span[0]:span[1]]
    pos = [x.start() for x in re.finditer(r'<li\b[^>]*>', cont)]
    out = []
    for i, p in enumerate(pos, 1):
        nxt = pos[i] if i < len(pos) else len(cont)
        chunk = cont[p:nxt]
        idm = re.search(r'id="([^"]+)"', chunk[:300])
        text = re.sub(r"\s+", " ", web_research.extract(chunk, max_chars=20000,
                                                        thin=0)).strip()
        if i <= n:
            out.append({"item": i, "li-id": idm.group(1) if idm else None,
                        "raw-offset": span[0] + p, "text": text})
    return out, len(pos)
_L048 = web_research.LEDGER[0]
_POL48, _PDIG48, _CTXT48 = _policy48()
_HTML48 = _B48.decode("utf-8", "replace")
_SPAN48 = _container48(_HTML48)
_ITEMS48, _NLI48 = _items48(_HTML48, _SPAN48)
_L148 = web_research.LEDGER[0]
_AC48 = _P48["extraction"]["acceptance"].split()[0]
_T511 = {
    "policy-frozen": (
        _PDIG48 == _P48["policy-digest"] and _PDIG48 in _CTXT48
        and _P48["policy"] == _POL48
        and _PDIG48 == "ad93895836a27e5efe6b03e334f7ef82b8f85690f8f05a5e341d8e9d0b4652ce"
        and _POL48["law"].startswith("A48-1")
        and _P48["label"] == "live"),
    "one-request-recorded": (
        _P48["request"]["calls"] == 1
        and _P48["request"]["network-requests"] == 1
        and _P48["request"]["status"] == 200
        and _P48["request"]["content-type"] == "text/html"
        and _P48["request"]["url-final"] == _P48["request"]["url-requested"]
        == _POL48["url"] == "https://en.wikipedia.org/wiki/Edicts_of_Ashoka"
        and _P48["request"]["redirect"] is False
        and _P48["request"]["transport"] == "answered"
        and _P48["request"]["ledger-before"] == 0
        and _P48["request"]["ledger-after"] == 1
        and _P48["budget"]["retries"] == 0
        and _P48["budget"]["substitutions"] == 0
        and _P48["budget"]["link-follows"] == 0
        and _P48["budget"]["additional-reads"] == 0),
    "body-preserved-and-verified": (
        len(_B48) == _P48["request"]["body-bytes"] == 925008
        and hashlib.sha256(_B48).hexdigest() == _P48["request"]["body-sha256"]
        == "d45350ce045e5af55b0141f85099acac0ceea839b024e8c905bb986398546f8b"),
    "frozen-extraction-replays": (
        _SPAN48 is not None
        and _SPAN48[0] == _P48["extraction"]["container"]["raw-offset"]
        and _NLI48 == _P48["extraction"]["container"]["items-in-container"] == 4
        and [i["li-id"] for i in _ITEMS48]
        == [i["li-id"] for i in _P48["extraction"]["items"]]
        == ["cite_note-71", "cite_note-73", "cite_note-118"]
        and [i["text"] for i in _ITEMS48] == [i["text"] for i in _P48["extraction"]["items"]]),
    "outcome-recorded-honestly": (
        _AC48 == "FAILED"
        and _P48["extraction"]["outcome"] == "NONE-RESOLVED"
        and all(_P48["extraction"]["markers"][m]["resolved"] is False
                for m in ("1", "2", "3"))
        and "WINDOW-SELECTION defect" in " ".join(_P48["limitations"])
        and "no retry" in " ".join(_P48["limitations"])),
    "no-comparison-possible": (
        _P48["comparison"]["possible"] is False
        and set(_P48["comparison"]["classes"].values()) == {"UNRESOLVED"}
        and _P48["comparison"]["extracted-entries-vs-C"].startswith("NO-VISIBLE-CONNECTION")),
    "no-promotion": (
        _P48["provenance"]["classification"].startswith("ATTRIBUTION-CHAIN-INCOMPLETE")
        and _P48["provenance"]["independence"] == "UNKNOWN - not promoted; a visible bibliography would not have sufficed, and none was recovered"
        and "UNDIFFERENTIATED" in _P48["provenance"]["four-propositions"]),
    "carry-over-unchanged": (
        _P48["carry-over"]["a46"].startswith("UNCHANGED")
        and _P48["carry-over"]["a47"].startswith("UNCHANGED")
        and _P48["carry-over"]["ladder"].startswith("DIVERSITY-ONLY")
        and _P48["carry-over"]["semantic"].startswith("UNKNOWN")),
    "config-untouched": (
        hashlib.sha256(open("config.json", "rb").read()).hexdigest()
        == _POL48["restoration"]["pre-config-sha256"]
        == "0b23f30ae0c89f61080796ef7fcf04196ca384f2855efb07826ee6fb27a931d0"),
    "limits-recorded": (
        len(_P48["limitations"]) == 4
        and any("925,008-byte body" in x for x in _P48["limitations"])),
    "replay-makes-no-network-call": _L048 == _L148,
    "history-whole": (
        _sig44("research-hold/a47-provenance.json", "a47-manifest.sha256")
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
expect("T201 A48: THE W REFERENCE-WINDOW READ AT ITS BYTES (the ONE live "
       "request was spent; the REPLAY spends NONE): the CONTRACT is the "
       "source (digest recomputed from its block) and it was committed "
       "BEFORE the request; EXACTLY ONE call rode (one url, 200, text/html, "
       "no redirect, ledger 0->1) and the EXACT 925,008-byte body is "
       "PRESERVED at its digest; the FROZEN extraction rule replays exactly "
       "- the FIRST <ol class='references'> is a NOTES group (4 items, ids "
       "cite_note-71/-73/-118) so NONE of [1][2][3] resolved and the "
       "acceptance word is FAILED, recorded as a WINDOW-SELECTION defect, "
       "NOT a transport failure and NOT repaired with a second request; no "
       "comparison against C was possible, so every marker rides UNRESOLVED; "
       "the provenance class stays ATTRIBUTION-CHAIN-INCOMPLETE and "
       "independence stays UNKNOWN with the four propositions "
       "undifferentiated - NO promotion from a visible bibliography (none "
       "was even recovered); A46/A47 and the DIVERSITY-ONLY ladder carry "
       "over UNCHANGED; the config sha is untouched; the body makes a "
       "CORRECTED zero-network replay possible under a NEW contract; the "
       "LEDGER is unmoved by the replay, the HISTORY stands whole, and the "
       "charter rides UNTOUCHED at file AND mirror",
       _T511,
       why=lambda tr: ([] if all(tr.values()) else
                       [str(sorted(k for k, v in tr.items() if not v))]))
