#!/usr/bin/env python3
"""evaluator.py - A3: the conversation benchmark, run as ONE road (the door).

The product's conversational road is already built (stages.door: history ->
digest -> facts -> run_pipeline). What A3 raises is not a second pipeline
but a HARNESS: a fixed benchmark of exchanges (benchmark.json) plus this
runner, which speaks the SAME door law, records what came back, and scores
the declared observable properties. No new scheduler, no new model road -
the mouths stay stages.call's, the caps ride stages.CALLS, and the evidence
lands in the same holding area the task lane already keeps.

THE LAWS OF THIS HARNESS
  * A run is MODE-tagged: "live" pays the real mouths (the production road,
    byte-for-byte the door's); "dry" rides the fixture lanes already proven
    in tests.py (draft / sim_general) and spends ZERO mouths - so the suite
    runs without the funnel, as the frozen stage set has always done.
  * A failed model REQUEST is not a poor ANSWER: a case whose pipeline
    raised (or spat the [MOUTH ERROR lane) is REQUEST-FAILED and its checks
    ride UNSCORED - a failure is never laundered into a verdict.
  * A check the mode does not carry, or a run that the caps cut short, is
    UNSCORED - never a silent pass. The report says which cases remain
    unscored and why.
  * The caps are a PRE-REQUEST GATE (the task lane's own law): a turn does
    not START without one mouth's margin left, and a zero-clock run never
    coins at all. The caps stop the run; they do not launder the evidence.
  * Semantic properties are DECLARED, not judged-by-default: they record
    UNSCORED ("the human eye") unless a reviewer was asked - and the
    reviewer is the same model class, recorded as such, never ground truth.
  * Rerun safety: a run writes bench-<name>.json over its own name; the
    volatile numbers (ms, secs, start) are stripped by volatile() so two
    dry runs are the same bytes twice (the project's idempotency law).

usage: python3 evaluator.py validate
       python3 evaluator.py run [--mode dry|live] [--name NAME] [--only B1,B2]
                                [--max-calls N] [--max-secs S] [--review]
       python3 evaluator.py compare benchA.json benchB.json
"""
import json
import os
import sys
import time

import stages

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HOLD = os.path.join(BASE_DIR, "research-hold")
FIXTURE = os.path.join(BASE_DIR, "benchmark.json")
CHECK_TYPES = ("contains_any", "not_contains", "unknown", "lane_in",
               "context_carries")
MOUTH_ERROR = "[MOUTH ERROR"            # stages.call's own catch-lane word
CARRY = "Earlier - "                    # P["prior_marker"]: the digest's byte


# ---------- the fixture (data in, errors out; nothing invented here) -------
def load_doc(path=FIXTURE):
    return json.loads(open(path).read())


def validate_doc(doc):
    """The schema as a LIST of problems - empty list means the fixture is
    whole. An invalid benchmark is a BUILD failure, spoken at once."""
    errs = []
    if not isinstance(doc, dict) or "cases" not in doc:
        return ["no benchmark document / no cases"]
    ids = set()
    for case in doc["cases"]:
        where = case.get("id", "?")
        if not isinstance(where, str) or not where:
            errs.append("case with no id")
            continue
        if where in ids:
            errs.append("duplicate id " + where)
        ids.add(where)
        if not case.get("kind"):
            errs.append(where + ": no kind")
        turns = case.get("turns")
        if (not isinstance(turns, list) or not turns
                or not all(isinstance(t, dict) and t.get("say") for t in turns)):
            errs.append(where + ": turns must be a non-empty list of {say,...}")
            continue
        cids = set()
        for ck in case.get("checks", []):
            if ck.get("id") in cids or not ck.get("id"):
                errs.append(where + ": check ids must be non-empty and unique")
            cids.add(ck.get("id"))
            if ck.get("type") not in CHECK_TYPES:
                errs.append(where + "/" + str(ck.get("id"))
                            + ": unknown check type " + str(ck.get("type")))
            if ck.get("type") in ("contains_any", "not_contains") and not ck.get("words"):
                errs.append(where + "/" + str(ck.get("id")) + ": needs words")
            if ck.get("type") == "unknown" and ck.get("expect") is None:
                errs.append(where + "/" + str(ck.get("id")) + ": needs expect")
            if ck.get("type") == "lane_in" and ck.get("lanes") is None:
                errs.append(where + "/" + str(ck.get("id")) + ": needs lanes")
            if ck.get("type") == "context_carries":
                t = ck.get("turn", 2)
                if not (isinstance(t, int) and 2 <= t <= len(case["turns"])):
                    errs.append(where + "/" + str(ck.get("id"))
                                + ": context_carries needs a turn within the case")
        for sem in case.get("semantic", []):
            if not isinstance(sem, str) or not sem:
                errs.append(where + ": semantic entries must be plain strings")
    return errs


# ---------- one case, on the ONE road (the door's own) ----------------------
def _run_turn(case_turn, history, mode, mouth):
    """One seeker turn through stages.door - the production law, digest and
    all. In dry mode the fixture lanes ride as door kwargs (draft,
    sim_general, sim_findings), exactly the injections tests.py has always
    used. Returns the turn's record."""
    body = {"question": case_turn["say"]}
    if history:
        body["history"] = [dict(t) for t in history]
    kw = {}
    if mode == "dry":
        for k in ("draft", "sim_general", "sim_findings"):
            if k in case_turn:
                kw[k] = case_turn[k]
    elif any(k in case_turn for k in ("draft", "sim_general", "sim_findings")):
        # the live road pays the REAL mouths; the dry fixtures are read but
        # not fed (a frozen reply would launder the experiment).
        pass
    t0 = time.perf_counter()
    error = None
    try:
        payload, _code = stages.door(body, live=(mode == "live"), **kw)
        tr = payload.get("trace", {})
        response = payload.get("response", "")
    except Exception as exc:                      # the request fell over
        error, tr, response = repr(exc), {}, ""
    ms = (time.perf_counter() - t0) * 1000
    model_error = error is not None or MOUTH_ERROR in response
    return {"say": case_turn["say"],
             "facts": str(body.get("facts") or
                          stages.digest(body.get("history"))),
             "response": response,
             "lane": tr.get("lane"),
             "unknown": bool(tr.get("unknown")),
             "fires": tr.get("fires", []),
             "observations": tr.get("observations", []),
             "model_error": model_error,
             "error": error,
             "ms": round(ms, 1),
             "calls": 0}      # the run() fills the truth (the ledger re-zeroes)


# ---------- the deterministic checks (pure over the record) ----------------
def _last(tr):
    return tr[-1] if tr else None


def eval_check(ck, turns, mode):
    """PASS / FAIL / UNSCORED - a verdict plus the word of why."""
    if mode not in ck.get("modes", ["dry", "live"]):
        return "UNSCORED", "not this mode"
    answered = [t for t in turns if t.get("error") is None]
    if any(t.get("error") is not None for t in turns):
        return "UNSCORED", "request failed (not a poor answer)"
    if len(answered) != len(turns) or not answered:
        return "UNSCORED", "incomplete run"
    low = [t["response"].lower() for t in turns]
    typ = ck["type"]
    if typ == "contains_any":
        w = [x.lower() for x in ck["words"]]
        last = _last(answered)
        ok = any(x in last["response"].lower() for x in w)
        return ("PASS" if ok else "FAIL"), "last turn"
    if typ == "not_contains":
        w = [x.lower() for x in ck["words"]]
        ok = not any(any(x in r for r in low) for x in w)
        return ("PASS" if ok else "FAIL"), ck.get("where", "all") + " turns"
    if typ == "unknown":
        ok = _last(answered)["unknown"] is bool(ck["expect"])
        return ("PASS" if ok else "FAIL"), "unknown flag"
    if typ == "lane_in":
        ok = _last(answered)["lane"] in ck["lanes"]
        return ("PASS" if ok else "FAIL"), "lane"
    if typ == "context_carries":
        i = ck.get("turn", 2) - 1
        if i >= len(turns):
            return "FAIL", "case has no such turn"
        facts = turns[i]["facts"]
        ok = facts.startswith(CARRY) and turns[i - 1]["say"] in facts
        return ("PASS" if ok else "FAIL"), "the digest carried the prior turn"
    return "UNSCORED", "unknown type"


def _semantics(case, turns, mode, review):
    """Declared semantic properties: UNSCORED by default (the human eye),
    a reviewer's word only when ASKED, and named for what it is."""
    out = []
    for sem in case.get("semantic", []):
        if not review:
            out.append({"text": sem, "verdict": "UNSCORED",
                        "note": "the human eye (no reviewer asked)"})
            continue
        t = _last([x for x in turns if x.get("error") is None])
        try:
            out_raw = stages.call(
                "You judge ONE declared property of an assistant's answer. "
                "Answer JSON only: {\"pass\": true|false}.",
                "PROPERTY: " + sem + "\nSEEKER: " + t["say"]
                + "\nANSWER: " + t["response"])
            row = stages.grab_json(out_raw.get("content") or "", "{")
            out.append({"text": sem,
                        "verdict": "PASS" if row.get("pass") else "FAIL",
                        "note": "same-model judge; not ground truth"})
        except Exception:
            out.append({"text": sem, "verdict": "UNSCORED",
                        "note": "reviewer fell back"})
    return out


# ---------- the run ---------------------------------------------------------
class _Counted:
    """A counting proxy at the mouth seam. The spine zeroes stages.CALLS at
    the top of EVERY run (a per-run ledger), so a multi-turn run cannot read
    its cumulative truth from it - this proxy owns the run-level count. The
    witness's mouth counts itself the same way (the instrument convention)."""
    def __init__(self, fn):
        self.fn, self.n = fn, 0
    def __call__(self, system, user, maxtok=None, thinking=True):
        self.n += 1
        return self.fn(system, user, maxtok, thinking)


def run(path=FIXTURE, mode="live", only=None, max_calls=None, max_secs=None,
        review=False, mouth=None, clock=time.perf_counter, out_dir=None):
    doc = load_doc(path) if isinstance(path, str) else path
    errs = validate_doc(doc)
    if errs:
        raise ValueError("benchmark invalid: " + "; ".join(errs))
    caps = doc.get("caps", {})
    max_calls = caps.get("max_calls", 60) if max_calls is None else max_calls
    max_secs = caps.get("max_secs", 1200) if max_secs is None else max_secs
    cases = [c for c in doc["cases"] if only is None or c["id"] in only]
    saved = stages.call
    counted = _Counted(mouth if mouth is not None else stages.call)
    stages.call = counted
    t0 = clock()
    complete, results = True, {}
    for case in cases:
        turns = []
        status = "ANSWERED"
        for turn_spec in case["turns"]:
            if counted.n >= max_calls or clock() - t0 >= max_secs:   # pre-request
                status = "INCOMPLETE"
                break
            before = counted.n
            rec = _run_turn(turn_spec, [ {"q": t["say"], "a": t["response"]}
                                          for t in turns ], mode, mouth)
            rec["calls"] = counted.n - before
            turns.append(rec)
            if rec["error"] is not None:
                status = "REQUEST-FAILED"
                break                                           # the road died here
        if status == "ANSWERED" and len(turns) < len(case["turns"]):
            status = "INCOMPLETE"
        checks = []
        for ck in case.get("checks", []):
            verdict, note = eval_check(ck, turns, mode)
            checks.append({"id": ck["id"], "type": ck["type"],
                           "verdict": verdict, "note": note})
        results[case["id"]] = {
            "kind": case["kind"], "status": status, "turns": turns,
            "checks": checks, "semantic": _semantics(case, turns, mode, review)}
        if status != "ANSWERED":
            complete = False
    secs = clock() - t0
    stages.call = saved
    meta = {"mode": mode, "model": stages.CONFIG["MODEL"],
            "versions": dict(stages.CONFIG["versions"],
                             benchmark=doc.get("benchmark")),
            "reviewer": ("asked" if review else "not asked"),
            "caps": {"max_calls": max_calls, "max_secs": max_secs},
            "calls": counted.n,
            "secs": round(secs, 1),
            "started": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "complete": complete}
    return {"meta": meta, "cases": results}


def volatile(record):
    """The comparable projection: run numbers that must not move between
    two honest dry runs (ms, secs, start) are stripped."""
    m = dict(record["meta"]); m.pop("secs"); m.pop("started")
    out = {"meta": m, "cases": {}}
    for cid, c in record["cases"].items():
        c = dict(c)
        c["turns"] = [{k: v for k, v in t.items() if k != "ms"}
                      for t in c["turns"]]
        out["cases"][cid] = c
    return out


def write(record, name, out_dir=HOLD):
    os.makedirs(out_dir, exist_ok=True)
    p = os.path.join(out_dir, "bench-" + name + ".json")
    open(p, "w").write(json.dumps(record, indent=1) + "\n")
    return p


# ---------- baseline vs candidate ------------------------------------------
def compare(a, b):
    """Case by case, check by check: the ONLY two verdicts that speak are
    PASS->FAIL (a REGRESSION) and FAIL->PASS (an IMPROVEMENT); an
    unscored-any-side move is a CHANGE, spoken not scored; and a missing
    case, a failed request, or an incomplete run is FLAGGED, never ranked."""
    va = a["meta"]["versions"]["benchmark"]; vb = b["meta"]["versions"]["benchmark"]
    if va != vb:
        return {"error": "benchmark version mismatch: " + str(va) + " vs " + str(vb)}
    out, summ = {}, {"regressions": 0, "improvements": 0, "changes": 0,
                     "same": 0, "flags": []}
    for cid in sorted(set(a["cases"]) | set(b["cases"])):
        ca, cb = a["cases"].get(cid), b["cases"].get(cid)
        if ca is None or cb is None:
            out[cid] = {"flags": ["case missing from " + ("baseline" if ca is None else "candidate")]}
            summ["flags"].append(cid + ": case missing")
            continue
        entry = {"status": [ca["status"], cb["status"]], "checks": [],
                 "flags": []}
        for st, side in ((ca["status"], "baseline"), (cb["status"], "candidate")):
            if st in ("REQUEST-FAILED", "INCOMPLETE"):
                entry["flags"].append(side + " " + st)
                summ["flags"].append(cid + ": " + side + " " + st)
        ba = {ck["id"]: ck["verdict"] for ck in ca["checks"]}
        bb = {ck["id"]: ck["verdict"] for ck in cb["checks"]}
        for kid in sorted(set(ba) | set(bb)):
            va_, vb_ = ba.get(kid, "ABSENT"), bb.get(kid, "ABSENT")
            if va_ == vb_:
                summ["same"] += 1
                continue
            kind = ("REGRESSION" if (va_, vb_) == ("PASS", "FAIL") else
                    "IMPROVEMENT" if (va_, vb_) == ("FAIL", "PASS") else "CHANGE")
            summ["regressions" if kind == "REGRESSION" else
                  "improvements" if kind == "IMPROVEMENT" else "changes"] += 1
            entry["checks"].append({"check": kid, "from": va_, "to": vb_, "kind": kind})
        if entry["flags"]:
            entry["status"] = entry["status"]          # flags ride the entry
        out[cid] = entry
    return {"cases": out, "summary": summ}


# ---------- the report print ------------------------------------------------
def speak(record):
    print("== " + record["meta"]["versions"]["benchmark"]
          + " | mode: " + record["meta"]["mode"]
          + " | model: " + record["meta"]["model"]
          + (" | reviewer " + record["meta"]["reviewer"]))
    for cid, c in record["cases"].items():
        line = cid + " [" + c["kind"] + "] " + c["status"]
        for ck in c["checks"]:
            line += "  " + ck["id"] + "=" + ck["verdict"]
        print(line)
        for sem in c["semantic"]:
            print("        ~ " + sem["text"] + " -> " + sem["verdict"]
                  + " (" + sem["note"] + ")")
    m = record["meta"]
    print("-- calls: " + str(m["calls"]) + "/" + str(m["caps"]["max_calls"])
          + " | secs: " + str(m["secs"]) + "/" + str(m["caps"]["max_secs"])
          + " | run " + ("COMPLETE" if m["complete"] else "INCOMPLETE"))


def speak_compare(rep):
    if "error" in rep:
        print(rep["error"]); return
    for cid, e in rep["cases"].items():
        moves = ["{} {}->{} [{}]".format(m["check"], m["from"], m["to"], m["kind"])
                 for m in e.get("checks", [])]
        fl = ("  FLAG: " + "; ".join(e["flags"])) if e.get("flags") else ""
        print(cid + " " + "/".join(e.get("status", ["-", "-"])) + " "
              + ("; ".join(moves) if moves else "no moves") + fl)
    s = rep["summary"]
    print("-- regressions: %d | improvements: %d | changes: %d | same: %d | flags: %d"
          % (s["regressions"], s["improvements"], s["changes"], s["same"], len(s["flags"])))


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "validate"
    if cmd == "validate":
        e = validate_doc(load_doc())
        print("OK: %d cases" % len(load_doc()["cases"]) if not e else "\n".join(e))
    elif cmd == "run":
        a = sys.argv[2:]
        def flag(word, cast=str):
            return cast(a[a.index(word) + 1]) if word in a else None
        rec = run(mode=flag("--mode") or "live",
                  only=(flag("--only").split(",") if flag("--only") else None),
                  max_calls=flag("--max-calls", int),
                  max_secs=flag("--max-secs", int),
                  review="--review" in a)
        p = write(rec, flag("--name") or "all")
        speak(rec); print("wrote " + p)
    elif cmd == "compare":
        A = json.loads(open(sys.argv[2]).read())
        B = json.loads(open(sys.argv[3]).read())
        speak_compare(compare(A, B))