
# ---------------- A39: the landing page, then the fork (adds) --------------
_P39 = json.loads(open("research-hold/a39-read.json").read())
_T38B = open("research-hold/a38-probe.json", "rb").read()
_sig39 = lambda p, man: (lambda want: want is not None and want ==
    hashlib.sha256(open(p, "rb").read()).hexdigest())(
        next((ln.split()[0] for ln in open(man)
              if ln.strip() and not ln.startswith("#")
              and ln.split()[1] == p), None))
_T391 = {
    "budget-honest": (_P39["budget-declared"]
                       == {"attempts": 1, "searches": 0}
                       and _P39["spent"]["search"] == 0
                       and _P39["spent"]["calls"] == 1
                       and _P39["spent"]["fetch"] == 1
                       and _P39["spent"]["ms"] > 0
                       and _P39["attempts-used"] == 1),
    "target-byte-exact": (_P39["target"]["url-BYTES"]
                          == json.loads(_T38B)["targets"]["EA5"]
                          ["read"]["final"]
                          and _P39["source-evidence"]["sha256"]
                          == hashlib.sha256(_T38B).hexdigest()),
    "digest-recomputes": (_P39["target"]["packet-digest-sha256"]
                          == hashlib.sha256(json.dumps(
                              json.loads(open(
                                  "research-hold/a35-six-final.json")
                                  .read())["cycles"]["EA5"]["stage-1"],
                              sort_keys=True).encode()).hexdigest()),
    "class-rederives": ((lambda err, tb: (
        "BLOCKED" if err and str(err).startswith("blocked:")
        else "FETCH-FAILURE" if err
        else "USABLE-CONTENT" if len(tb) >= 60
        else "EMPTY/NON-CONTENT") == _P39["class"])(
            _P39["read"]["error"], _P39["read"]["head-verbatim"])
        and _P39["read"]["status"] == 202
        and _P39["road-opened"] == 1),
    "fork-follows-law": (
        (_P39["class"] in ("EMPTY/NON-CONTENT", "FETCH-FAILURE")
         and _P39["fork"].startswith("BRANCH CLOSED"))
        or (_P39["class"] == "USABLE-CONTENT"
            and _P39["fork"].startswith("CONTENT RECORDED"))
        or (_P39["class"] == "BLOCKED"
            and _P39["fork"].startswith("BLOCKER PRINTED"))),
    "no-second-redirect": (_P39["read"]["final"] is None
                           and _P39["read"]["publisher"]
                           == web_research.provider_host()),
    "gaps-ride-as-words": (set(_P39["gaps-predeclared"])
                           == {"content-type", "body-count",
                               "redirect-chain"}),
    "prior-evidence-whole": (
        _sig39("research-hold/a38-probe.json", "a38-manifest.sha256")
        and json.loads(open("research-hold/a37-probe.json").read())
        ["packets"]["EA1"]["a36-file-sha"]
        == hashlib.sha256(open("research-hold/a36-read-EA1.json",
                               "rb").read()).hexdigest()),
    "charter-untouched": (loop.read_cfg().get("GENERAL_MAXTOK")
                          == stages.CONFIG.get("GENERAL_MAXTOK")
                          == 1024)}
expect("T192 THE LANDING PAGE'S DISPOSITION (live read, replayed at the "
       "held bytes, the net UNTOUCHED by this test): the budget was "
       "DECLARED 1 attempt and ZERO searches and the ACTIVITY EQUALS the "
       "words at the road's OWN spent; the target rides BYTE-EXACT to the "
       "A38 held FINAL word (the no-reconstruction law PINNED, the source "
       "evidence RE-SIGNED) and the packet digest RE-COMPUTES from the "
       "immutable record; the CLASS RE-DERIVES from the held road-words at "
       "the FROZEN law alone (202, no error, ZERO extracted bytes -> "
       "EMPTY/NON-CONTENT - a STATUS is NOT content at this line's own "
       "law); the FORK WORD FOLLOWS the class at the PREDECLARED rule "
       "(BRANCH CLOSED - the stub-family is proven NON-CONTENT BY "
       "CONSTRUCTION, the twelve stub-rows ride untested BY LAW not by "
       "taste, the branch re-opens only for GENUINELY NEW evidence); the "
       "landing answered ON THE SPOT (no second redirect, the house word "
       "at the publisher) - the 202-and-empty is the ENDPOINT'S OWN WORD, "
       "not a chain's; the three GAPS ride AS WORDS (no silence at the "
       "road's face); the PRIOR evidences stand WHOLE (A38's record "
       "re-signs at its OWN manifest, A36's witness at A37's stored word); "
       "and the charter rides UNTOUCHED at file AND mirror",
       _T391,
       why=lambda tr: ([] if all(tr.values()) else
                       [str(sorted(k for k, v in tr.items()
                                    if not v))]))
