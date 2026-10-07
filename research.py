# research.py — the RESEARCH AGENT: the blessed charter, one module.
# Founder authorization at ARCHITECTURE rank — not law, not an amendment.
# The role, in its own words:
#   one bounded task -> designated retrieval -> a provenance-preserving
#   research artifact -> Ascended / human evaluation.
# A WORKER role, not an authority: it GRANTS nothing — no admission, no
# promotion, no membership, no standing, no DO (RP-12 stands: the office is
# not installed; "a permission in law is a door, not a tenant"). The shelf
# grows by ADMISSION, not by ARRIVAL — and admission itself stays documented
# practice awaiting its own word: this module neither grants nor implies it.
# Two founder corrections, binding: human research precedent does not itself
# authorize agent DELEGATION (the blessing is the delegation); the standing
# to displease is an EVALUATION requirement, not a permission here.
# The HOLDING AREA is disposable, founder-controlled storage — not the Bench,
# not the Shelf, not an installed stage; it may be deleted wholesale.
# No new organ: no registry, no bus, no provider abstraction, no tool
# framework, no second provenance system (the existing words ride the rows),
# no second pipeline. DRY BY DESIGN: the agent's mouth is not ambient — the
# existing call()/config seam stands for whoever one day wants synthesis;
# today the agent speaks in typed rows and the CALLS ledger proves it.
# The RUNG rides UNASSIGNED — the Report's grammar: an absent grant is NOT a
# ladder-value; absent is silence (K2), never UNKNOWN(-1).
# The law's own leash stays above the file: "Retrieval before authority.
# Never generate a citation" — what is not designated is not reached; what is
# not fetched by the designated path is a GAP, not a failure.

import json
import os

import stages

BUILD = "research-0.1"
HOLD_DIR = os.path.join(stages.BASE_DIR, "research-hold")
STATUSES = ("DONE", "THIN", "CONTENDING", "EMPTY")      # all four are passes
COPIES = ("work", "who", "date", "loculus", "provenance", "evidence",
          "counterexample")                              # the shelf's words


def read_guard(path):
    # The bridge's rule, adopted whole: root-relative; '..' REJECTED; no
    # arbitrary filesystem authority — a designation may not escape the root.
    return bool(path) and ".." not in path and not path.startswith("/")


def default_fetch(s):
    # The reach IS the designation, never ambient: "text" already provided,
    # "file" read at the repo's root, "url" demanding an injected fetcher
    # (no arbitrary network). No designation, no fetch: a GAP.
    if "text" in s:
        return {"fetched": s["text"]}
    if "file" in s:
        if not read_guard(s["file"]):
            return {"gap": "out-of-bounds"}
        try:
            with open(os.path.join(stages.BASE_DIR, s["file"])) as fh:
                return {"fetched": fh.read()}
        except OSError:
            return {"gap": "fetch-failed"}
    if "url" in s:
        return {"gap": "network-not-designated"}
    return {"gap": "no-designation"}


def run(task, fetch=None):
    """One bounded task, one pass: rows in the shelf's own words; a field
    absent is SILENCE, never a zero (K2's law, held whole here)."""
    f = fetch or default_fetch
    rows, gaps = [], []
    for s in task.get("designated") or []:
        out = f(s)
        if "gap" in out:
            gaps.append("gap:" + out["gap"] + ":" + str(s.get("id", "?")))
            continue
        row = {"id": str(s.get("id", "S%d" % (len(rows) + 1))),
               "captured": out.get("fetched") or "",
               "edges": list(s.get("edges") or [])}
        for k in COPIES:                    # COPIED, never GENERATED —
            if k in s:                      # the current path must be treated
                row[k] = s[k]               # as lying about sources until
        rows.append(row)                    # retrieval proves otherwise
    ids = [r["id"] for r in rows]
    # THE JOINING (ours, and always marked as ours): two captures at least
    # may compare; one does not join. The boundary re-armed at the agent:
    # a cite outside the FETCHED set dies here, noted (T36's shape).
    syn = None
    if len(rows) >= 2:
        cites = [str(c) for c in task.get("synthesis_cites") or ids]
        syn = {"id": "RS", "provenance": "ours-synthesis",
               "cites": [c for c in cites if c in ids],
               "lineage": "SYNTHESIS: comparison from " + "+".join(ids)}
        dropped = [c for c in cites if c not in ids]
        if dropped:
            syn["cite_dropped"] = dropped
    # THE STATUS ARITHMETIC (the agent's sibling of answerability):
    # EMPTY is the RP-10 shape — "that is an answer, not a failure";
    # a conflict is PRESERVED (contending), never smoothed into a merge.
    min_sources = (task.get("bounds") or {}).get("min_sources", 1)
    contending = any(e.get("type") == "CONTRADICTS" and e.get("to") in ids
                     for r in rows for e in r["edges"])
    status = ("EMPTY" if not rows else
              "CONTENDING" if contending else
              "THIN" if len(rows) < min_sources else "DONE")
    return {"task_id": task["id"], "status": status, "rows": rows,
            "synthesis": syn, "gaps": gaps,
            "run": dict(stages.CONFIG["versions"],                        # the
                        model=stages.CONFIG["MODEL"], build=BUILD)}      # stamp


LIVE_SYS = (
    "You may say plainly what the shown sources say; you may not claim more "
    "than the sources. Join only what you were shown. Cite only ids you were "
    "shown - never from memory (the shown set IS your retrieval). You have no "
    "rank here: your sentence is ours, and ours only under this joining.")


def _sources_text(art):
    # The mouth's packet (the SYNTHESIS-EVAL shape, reused at the agent's
    # address): [id] (work | loculus): captured - loculus when present (K2:
    # absent is silence), captured verbatim (the fetcher's bytes ARE the
    # source; the mouth must not launder them).
    out = []
    for r in art["rows"]:
        line = "[" + str(r["id"]) + "] "
        if r.get("work"):
            line += "(" + str(r["work"])
            line += (" | " + str(r["loculus"])) if r.get("loculus") else ""
            line += "): "
        line += str(r.get("captured", ""))
        out.append(line)
    return "\n".join(out)


def live(task, fetch=None, mouth=None):
    """THE LIVE PATH - one mouthful over the fetched set, nothing more.
    The boundary is the shape: the mouth may ADD the join's sentence and
    cites (the T36 law stands - a cite outside the fetched set dies, noted);
    it may change NO else. STATUS IS COMPUTED, NOT ASSERTED - the contract
    has no status field, so the worker cannot promote itself by prose.
    EMPTY rides plain (no mouth - the RP-10 shape); one source does not
    join and therefore does not speak (the dry law stands). A mouth
    failure is LANED (synthesis:fell-back), never re-raised, never a
    promotion (the empty-completion lesson). Model-neutral: stages.call is
    the seam and is never NAMED here."""
    call = mouth or stages.call
    art = run(task, fetch)
    if not art["rows"] or art["synthesis"] is None:
        return art
    ids = [r["id"] for r in art["rows"]]
    out = call(LIVE_SYS,
               "TASK: " + str(task.get("description") or task["id"])
               + "\nBOUNDS: min_sources="
               + str((task.get("bounds") or {}).get("min_sources", 1))
               + "\nSOURCES:\n" + _sources_text(art)
               + "\nRespond ONLY with JSON: {\"node\": \"one plain sentence\","
                 " \"cites\": [ids shown]}")
    syn = art["synthesis"]
    try:
        row = stages.grab_json(out.get("content") or "", "{")
        node = (row.get("node") or "").strip()
        cites = [str(c) for c in (row.get("cites") or [])]
    except (ValueError, AttributeError, TypeError):
        syn["notes"] = (syn.get("notes") or []) + ["synthesis:fell-back"]
        return art
    if node:
        syn["node"] = node
    if "cites" in row:
        syn["cites"] = [c for c in cites if c in ids]
        dead = [c for c in cites if c not in ids]
        if dead:
            syn["cite_dropped"] = (syn.get("cite_dropped") or []) + dead
    return art


def hold(artifact, name, to=None):
    """The single write-path: a disposable row to the founder's storage.
    The protected bytes (root) answer the agent's pen with a refusal — the
    agent does not commit, push, deploy, or modify itself."""
    d = to or HOLD_DIR
    if not read_guard(name):
        return "refused: outside the holding area (the name escapes the root)"
    if os.path.abspath(d) == os.path.abspath(stages.BASE_DIR):
        return "refused: outside the holding area (the root is where the protected bytes live)"
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, name), "w") as fh:
        fh.write(json.dumps(artifact) + "\n")
    return artifact
