# window.py — the WINDOW. One pure reading of the trace: no second
# reasoning system, no new truth, no reading-back of the response text
# to find reasons (the trace's own protocol applies to the product).
# Six lanes, each fed ONLY by recorded bytes:
#   EVIDENCE  <- trace["retrieval"] x the shelf rows (claim, level,
#               kind WHEN PRESENT — absent is silence, K2's law)
#   DISTINCTION <- the shown records' own level/kind fields (data)
#   DISAGREEMENT <- shelf edges BETWEEN shown records, plus the
#               machine's own RP-13 notes among the observations
#   UNCERTAINTY <- the unknown flag, the non-RP-13 observations, the
#               appended caution, the required-content survival
#   SYNTHESIS <- each draft node's lineage label + cites (+ the
#               cite_drop, the boundary's mark, when present)
#   BOUNDARY  <- the blocked arm, the guard firings, the repair ops,
#               the audit's count — WHY the claim is no stronger
# The EARLY-RETURN trace (empty retrieval: only versions/retrieval/
# fires/unknown/response) must read through every lane without a raise.

def why_lane(trace, by_id=None):
    import stages  # late import: the window sits ABOVE the spine
    BY = stages.BY_ID if by_id is None else by_id
    ids = trace.get("retrieval") or []

    evidence = []
    levels, kinds = {}, {}
    for i in ids:
        r = BY.get(i) or {}
        row = {"id": i, "claim": r.get("claim", "?"),
               "level": r.get("level", "?")}
        if r.get("kind"):                      # absent = silence
            row["kind"] = r["kind"]
        evidence.append(row)
        levels[row["level"]] = levels.get(row["level"], 0) + 1
        if "kind" in row:
            kinds[row["kind"]] = kinds.get(row["kind"], 0) + 1

    edges = []
    for row in evidence:
        for e in ((BY.get(row["id"]) or {}).get("edges") or []):
            if e.get("to") in ids:
                edges.append("%s %s %s" % (row["id"], e.get("type"),
                                           e.get("to")))

    obs = trace.get("observations") or []
    disagreement = edges + [o for o in obs if "RP-13" in o]

    uncertainty = []
    if trace.get("unknown"):
        uncertainty.append("the UNKNOWN exit spoke (RP-10): the shown "
                           "set was empty — the mouth was not called")
    uncertainty += [o for o in obs if "RP-13" not in o]
    if trace.get("caution_appended"):
        uncertainty.append("a caution was APPENDED (owed, named once)")
    rc = trace.get("required_content")
    if rc:
        uncertainty.append("required content %s in the final speech (RP-02)"
                           % ("SURVIVES" if rc.get("survives_to_speech")
                              else "DID NOT SURVIVE"))

    synthesis = []
    for nd in (trace.get("draft") or []):
        s = {"lineage": nd.get("lineage") or "UNSOURCED",
             "cites": list(nd.get("cites") or [])}
        if nd.get("cite_dropped"):
            s["cite_dropped"] = list(nd["cite_dropped"])
        synthesis.append(s)

    boundary = []
    if trace.get("blocked"):
        boundary.append("blocked: no node carried a cite; the plain "
                        "lane spoke instead")
    boundary += ["fired: " + f for f in (trace.get("fires") or [])]
    boundary += ["repaired: " + o for o in (trace.get("repair_ops") or [])]
    if trace.get("audit_findings"):
        boundary.append("audit recorded %d finding(s)"
                        % len(trace["audit_findings"]))

    return {"lane": trace.get("lane", "retrieval"),
            "evidence": evidence,
            "distinction": {"levels": levels, "kinds": kinds},
            "disagreement": disagreement,
            "uncertainty": uncertainty,
            "synthesis": synthesis,
            "boundary": boundary}
