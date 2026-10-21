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
                        "answer_len": len(tr.get("response") or "")})
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
    art["applied"] = {key: cand, "was_present": old is not None}
    art["after"] = measure_door(n, doc["question"], measure)
    art["decision"] = decide(art["before"], art["after"], crit)
    art["outcome"] = ("APPLIED (the verdict rode)"
                      if art["decision"]["decision"] == "APPLIES-HOLDS"
                      else "APPLIED then ROLLED BACK (the lap failed "
                           "honestly)")
    if art["decision"]["decision"] == "ROLLBACK":
        restore_bytes(cfgp, prior_text)
        art["rolled_back"] = True
        art["restoration_verified"] = (effective_word(read_cfg(cfgp), key)
                                       == before_word)
    art["word_effective_after"] = effective_word(read_cfg(cfgp), key)
    research.hold(art, hold_name, to=hold_to)
    art["held_as"] = hold_name + " (research.hold - the one pen)"
    return art


if __name__ == "__main__":
    a = run_lap()
    print(json.dumps(a, indent=1))
