
# ---------------- A32: the bound becomes OBSERVABLE (adds) -----------------
# The finish word, the token words, the source words - at the trace, at the
# records, in the table. T176 is SYNTHETIC fixtures at the call mouth (a
# canned endpoint, zero live bytes); T177 is the SYNTHETIC table and a
# WHOLE injected lap at the new clause; T178 is the REPLAY of A32's held
# live bytes (a replay never wears live's clothes). The transport law
# (A28/T167), the raise law (T125) and the mumble lanes (A29) ride UNMOVED.
import urllib.request as _UR32

_CRIT32 = json.loads(open("a32-contract.json").read())["criteria"]


def _raw32(**ch_kw):
    import json as _j
    msg = {"content": '{"knows": true, "node": "The strip rides.", '
                       '"verbs": ["CLAIM"]}', "reasoning_content": ""}
    ch = {"message": msg}
    ch.update({k: v for k, v in ch_kw.items() if k != "no_usage"})
    doc = {"choices": [ch]}
    if not ch_kw.get("no_usage"):
        doc["usage"] = {"completion_tokens": 66, "prompt_tokens": 816,
                        "total_tokens": 882}
    return _j.dumps(doc).encode()


class _Resp32:
    def __init__(self, payload):
        self._p = payload

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False

    def read(self):
        return self._p


def _canned32(payload):
    def fake(req, *a, **kw):
        return _Resp32(payload)
    return fake


_T176 = {}
_SC32 = stages.call
_UR_SAVE = _UR32.urlopen
try:
    _UR32.urlopen = _canned32(_raw32(finish_reason="stop"))
    _T176["done"] = stages.call("s", "u")
    _UR32.urlopen = _canned32(_raw32(finish_reason="length"))
    _T176["cut"] = stages.call("s", "u")
    _UR32.urlopen = _canned32(_raw32(no_usage=True))
    _T176["no-meta"] = stages.call("s", "u")
    _UR32.urlopen = _canned32(
        b'{"choices": [{"message": {"content": "x"}, '
        b'"finish_reason": "aborted"}]}')
    _T176["weird-word"] = stages.call("s", "u")

    def _boom32(req, *a, **kw):
        raise OSError("the socket fell over")
    _UR32.urlopen = _boom32
    _T176["mouth-error"] = stages.call("s", "u")
finally:
    _UR32.urlopen = _UR_SAVE

_FAKE32 = {}


def _fake32(out):
    def f(*a, **kw):
        return out
    return f


_TR32A = {"stages_ms": {}}
stages.call = _fake32({"content": "x", "reasoning": "", "truncated": False,
                       "finish_reason": "stop", "finish_src": "reported",
                       "tokens_src": "reported", "completion_tokens": 66})
stages.general_exit(_TR32A, _F29M, True)
_T176["trace-reported"] = {k: _TR32A.get(k) for k in (
    "general_finish", "general_finish_src", "general_tokens_src",
    "general_completion_tokens")}
_TR32B = {"stages_ms": {}}
stages.call = _fake32({"content": "not json at all", "reasoning": "",
                       "truncated": False})
stages.general_exit(_TR32B, _F29M, True)
_T176["trace-double"] = {k: _TR32B.get(k) for k in (
    "general_finish", "general_finish_src", "general_note")}
stages.call = _SC32

expect("T176 THE ENDPOINT'S OWN WORDS RIDE OUT AND UP (synthetic fixtures, "
       "a canned mouth, ZERO live bytes): a completed call carries "
       "finish_reason=stop REPORTED with the usage trio at their numbers; "
       "a cut carries finish_reason=length REPORTED and the A29 truncated "
       "bit still speaks IT (the one admitted inference, UNMOVED); a "
       "completion with NO metadata says finish_src=absent, "
       "tokens_src=absent, finish_reason=None and NO token key at all - "
       "UNKNOWN is UNKNOWN, never a fabricated stop and never an "
       "inference from a short answer or the configured cap; a word the "
       "house has never seen (aborted) rides RAW (surfacing does not "
       "translate); the [MOUTH ERROR] shape (the transport's own last word "
       "- T167's and T125's laws UNMOVED) carries its words as absent; "
       "and at the general seam the words ride the TRACE (general_finish, "
       "the *_src words, the token words) - a reporting double's words all "
       "arrive, a plain content-only double (the A29/A30-era shape) speaks "
       "None-with-absent, NEVER a guess, and its lane-word rides beside "
       "them untouched",
       _T176,
       why=lambda tr: ([] if (
           tr["done"].get("finish_reason") == "stop"
           and tr["done"].get("finish_src") == "reported"
           and tr["done"].get("completion_tokens") == 66
           and tr["cut"].get("finish_reason") == "length"
           and tr["cut"].get("truncated") is True
           and tr["cut"].get("finish_src") == "reported"
           and tr["no-meta"].get("finish_src") == "absent"
           and tr["no-meta"].get("tokens_src") == "absent"
           and tr["no-meta"].get("finish_reason") is None
           and "completion_tokens" not in tr["no-meta"]
           and tr["weird-word"].get("finish_reason") == "aborted"
           and tr["weird-word"].get("tokens_src") == "absent"
           and tr["mouth-error"]["content"].startswith("[MOUTH ERROR")
           and tr["mouth-error"].get("finish_src") == "absent"
           and tr["trace-reported"]["general_finish"] == "stop"
           and tr["trace-reported"]["general_finish_src"] == "reported"
           and tr["trace-reported"]["general_completion_tokens"] == 66
           and tr["trace-double"]["general_finish"] is None
           and tr["trace-double"]["general_finish_src"] == "absent"
           and tr["trace-double"]["general_note"] == "mouth-fell-back")
       else ["a word was invented, translated, lost between seams, or the "
             "unknown failed to stay unknown"]))


def _rec32(**kw):
    r = {"label": "synthetic", "code": 200, "wall_ms": 3000,
         "lane": "general", "general_note": None,
         "fires": ["INTENT:shelf-silent", "GENERAL:UNSOURCED"],
         "finish": "stop", "finish_src": "reported",
         "completion_tokens": 60}
    r.update(kw)
    return r


_T177 = {}
_T177["clean"] = loop.decide([_rec32()], [_rec32()], _CRIT32)
_T177["cut-parses"] = loop.decide(
    [_rec32()], [_rec32(finish="length", completion_tokens=22)], _CRIT32)
_T177["cut-lanes"] = loop.decide(
    [_rec32()],
    [_rec32(lane=None, general_note="mouth-fell-back", finish="length",
            completion_tokens=22)], _CRIT32)
_T177["a31-shape"] = loop.decide(
    [{"label": "synthetic", "code": 200, "wall_ms": 3000, "lane": "general",
      "general_note": None, "fires": ["GENERAL:UNSOURCED"]}] * 2,
    [{"label": "synthetic", "code": 200, "wall_ms": 3000, "lane": "general",
      "general_note": None, "fires": ["GENERAL:UNSOURCED"]}] * 2,
    _CRIT32)
_T177["unknown-word"] = loop.decide(
    [_rec32()], [_rec32(finish=None, finish_src="absent",
                        completion_tokens=None)], _CRIT32)

import tempfile
_T177["lap"] = {}
with tempfile.TemporaryDirectory() as _td32:
    import os as _os32
    _p32 = _os32.path.join(_td32, "cfg.json")

    def _mk32(**over):
        r = {"label": "injected", "code": 200, "wall_ms": 3000,
             "lane": "general", "general_note": None,
             "fires": ["INTENT:shelf-silent", "GENERAL:UNSOURCED"],
             "finish": "stop", "finish_src": "reported",
             "completion_tokens": 60}
        r.update(over)
        return r

    def _meas32_clean(n, q):
        return [_mk32() for _ in range(n)]

    def _meas32(n, q):
        return [_mk32(wall_ms=2000, lane=None,
                      general_note="mouth-fell-back", finish="length",
                      fires=["INTENT:shelf-silent"],
                      completion_tokens=22) for _ in range(n)]
                recs.append({"label": "injected", "code": 200,
                             "wall_ms": 3000, "lane": "general",
                             "general_note": None,
                             "fires": ["INTENT:shelf-silent",
                                       "GENERAL:UNSOURCED"],
                             "finish": "stop", "finish_src": "reported",
                             "completion_tokens": 60})
            else:
                recs.append({"label": "injected", "code": 200,
                             "wall_ms": 2000, "lane": None,
                             "general_note": "mouth-fell-back",
                             "fires": ["INTENT:shelf-silent"],
                             "finish": "length",
                             "finish_src": "reported",
                             "completion_tokens": 22})
        return recs

    _prior32 = json.dumps({"MAXTOK": 4096}, indent=2)
    with open(_p32, "w") as _fh32:
        _fh32.write(_prior32)

    def _two_phase32(n, q):
        # the before-leg speaks the clean road; once the charter carries
        # the candidate, the SAME eyes must see the CUT road (a canned
        # endpoint could not know the difference; the injection reads
        # the charter - the state machine at work, bytes deciding)
        doc = json.loads(open(_p32).read())
        return _meas32(n, q) if doc.get("GENERAL_MAXTOK") == 22 \
            else _meas32_clean(n, q)

    _art32 = loop.run_lap(contract_path="a32-contract.json", cfg_path=_p32,
                          measure=_two_phase32,
                          hold_name="t177-lap.json", hold_to=_td32)
    _T177["lap"] = {
        "outcome": _art32["outcome"],
        "decision": _art32["decision"]["decision"],
        "rolled_back": _art32.get("rolled_back"),
        "restoration_verified": _art32.get("restoration_verified"),
        "bytes-exact": (open(_p32).read() == _prior32),
        "word-after": _art32["word_effective_after"],
        "mirror-untouched": (stages.CONFIG.get("GENERAL_MAXTOK") == 1024),
    }

expect("T177 THE NEW CLAUSE STANDS ALONE WHERE THE LANE HELD AND TOGETHER "
       "WITH IT WHERE IT FELL (synthetic, the REAL a32 contract's eyes): a "
       "clean stop-table APPLIES-HOLDS with an EMPTY rationale; a "
       "PARSE-INTACT but REPORTED-length after speaks ROLLBACK by the CUT "
       "WORD ALONE (the very shape the old table would have passed as "
       "fast-and-fine - a truncated fast answer is not an ordinary "
       "success); a lane-LOST cut speaks BOTH words (wound and cause, read "
       "together, the A32 law); A31's era-shape records (no finish words "
       "at all) cannot fire the clause - the replay's safety IS this "
       "clause's absence-law; an UNKNOWN finish (None at absent-src) does "
       "not fire it either; and a WHOLE injected lap at the a32 contract "
       "comes home ROLLED BACK with the temp charter's bytes EXACTLY prior "
       "and the restoration VERIFIED at both reads - and the REAL "
       "pipeline's mirror stayed at its own 1024 UNTOUCHED (a temp-charter "
       "lap does not smirch the mirror)",
       {k: _T177[k] for k in _T177 if k != "clean"} | {
           "clean-empty": _T177["clean"]["decision"] == "APPLIES-HOLDS"
                          and _T177["clean"]["rationale"] == [],
           "clean-decision": _T177["clean"]["decision"]},
       why=lambda tr: ([] if (
           tr["clean-decision"] == "APPLIES-HOLDS" and tr["clean-empty"]
           and tr["cut-parses"]["decision"] == "ROLLBACK"
           and tr["cut-parses"]["rationale"] == [
               "the cap cut the road's mouth (finish=length, REPORTED)"]
           and tr["cut-lanes"]["decision"] == "ROLLBACK"
           and len(tr["cut-lanes"]["rationale"]) == 2
           and all("the cap cut" in w for w in
                   tr["cut-lanes"]["rationale"])
           and tr["a31-shape"]["decision"] == "APPLIES-HOLDS"
           and tr["a31-shape"]["rationale"] == []
           and tr["unknown-word"]["decision"] == "APPLIES-HOLDS"
           and tr["lap"]["outcome"].startswith("APPLIED then ROLLED BACK")
           and tr["lap"]["decision"] == "ROLLBACK"
           and tr["lap"]["rolled_back"] is True
           and tr["lap"]["restoration_verified"] is True
           and tr["lap"]["bytes-exact"]
           and tr["lap"]["word-after"] == 4096
           and tr["lap"]["mirror-untouched"])
       else ["the new clause leaned on its neighbours, the era-bytes "
             "smuggled a cut, or the rolled-back lap left a word behind"]))

_T178 = {}
_ART32 = json.loads(open("research-hold/a32-evidence.json").read())
_CTL32 = json.loads(open("research-hold/a32-control.json").read())
_V32 = loop.decide(_ART32["before"], _ART32["after"], _CRIT32)
_T178 = {
    "replay": _V32["decision"],
    "recorded": _ART32["decision"]["decision"],
    "medians-match": (_V32["medians_ms"]
                      == _ART32["decision"]["medians_ms"]),
    "all-live": all(r.get("label") == "live"
                    for r in _ART32["before"] + _ART32["after"]),
    "before-spoke-stop": all(r.get("finish") == "stop"
                             and r.get("finish_src") == "reported"
                             for r in _ART32["before"]),
    "after-spoke-cut": all(r.get("finish") == "length"
                           and r.get("finish_src") == "reported"
                           and r.get("completion_tokens")
                           == _ART32["candidate"]
                           for r in _ART32["after"]),
    "control-live": (_CTL32.get("label") == "live"
                     and _CTL32.get("general_finish") == "stop"
                     and _CTL32.get("general_finish_src") == "reported"
                     and isinstance(_CTL32.get("general_completion_tokens"),
                                    int)),
    "no-persistence": (stages.CONFIG.get("GENERAL_MAXTOK") == 1024
                       and _ART32["candidate"] != 1024
                       and _ART32.get("rolled_back") is True
                       and _ART32.get("restoration_verified") is True),
    "words": (_ART32["word_effective_before"],
              _ART32["word_effective_after"]),
}

expect("T178 THE REPLAY RE-THINKS THE CUT AND THE PRODUCTION WORD DID NOT "
       "MOVE (replay at the held A32 bytes, zero live calls): re-deciding "
       "the held before/after records at the a32 eyes speaks the SAME "
       "verdict (ROLLBACK - the demonstration bit) and the SAME medians; "
       "every held record is label live (the truth INSIDE says so; this "
       "run's own name is replay); the before-leg spoke REPORTED stop at "
       "its tokens and the after-leg spoke REPORTED length at completion "
       "EXACTLY the candidate (22 - the cap enforced to the byte, the "
       "record's fact, not a fresh observation); the CONTROL is label live "
       "with REPORTED stop and a NUMBER for completion (the endpoint "
       "REPORTS - the A32 gate passed on DIRECTLY-SPOKEN words, no "
       "inference anywhere); the charter AS IT STANDS in the pipeline's "
       "own read rides A31's kept 1024 with rolled_back and "
       "restoration_verified TRUE AT BYTES - a failed candidate did not "
       "persist; and the words still read 1024 -> 1024 (the file's truth, "
       "A31's law unchanged)",
       _T178,
       why=lambda tr: ([] if (
           tr["replay"] == tr["recorded"] == "ROLLBACK"
           and tr["medians-match"] and tr["all-live"]
           and tr["before-spoke-stop"] and tr["after-spoke-cut"]
           and tr["control-live"] and tr["no-persistence"]
           and tr["words"] == (1024, 1024))
       else ["the replay stopped matching the lap, the labels lied, the "
             "cut was not REPORTED at the held bytes, or the candidate "
             "outstayed its demonstration"]))

