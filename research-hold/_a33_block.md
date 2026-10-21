
# ---------------- A33: the loop PROPOSES the bound (adds) ------------------
# The founder's HAND (the filled number) moves into the CONTRACT (the word
# "AUTO"); a PURE propose derives the number from the trusted count ALONE;
# the APPLICATION grows the sharpest eye the A-series has needed - the ROAD
# SPEAKS its own cap word. T179 pins the PURE law at MANY counts (never the
# one answer 22); T180 rides the THREE applications and WHOLE SYNTHETIC AUTO
# LAPS; T181 re-thinks A33's live bytes and proves A31-era bytes CANNOT
# propose (history reads as history, never rewritten). The decision
# VOCABULARY rides UNMOVED.
_POL33 = json.loads(open("a33-contract.json").read())["auto_rule"]
_CRIT33 = json.loads(open("a33-contract.json").read())["criteria"]


def _ctl33(**kw):
    r = {"label": "live", "finish_src": "reported",
         "completion_tokens": 66}
    r.update(kw)
    return r


_T179 = {}
for _nm33, _t33, _capx, _want in (
        ("sixty-six", 66, 1024, 22),      # the CONTINUITY, not the point
        ("floor-of", 61, 1024, 20),       # the FLOOR: 20.33 -> 20
        ("floor-at", 24, 1024, 8),        # the raw sits ON the floor
        ("floor-under", 20, 1024, 8),     # 6 would seat UNDER the floor
        ("floor-above", 27, 1024, 9),     # the raw just above the floor
        ("clamp-at", 66, 22, None),       # candidate == cap: NOT strictly
        ("clamp-under", 66, 10, None),    # clamped to the cap it found
        ("clamp-past", 66, 23, 22)):      # one token of ROOM
    _p33 = loop.propose(_POL33, _capx, _ctl33(completion_tokens=_t33))
    _T179[_nm33] = (_p33["candidate"]
                     if _p33["proposal"] == "PROPOSED" else None)
_T179["at-cap"] = loop.propose(_POL33, 22, _ctl33())
_T179["rejects"] = {
    _k: loop.propose(_POL33, 1024, _ctl33(**_over))["why"]
    for _k, _over in (
        ("missing", {"completion_tokens": None}),
        ("unreported", {"finish_src": "absent"}),
        ("replay-lie", {"label": "replay"}),
        ("negative", {"completion_tokens": -5}),
        ("str", {"completion_tokens": "many"}),
        ("bool", {"completion_tokens": True}),
        ("zero", {"completion_tokens": 0}))}
_T179["independent"] = (
    loop.propose(_POL33, 1024, _ctl33(completion_tokens=66,
                                      answer_len=999,
                                      wall_ms=9000))["candidate"],
    loop.propose(_POL33, 1024, _ctl33(completion_tokens=66,
                                      answer_len=3,
                                      wall_ms=100))["candidate"])
_T179["inputs"] = loop.propose(_POL33, 1024, _ctl33())["inputs"]
_T179["flags"] = (loop.propose(_POL33, 1024,
                               _ctl33(completion_tokens=20))["floor_hit"],
                  loop.propose(_POL33, 1024, _ctl33())["why"])

expect("T179 THE PROPOSAL IS A PURE TABLE AT MANY COUNTS (synthetic - and "
       "PINNED AT SEVERAL numbers, not the one answer 22): the A33-1 law "
       "min(cap, max(8, T//3)) speaks 22 at 66, FLOORS at 61 (20), seats ON "
       "the floor at 24 (8), RISES to the floor's shield at 20 (8) and "
       "above it at 27 (9), REFUSES at cap==candidate and at a clamp that "
       "reaches the cap it found (a bound, never a wish - and the found "
       "number still RIDES the record at 22), and finds room at one token "
       "of room (23 caps 22). TRUST comes FIRST: a missing count, an "
       "UNREPORTED src, a REPLAY label wearing a live coat, a NEGATIVE, a "
       "STR (the str truthiness that would otherwise SEAT at the floor!), "
       "a BOOL masquerading as a count, and a ZERO all answer NO-PROPOSAL "
       "at a NON-EMPTY word - and a PROPOSAL carries an EMPTY why; the "
       "candidate rides the COUNT ALONE (999 chars at 9000ms and 3 at 100 "
       "propose the SAME 22); and the INPUTS are RECORDED (count, "
       "effective cap, floor, divisor - the arithmetic auditable at bytes, "
       "the floor_hit and clamped flags honest about which shield seated)",
       _T179,
       why=lambda tr: ([] if (
           tr["sixty-six"] == 22 and tr["floor-of"] == 20
           and tr["floor-at"] == 8 and tr["floor-under"] == 8
           and tr["floor-above"] == 9
           and tr["clamp-at"] is None and tr["clamp-under"] is None
           and tr["clamp-past"] == 22
           and tr["at-cap"]["proposal"] == "NO-PROPOSAL"
           and tr["at-cap"]["candidate"] == 22
           and tr["at-cap"]["clamped"] is True
           and all((("no completion-token word" in tr["rejects"]["missing"])
                    or ("not a count" in tr["rejects"]["missing"])))
           and "REPORTED" in tr["rejects"]["unreported"]
           and "TRUSTED" in tr["rejects"]["replay-lie"]
           and all("not a count" in tr["rejects"][k]
                   for k in ("negative", "str", "bool", "zero"))
           and tr["independent"] == (22, 22)
           and tr["inputs"] == {"completion_tokens": 66,
                                 "effective_cap": 1024,
                                 "floor": 8, "divisor": 3}
           and tr["flags"][0] is True and tr["flags"][1] is True
           and tr["flags"][2] == "")
       else ["the table leaned on one number, trust came AFTER the "
             "arithmetic, a word was missing, or the inputs did not ride"]))


def _rec33(after, **over):
    r = {"label": "injected", "code": 200, "wall_ms": 3000,
         "lane": "general", "general_note": None,
         "fires": ["INTENT:shelf-silent", "GENERAL:UNSOURCED"],
         "finish": "stop", "finish_src": "reported",
         "completion_tokens": 66, "max_tokens": 1024}
    r.update({"max_tokens": 22 if after else 1024} if after else {})
    r.update(over)
    return r


_T180 = {}
import tempfile
with tempfile.TemporaryDirectory() as _td33:
    import os as _os33
    import json as _json33
    # the temp pile's OWN auto-contract: the SAME law, trust WIDENED to the
    # injected word (a synthetic control is a synthetic control), trials 2
    _doc33 = _json33.load(open("a33-contract.json"))
    _doc33["auto_rule"]["trust_labels"] = ["live", "injected"]
    _doc33["trials_per_side"] = 2
    _cp33 = _os33.path.join(_td33, "contract.json")
    _json33.dump(_doc33, open(_cp33, "w"))
    _PRIOR33 = _json33.dumps({"MAXTOK": 4096}, indent=2)

    def _lap33(nm, after_mak):
        p = _os33.path.join(_td33, nm + ".json")
        open(p, "w").write(_PRIOR33)

        def m(n, q):
            if _json33.loads(open(p).read()).get("GENERAL_MAXTOK") is None:
                return [_rec33(False) for _ in range(n)]
            return [after_mak() for _ in range(n)]
        return loop.run_lap(contract_path=_cp33, cfg_path=p, measure=m,
                            hold_name=nm + "-art.json", hold_to=_td33)

    _cut = _lap33("cut", lambda: _rec33(True, lane=None,
                                        general_note="mouth-fell-back",
                                        finish="length",
                                        completion_tokens=22,
                                        fires=["INTENT:shelf-silent"]))
    _keep = _lap33("keep", lambda: _rec33(
        True, completion_tokens=20))
    _stale = _lap33("stale", lambda: _rec33(True, max_tokens=4096))
    _T180["cut"] = {
        "outcome": _cut["outcome"],
        "application_all_three": all(_cut["application"].values()),
        "decision": _cut["decision"]["decision"],
        "rolled": _cut.get("rolled_back"), "verified": _cut.get(
            "restoration_verified"),
        "bytes-exact": open(_os33.path.join(_td33, "cut.json")).read()
                       == _PRIOR33,
        "word-after": _cut["word_effective_after"]}
    _T180["keep"] = {
        "outcome": _keep["outcome"],
        "no-rollback": "rolled_back" not in _keep,
        "word-after": _keep["word_effective_after"],
        "file-carries": _json33.loads(open(_os33.path.join(
            _td33, "keep.json")).read()).get("GENERAL_MAXTOK")}
    _T180["stale"] = {
        "outcome": _stale["outcome"],
        "road-said-no": _stale["application"]["road"] is False,
        "file-mirror-still-true": (_stale["application"]["file"] is True
                                   and _stale["application"]["mirror"]),
        "decision-forced": _stale["decision"]["decision"],
        "word-in-rationale": any("did not RIDE" in w for w in
                                 _stale["decision"]["rationale"]),
        "rolled": _stale.get("rolled_back")}
# the MIRROR's own rail, in ISOLATION (the real mirror, NO file write):
stages.CONFIG["GENERAL_MAXTOK"] = 33
_diverged = stages.CONFIG.get("GENERAL_MAXTOK")
stages.reload_config()
_T180["mirror"] = {"diverged": _diverged,
                   "reloaded": stages.CONFIG.get("GENERAL_MAXTOK")}

expect("T180 THE APPLICATION IS THREE PROOFS OR IT IS NOTHING (synthetic "
       "laps at the REAL entry with the injected mouth, plus the mirror's "
       "own rail): a CUT leg comes home APPLIED-then-ROLLED-BACK (answered "
       "honestly) with the file, the mirror-read, and the ROAD-WORD all "
       "true, the exact PRIOR BYTES back, and the fallback word standing; "
       "a CLEAN-STOP leg is KEPT at the candidate (the kept candidate "
       "RIDES the file - what is refused does not persist, what is KEPT "
       "does) and carries NO rollback word at all; a STALE leg (the road "
       "spoke the OLD word where the file and the mirror agreed) is "
       "ROLLED BACK by the A33 word INSIDE the rationale - the A31/SISTER "
       "class CAUGHT by a WORD, not by an after-the-fact token count; and "
       "the MIRROR rail in isolation: a diverged in-memory word (33, no "
       "file touch) is RESTORED to the file's truth (1024) by the reload "
       "- file-first, mirror-follows, at the real charter",
       {**{"%s-%s" % (a, b): v for a, d in
           (("cut", _T180["cut"]), ("keep", _T180["keep"]),
            ("stale", _T180["stale"])) for b, v in d.items()},
        "mirror-diverged": _T180["mirror"]["diverged"],
        "mirror-reloaded": _T180["mirror"]["reloaded"]},
       why=lambda tr: ([] if (
           tr["cut-outcome"] == ("APPLIED then ROLLED BACK (the lap "
                                "answered honestly)")
           and tr["cut-application_all_three"] is True
           and tr["cut-decision"] == "ROLLBACK"
           and tr["cut-rolled"] is True and tr["cut-verified"] is True
           and tr["cut-bytes-exact"] and tr["cut-word-after"] == 4096
           and tr["keep-outcome"] == ("APPLIED (the verdict rode - the "
                                      "candidate is the kept word)")
           and tr["keep-no-rollback"] is True
           and tr["keep-word-after"] == 22
           and tr["keep-file-carries"] == 22
           and tr["stale-outcome"] == ("APPLIED then ROLLED BACK (the "
                                       "road rode no such word)")
           and tr["stale-road-said-no"] is True
           and tr["stale-file-mirror-still-true"] is True
           and tr["stale-decision-forced"] == "ROLLBACK"
           and tr["stale-word-in-rationale"] is True
           and tr["stale-rolled"] is True
           and tr["mirror-diverged"] == 33
           and tr["mirror-reloaded"] == 1024)
       else ["an application leg fused, persisted wrongly, or the mirror "
             "rail did not ride the file's truth"]))

_A33 = json.loads(open("research-hold/a33-evidence.json").read())
_A31R = json.loads(open("research-hold/a31-evidence.json").read())
_A33V = loop.decide(_A33["before"], _A33["after"], _CRIT33)
_T181 = {
    "replay": _A33V["decision"],
    "recorded": _A33["decision"]["decision"],
    "medians-match": (_A33V["medians_ms"]
                      == _A33["decision"]["medians_ms"]),
    "all-live": all(r.get("label") == "live"
                    for r in _A33["before"] + _A33["after"]),
    "chain": (_A33["proposal"]["proposal"] == "PROPOSED"
              and _A33["proposal"]["candidate"]
              == min(1024, max(8, _A33["before"][0]["completion_tokens"]
                               // 3))
              and _A33["proposal"]["inputs"]["completion_tokens"]
              == _A33["before"][0]["completion_tokens"]
              and all(r.get("max_tokens") == _A33["proposal"]["candidate"]
                      for r in _A33["after"])),
    "application-bytes": all(_A33["application"].values()) is True,
    "final-state": (loop.effective_word(loop.read_cfg(), "GENERAL_MAXTOK")
                    == stages.CONFIG.get("GENERAL_MAXTOK")
                    == 1024
                    and _A33.get("rolled_back") is True
                    and _A33.get("restoration_verified") is True),
    "a31-bytes-cannot": (loop.propose(
        _POL33, 1024, _A31R["before"][0])["proposal"],
        "NO-PROPOSAL"),
    "words": (_A33["word_effective_before"],
              _A33["word_effective_after"]),
}

expect("T181 THE CHAIN READS AT BYTES AND HISTORY STAYS HISTORY (replay, "
       "zero live calls): the held A33 bytes speak the WHOLE chain - "
       "PROPOSED from the control's OWN reported count (the proposal's "
       "inputs ARE the first record's count; the candidate IS min(1024, "
       "max(8, T//3)) of THAT count - the number the loop found, not the "
       "number A32 hand-filled, and the arithmetic RE-DERIVABLE here at "
       "zero cost); every after-trial's ROAD-WORD is the candidate (the "
       "application proven at the held live records); the application dict "
       "is TRUE at all three places AT BYTES; re-deciding the held records "
       "at the A33 eyes speaks the SAME word and the SAME medians; the "
       "final charter reads 1024 at the FILE and at the MIRROR AGREEING, "
       "with rolled_back and restoration_verified TRUE at bytes; and "
       "A31's held control record - no finish_src, no token word - cannot "
       "PROPOSE at the A33 law (NO-PROPOSAL: history reads as history, no "
       "witness REWRITTEN to flatter the new code); and the held words "
       "still read 1024 -> 1024",
       _T181,
       why=lambda tr: ([] if (
           tr["replay"] == tr["recorded"]
           and tr["replay"] in ("APPLIES-HOLDS", "ROLLBACK")
           and tr["medians-match"] and tr["all-live"]
           and tr["chain"] is True
           and tr["application-bytes"] is True
           and tr["final-state"] is True
           and tr["a31-bytes-cannot"] == ("NO-PROPOSAL", "NO-PROPOSAL")
           and tr["words"] == (1024, 1024))
       else ["the chain broke at bytes, the replay stopped matching, the "
             "final state and the verdict disagreed, or history tried to "
             "propose"]))

