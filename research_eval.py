#!/usr/bin/env python3
"""research_eval.py - A5's fixed evaluation (fixture: research-eval.json,
EA-0.1). Six questions at the web lanes, the wording FROZEN (the seeker's
words ride as spoken); the expected-lane words were written from a live
search-level probe of the day BEFORE any scoring (an expectation is not a
score).

The runner records TRUTH, never a verdict: per question it runs
web_research (the search, the fetches, the kinds, the corroboration words),
then - live mode - the SAME real door the conversation rides (web:true:
the eval asks of the WEB lanes; the auto lanes' sufficiency was weighed at
T140 and the A5 live file). The axes (§6's separate scores) are filled by
the MACHINE where they are counts (retrieval, traceability, independence
- the words ride below) and by the OPERATOR by hand elsewhere (factual
correctness, citation support, appropriate uncertainty, evasiveness) -
the same brain that wrote the code, disclosed, never an independent
model judging its own child.

The caps are PRE-REQUEST like the whole house's law: a leg does not START
without margin (max_secs_per_question rides the wall-clock of the
question's own run; the web phase carries its own MAX_SECS inside, and
the door's mouths are bounded by their own road). Over-budget legs ride
the word "over-budget" - a stated skip, never a silent loss.

Modes: no argument = the full live road (search + fetches + the door's
mouths - the run the report's numbers come from); --search = the cheap
re-check (web lanes only, zero mouthfuls). The deterministic truths of
this eval's machinery ride the T-series; this runner IS live by nature
(an eval that never saw the net is a fixture).
"""
import json
import os
import sys
import time

import stages
import urllib.parse

import web_research

HERE = os.path.dirname(os.path.abspath(__file__))


def load_doc():
    return json.loads(open(os.path.join(HERE, "research-eval.json")).read())


def run_one(qtext, live, caps, query=None):
    # A22: the OPTIONAL explicit retrieval query, kept SEPARATE from the
    # question. The question rides byte-for-byte everywhere (the record's
    # "question" key, the door's body, the pipeline's road); the query
    # rides the SEARCH ALONE - the door's own A15 word (body["query"],
    # used by web_research.research and recorded at the packet), spent
    # here at the runner. Absent or malformed (not a string, empty, all
    # space) it IS the question's bytes: today's road byte-exact. No
    # rewriting, no extra model call, no new provider behavior - the
    # runner accepts, uses, and RECORDS, and the actual query is recorded
    # from the PACKET'S OWN WORD and the door's OWN trace, never
    # reconstructed.
    t0 = time.time()
    out = {"question": qtext}
    rquery = query.strip() if isinstance(query, str) else ""
    pk = web_research.research(rquery or qtext)   # its own MAX_SECS bounds it
    rows, ids = web_research.to_rows(pk)
    out["web"] = {"provider": pk["provider"], "ok": pk["ok"],
                  "query": pk.get("query"),       # A22: the query ACTUALLY
                                                  # ridden, the packet's
                                                  # own word (the A15
                                                  # trace-stamp idiom, at
                                                  # the record as well)
                  "results": len(pk["results"]), "gaps": pk["gaps"],
                  "spent": pk["spent"],
                  "corroboration": web_research.corroboration(pk),
                  "rows": [{"id": r["id"], "kind": r.get("kind"),
                            "evidence": r.get("evidence"),
                            "note": r.get("note"), "work": r.get("work"),
                            "publisher": r.get("publisher"),
                            "url": r["url"], "claim": r["claim"]}
                           for r in rows]}        # THE BYTES THE MOUTH SAW
    left = caps.get("max_secs_per_question", 240) - (time.time() - t0)
    if live:
        if left > 0:
            body = {"question": qtext, "web": True}
            if rquery:
                body["query"] = rquery            # the A15 door word, spent
            payload, code = stages.door(body, live=True)
            tr = payload["trace"]
            # A18: the runner's record now carries the door's OWN status
            # word VERBATIM (a tr.get, never a reconstruction from prose):
            # a missing word rides as ABSENCE (null), never as an invented
            # stronger claim; the over-budget lane stays sparse as built.
            out["door"] = {"code": code, "lane": tr.get("lane"),
                           "retrieval": tr.get("retrieval"),
                           "response": tr.get("response"),
                           "model_calls": tr.get("model_calls"),
                           "evidence_status": tr.get("evidence_status"),
                           "web_stamped": tr.get("web") is not None}
            if rquery:
                # A22: and beside it the door's OWN query word (a tr.get of
                # the A15 trace stamp, verbatim). A fold leaves no web
                # stamp, so the word rides as ABSENCE (None) - never a
                # promotion; the key rides only where a query was spoken,
                # and the over-budget branch (no door call) stays sparse.
                out["door"]["query"] = (tr.get("web") or {}).get("query")
        else:
            out["door"] = {"lane": "over-budget"}    # the word, not a shrug
    out["secs"] = round(time.time() - t0, 1)
    return out


# ---------- A34: the CYCLE (two stages, the gap-born query, the words) ----
# The rail is the FOUNDATION'S OWN (run_one rides the net search, the
# fetcher's lanes, and the door's web road with the A15/A18/A19 status
# words at bytes; A22's FROZEN-QUERY rail carries the follow-up). A34 adds
# the three WORDS the cycle lacks - the gap's CLASS, the follow-up's
# SHAPE, the COMPARISON - and none of them a framework.

GAPS = ("RETRIEVAL-FAIL", "SEARCH-EMPTY", "NO-ORIGIN", "SINGLE-ORIGIN",
        "SUFFICIENT")


def gap_word(rec):
    """the RECORD's OWN fields decide (never its prose); first match
    wins; the lane's own word rides FIRST (A19's law: the lane-word,
    never an empty results-list, decides a failure)."""
    web = rec.get("web") or {}
    c = web.get("corroboration") or {}
    gaps = web.get("gaps") or []
    if web.get("ok") is not True or gaps:
        # A19's law, read CLOSE: the lane-WORD decides, and emptiness IS
        # a lane ("search-empty" rides gaps, ok False rides emptiness per
        # the provider's own bool(rows) law at web_research). EA4's frozen
        # expectation names SEARCH-EMPTY as its OWN honest class; the
        # failure class is what is NEITHER empty nor well.
        if "search-empty" in gaps:
            return "SEARCH-EMPTY"
        return "RETRIEVAL-FAIL"
    if not web.get("results"):
        return "SEARCH-EMPTY"
    if not c.get("read"):
        return "NO-ORIGIN"
    if (c.get("origin_publishers") or 0) < 2:
        return "SINGLE-ORIGIN"
    return "SUFFICIENT"


def follow_query(gap, rec):
    """A34-C1: the words come from the RECORD (a publisher the record
    NAMED, the question's own bytes) - never from a hardcoded second
    query wearing an autonomy coat."""
    q = rec.get("question") or ""
    if gap == "RETRIEVAL-FAIL":
        return q + " overview"          # the retry idiom, named AS one
    if gap == "SEARCH-EMPTY":
        return q + " definition"
    if gap in ("NO-ORIGIN", "SINGLE-ORIGIN"):
        rows = (rec.get("web") or {}).get("rows") or []
        named = next((r.get("publisher") for r in rows if r.get("publisher")),
                     None)
        if named is None:
            url = next((r.get("url") for r in rows if r.get("url")), "")
            try:
                named = urllib.parse.urlparse(url).hostname or ""
            except ValueError:
                named = ""
        return (named + " " if named else "") + q
    if gap == "SUFFICIENT":
        return q + " in summary"        # BREADTH, declared as such
    return q                             # the word rode; the bytes ride


def compare_stages(one, two, gap):
    """what CHANGED, what did NOT, and the pre-declared word (bytes
    only; a NO-improvement is a FINDING, printed as one)."""
    def _w(rec):
        web = rec.get("web") or {}
        c = web.get("corroboration") or {}
        return {"urls": web.get("results") or 0,
                "read": c.get("read") or 0,
                "origins": c.get("origin_publishers") or 0,
                "independence": c.get("independence"),
                "status": status_word(rec),
                "seen": sorted({str(r.get("url") or "")
                                for r in web.get("rows") or []}),
                "response": (rec.get("door") or {}).get("response")}
    a, b = _w(one), _w(two)
    unread1 = a["status"].startswith(("research inconclusive",
                                       "provider words only",
                                       "no origin read", "no-door",
                                       "status-unspoken"))
    read2 = b["status"].startswith("carried by")
    improved = (b["read"] > a["read"] or b["origins"] > a["origins"]
                or (unread1 and read2))
    why = []
    if b["read"] > a["read"]:
        why.append("read origins rose (%d -> %d)" % (a["read"], b["read"]))
    if b["origins"] > a["origins"]:
        why.append("distinct voices rose (%d -> %d)"
                   % (a["origins"], b["origins"]))
    if unread1 and read2:
        why.append("the A15 word moved to a READ origin")
    if not improved:
        why.append("no declared leg moved (a VALID finding, printed as one)")
    return {"gap": gap,
            "query_ridden": (two.get("web") or {}).get("query"),
            "improved": improved, "why": why,
            "changed": {
                "urls": [a["urls"], b["urls"]],
                "read": [a["read"], b["read"]],
                "origins": [a["origins"], b["origins"]],
                "independence": [a["independence"], b["independence"]],
                "status": [a["status"], b["status"]],
                "urls_gained": sorted(set(b["seen"]) - set(a["seen"])),
                "urls_lost": sorted(set(a["seen"]) - set(b["seen"])),
                "response_changed": a["response"] != b["response"]}}


def run_cycle(qtext, caps=None, hold_name="a34-cycle.json"):
    """ONE cycle at one entry: stage one (the whole live road), the GAP at
    the record's own words, the follow-up at the A34-C1 law over the
    A22 frozen-query rail, stage two, the byte-comparison; persisted
    through the ONE pen, label LIVE (a cycle rides the net; a replay
    rides bytes, never this road)."""
    caps = caps or (load_doc().get("caps") or {})
    one = run_one(qtext, True, caps)
    one["label"] = "live"
    gap = gap_word(one)
    q2 = follow_query(gap, one)
    two = run_one(qtext, True, caps, query=q2)
    two["label"] = "live"
    cmp = compare_stages(one, two, gap)
    art = {"cycle": "A34-C1", "label": "live",
           "date": time.strftime("%Y-%m-%dT%H:%M:%S"),
           "question": qtext, "gap": gap, "follow_query": q2,
           "compare": cmp, "stage-1": one, "stage-2": two}
    import research
    research.hold(art, hold_name)
    return art


def status_word(rec):
    # A19: main's readable line SELECTS the word the RECORD already
    # carries (never the answer's prose, never the trace). A run whose
    # door never rode (the search-only mode) says so; a door record whose
    # trace left the word un-spoken (a pre-A15 shape, the over-budget
    # lane) says so; neither ever leans toward VERIFIED.
    d = rec.get("door")
    if d is None:
        return "no-door (search-only)"
    s = d.get("evidence_status")
    return s if s else "status-unspoken"


def main(argv):
    live = "--search" not in argv
    doc = load_doc()
    caps = doc.get("caps") or {}
    rec = {"eval": doc.get("eval"),
           "mode": "live" if live else "search-only",
           "provider": web_research.provider_name(),
           "caps": caps, "date": time.strftime("%Y%m%d"),
           "review": "operator (the A5 hand; same brain that wrote the "
                     "code - disclosed, not independent)",
           "questions": []}
    for q in doc.get("questions") or []:
        # A22: a question may carry its own FROZEN retrieval query; the
        # A5 fixture carries none, so every question rides the old road
        # byte-exact (run_one's fallback = the question's own bytes).
        r = run_one(q["question"], live, caps, q.get("query"))
        r["id"] = q.get("id")
        r["kind"] = q.get("kind")
        r["expect"] = q.get("expect")
        rec["questions"].append(r)
        d = r.get("door")
        print(r["id"], "| ok:", r["web"]["ok"], "| results:", r["web"]["results"],
               "| gaps:", r["web"]["gaps"], "| indep:",
               r["web"]["corroboration"]["independence"],
               "| lane:", (d or {}).get("lane"),
               "| calls:", (d or {}).get("model_calls"),
               "| status:", status_word(r),
               "| query:", r["web"].get("query"),
               "| %.1fs" % r["secs"])
    out = os.path.join(HERE, "research-hold",
                       "a5-eval-live.json" if live else "a5-eval-search.json")
    open(out, "w").write(json.dumps(rec, indent=1))
    print("wrote", out)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
