# loop.py — A31: ONE lap of the loop, on purpose.
# measure -> decide -> apply(one bounded word) -> re-measure -> judge,
# run by the SYSTEM at one module entry (the smallest missing integration:
# task.py is a research voyage with its own laws; the charter is the
# pipeline's bytes; neither was built to re-price itself — this module is).
# Powers are BOUNDED on purpose: the lap READS the charter, measures
# through the SAME door the conversation rides, WRITES ONE KEY of the
# charter (the founder's A31 grant, one word, not general file authority),
# RE-MEASURES, may RESTORE the exact prior bytes, and persists its
# provenance through the EXISTING single write-path (research.hold - the
# holding area; the root stays protected). No daemon, no framework: the
# tests replay the whole verdict from the preserved bytes with ZERO live
# calls, and a replay never wears the label of a live observation.
import json
import os
import time

import research
import stages

CFG_PATH = os.path.join(stages.BASE_DIR, "config.json")
CONTRACT = os.path.join(stages.BASE_DIR, "a31-contract.json")


def effective_word(cfg, key, fallback="MAXTOK"):
    """the value a road ACTUALLY rides: the key when the charter speaks
    it, the fallback's word when it does not (the same fallback
    stages.call speaks - read off both, never assumed)."""
    v = cfg.get(key)
    return v if v is not None else cfg.get(fallback)


def read_cfg(path=None):
    return json.load(open(path or CFG_PATH))


def apply_word(path, key, value):
    """the ONE bounded self-modification: write one key at the charter,
    keep the other bytes' ORDER (json dicts keep insertion order; a NEW
    key lands last), hand back the word the file rode before. A restore
    rides the prior BYTES verbatim (rollback must not re-flow the file)."""
    text = open(path).read()
    doc = json.loads(text)
    old = doc.get(key)
    doc[key] = value
    open(path, "w").write(json.dumps(doc, indent=2) + "\n")
    return old, text


def restore_bytes(path, text):
    open(path, "w").write(text)
    return read_cfg(path)                    # the verification: read-back


def measure_door(n, question, measure=None):
    """n live door runs as RECORDS of the road's own words (the trace's
    keys, never a reconstruction from the answer's prose). 'measure' is
    the injection seam the tests ride (a replay feeds canned records;
    no replay claims to be live)."""
    if measure is not None:
        return measure(n, question)
    out = []
    for _ in range(n):
        t0 = time.time()
        try:
            payload, code = stages.door({"question": question}, live=True)
            tr = payload["trace"]
            out.append({"label": "live", "code": code,
                        "wall_ms": round((time.time() - t0) * 1000),
                        "lane": tr.get("lane"),
                        "general_note": tr.get("general_note"),
                        "seam_ms": round((tr.get("stages_ms") or {})
                                         .get("general", 0)),
                        "fires": list(tr.get("fires", [])),
                        "model_calls": tr.get("model_calls"),
                        "answer_len": len(tr.get("response") or ""),
                        # A32: the endpoint's words at the RECORD level
                        # (A31-era held records carry neither key - the
                        # reject-clause below CANNOT fire on them, which
                        # is what keeps the replay honest for bytes that
                        # predate the fields).
                        "finish": tr.get("general_finish"),
                        "finish_src": tr.get("general_finish_src",
                                             "absent"),
                        "completion_tokens":
                            tr.get("general_completion_tokens"),
                        # A33: the word the ROAD rode (the trace's own
                        # word, not a reconstruction) - the application's
                        # sharpest eye lives here.
                        "max_tokens": tr.get("general_max_tokens")})
        except Exception as e:
            out.append({"label": "live", "raised": type(e).__name__,
                        "wall_ms": round((time.time() - t0) * 1000)})
    return out


def _median(xs):
    xs = sorted(xs)
    return xs[len(xs) // 2] if xs else None


def decide(before, after, crit):
    """the PRE-DECLARED eyes, PURE: the same bytes in always speak the
    same words out - that is what makes the replay REAL (and what a test
    can pin without a network)."""
    why, ok = [], True
    for r in after:
        if "raised" in r or r.get("code") != 200:
            ok = False
            why.append("a trial did not arrive")
            continue
        if r.get("lane") != crit["required_lane"]:
            ok = False
            why.append("the road left its lane (a cut cap lands at the "
                       "shelf's exit)")
        elif crit.get("forbid_note") and r.get("general_note"):
            ok = False
            why.append("the lane drew " + str(r.get("general_note")) +
                       " - the cap ate the answer")
        # the road's own word rides ONLY when the road rode its lane;
        # a road that LEFT the lane speaks the shelf's exit-word INSTEAD
        # (the door's own law read, not a new one) - so the three wounds
        # are ONE chain, three faces of "the road lost its road", never
        # double-toll for one wound.
        elif crit.get("required_fire") and \
                crit["required_fire"] not in (r.get("fires") or []):
            ok = False
            why.append("the road's own word (" + crit["required_fire"] +
                       ") did not ride")
    if crit.get("reject_reported_length"):
        # A32's ONE new clause: a REPORTED length is NOT an ordinary
        # success - a cut that still PARSES is the shape the old table
        # would have passed as fast-and-fine. A lane-loss CAUSED by the
        # cut may speak two words (wound and cause, read together, not
        # double-toll). Absent words (A31's bytes) cannot fire it.
        for r in after:
            if (r.get("finish_src") == "reported"
                    and r.get("finish") == "length"):
                ok = False
                why.append("the cap cut the road's mouth "
                           "(finish=length, REPORTED)")
    b = [r["wall_ms"] for r in before if "wall_ms" in r and "raised" not in r]
    a = [r["wall_ms"] for r in after if "wall_ms" in r and "raised" not in r]
    bmed, amed = _median(b), _median(a)
    if not b or not a:
        ok = False
        why.append("too little truth to weigh")
    elif amed > bmed * crit["max_median_factor"]:
        ok = False
        why.append("a new floor: after-median over the declared band")
    return {"decision": ("APPLIES-HOLDS" if ok else "ROLLBACK"),
            "rationale": why,
            "medians_ms": {"before": bmed, "after": amed}}


def propose(rule, effective_cap, control):
    """A33-1, PURE: the same bytes in speak the same candidate out. Trust
    FIRST (a truthy word is not a count), arithmetic SECOND, and
    insufficiency answers at a WORD (a structured no-change), never a
    raise and never a silent zero. No clock, no char-count, no inferred
    seat - the candidate rides the count ALONE."""
    def _no(reason, cand=None, floor_hit=False, clamped=False):
        return {"proposal": "NO-PROPOSAL", "candidate": cand,
                 "inputs": {"completion_tokens":
                            control.get("completion_tokens"),
                            "effective_cap": effective_cap},
                 "floor_hit": floor_hit, "clamped": clamped,
                 "why": reason}
    if control.get("label") not in rule["trust_labels"]:
        return _no("the control word is not TRUSTED (label "
                   + repr(control.get("label")) + ")")
    if control.get("finish_src") != "reported":
        return _no("the control spoke no REPORTED finish word")
    t = control.get("completion_tokens")
    if t is None:
        return _no("the control carries no completion-token word")
    if isinstance(t, bool) or not isinstance(t, int) or t <= 0:
        return _no("the token word is not a count (got " + repr(t) + ")")
    raw = t // rule["divisor"]
    floor_hit = raw < rule["floor"]
    cand = min(effective_cap, max(rule["floor"], raw))
    if cand >= effective_cap:
        return _no("the found candidate is not STRICTLY below the word it "
                   "found (a bound, never a wish)", cand, floor_hit,
                   cand == effective_cap)
    return {"proposal": "PROPOSED", "candidate": cand,
            "inputs": {"completion_tokens": t,
                       "effective_cap": effective_cap,
                       "floor": rule["floor"], "divisor": rule["divisor"]},
            "floor_hit": floor_hit,
            "clamped": cand == effective_cap, "why": ""}


def compare(chain_a, chain_b):
    """A34's PURE verdict on the two held chains (the same replay law as
    decide: bytes in, words out, zero live). Reads ONLY what the laps
    already spoke (proposal/application/decision); the classification is
    the contract's table, word for word."""
    def _support(art):
        if art.get("proposal", {}).get("proposal") != "PROPOSED":
            return ("NO-PROPOSAL",
                    art.get("proposal", {}).get("why", "no word"))
        if not art.get("application_verified", True):
            return ("APP-FAIL",
                    "the word did not ride all three places")
        d = art["decision"]["decision"]
        if d == "APPLIES-HOLDS":
            return ("KEPT", "the road completed at the bound")
        if any("length" in w for w in art["decision"]["rationale"]):
            return ("ROLLED-CUT", "the bound cut the road (REPORTED length)")
        return ("ROLLED-UNCUT",
                "rolled at a non-length word (a correctness failure)")
    a, wa = _support(chain_a)
    b, wb = _support(chain_b)
    if a == "KEPT" and b == "ROLLED-CUT":
        verdict, why = "A33-1-HELD", ("A completed where B cut")
    elif b == "KEPT" and a == "ROLLED-CUT":
        verdict, why = "A34-B-HELD", ("B completed where A cut")
    elif a == "KEPT" and b == "KEPT":
        verdict, why = ("A33-1-SAFER-SUPPORTED",
                        "both complete - the tighter bound is the safer")
    elif a == "ROLLED-CUT" and b == "ROLLED-CUT":
        verdict, why = ("A33-1-SAFER-SUPPORTED",
                        "equal correctness (both cut); the tighter bound "
                        "bounds the tail harder; the safe production word "
                        "rides UNTOUCHED")
    else:
        verdict, why = ("NEITHER-JUSTIFIED",
                        "insufficient evidence or unclear correctness")
    return {"decision": verdict, "why": why,
            "support": {"A": [a, wa], "B": [b, wb]},
            "evidence": {k: {
                "candidate": c.get("proposal", {}).get("candidate"),
                "after_finishes": [r.get("finish") for r in c.get("after", [])],
                "after_tokens": [r.get("completion_tokens")
                                 for r in c.get("after", [])],
                "after_walls": [r.get("wall_ms") for r in c.get("after", [])],
                "road_words": [r.get("max_tokens")
                               for r in c.get("after", [])]}
                for k, c in (("A", chain_a), ("B", chain_b))}}


def _lap_auto(art, doc, crit, key, n, cfgp, before_word, measure,
              hold_name, hold_to):
    """A33 at the ONE entry: the before-leg IS the control-leg (its first
    record is the control at bytes); the PROPOSAL precedes every
    application; the application then stands on THREE proofs - the FILE,
    the MIRROR (where the mirror rides), and the ROAD's OWN spoken word
    at every after-trial. Acceptance keeps the A32 eyes whole. Nothing
    re-rolls, nothing chases."""
    art["before"] = measure_door(n, doc["question"], measure)
    control = art["before"][0] if art["before"] else {}
    prop = propose(doc["auto_rule"], before_word, control)
    art["proposal"] = prop
    if prop["proposal"] != "PROPOSED":
        art["outcome"] = ("NO-CHANGE (the PROPOSAL could not PROPOSE: "
                          + prop["why"] + ")")
        art["word_effective_after"] = before_word
        research.hold(art, hold_name, to=hold_to)
        return art
    cand = prop["candidate"]
    art["candidate"] = cand
    old, prior_text = apply_word(cfgp, key, cand)
    art["applied"] = {key: cand, "was_present": old is not None}
    if cfgp == CFG_PATH:
        stages.reload_config()
    art["after"] = measure_door(n, doc["question"], measure)
    _ride = [r for r in art["after"] if "raised" not in r]
    art["application"] = {
        "file": read_cfg(cfgp).get(key) == cand,
        "mirror": (cfgp != CFG_PATH)
                  or (stages.CONFIG.get(key) == cand),
        "road": bool(_ride) and all(r.get("max_tokens") == cand
                                     for r in _ride)}
    art["application_verified"] = all(art["application"].values())
    art["decision"] = decide(art["before"], art["after"], crit)
    if not art["application_verified"]:
        # the A33 named class: a word that did not RIDE is no result -
        # the lap rolls back SAFELY and the reason rides the rationale
        art["decision"] = dict(art["decision"], decision="ROLLBACK",
                               rationale=(art["decision"]["rationale"]
                                          + ["the word did not RIDE the "
                                             "file/mirror/road"]))
    if art["decision"]["decision"] == "ROLLBACK":
        restore_bytes(cfgp, prior_text)
        if cfgp == CFG_PATH:
            stages.reload_config()
        art["rolled_back"] = True
        art["restoration_verified"] = (
            effective_word(read_cfg(cfgp), key) == before_word)
        if cfgp == CFG_PATH:
            art["restoration_verified"] = (
                art["restoration_verified"]
                and effective_word(stages.CONFIG, key) == before_word)
        art["outcome"] = ("APPLIED then ROLLED BACK (the lap answered "
                          "honestly)"
                          if art["application_verified"]
                          else "APPLIED then ROLLED BACK (the road rode "
                               "no such word)")
    else:
        art["outcome"] = ("APPLIED (the verdict rode - the candidate is "
                          "the kept word)")
    art["word_effective_after"] = effective_word(read_cfg(cfgp), key)
    research.hold(art, hold_name, to=hold_to)
    art["held_as"] = hold_name + " (research.hold - the one pen)"
    return art


def run_lap(contract_path=None, cfg_path=None, measure=None,
            hold_name="a31-lap-state.json", hold_to=None):
    """the ONE lap, end to end, at one entry. Returns the artifact (the
    provenance) and holds it to the EXISTING holding area (a test's lap
    may ride its OWN pile - the evidence file stays the evidence's)."""
    doc = json.load(open(contract_path or CONTRACT))
    cfgp = cfg_path or CFG_PATH
    crit = doc["criteria"]
    key, cand, n = doc["seam_key"], doc["candidate"], doc["trials_per_side"]
    art = {"contract": os.path.basename(contract_path or CONTRACT),
           "date": time.strftime("%Y-%m-%dT%H:%M:%S"),
           "label": "live" if measure is None else "injected"}
    cfg0 = read_cfg(cfgp)
    before_word = effective_word(cfg0, key)
    art["word_effective_before"] = before_word
    art["candidate"] = cand
    if cand == "AUTO":
        return _lap_auto(art, doc, crit, key, n, cfgp, before_word,
                         measure, hold_name, hold_to)
    if cand == before_word:
        art["outcome"] = ("NO-CHANGE (the word ALREADY RIDES the candidate "
                          "value)")
        art["word_effective_after"] = before_word
        research.hold(art, hold_name, to=hold_to)
        return art
    if cand > before_word:
        art["outcome"] = ("NO-CHANGE (the candidate would WIDEN the "
                          "bound - a cap is a bound, never a wish)")
        art["word_effective_after"] = before_word
        research.hold(art, hold_name, to=hold_to)
        return art
    art["before"] = measure_door(n, doc["question"], measure)
    old, prior_text = apply_word(cfgp, key, cand)
    if cfgp == CFG_PATH:
        # A32: the charter's bytes are the LAW; stages.CONFIG is their
        # import-time MIRROR. A mid-flight writer must refresh the
        # mirror or its own after-trials ride the yesterday (the first
        # A32 lap proved it live: a 22-token cap, completion 50-67,
        # finish=stop - the word had not RIDDEN). A TEST's temp charter
        # is not the mirror's file - no refresh there, the injected
        # measure reads nothing.
        stages.reload_config()
    art["applied"] = {key: cand, "was_present": old is not None}
    art["after"] = measure_door(n, doc["question"], measure)
    art["decision"] = decide(art["before"], art["after"], crit)
    art["outcome"] = ("APPLIED (the verdict rode)"
                      if art["decision"]["decision"] == "APPLIES-HOLDS"
                      else "APPLIED then ROLLED BACK (the lap failed "
                           "honestly)")
    if art["decision"]["decision"] == "ROLLBACK":
        restore_bytes(cfgp, prior_text)
        if cfgp == CFG_PATH:
            stages.reload_config()      # the mirror rides the restore too
        art["rolled_back"] = True
        art["restoration_verified"] = (effective_word(read_cfg(cfgp), key)
                                        == before_word)
        if cfgp == CFG_PATH:
            # the MIRROR's proof belongs where the mirror rides: the real
            # charter's read must agree too (a temp-charter lap has no
            # mirror, and the pipeline's words are the REAL file's truth)
            art["restoration_verified"] = (
                art["restoration_verified"]
                and effective_word(stages.CONFIG, key) == before_word)
    art["word_effective_after"] = effective_word(read_cfg(cfgp), key)
    research.hold(art, hold_name, to=hold_to)
    art["held_as"] = hold_name + " (research.hold - the one pen)"
    return art


if __name__ == "__main__":
    a = run_lap()
    print(json.dumps(a, indent=1))
