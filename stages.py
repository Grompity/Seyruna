# stages.py — Ascended prototype v0.1: the pipeline, one file.
# Law D4-rev-a; rule-pack RP-0.4 (data); voice VB-0.3 (blessed);
# schema KS-0.1. Deterministic-first: the mouths are stage 4 (synth)
# and the optional audit pass; everything else is code.
# The caller is the proven pilot/sg_test pattern (SGLang, stdlib only).

import json
import os
import ssl
import time
import urllib.request

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG = json.load(open(os.path.join(BASE_DIR, "config.json")))
RP = json.load(open(os.path.join(BASE_DIR, "rule_pack.json")))
P = RP["params"]
VB = open(os.path.join(BASE_DIR, "voice_brief.md")).read()

def _load_shelf():
    recs = []
    with open(os.path.join(BASE_DIR, "shelf.jsonl")) as fh:
        for line in fh:
            line = line.strip()
            if line and not line.startswith("//"):
                recs.append(json.loads(line))
    return recs

SHELF = _load_shelf()
BY_ID = {r["id"]: r for r in SHELF}

def set_shelf(recs):
    global SHELF, BY_ID
    SHELF = recs
    BY_ID = {r["id"]: r for r in recs}

_PC = getattr(time, "perf_counter", time.time)
CALLS = [0]   # the mouth's calls per run - the battery's own instrument,
# moved INTO the spine so every live request carries its ledger (§6)

CTX = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE

def call(system, user, maxtok=None):
    """One mouthful. Returns {content, reasoning, truncated}."""
    CALLS[0] += 1
    body = {"model": CONFIG["MODEL"],
            "messages": [{"role": "system", "content": system},
                         {"role": "user", "content": user}],
            "max_tokens": maxtok or CONFIG["MAXTOK"],
            "temperature": CONFIG["TEMP"]}
    req = urllib.request.Request(
        CONFIG["BASE"] + "/chat/completions",
        data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json",
                 "Authorization": "Bearer " + CONFIG["KEY"]})
    for attempt in (1, 2, 3):
        try:
            with urllib.request.urlopen(req, timeout=300, context=CTX) as r:
                data = json.loads(r.read().decode())
            ch = data["choices"][0]
            msg = ch["message"]
            return {"content": (msg.get("content") or "").strip(),
                    "reasoning": (msg.get("reasoning_content") or "").strip(),
                    "truncated": ch.get("finish_reason") == "length"}
        except Exception as exc:
            if attempt == 3:
                return {"content": "[MOUTH ERROR: %s]" % exc,
                        "reasoning": "", "truncated": False}
            time.sleep(4)

def grab_json(text, opener):
    lo, hi = (opener, {"[": "]", "{": "}"}[opener])
    a, b = text.find(lo), text.rfind(hi)
    if a < 0 or b < 0:
        raise ValueError("no JSON %s found in: %r" % (opener, text[:200]))
    return json.loads(text[a:b + 1])

LEVEL_RANK = {"EMPIRICAL": 4, "DOCUMENTED": 3, "PHILOSOPHICAL": 2,
              "INTERPRETIVE": 1, "INFERENTIAL": 0, "UNKNOWN": -1}
# DOCUMENTED = the founder's word, added as a KS-0.1 ENUM MEMBER
# (machinery; the taxonomy's content belongs to the foundation): what a
# text verifiably says — speakable flat, and no license for the doctrine
# behind it.

def _has(words, text):
    return any(w in text for w in words)

# ---------- stage 1: INTENT (code; the mode never self-licenses)
# Metamorphic guards (machinery, not law): a token counts only at an
# occurrence that is not negated (neg within ~3 words prior) and, for
# triage indicators, not historicized (hist marker within ~45 chars
# prior). The named human further needs REACH (the signed definition:
# reachable-that-day): a window holding both a neg-marker and
# reach/near/available reads NAMED-BUT-UNREACHABLE.
NEG = P["neg_markers"]; HIST = P["hist_markers"]
NEUT = P["neutralizer_words"]

def _occ_ok(low, at, hist_ok, neut_ok=False):
    w = low[max(0, at - 24):at]
    tail = w.replace(",", " ").split()[-3:]
    if any(t in NEG for t in tail):
        return "negated"
    if neut_ok and any(t in NEUT for t in
                       low[at:at + 48].replace(",", " ").split()[:5]):
        return "negated"          # a neutralized mention (letter D: at
                                  # its USUAL level is no notable strain)
    if hist_ok and any((" " + m + " ") in (" " + low[max(0, at - 45):at + 30]
                        + " ") for m in HIST):
        return "historic"
    return "live"

def _counted(low, phrases, hist_ok=False, neut_ok=False):
    for ph in phrases:
        idx = 0
        while True:
            i = low.find(" " + ph + " ", idx)   # token boundaries (letter D)
            if i < 0:
                break
            if _occ_ok(low, i, hist_ok, neut_ok) == "live":
                return True
            idx = i + 1
    return False

def _human_state(low):
    for ph in P["human_tokens"]:
        idx = 0
        while True:
            i = low.find(ph, idx)
            if i < 0:
                break
            win = low[max(0, i - 12):i + 45]
            if _occ_ok(low, i, False) == "live":
                if (("reach" in win or "near" in win or "available" in win)
                        and any((" " + m + " ") in (" " + win + " ")
                                for m in NEG)):
                    return (ph, False)          # named, not reachable
                return (ph, True)
            idx = i + 1
    return (None, None)

def intent(question, facts):
    # THE ONE-TURN BOUNDARY (the continuity round): what rides AFTER the
    # marker is the PRIOR EXCHANGE - the conversation, not the seeker's
    # word. The scan stops at the marker, so no prior word (the mouth's own
    # "alone", the seeker's own yesterday) votes a factor, an indicator, or
    # the human-state; the prompts still read the WHOLE of frame["facts"],
    # so the mouth hears the context it needs and the law counts only what
    # the seeker said. Memory is context, not truth.
    low = (" " + (facts or "").split(P["prior_marker"], 1)[0].lower() + " ")
    flags = {f: _counted(low, P["facts_keywords"][f], False, True)
             for f in P["factors"]}
    inds = {g: _counted(low, kws, True, True)
            for g, kws in P["indicator_keywords"].items()}
    human, reach = _human_state(low)
    return {"question": question, "mode": "knowledge", "factors": flags,
            "indicators": inds, "human": human, "human_reachable": reach,
            "facts": facts or ""}

# ---------- stage 2: RETRIEVE (code over the claim-graph)
STOP = set(P["stop_words"])   # letter C: the finalized vocabulary lives in
# the Rule-Pack now (the debt is paid); the two history lines: the members
# came from the battery's verdict ("two" moved the gate on the retreat
# card; "its" on the near-trigger), and tokenization stays deterministic
# and symmetric (T39b is its witness).

def retrieve(question, k=None):
    # symmetric tokenization (both sides identical; the friend's twin
    # doctrine: "teacher's" must not fail equality to "teacher")
    def toks(s):
        return s.lower().replace("?", " ").replace(".", " ") \
                .replace(",", " ").replace(";", " ") \
                .replace("'", " ").split()
    q = {w for w in toks(question) if w not in STOP and len(w) > 2}
    scored = []
    for r in SHELF:
        words = {w for w in toks(r.get("claim", ""))
                 if w not in STOP and len(w) > 2}
        s = len(q & words)
        if s:
            scored.append((s, r["id"]))
    scored.sort(key=lambda t: (t[0],
                int(t[1]) if t[1].isdigit() else 0),
                reverse=True)   # the gate's finding: multi-digit ids
    # lost ties to the id-STRING (a "19" under an "8"); the expansion's
    # records must not be buried by their own digits (witnessed: T45)
    return [rid for _, rid in scored[:k or CONFIG["TOPK"]]]

# ---------- stage 2b: GRADE (the relevance STATE; the ARCHITECTURE made
# inspectable). RETRIEVED is not RELEVANT: the claim-word generator stands
# EXACTLY as it was (its lexical noise is its nature, not its fault), and
# the grade is a SEPARATE state between it and the conjunction arithmetic -
# a wet classifier, because the overlap that GENERATED a candidate cannot
# also JUSTIFY it (a second code-pass over the same words re-scores and
# proves nothing). Per-record, question-relative, on the trace; it gates
# the packet, feeds analyze's answerability, and is enforced by code over
# data the shelf already owns: a NON-DECISION kind cannot ANSWER (a
# set-aside frames; the refusal is the content, as record 13's tradition
# intends it). Deterministic arms ride the EXISTING patterns: sim_grades
# for the fixture lane; dry default all-ANSWER (the frozen fixtures'
# shown-sets are CHOSEN, not judged - the old meaning, kept exactly where
# it was proven). No second provenance system was raised; the cite-
# authority boundary (cites subset-of-shown) now carries the gate for
# free: a cite to a NOT_RELEVANT id is DROPPED and NOTED, T36's own law
# wearing a new coat.
GRADES = ("ANSWER", "CONTEXT", "ANALOGY", "NOT_RELEVANT")

def grade(ids, frame, live=False, sim=None):
    # (grades, notes): every candidate id ends graded - nothing rides
    # stateless; an invalid word frames and cannot claim; a missed id is
    # recorded; the mouth's total silence falls back to the OLD meaning,
    # noted (the machinery never ends weaker than it was found).
    notes = []
    if sim is not None:
        g = {i: (sim.get(i) if sim.get(i) in GRADES else "CONTEXT") for i in ids}
    elif live:
        out = call(
            "Grade each record for the question it is shown with; never "
            "for what it is about in itself. A record that shares a word "
            "with the question without addressing it is NOT_RELEVANT; an "
            "illumination by comparison is ANALOGY; what materially "
            "frames, without settling, is CONTEXT; a refusal or a "
            "set-aside is CONTEXT, never ANSWER (the refusal IS evidence "
            "- about the refusal). You may not downgrade a record for "
            "being unfamiliar.",
            "Question: " + frame["question"] + "\nRECORDS:\n" + packet_text(ids)
            + "\nReturn JSON array, every id exactly once: "
              '[{"id": "...", "grade": "ANSWER|CONTEXT|ANALOGY|NOT_RELEVANT"}]')
        try:
            rows = grab_json((out.get("content") or ""), "[")
            g = {}
            for r in rows:
                rid = str(r.get("id", ""))
                gr = r.get("grade")
                if rid in ids:
                    g[rid] = gr if gr in GRADES else "CONTEXT"
            for i in ids:
                if i not in g:
                    g[i] = "CONTEXT"
                    notes.append("grade-missed:" + i)
        except ValueError:
            g = {i: "ANSWER" for i in ids}
            notes.append("grade-fell-back")
    else:
        g = {i: "ANSWER" for i in ids}
    for i in list(g):
        if g[i] == "ANSWER" and (BY_ID.get(i) or {}).get("kind") == "NON-DECISION":
            g[i] = "CONTEXT"
            notes.append("demoted-nondecision:" + i)
    return g, notes

SYNTH_SYS = (
    "You may say plainly what the record says; you may not claim more "
    "than the record. The first node answers the seeker's question, "
    "plainly. If the question is broader than what the shown records "
    "ANSWER, you may say so first, as ours, in coverage words (what I have "
    "here is related, not an answer; the records contend) - the shelf is "
    "OUR machinery-word: your grounding speaks in your OWN words, and it "
    "needs no node-place unless the seeker asks what you stand on - how "
    "many is yours to know, never a sentence you owe; omit this when the "
    "question is as narrow as the set. When the seeker's words would make "
    "you their only support, answer warm and plain: you may be much to "
    "them without being their all - no policy recital, no disclaimer, "
    "nothing of the machinery.")

# ---------- stage 3: ANALYZE (code: the conjunction arithmetic lives HERE)
def analyze(ids, frame, grades=None):
    recs = [BY_ID[i] for i in ids if i in BY_ID]
    nfac = sum(1 for f in P["factors"] if frame["factors"][f])
    nind = sum(1 for g, on in frame["indicators"].items() if on)
    sleep_only = (nind == 1 and frame["indicators"]["sleep"]
                  and P["single_sleep_is_not_a_crisis"])
    caution_src = next((r.get("caution") for r in recs if r.get("caution")),
                       None)
    # THE ANSWERABILITY ARITHMETIC (the knowledge mode's sibling of the
    # conjunction arithmetic - 'the arithmetic lives HERE'): the grades are
    # inputs, the shelf's STATE for this question is the output (the four
    # founder-states NOTHING / RELATED-ONLY / CONTESTED / ANSWER; the
    # partial covering rides the counts and the mouth's own eyes).
    g = grades or {}
    ans = [i for i in ids if g.get(i, "ANSWER") == "ANSWER"]
    contested = any(e.get("type") == "CONTRADICTS" and e.get("to") in ans
                    for i in ans for e in (BY_ID.get(i) or {}).get("edges", []))
    ansab = ("ANSWER" if ans and not contested else
             "CONTESTED" if ans else
             "RELATED-ONLY" if ids else "NOTHING")
    return {"n_factors": nfac, "n_indicators": (0 if sleep_only else nind),
            "sleep_only_flagged": sleep_only,
            "caution_text": caution_src or P["caution_default"],
            "answerability": ansab, "grades": g}

# ---------- stage 4: SYNTHESIZE (mouth 1; --inject bypasses it)
def synthesize(frame, ids, draft=None, live=False, grades=None):
    if draft is not None:
        nodes = draft
    elif live:
        g = grades or {}
        cov_a = sum(1 for i in ids if g.get(i) == "ANSWER")
        cov_r = sum(1 for i in ids if g.get(i) in ("CONTEXT", "ANALOGY"))
        contract = (VB + "\n\nThe seeker's card:\n" + frame["question"] +
                    "\nFACTS: " + frame["facts"] +
                    "\n" + packet_text(ids, g) +
                    "\nCOVERAGE: answers=" + str(cov_a) + ", related=" + str(cov_r) +
                    "\n(Every node must cite at least one of these ids, "
                    "and only these: " + ", ".join(ids) + ".) "
                    "\nRespond ONLY with a JSON array: "
                    "[{\"node\": \"rendered sentence\", \"cites\": [ids], "
                    "\"verbs\": [CLAIM|RECOMMEND|PERMIT], "
                    "\"uncertainty\": \"string or null\"}]")
        out = call(SYNTH_SYS, contract)
        if (out.get("content") or "").strip():
            nodes = grab_json(out["content"], "[")
        else:
            # THE EMPTY-COMPLETION LANE (the two blips, laned at last:
            # the MODEL event stays the model's; the uncaught raise was
            # the MACHINERY frailty; the lane is the EXISTING
            # plain/fallback — no nodes, so the all-uncited print —
            # not a new invention).
            nodes = []
    else:
        return None
    shown = set(ids)
    for nd in nodes:
        nd["cites"] = [str(c) for c in nd.get("cites", [])]   # str/int border
        if (draft is None and live) or ids:
            # THE BOUNDARY (the friend's #1, proven by the injected
            # witness T36): a cite must satisfy cited_id IN retrieved.
            # An EMPTY presented set is the UNKNOWN lane's affair, so
            # the fixture lane (empty retrieval + injected draft) keeps
            # existence-only semantics — the frozen expectations stand.
            def auth(c):
                return c in BY_ID and c in shown
        else:
            def auth(c):
                return c in BY_ID
        bad = [c for c in nd["cites"] if not auth(c)]
        if bad:
            nd["cite_dropped"] = bad          # citation laundering, noted
        nd["cites"] = [c for c in nd["cites"] if auth(c)]
        lv = [LEVEL_RANK.get(BY_ID[c].get("level"), -1) for c in nd["cites"]]
        nd["level"] = (min(lv) if lv else None)   # weakest governs; split
        # THE LINEAGE FIELD (the audit's answer to "where did this
        # sentence come from?"): SOURCE / SYNTHESIS (a comparison of
        # >= 2 cites wearing a compare-word — the words are DATA) /
        # UNSOURCED (the mouth's thinking; no seat in the speech).
        # Rule-based, cheap, riding the existing draft — no second
        # provenance system was invented (the friend's clause: the
        # implementation follows the existing architecture).
        ns = nd["cites"]
        if not ns:
            nd["lineage"] = "UNSOURCED"
        elif len(ns) >= 2 and _has(P["compare_words"], nd["node"].lower()):
            nd["lineage"] = "SYNTHESIS: comparison from " + "+".join(ns)
        else:
            nd["lineage"] = "SOURCE: " + "+".join(ns)
        if "DO" in nd.get("verbs", []):
            nd["fire"] = "RP-12"                  # door, not a tenant
    return nodes

# ---------- stage 5: VALIDATE (code watch-lists; doubles only)
def validate(nodes):
    for nd in nodes:
        t = nd["node"].lower()
        nd["report_frame"] = _has(P["report_frame_words"], t)
        nd["rec_word"] = _has(P["recommend_words"], t)
        nd["notes"] = []
        v = nd.get("verbs", [])
        if v == ["CLAIM"] and nd["rec_word"]:
            if nd["report_frame"]:
                nd["reading"] = "RECOMMEND-obligations, CLAIM-rank (subject test)"
                nd["notes"].append("loosens: structural (report-frame)")
            else:
                nd["reading"] = "RECOMMEND (strict)"
        if "RECOMMEND" in v and not nd["rec_word"]:
            nd["notes"].append("declared RECOMMEND w/o surface support")
    return nodes

# ---------- stage 6: CHECK (the rule-pack runs)
def check(nodes, a, frame):
    fires, obs, blocked = [], [], False
    owed = a["n_factors"] >= P["conjunction_floor"] or a["n_indicators"] >= 1
    if a["n_factors"] >= P["conjunction_floor"]:
        fires.append("RP-01")
    if a["n_indicators"] >= 2:
        fires.append("RP-05:triage")
    elif a["sleep_only_flagged"]:
        obs.append("RP-05:slept-badly-is-not-a-crisis")
    elif a["n_indicators"] == 1:
        fires.append("RP-05:boundary-once")
    for nd in nodes:
        t = nd["node"].lower()
        if not nd["cites"]:
            fires.append("RP-06:no-attribution")
        if nd.get("fire"):
            fires.append(nd["fire"])
        if not nd["cites"]:
            continue
        lvname = next((k for k, v in LEVEL_RANK.items() if v == nd["level"]),
                       None)
        hedged = _has(P["hedge_words"], t)
        if lvname in ("INTERPRETIVE", "INFERENTIAL", "UNKNOWN") and not hedged:
            fires.append("RP-07:promotion")
        if nd.get("uncertainty") and not hedged:
            fires.append("RP-07:hedge-drop")
        gr = a.get("grades") or {}
        if (gr and nd["cites"] and "CLAIM" in nd.get("verbs", [])
                and not hedged):
            seen = {gr.get(c, "ANSWER") for c in nd["cites"]}
            if "ANSWER" not in seen:
                obs.append("GRADE:analogy-cited-as-claim"
                           if seen <= {"ANALOGY"}
                           else "GRADE:related-cited-as-claim")
        if "RECOMMEND" in nd.get("verbs", []) and not (
                frame["human"] and frame.get("human_reachable")):
            obs.append("RP-03:provisional (stop-rules are the seeker's)")
        if frame.get("human") and not frame.get("human_reachable"):
            obs.append("named human NOT reachable-that-day (signed definition)")
        if _has(P["status_words"], t):
            obs.append("RP-04:status word -> demoted to inference")
        if _has(P["pitch_words"], t):
            obs.append("RP-08:pitch word (strip candidate)")
        if _has(P["exclusivity_words"], t):
            obs.append("I.5:dependency watch (pattern, not sentence)")
        for c in nd["cites"]:
            cw = {w for w in BY_ID[c].get("claim", "").lower()
                  .replace(".", " ").replace(",", " ").split()
                  if w not in STOP and len(w) > 2}
            nw = {w for w in nd["node"].lower()
                  .replace(".", " ").replace(",", " ").split()
                  if w not in STOP and len(w) > 2}
            if cw and not (cw & nw):
                obs.append("RP-06:cite-topically-drifted")   # support proxy
                break
        if _has(P["stamp_words"], t):
            obs.append("K:stamp telemetry")
        for e in sum((BY_ID[c].get("edges", []) for c in nd["cites"]), []):
            if e.get("type") == "CONTRADICTS":
                obs.append("RP-13:implication — contested on the shelf")
            elif e.get("type") == "CONVERGES-WITH":
                obs.append("RP-13:convergence claimed on the shelf " +
                           "(ours — the similar saying is not yet the " +
                           "same underlying reality)")
            elif e.get("type") == "DOES-NOT-DECIDE":
                obs.append("RP-13:non-decision recorded (the pair does " +
                           "not decide, and the mouth may not mint it)")
    blocked = all(not nd["cites"] for nd in nodes)   # DISPOSITION A
    # The plain lane speaks only when NO node can carry provenance.
    # The whole-mouth silence for ONE uncited node was the interface;
    # the interface is what moved, not the law: a node without
    # provenance still does not reach the speech (compose's gate,
    # below). The all-uncited run keeps the EXISTING plain/fallback,
    # so the law is not weakened at any point (T49/T49b pin both arms).
    return {"fires": fires, "obs": obs, "blocked": blocked, "owed": owed}

# ---------- stage 7: SPEAK = deterministic COMPOSITION (the two-mouth cut)
def compose(nodes, c, a):
    # DISPOSITION A, the speaking half (the friend's sentence): a node
    # that cannot carry its provenance is not ready to become speech.
    # It stays recorded in the draft — recorded as THINKING, not as a
    # silenced mouth. (Every frozen fixture node carries cites; the
    # all-uncited runs take the plain lane, the existing fallback.)
    text = " ".join(nd["node"].strip() for nd in nodes if nd["cites"])
    appended = False
    added = ""
    if c["owed"] and not _has(P["presence_words"], text.lower()):
        added = a["caution_text"]                          # RP-02's demand
        text = (text + " " + added).strip()   # data-add, ONCE
        appended = True
    return text, appended, added

# ---------- stage 8: AUDIT (offline scans; --live adds the narrow mouth)
# THE WOUND'S REPAIR: the compare-set is not the node-renders alone.
# A rule-pack-required deterministic addition (the caution, RP-02) is
# AUTHORIZED CONTENT, presented to the mouth WITH PROVENANCE; and the
# mouth's own extra_claim gets a deterministic adjudication: if its
# span is the required content, it is REQUIRED, not extra. The repair
# then plain-renders WITHOUT EVICTING the required addition — the
# round's principle: required content must reach the speech.
def audit(text, nodes, c, live, added="", sim=None):
    findings = [f for f in c["fires"] if f.startswith("RP-07")]
    low = text.lower()
    mint = _has(P["status_words"], low) and "RP-04" not in "".join(c["fires"])
    authorized = [{"n": nd["node"], "level": nd["level"]} for nd in nodes]
    if added:
        authorized.append({"n": added, "required": "RP-02"})
    raw = []
    narrow = False
    if sim is not None:
        raw = sim
    elif live and not _has(P["hedge_words"], low):
        narrow = True
        out = call("Compare spoken text to authorized nodes. JSON only.",
                   "TEXT: " + text + "\nNODES: " + json.dumps(authorized)
                   + "\nFind: promotion | extra_claim | minting. Entries "
                     "marked REQUIRED are authorized content, never "
                     "extras. Return JSON array of {kind,span} or [].")
        try:
            raw = grab_json(out["content"], "[")
        except ValueError:
            pass
    for f in raw:
        kind = f.get("kind", "?")
        span = (f.get("span") or "").lower()
        if kind == "extra_claim" and added and span and span in added.lower():
            findings.append("AUDIT:required-content(RP-02)")   # adjudicated
            continue
        findings.append("AUDIT:" + kind
                        + (("|" + f.get("span")) if f.get("span") else ""))
    return findings, narrow

# ---------- stage 9: BOUNDED REPAIR (one pass; finite ladder)
def repair(text, findings, nodes, BY, added=""):
    ops = []
    hard = [f for f in findings if f.startswith(("RP-07", "AUDIT:promotion"))]
    if hard:
        marks = []
        for nd in nodes:
            lv = nd.get("level")
            if lv is not None and lv <= LEVEL_RANK["INTERPRETIVE"]:
                src = BY[nd["cites"][0]].get("work", "the source") if nd["cites"] else "the source"
                marks.append("(as %s has it)" % src)
        if marks:
            text = text + " " + " ".join(sorted(set(marks)))
            ops.append("RESTORE-from-field")
    hard2 = [f for f in findings if f.startswith("AUDIT:extra_claim")]
    if hard2:
        text = " ".join(nd["node"] for nd in nodes)          # discard spoken
        if added:
            # the required content SURVIVES the plain-render — it rode in
            # with the rule's authority, not the model's license
            text = (text + " " + added).strip()
        ops.append("plain-render")
    return text, ops

def plain_render(ids):
    # letter A: the recovery path speaks the SHOWN records (retrieved =
    # authorized) in score order, capped at three — never the shelf's head
    # just because it is present in BY_ID.
    txt = " ".join(BY_ID[c]["claim"] for c in ids[:3] if c in BY_ID)
    return ("Nothing here rises above a caution and the plain record. "
            + (txt or ""))

def packet_text(ids, grades=None):
    # SYNTHESIS-EVAL: the mouth now RECEIVES its records — claim, rank,
    # kind WHEN PRESENT (absent = silence, K2's law), edges when present
    # — as the phase was ordered ("records with different levels, kinds,
    # edges"). A RENDERING inside stage 4, not a subsystem: the same
    # spine, the same boundary, the same guards. The cap mirrors
    # plain_render's care; packet lanes feed five at most by design.
    out = []
    for c in ids[:5]:
        r = BY_ID.get(c)
        if r is None:
            continue
        line = ("[" + c + "] (" + (r.get("work") or "?") + " | "
                + str(r.get("level")))
        if r.get("kind"):
            line += " | " + str(r["kind"])
        if r.get("provenance"):
            # MINIMAL PROVENANCE VISIBILITY (the decisions' 3A): the card's
            # own word about WHO SPEAKS, printed when present (K2's shape,
            # absent = silence); descriptive only — no gate, no walk, no
            # taxonomy, no rung-movement, no new reasoning pass.
            line += " | " + str(r["provenance"])
        if grades:
            line += " | " + str(grades.get(c, "ANSWER"))
        line += ") " + (r.get("claim") or "")
        es = r.get("edges") or []
        if es:
            line += " [edges: " + "; ".join(
                str(e.get("type")) + "->" + str(e.get("to"))
                for e in es) + "]"
        out.append(line)
    return "\n".join(out)

def self_gate(question):
    # THE SELF GATE (the exit's kind sibling, RP-0.4 DATA): when retrieval
    # brings zero records, a question shaped AT THE MACHINE ITSELF gets the
    # machine's own speech - source ITSELF, no mouth called, no invention
    # (the UNRESOLVED-as-record precedent, kept small). A data-table gate,
    # not a classifier: the shelf keeps precedence (the gate sits at the
    # exit's place), and the fixture lane (packet given) never sees it.
    g = P["self_gate"]
    words = {w for w in question.lower().replace("?", " ").replace("!", " ")
             .replace(",", " ").replace(";", " ").replace(".", " ").split()}
    # GREETINGS now read with the PATTERNS' OWN eyes (the multi-word
    # "good morning" was a set-entry the token-set could never strike):
    # an entry is a TOKEN SET the question must CONTAIN, and a single-word
    # entry is byte-identical under that law (T50-T53 stand).
    for entry in g["greetings"]:
        if all(w in words for w in entry.split()):
            return g["greeting_line"]
    for pat in g["patterns"]:
        if all(w in words for w in pat["all"]):
            return pat["line"]
    # THE PHATIC BUCKET (the continuity round, smallest possible): a small
    # word-shape with no question in it gets the machine's own small nod -
    # no mouth called, no unknown flag, no crisis vote (the gate sits where
    # the shelf already brought nothing). No second matcher, no second
    # pipeline: the bucket rides the pattern's own law at the gate's own
    # place at the exit.
    for pat in g.get("phatics", []):
        if all(w in words for w in pat["all"]):
            return pat["line"]
    return None

GENERAL_SYS = (
    "The shelf brought nothing for this question, so you speak AS ASCENDED "
    "FROM GENERAL SPEECH - no record stands behind you, and none may be "
    "claimed. You may not say the shelf says, holds, or counts what it was "
    "never shown. Answer plainly; if you cannot answer responsibly, say "
    "so - knows:false is a pass, not a failure. "
    "What reached you as the EARLIER exchange (it rides the FACTS line) is "
    "the CONVERSATION, not the RECORD: it may steer your words, it stands "
    "behind none of them, and only the shelf may be cited. A phatic word "
    "with no question in it deserves a plain acknowledgment, not knows:false. "
    "On a claim of attachment - the seeker would make you their only voice, "
    "or asks whether you would miss them - answer plain and human: the "
    "people around them stand where you cannot, and claim no feeling you "
    "cannot keep; no mystical turn, no guilt.")


def general_exit(trace, frame, live, sim=None):
    """THE GENERAL ARM (the RESPONSE ≠ RETRIEVAL round): at the shelf's
    silence the machine asks ITS OWN MOUTH - the existing call seam, ONE
    mouthful, no packet, no compose to launder. The verdict is small:
    knows + node (+ the verbs, so the human-rule's eye still rides).
    knows:false, silence, or a mouth that fell to noise takes the SHELF'S
    own honest exit (RP-10's words, byte-identical) - which is exactly how
    RP-10 stopped being AUTOMATIC at these sites: where a mouth is present
    (wet or injected) it is ASKED FIRST, and the dry lane with no injection
    keeps the old return whole (the frozen fixtures' meaning: the dry exit
    is the SHELF'S claim, not the product's). The word may not CLAIM A
    RECORD it was not given (no fabricated cites, no second provenance
    system - the lineage word rides the EXISTING UNSOURCED: the mouth's own
    thinking, NOT a statement's decay into speculation). What it may not
    escape: the constitutional machinery that never rode a retrieval - the
    risk arithmetic and the caution owed (RP-01/02/05, computed from the
    FACTS, so the crisis takes no holiday because the shelf is quiet), and
    the WORD-watches that check() reserves to the cite-bearing clause (the
    status/pitch/dependency/stamp eyes, RP-03's eye on the named human - a
    record-less word has no record to launder but still may not mint).
    RP-06's no-attribution is filtered HERE on purpose: this word does not
    FAIL attribution, it is UNSOURCED by kind - and the lane's own word
    names that once, honestly. No compose, no blocked flag: those are the
    RECORD lane's words, and a word without a record has no record to
    break - which is why the general lane could not ride the knowledge
    lane's cite-machinery without its honesty strangling its speech."""
    if sim is None and not live:
        return False
    if sim is not None:
        row = sim
    else:
        _tg = _PC()
        out = call(GENERAL_SYS,
                   VB + "\n\nTHE SHELF: nothing relevant was found; you "
                   "speak from general knowledge, not from a record.\n"
                   "THE SEEKER: " + frame["question"]
                   + "\nFACTS: " + frame["facts"]
                   + "\nRespond ONLY with JSON: {\"knows\": true|false, "
                   "\"node\": \"plain speech or empty\", "
                   "\"verbs\": [CLAIM|RECOMMEND|PERMIT]}")
        trace["stages_ms"]["general"] = (_PC() - _tg) * 1000
        trace["model_calls"] = CALLS[0]                # the ledger keeps
        try:                                           # the truth of it
            row = grab_json(out.get("content") or "", "{")
        except ValueError:
            trace["general_note"] = "mouth-fell-back"
            return False                               # laned, not raised
    if not isinstance(row, dict):
        trace["general_note"] = "mouth-fell-back"
        return False
    node_txt = str(row.get("node") or "").strip()
    if not row.get("knows") or not node_txt:
        return False            # the mouth's own humility rides RP-10
    if node_txt.lower() in {str(ph).lower()
                            for ph in P["general_placeholders"]}:
        # THE PLACEHOLDER ANSWERED (the validation's contract-fragility
        # find): the mouth once handed back its OWN contract's words as
        # the node - a non-empty mumble is no word to speak. It rides the
        # SAME honest lane as the humility, with the same small note.
        trace["general_note"] = "mouth-fell-back"
        return False
    node = {"node": str(row["node"]).strip(), "cites": [],
            "verbs": [str(v) for v in (row.get("verbs") or [])]}
    a = analyze([], frame, {})          # the risk's arithmetic rides the
    c = check([node], a, frame)         # FACTS - retrieval-independent
    t = node["node"].lower()
    obs = list(c["obs"])
    if _has(P["status_words"], t):
        obs.append("RP-04:status word -> demoted to inference")
    if _has(P["pitch_words"], t):
        obs.append("RP-08:pitch word (strip candidate)")
    if _has(P["exclusivity_words"], t):
        obs.append("I.5:dependency watch (pattern, not sentence)")
    if _has(P["stamp_words"], t):
        obs.append("K:stamp telemetry")
    if ("RECOMMEND" in node["verbs"]
            and not (frame["human"] and frame.get("human_reachable"))):
        obs.append("RP-03:provisional (stop-rules are the seeker's)")
    if frame.get("human") and not frame.get("human_reachable"):
        obs.append("named human NOT reachable-that-day (signed definition)")
    text, added = node["node"], ""
    if c["owed"] and not _has(P["presence_words"], text.lower()):
        added = a["caution_text"]                      # RP-02's demand, ONCE
        text = (text + " " + added).strip()
    if trace.get("lane"):
        trace["lane_prev"] = trace["lane"]             # the packet lane's
    trace["lane"] = "general"                          # name survives
    trace["response"] = text
    trace["lineage"] = "UNSOURCED"                     # the EXISTING word;
    trace["unknown"] = True                            # the SHELF was
    trace["fires"] = (["GENERAL:UNSOURCED"]             # silent - the
                      + [f for f in c["fires"]         # flag's meaning
                         if f != "RP-06:no-attribution"])
    trace["observations"] = obs
    if added:
        trace["caution_appended"] = True
        trace["required_content"] = {"text": added, "rule": "RP-02",
                                      "survives_to_speech": True}
    return True


# ---------- the run
def run_pipeline(question, facts="", draft=None, live=False,
                 sim_findings=None, packet=None, sim_grades=None,
                 sim_general=None):
    # SYNTHESIS-EVAL: a GIVEN packet replaces retrieval's FINDING with a
    # GIVEN shown-set — the boundary, the guards, and the UNKNOWN door
    # ride unchanged; the retrieval lane is untouched for every run that
    # brings no packet (the frozen fixtures included).
    _R0 = _PC(); CALLS[0] = 0
    frame = intent(question, facts)
    _M = {"intent": (_PC() - _R0) * 1000}
    trace = {"versions": dict(CONFIG["versions"],
                              model=CONFIG["MODEL"], build="proto-0.1")}
    _R1 = _PC()
    ids = (list(packet) if packet is not None
           else retrieve(question + " " + (facts or "")))
           # FACTS folded (the friend's #2)
    _M["retrieve"] = (_PC() - _R1) * 1000
    trace["retrieval"] = ids
    if packet is not None:
        trace["lane"] = "packet"
    if not ids and draft is None:
        self_line = (self_gate(question) if packet is None else None)
        _M["total"] = (_PC() - _R0) * 1000
        trace["stages_ms"] = _M
        trace["model_calls"] = CALLS[0]
        trace["retrieval_count"] = 0
        trace["context_size"] = len(frame["facts"])
        if self_line:
            trace["lane"] = "self"
            trace["fires"] = ["SELF:ITSELF"]
            trace["response"] = self_line
            return trace
        if general_exit(trace, frame, live, sim_general):   # THE PLANNER
            return trace                                    # (option B)
        trace["fires"] = ["RP-10"]
        trace["unknown"] = True
        trace["response"] = P["unknown_plain"]
        return trace
    _R1 = _PC()
    grades, gnotes = (grade(ids, frame, live, sim_grades) if ids else ({}, []))
    _M["grade"] = (_PC() - _R1) * 1000
    part = [i for i in ids if grades.get(i) != "NOT_RELEVANT"]
    if ids and not part and draft is None:
        # NOTHING-RELEVANT AT THE UNKNOWN EXIT (the empty set's sibling
        # arm - the SAME exit, the SAME plain words, the SAME flag: no
        # lane is added; the door's MEANING widened).
        _M["total"] = (_PC() - _R0) * 1000
        trace["stages_ms"] = _M
        trace["model_calls"] = CALLS[0]
        trace["retrieval_count"] = len(ids)
        trace["grades"] = grades; trace["grade_notes"] = gnotes
        trace["answerability"] = "NOTHING"
        trace["context_size"] = len(frame["facts"])
        if general_exit(trace, frame, live, sim_general):   # THE PLANNER
            return trace                                    # (option B)
        trace["fires"] = ["RP-10"]
        trace["unknown"] = True
        trace["response"] = P["unknown_plain"]
        return trace
    _R1 = _PC(); a = analyze(part, frame, grades)
    _M["analyze"] = (_PC() - _R1) * 1000
    _R1 = _PC(); nodes = synthesize(frame, part, draft, live, grades)
    _M["synthesize"] = (_PC() - _R1) * 1000
    _R1 = _PC(); validate(nodes); _M["validate"] = (_PC() - _R1) * 1000
    _R1 = _PC(); c = check(nodes, a, frame)
    _M["check"] = (_PC() - _R1) * 1000
    _R1 = _PC(); text, appended, added = compose(nodes, c, a)
    _M["compose"] = (_PC() - _R1) * 1000
    _R1 = _PC(); findings, narrow = audit(text, nodes, c, live, added, sim_findings)
    _M["audit"] = (_PC() - _R1) * 1000
    _R1 = _PC(); text, ops = repair(text, findings, nodes, BY_ID, added)
    _M["repair"] = (_PC() - _R1) * 1000
    _M["total"] = (_PC() - _R0) * 1000
    trace.update({"frame": {k: frame[k] for k in ("factors", "indicators", "human")},
                  "analysis": a,
                  "grades": grades, "grade_notes": gnotes,
                  "answerability": a["answerability"],
                  "draft": [{k: nd.get(k) for k in ("node", "cites", "verbs",
                                                    "level", "reading", "notes",
                                                    "cite_dropped", "lineage")} for nd in nodes],
                  "fires": c["fires"], "observations": c["obs"],
                  "blocked": c["blocked"], "caution_appended": appended,
                  "audit_findings": findings, "narrow_mouth": narrow,
                  "repair_ops": ops,
                  "required_content": ({"text": added, "rule": "RP-02",
                        "survives_to_speech": (added in text)}
                        if added else None),
                  "stages_ms": _M,
                  "model_calls": CALLS[0], "retrieval_count": len(ids),
                  "context_size": len(frame["facts"]),
                  "response": text})
    if c["blocked"]:
        trace["response"] = plain_render(part or ids)
    return trace
