# ---------------- A46: held-source claim comparison, replayed (adds) ----------------
_P46 = json.loads(open("research-hold/a46-compare.json").read())
_A42b = json.loads(open("research-hold/a42-duel.json").read())
_A44b = json.loads(open("research-hold/a44-read.json").read())
_W46 = _A42b["reads"]["results"][0]
_C46 = _A44b["read"]["packet"]["results"][0]
def _policy46():
    import re
    txt = open("a46-contract.md").read()
    m = re.search(r"<!-- A46-POLICY -->(.*?)<!-- /A46-POLICY -->", txt, re.S)
    pol = json.loads(m.group(1))
    return (pol, hashlib.sha256(json.dumps(pol, sort_keys=True)
                                .encode()).hexdigest(), txt)
def _tokens46(text, pol):
    import re, unicodedata
    stop = set(pol["normalization"]["stopword-list"])
    var = pol["normalization"]["variant-map"]
    s = unicodedata.normalize("NFKC", text).casefold()
    out = []
    for m in re.finditer(pol["normalization"]["token-regex"], s):
        t = var.get(m.group(0), m.group(0))
        if t not in stop:
            out.append(t)
    return out
def _measure46(A, B, topic=None):
    if topic is not None:
        A = [t for t in A if t not in topic]
        B = [t for t in B if t not in topic]
    sa, sb = set(A), set(B)
    inter = sa & sb
    mult = sum((__import__("collections").Counter(A) &
                __import__("collections").Counter(B)).values())
    return {"types-shared": len(inter), "types-A": len(sa), "types-B": len(sb),
            "multiset-shared": mult,
            "jaccard": round(len(inter)/len(sa | sb), 4),
            "dice": round(2*len(inter)/(len(sa)+len(sb)), 4)}
_L046 = web_research.LEDGER[0]
_POL46, _PDIG46, _CTXT46 = _policy46()
_TP46 = set(_POL46["overlap"]["topic-terms"])
_A46 = _tokens46(_W46["text"], _POL46)
_B46 = _tokens46(_C46["text"], _POL46)
_F46 = _measure46(_A46, _B46)
_N46 = _measure46(_A46, _B46, _TP46)
_OUT46 = {"AGREEMENT", "CONFLICT", "PARTIAL", "INDETERMINATE", "NO-MATCH"}
_EX46 = {c["id"]: c for c in _P46["claims"]["W"] + _P46["claims"]["C"]}
def _exok46():
    src = {"W": _W46["text"], "C": _C46["text"]}
    for c in _P46["claims"]["W"] + _P46["claims"]["C"]:
        s, e = c["offset"]
        if src[c["source"]][s:e] != c["excerpt"]:
            return False
    return True
_PAIRS46 = [p for p in _P46["comparisons"]]
_L146 = web_research.LEDGER[0]
_T491 = {
    "policy-frozen": (
        _PDIG46 == _P46["policy-digest"] and _PDIG46 in _CTXT46
        and _P46["policy"] == _POL46
        and _PDIG46 == "cef965bf784ec22010dec93cdc68582a96a6fe05ec2ceb6f338d896ee1bf796b"
        and _POL46["law"].startswith("A46-1")),
    "evidence-verified": (
        _POL46["sources"]["W"]["text-sha256"]
        == hashlib.sha256(_W46["text"].encode()).hexdigest()
        and _POL46["sources"]["C"]["text-sha256"]
        == hashlib.sha256(_C46["text"].encode()).hexdigest()
        and _POL46["sources"]["W"]["chars"] == len(_W46["text"]) == 1200
        and _POL46["sources"]["C"]["chars"] == len(_C46["text"]) == 1200
        and _POL46["sources"]["W"]["publisher"] == "wikipedia.org"
        and _POL46["sources"]["C"]["publisher"] == "colostate.edu"
        and _P46["boundary"]["extraction-cap"] == 1200),
    "overlap-replays": (
        _F46["types-shared"] == _P46["overlap"]["all-content"]["types-shared"] == 20
        and _F46["types-A"] == 101 and _F46["types-B"] == 103
        and _F46["jaccard"] == _P46["overlap"]["all-content"]["jaccard"] == 0.1087
        and _F46["dice"] == _P46["overlap"]["all-content"]["dice"] == 0.1961
        and _F46["multiset-shared"] == _P46["overlap"]["all-content"]["multiset-shared"] == 24
        and _N46["types-shared"] == _P46["overlap"]["minus-topic-terms"]["types-shared"] == 11
        and _N46["types-A"] == 85 and _N46["types-B"] == 90
        and _P46["overlap"]["all-content"]["bigrams"]["shared"] == 2
        and _P46["overlap"]["all-content"]["trigrams"]["shared"] == 0
        and _P46["overlap"]["minus-topic-terms"]["trigrams"]["shared"] == 1
        and _P46["overlap"]["all-content"]["floor-met"] is True),
    "claims-auditable": (
        _exok46() and _P46["claims"]["layer"].startswith("ANALYST JUDGMENT")
        and _P46["claims"]["counts"]["W"] == 11
        and _P46["claims"]["counts"]["C"] == 8
        and _P46["claims"]["counts"]["ambiguous"] == 1
        and _EX46["C-08"]["status"] == "AMBIGUOUS"
        and all(c["status"] in ("CLAIM", "AMBIGUOUS")
                for c in _P46["claims"]["W"] + _P46["claims"]["C"])
        and len(_EX46) == 19),
    "comparisons-frozen": (
        _P46["counts"] == {"agreement": 2, "conflict": 0, "partial": 2,
                           "indeterminate": 0, "no-match": 9,
                           "comparisons-total": 13}
        and all(p["outcome"] in _OUT46 for p in _PAIRS46)
        and [p["id"] for p in _PAIRS46 if p["outcome"] == "AGREEMENT"] == ["X1", "X2"]
        and all((p["left-excerpt"] or p["right-excerpt"]) for p in _PAIRS46)
        and _P46["claims"]["comparable-claims"] == 7
        and set(_P46["claims"]["comparable-claim-ids"])
        == {"W-01", "W-02", "W-04", "W-10", "C-01", "C-05", "C-06"}),
    "no-promotion": (
        _P46["independence"]["assessment"] == "UNKNOWN"
        and _P46["corroboration"]["ladder"].startswith("DIVERSITY-ONLY")
        and "corroborated" not in _P46["corroboration"]["ladder"].lower()
        and _P46["corroboration"]["claim-support"].startswith("CLAIM-AGREEMENT")
        and "NOT corroboration" in _P46["corroboration"]["claim-support"]
        and _P46["corroboration"]["conditions"]["4-genuine-independence"] == "UNKNOWN"),
    "ea1-unchanged": (
        _P46["ea1"]["changed"] is False
        and _P46["ea1"]["a42"].startswith("PARTIAL")
        and _P46["ea1"]["a43"].startswith("EVIDENCE-GAP")
        and _P46["ea1"]["a44"].startswith("EVIDENCE-GAP")),
    "semantic-unknown": _P46["semantic-improvement"].startswith("UNKNOWN"),
    "zero-budget-and-replay-label": (
        all(_P46["budget"][k] == 0 for k in ("searches", "network-requests",
            "source-reads", "new-evidence", "pdf-work", "substitutions"))
        and _P46["label"] == "replay"
        and "ZERO searches" in _P46["label-law"]),
    "limitations-recorded": (
        len(_P46["limitations"]) == 5
        and any("1200-char" in x for x in _P46["limitations"])
        and any("analyst judgment" in x for x in _P46["limitations"])),
    "replay-makes-no-network-call": _L046 == _L146,
    "history-whole": (
        _sig44("research-hold/a45-reclass.json", "a45-manifest.sha256")
        and _sig44("research-hold/a44-read.json", "a44-manifest.sha256")
        and _sig44("research-hold/a43-read.json", "a43-manifest.sha256")
        and _sig44("research-hold/a42-duel.json", "a42-manifest.sha256")
        and json.loads(open("research-hold/a37-probe.json").read())
        ["packets"]["EA1"]["a36-file-sha"]
        == hashlib.sha256(open("research-hold/a36-read-EA1.json",
                               "rb").read()).hexdigest()),
    "charter-untouched": (loop.read_cfg().get("GENERAL_MAXTOK")
                          == stages.CONFIG.get("GENERAL_MAXTOK") == 1024)}
expect("T199 HELD-SOURCE CLAIM COMPARISON AT ITS BYTES (ALL offline - ZERO "
       "searches, ZERO network, ZERO source reads, ZERO new evidence; both "
       "texts are the 1200-char extract WINDOWS): the CONTRACT is the source "
       "(digest recomputed from its own block) and both held sources VERIFY "
       "at their text digests; the DETERMINISTIC overlap REPLAYS exactly "
       "(20 shared content types of 101/103, Jaccard 0.1087, Dice 0.1961; "
       "with topic terms removed 11 of 85/90, Jaccard 0.0671 - the headline "
       "is TOPIC-INFLATED, and the floor is met); the CLAIM layer is declared "
       "ANALYST JUDGMENT and every excerpt is RE-LOCATABLE at its recorded "
       "offset (19 claims, 1 AMBIGUOUS excluded from comparison); the FROZEN "
       "rubric yields 2 AGREEMENT, 0 CONFLICT, 2 PARTIAL, 0 INDETERMINATE, 9 "
       "NO-MATCH over 13 comparison rows, with 7 distinct comparable claims "
       "and excerpts preserved on both sides; INDEPENDENCE is UNKNOWN (a "
       "domain difference is not independence) so the ladder stays "
       "DIVERSITY-ONLY and the claim-level word is explicitly NOT "
       "corroboration - NO promotion is made; EA1's classification is "
       "unchanged, semantic improvement stays UNKNOWN, the limitations "
       "(window truncation, analyst judgment, topic inflation, independence) "
       "ride recorded, the LEDGER is unmoved, the HISTORY stands whole "
       "(A45/A44/A43/A42 manifests, A36 at A37's word), and the charter "
       "rides UNTOUCHED at file AND mirror",
       _T491,
       why=lambda tr: ([] if all(tr.values()) else
                       [str(sorted(k for k, v in tr.items() if not v))]))
