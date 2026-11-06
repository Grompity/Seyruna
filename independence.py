#!/usr/bin/env python3
"""independence.py - A50's independence and corroboration model.

A PURE classifier over evidence records. It retrieves nothing, fetches
nothing, and imports nothing that can reach the network. It answers six
separate questions and never collapses them into a score or a ladder:

  attribution      are DIFFERENT named attribution terminals visible?
  underlying       are the underlying source materials demonstrably distinct?
  editorial        were the works independently researched/assembled?
  institutional    are the source-production processes institutionally independent?
  observational    do the sources derive from separate observations/records?
  corroboration    do multiple chains independently support the same claim?

The law, in one sentence: a different author, citation, publisher,
institution, date, domain or wording is NEVER independence, and the
absence of a discovered dependency is NOT independence.

Case schema (JSON):
  {
    "id": "case-name",
    "chains": {"W": {"terminals": ["w:olivelle"]}, "C": {...}},
    "terminals": {"w:olivelle": {"label": "Olivelle 2024",
                                 "kind": "work|translation|edition|document|
                                          dataset|observation|unknown",
                                 "status": "COMPLETE|PARTIAL|UNRESOLVED",
                                 "publisher": optional, "institution": optional}},
    "relations": [{"id": "r1", "type": <RELATION_EFFECTS key>,
                   "a": "w:olivelle", "b": "c:dhammika",
                   "evidence": "why this relation is recorded"}],
    "claims": [{"id": "claim-1", "text": "...",
                "supports": ["W", "C"], "agreement": "AGREE|CONFLICT|UNKNOWN"}],
    "facts": [optional human-readable statements - never read by the model]
  }

The model follows only what is recorded. It does not read prose, does not
match labels, and does not infer a relation because two sources share a
subject.
"""
import json
import os
import sys

DIMENSIONS = ("attribution", "underlying", "editorial", "institutional",
              "observational", "corroboration")
STATUSES = ("SUPPORTED", "CONTRADICTED", "UNKNOWN")

# The per-dimension relation effect table, frozen in a50-contract.md.
RELATION_EFFECTS = {
    "shares-edition": {"underlying": "CONTRADICTED"},
    "translation-ancestor": {"underlying": "CONTRADICTED"},
    "derives-from": {"underlying": "CONTRADICTED"},
    "same-underlying-work": {"underlying": "CONTRADICTED"},
    "same-primary-document": {"underlying": "CONTRADICTED",
                              "observational": "CONTRADICTED"},
    "same-dataset": {"underlying": "CONTRADICTED",
                     "observational": "CONTRADICTED"},
    "same-observation": {"underlying": "CONTRADICTED",
                         "observational": "CONTRADICTED"},
    "independent-underlying": {"underlying": "SUPPORTED"},
    "independent-editorial": {"editorial": "SUPPORTED"},
    "shared-editorial-control": {"editorial": "CONTRADICTED"},
    "independent-institutional": {"institutional": "SUPPORTED"},
    "shared-funder": {"institutional": "CONTRADICTED"},
    "shared-commissioner": {"institutional": "CONTRADICTED"},
    "shared-institutional-control": {"institutional": "CONTRADICTED"},
    "independent-observation": {"observational": "SUPPORTED"},
    "unknown-derivation": {"note": "unknown"},
}

MATERIAL = ("shares-edition", "translation-ancestor", "derives-from",
            "same-underlying-work", "same-primary-document", "same-dataset",
            "same-observation")
OBSERVATION = ("same-primary-document", "same-dataset", "same-observation")
EDITORIAL = ("shared-editorial-control",)
INSTITUTIONAL = ("shared-funder", "shared-commissioner",
                 "shared-institutional-control")
SUPPORT_TYPE = {"underlying": "independent-underlying",
                "editorial": "independent-editorial",
                "institutional": "independent-institutional",
                "observational": "independent-observation"}
GRAPH = {"underlying": MATERIAL, "observational": OBSERVATION,
         "editorial": EDITORIAL, "institutional": INSTITUTIONAL}

ATTRIBUTION_LABEL = {
    "SUPPORTED": "DISTINCT-STATED-ATTRIBUTIONS",
    "CONTRADICTED": "EXPLICIT-SHARED-ATTRIBUTION",
    "UNKNOWN": "UNKNOWN",
}


# ---------- a tiny union-find + path evidence (no graph dependency) ----------
def _graph(relations, types):
    parent, adj = {}, {}
    def find(x):
        parent.setdefault(x, x)
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for r in relations:
        if r["type"] not in types:
            continue
        a, b = r["a"], r["b"]
        adj.setdefault(a, set()).add(b)
        adj.setdefault(b, set()).add(a)
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb
    return find, adj


def _path_evidence(adj, relations, types, a, b):
    """The relation ids on the shortest documented path a..b, or None. Only
    the relations that BUILD this graph may be cited as its evidence - a
    supporting record must never leak into a contradiction list."""
    if a == b:
        return []
    edge = {}
    for r in relations:
        if r["type"] not in types:
            continue
        edge.setdefault((r["a"], r["b"]), []).append(r["id"])
        edge.setdefault((r["b"], r["a"]), []).append(r["id"])
    seen, q = {a}, [(a, [])]
    while q:
        node, ids = q.pop(0)
        for nxt in sorted(adj.get(node, ())):
            if nxt in seen:
                continue
            nids = ids + edge.get((node, nxt), [])
            if nxt == b:
                return sorted(set(nids))
            seen.add(nxt)
            q.append((nxt, nids))
    return None


def _linked(a_ids, b_ids, find):
    """The first terminal pair in one material component (or equal ids)."""
    for x in a_ids:
        for y in b_ids:
            if x == y or find(x) == find(y):
                return (x, y)
    return None


# ---------- attribution: a count of DIFFERENT named terminals ----------
def _named(term):
    return (term.get("status") in ("COMPLETE", "PARTIAL")
            and bool(term.get("label")))


def _attribution(case):
    chains = case["chains"]
    terms = case["terminals"]
    named, missing = {}, []
    for cid in sorted(chains):
        ids = [t for t in chains[cid].get("terminals") or []
               if _named(terms.get(t) or {})]
        named[cid] = ids
        if not ids:
            missing.append(cid)
    if len(named) < 2:
        return {"dimension": "attribution", "status": "UNKNOWN",
                "label": "UNKNOWN", "evidence": {"supports": [],
                                                 "contradicts": []},
                "why": "fewer than two chains are in the case"}
    if missing:
        return {"dimension": "attribution", "status": "UNKNOWN",
                "label": "UNKNOWN", "evidence": {"supports": [],
                                                 "contradicts": []},
                "why": "chain(s) without a named terminal: " +
                       ", ".join(missing)}
    ids = [cid for cid in sorted(named)]
    shared = sorted({x for i, a in enumerate(ids) for b in ids[i + 1:]
                     for x in set(named[a]) & set(named[b])})
    if shared:
        return {"dimension": "attribution", "status": "CONTRADICTED",
                "label": ATTRIBUTION_LABEL["CONTRADICTED"],
                "evidence": {"supports": [], "contradicts": shared},
                "why": "the same terminal id appears in more than one "
                       "chain: " + ", ".join(shared)}
    return {"dimension": "attribution", "status": "SUPPORTED",
            "label": ATTRIBUTION_LABEL["SUPPORTED"],
            "evidence": {"supports": sorted({x for v in named.values()
                                             for x in v}),
                         "contradicts": []},
            "why": "; ".join("%s = [%s]" % (c, ", ".join(named[c]))
                             for c in ids)}


# ---------- the pairwise dimensions ----------
def _pair_dimension(kind, a, b, a_ids, b_ids, relations, find, adj):
    con_types = GRAPH[kind]
    support = SUPPORT_TYPE[kind]
    link = _linked(a_ids, b_ids, find)
    con_ids = []
    if link and link[0] == link[1]:
        # the SAME terminal id stands in both chains - the strongest form of
        # shared material; there is no relation to cite, so the identity is
        # the evidence and it is named as such.
        con_ids = ["identity:" + link[0]]
    elif link:
        con_ids = _path_evidence(adj, relations, con_types,
                                 link[0], link[1]) or []
    sup_ids = sorted(r["id"] for r in relations
                     if r["type"] == support
                     and ((r["a"] in a_ids and r["b"] in b_ids)
                          or (r["b"] in a_ids and r["a"] in b_ids)))
    if con_ids and sup_ids:
        status, conflict = "UNKNOWN", True
        why = ("both support and contradiction are recorded for this pair; "
               "the conflict is preserved")
    elif con_ids:
        status, conflict = "CONTRADICTED", False
        why = "a documented dependency path links the chains"
    elif sup_ids:
        status, conflict = "SUPPORTED", False
        why = "an explicit independent-%s record qualifies this pair" % kind
    else:
        status, conflict = "UNKNOWN", False
        why = ("no record documents either independence or dependence for "
               "this pair")
    return {"status": status, "conflict": conflict, "why": why,
            "evidence": {"supports": sup_ids, "contradicts": sorted(con_ids)},
            "linked-terminal-pair": list(link) if link else None}


def _dimension(kind, case):
    chains = case["chains"]
    terms = case["terminals"]
    relations = case["relations"]
    find, adj = _graph(relations, GRAPH[kind])
    cids = sorted(chains)
    pairs = {}
    for i, a in enumerate(cids):
        for b in cids[i + 1:]:
            pairs["%s|%s" % (a, b)] = _pair_dimension(
                kind, a, b,
                chains[a].get("terminals") or [],
                chains[b].get("terminals") or [], relations, find, adj)
    statuses = [p["status"] for p in pairs.values()]
    conflict = any(p["conflict"] for p in pairs.values())
    if not pairs:
        status = "UNKNOWN"
        why = "fewer than two chains are in the case"
    elif conflict:
        status = "UNKNOWN"
        why = "conflicting records leave at least one pair unresolved"
    elif "CONTRADICTED" in statuses:
        status = "CONTRADICTED"
        why = "at least one pair is demonstrably NOT independent"
    elif all(s == "SUPPORTED" for s in statuses):
        status = "SUPPORTED"
        why = "every pair carries an explicit independence record"
    else:
        status = "UNKNOWN"
        why = "at least one pair has no qualifying evidence"
    sup = sorted({x for p in pairs.values()
                  for x in p["evidence"]["supports"]})
    con = sorted({x for p in pairs.values()
                  for x in p["evidence"]["contradicts"]})
    return {"dimension": kind, "status": status, "conflict": conflict,
            "pairs": pairs, "evidence": {"supports": sup,
                                         "contradicts": con},
            "why": why}


# ---------- corroboration: one declared claim, two qualified chains --------
def _corroboration(case, dims):
    claims = case.get("claims") or []
    if not claims:
        return {"dimension": "corroboration", "status": "UNKNOWN",
                "conflict": False, "claims": {},
                "evidence": {"supports": [], "contradicts": []},
                "why": "no material claim is declared, so nothing can be "
                       "corroborated"}
    out = {}
    for claim in claims:
        chains = list(claim.get("supports") or [])
        agreement = claim.get("agreement") or "UNKNOWN"
        pairs, missing = {}, []
        for i, a in enumerate(sorted(chains)):
            for b in sorted(chains)[i + 1:]:
                key = "%s|%s" % tuple(sorted((a, b)))
                u = dims["underlying"]["pairs"].get(key)
                o = dims["observational"]["pairs"].get(key)
                if u is None or o is None:
                    missing.append(key)
                    continue
                pairs[key] = {"underlying": u["status"],
                              "observational": o["status"],
                              "evidence": sorted(set(u["evidence"]["supports"]
                                                     + u["evidence"]["contradicts"]
                                                     + o["evidence"]["supports"]
                                                     + o["evidence"]["contradicts"]))}
        if len(chains) < 2:
            status, why = "UNKNOWN", "fewer than two chains support the claim"
        elif agreement == "CONFLICT":
            status, why = "CONTRADICTED", "the declared sources CONFLICT on " \
                                          "the claim; agreement is required"
        elif agreement != "AGREE":
            status, why = "UNKNOWN", "the claim's agreement is not declared"
        elif missing:
            status, why = "UNKNOWN", "no pair record exists for " + \
                                     ", ".join(sorted(missing))
        elif any(p["underlying"] == "CONTRADICTED"
                 or p["observational"] == "CONTRADICTED"
                 for p in pairs.values()):
            status, why = "CONTRADICTED", ("a documented dependency makes at "
                                           "least one supporting chain NOT "
                                           "independent")
        elif all(p["underlying"] == "SUPPORTED"
                 and p["observational"] == "SUPPORTED"
                 for p in pairs.values()):
            status, why = "SUPPORTED", ("every supporting pair is SUPPORTED on "
                                        "underlying AND observational, on one "
                                        "declared claim")
        else:
            status, why = "UNKNOWN", ("at least one supporting pair lacks the "
                                      "independence evidence corroboration "
                                      "requires")
        out[claim.get("id") or "claim"] = {
            "status": status, "why": why, "pairs": pairs,
            "agreement": agreement}
    statuses = [c["status"] for c in out.values()]
    if "SUPPORTED" in statuses and "CONTRADICTED" in statuses:
        status, conflict = "UNKNOWN", True
        why = "one claim is corroborated and another is contradicted; the " \
              "conflict is preserved"
    elif "SUPPORTED" in statuses:
        status, conflict = "SUPPORTED", False
        why = "at least one declared material claim is independently " \
              "supported"
    elif "CONTRADICTED" in statuses:
        status, conflict = "CONTRADICTED", False
        why = "no claim reaches corroboration and at least one is contradicted"
    else:
        status, conflict = "UNKNOWN", False
        why = "no declared claim has the evidence corroboration requires"
    sup = sorted({x for c in out.values() for p in c["pairs"].values()
                  for x in p["evidence"]
                  if x in dims["underlying"]["evidence"]["supports"]
                  or x in dims["observational"]["evidence"]["supports"]})
    con = sorted({x for c in out.values() for p in c["pairs"].values()
                  for x in p["evidence"]})
    con = [x for x in con if x not in sup]
    return {"dimension": "corroboration", "status": status,
            "conflict": conflict, "claims": out,
            "evidence": {"supports": sup, "contradicts": con},
            "why": why}


# ---------- dependency surface ----------
def _dependencies(case):
    terms = case["terminals"]
    out, unknown = [], []
    for r in sorted(case["relations"], key=lambda x: x["id"]):
        item = {"relation": r["id"], "type": r["type"],
                "a": r["a"], "b": r["b"],
                "a-label": (terms.get(r["a"]) or {}).get("label", r["a"]),
                "b-label": (terms.get(r["b"]) or {}).get("label", r["b"]),
                "evidence": r.get("evidence", "")}
        (unknown if r["type"] == "unknown-derivation" else out).append(item)
    return out, unknown


def _next_evidence(dims, deps, unknown):
    hints = []
    if dims["attribution"]["status"] != "SUPPORTED":
        hints.append("name at least one attribution terminal per chain")
    if dims["underlying"]["status"] != "SUPPORTED":
        hints.append("record whether the works share an edition, translation "
                     "ancestor, dataset, primary document or observation")
    if dims["editorial"]["status"] != "SUPPORTED":
        hints.append("record independent editorial process, or shared "
                     "editorial control")
    if dims["institutional"]["status"] != "SUPPORTED":
        hints.append("record independent production, or shared funding, "
                     "commissioning or control")
    if dims["observational"]["status"] != "SUPPORTED":
        hints.append("record whether the sources derive from separate "
                     "observations or the same record")
    if dims["corroboration"]["status"] != "SUPPORTED":
        hints.append("declare one material claim supported by two or more "
                     "chains and qualify their independence")
    if unknown:
        hints.append("resolve the recorded unknown derivation(s): " +
                     ", ".join(u["relation"] for u in unknown))
    return hints


# ---------- assess + explain ----------
def assess(case):
    """Classify the case. Pure and deterministic; no I/O except the values
    already in the case dict."""
    for key in ("chains", "terminals", "relations"):
        if key not in case:
            raise ValueError("case is missing %r" % key)
    for r in case["relations"]:
        if r.get("type") not in RELATION_EFFECTS:
            raise ValueError("unknown relation type %r" % r.get("type"))
        if not r.get("id") or "a" not in r or "b" not in r:
            raise ValueError("relation needs id, a and b")
    dims = {"attribution": _attribution(case)}
    for kind in ("underlying", "editorial", "institutional", "observational"):
        dims[kind] = _dimension(kind, case)
    dims["corroboration"] = _corroboration(case, dims)
    deps, unknown = _dependencies(case)
    indep_ev = (dims["underlying"]["status"] == "SUPPORTED"
                and dims["observational"]["status"] == "SUPPORTED")
    return {"case": case.get("id", "unnamed"),
            "dimensions": dims,
            "dependencies": deps,
            "unknown-derivations": unknown,
            "independent-evidence": indep_ev,
            "independent-corroboration":
                dims["corroboration"]["status"] == "SUPPORTED",
            "unresolved": [d for d in DIMENSIONS
                           if dims[d]["status"] != "SUPPORTED"],
            "next-evidence": _next_evidence(dims, deps, unknown)}


def explain(result):
    """Concise, report-ready text. It never lets attribution diversity read
    as independent evidence or corroboration."""
    dims = result["dimensions"]
    att = dims["attribution"]
    lines = ["INDEPENDENCE - %s" % result["case"]]
    if att["status"] == "SUPPORTED":
        lines.append("  different attributions: %s (attribution only; NOT "
                     "independent evidence)" % att["label"])
    else:
        lines.append("  different attributions: %s (%s)"
                     % (att["label"], att["status"]))
    lines.append("  independent evidence: %s"
                 % ("ESTABLISHED" if result["independent-evidence"]
                    else "NOT ESTABLISHED"))
    lines.append("  independent corroboration: %s"
                 % ("ESTABLISHED" if result["independent-corroboration"]
                    else "NOT ESTABLISHED"))
    for d in ("underlying", "editorial", "institutional", "observational",
              "corroboration"):
        dim = dims[d]
        lines.append("  %s: %s - %s" % (d, dim["status"], dim["why"]))
    if result["dependencies"]:
        lines.append("  dependencies: " + "; ".join(
            "%s %s %s" % (x["a-label"], x["type"], x["b-label"])
            for x in result["dependencies"]))
    else:
        lines.append("  dependencies: none documented")
    if result["unknown-derivations"]:
        lines.append("  unknown derivations: " + ", ".join(
            x["relation"] for x in result["unknown-derivations"]))
    if result["next-evidence"]:
        lines.append("  to resolve: " + "; ".join(result["next-evidence"]))
    return "\n".join(lines)


# ---------- the A49 regression case (deterministic, no retrieval) ----------
A49_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "research-hold", "a49-citation-replay.json")


def case_from_a49(path=None):
    """Build the A49 case from the HELD RECORD only. It reads no page, follows
    no link, and does not chase #CITEREFLe2010. Relations stay EMPTY because
    A49 documented none; an empty list is not independence - it is UNKNOWN."""
    art = json.loads(open(path or A49_PATH).read())
    bib = art["bibliographic"]
    terms = {}
    w_ids = []
    for k in ("1", "2", "3"):
        b = bib[k]
        label = {1: "Le 2010 (partial)", 2: "Olivelle 2024",
                 3: "Singh 2008"}[int(k)]
        tid = "w:" + label.split()[0].lower()
        w_ids.append(tid)
        t = {"label": label, "kind": "work", "status": b["completeness"]}
        if b.get("publisher"):
            t["publisher"] = b["publisher"]
        if k == "1":
            t["work"] = ("UNKNOWN (the entry points to #CITEREFLe2010; not "
                         "followed)")
        terms[tid] = t
    c_ids, c_labels = [], {
        "H.G. Wells": ("c:wells", "H.G. Wells", "work", "COMPLETE"),
        "Dhammika": ("c:dhammika", "Ven. S. Dhammika / the present rendering",
                     "translation", "COMPLETE"),
        "earlier translations": ("c:earlier-translations",
                                 "earlier translations (unnamed)", "unknown",
                                 "UNRESOLVED"),
        "Buddhist literature": ("c:buddhist-literature",
                                "Buddhist literature (legend carrier)",
                                "unknown", "UNRESOLVED"),
    }
    seen = set()
    for row in art["comparisons"]:
        sig = row["vs-C"]
        if sig in seen:
            continue
        seen.add(sig)
        tid, label, kind, status = c_labels[sig]
        c_ids.append(tid)
        terms[tid] = {"label": label, "kind": kind, "status": status}
    return {
        "id": "a49-w-vs-c",
        "source": {
            "artifact": "research-hold/a49-citation-replay.json",
            "policy-digest": art["policy-digest"],
            "label": art["label"],
        },
        "chains": {"W": {"terminals": w_ids}, "C": {"terminals": c_ids}},
        "terminals": terms,
        "relations": [],
        "claims": [],
        "facts": [
            "W's named terminals are Olivelle 2024, Singh 2008 and the "
            "PARTIAL Le 2010 note.",
            "Le 2010's work-level comparison is UNRESOLVED; #CITEREFLe2010 "
            "was recorded but NOT followed.",
            "No primary edition or translation of the edicts appears among "
            "W's three recovered entries.",
            "C's named terminals are Dhammika and Wells; 'earlier "
            "translations' and 'Buddhist literature' remain unnamed.",
            "No visible connection to C's signals was found in W's entries.",
            "Underlying overlap, editorial, institutional and observational "
            "independence are UNKNOWN.",
            "No shared material claim was evaluated, so corroboration is "
            "UNKNOWN.",
        ],
    }


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    as_json = "--json" in argv
    argv = [a for a in argv if a != "--json"]
    if not argv or argv[0] == "--a49":
        case = case_from_a49()
    else:
        doc = json.loads(open(argv[0]).read())
        case = doc.get("case") if isinstance(doc, dict) and "case" in doc \
            else doc
    result = assess(case)
    print(json.dumps(result, indent=1, sort_keys=True) if as_json
          else explain(result))
    return 0


if __name__ == "__main__":
    sys.exit(main())
