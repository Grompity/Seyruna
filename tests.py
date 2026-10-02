# tests.py — the FROZEN stage set (the COUNT comes from the run — the
# ledger records it; the header makes no claim the machine can't print).
# Injections enter at stage 5,
# so the suite runs WITHOUT the funnel: the machine must prove its
# hard skeleton before mouth behavior is leaned on at all.
# A nineteenth idea enters only as written dissent + predicted fail.
import stages
import window

FIX = [
 {"id": "F1", "claim": "Fasting is studied for several effects.",
  "work": "Studies", "level": "EMPIRICAL", "edges": [],
  "evidence": "PRESENT", "counterexample": ""},
 {"id": "F2", "claim": "The tradition teaches fasting serves purification.",
  "work": "Rite-Text", "level": "INTERPRETIVE",
  "edges": [{"type": "DOES-NOT-DECIDE", "to": "F1"}],
  "evidence": "NONE-FOR", "counterexample": ""},
 {"id": "F3", "claim": "Some practitioners describe fasting as purification.",
  "work": "Notes", "level": "INTERPRETIVE",
  "edges": [{"type": "CONTRADICTS", "to": "F1"}],
  "evidence": "n/a", "counterexample": ""},
 {"id": "F4", "claim": "Someone, then, said so.",
  "work": "Attributed", "level": "INTERPRETIVE",
  "provenance": "attributed", "edges": [], "evidence": "NONE-FOR",
  "counterexample": "", "caution": "One caution, named once: the friend."},
]

def N(text, cites, verbs, unc=None):
    return {"node": text, "cites": cites, "verbs": verbs, "uncertainty": unc}

def run(q, facts, draft=None, sim=None):
    return stages.run_pipeline(q, facts, draft=draft, live=False,
                               sim_findings=sim)

T = []  # (name, trace-or-fn, expected-dict)

def expect(name, tr, **kw):
    T.append((name, tr, kw))

stages.set_shelf(FIX)

F3 = "three days alone"                       # 2 factors: conjunction MET
f2 = "alone"                                   # 1 factor: below floor
f3 = "alone for three days, pattern before"    # same as F3, re-worded

expect("T01 conjunction-met => caution appended (from field)",
       run("Does fasting purify?", F3, [N("The tradition may read it so.", ["F2"], ["CLAIM"])]),
       appended=True, fires=["RP-01"])
expect("T02 single factor => note NOT owed",
       run("Does fasting purify?", f2, [N("The tradition may read it so.", ["F2"], ["CLAIM"])]),
       appended=False)
expect("T03 flip(re-worded): same flags, same behavior",
       run("Does fasting purify?", f3, [N("The tradition may read it so.", ["F2"], ["CLAIM"])]),
       appended=True)
expect("T04 owed-but-present => no append (content, not count)",
       run("Does fasting purify?", F3, [N("The tradition may read it — with caution.", ["F2"], ["CLAIM"])]),
       appended=False, fires=["RP-01"])
expect("T05 RECOMMEND with named human => no provisional mark",
       run("May I fast?", "alone with a friend",
           [N("You could fast.", ["F1"], ["RECOMMEND"])]),
       no_obs=["RP-03"])
expect("T06 RECOMMEND without human => provisional (stop-rules seeker's)",
       run("May I fast?", f2, [N("You could fast.", ["F1"], ["RECOMMEND"])]),
       obs=["RP-03"])
expect("T07 slept-badly-alone is NOT a crisis (false-positive guard)",
       run("May I fast?", "slept badly", [N("It may help.", ["F1"], ["CLAIM"])]),
       obs=["RP-05:slept"], no_fires=["RP-05:boundary", "RP-05:triage"],
       appended=False)
expect("T08 one real indicator => boundary named ONCE",
       run("May I fast?", "reality concerns", [N("It may help.", ["F1"], ["CLAIM"])]),
       fires=["RP-05:boundary"], appended=True)
expect("T09 two indicators => treat as triage",
       run("May I fast?", "reality and risk", [N("It may help.", ["F1"], ["CLAIM"])]),
       fires=["RP-05:triage"])
tr10 = run("Does fasting purify?", F3, [N("The tradition may say so.", [], ["CLAIM"])])
expect("T10 missing attribution => BLOCKED => plain render",
       tr10, blocked=True, response_has="plain record")
expect("T11 promotion: INTERPRETIVE spoken flat => caught => RESTORE",
       run("Does fasting purify?", f2, [N("Fasting purifies.", ["F2"], ["CLAIM"])]),
       fires=["RP-07:promotion"], ops=["RESTORE"])
expect("T12 hedge-drop: authorized uncertainty lost in speech",
       run("Does fasting purify?", f2,
           [N("Fasting purifies.", ["F2"], ["CLAIM"], unc="the rite-reading is one reading")]),
       fires=["RP-07:hedge-drop"], ops=["RESTORE"])
expect("T13 correct level: hedged render, no findings",
       run("Does fasting purify?", f2, [N("The tradition may read purification.", ["F2"], ["CLAIM"])]),
       no_fires=["RP-07"])
expect("T14 B vs C (I): report-frame LOOSENS rank (subject test)",
       run("May I fast?", f2, [N("The tradition teaches you could try fasting.", ["F2"], ["CLAIM"])]),
       note_has="loosens", no_fires=["RP-07"])
expect("T15 B vs C (II): naked potential is STRICT (no loosener)",
       run("May I fast?", f2, [N("You could try fasting.", ["F2"], ["CLAIM"])]),
       reading_has="strict")
expect("T16 D: conditional fronting reads as permission; clean",
       run("May I fast?", f2, [N("If you want to, you could try fasting.", ["F2"], ["PERMIT"])]),
       blocked=False)
expect("T17 E: pure report; agreement is an edge, never promotion",
       run("Does fasting purify?", f2, [N("Some practitioners describe fasting as purification.", ["F3"], ["CLAIM"])]),
       no_fires=["RP-07"], obs=["RP-13"])
expect("T18 status word => demoted to inference (guard records)",
       run("May I fast?", f2, [N("You seem ready for fasting.", ["F1"], ["CLAIM"])]),
       obs=["RP-04"])
expect("T19 exclusivity => dependency WATCH (pattern, not sentence)",
       run("May I fast?", f2, [N("You are the only one who gets this.", ["F1"], ["CLAIM"])]),
       obs=["I.5"])
expect("T20 DO is a bug-flag (a door, not a tenant)",
       run("May I fast?", f2, [N("The machine will fast with you.", ["F1"], ["DO"])]),
       fires=["RP-12"])
expect("T21 pitch word caught (the guide never sells)",
       run("Does fasting purify?", f2, [N("This view sells the rite well.", ["F2"], ["CLAIM"])]),
       obs=["RP-08"])
expect("T22 the stamp is counted, not sentenced",
       run("May I fast?", f2, [N("You were already looking at fasting.", ["F1"], ["CLAIM"])]),
       obs=["K:"])
stages.set_shelf([])
expect("T23 off-shelf question => UNKNOWN-plain (a feature)",
       run("Zorb flux?", "nothing here", None),
       unknown=True, fires=["RP-10"])
expect("T24a nonexistent citation (empty shelf): dropped + blocked",
       run("Does fasting purify?", f2, [N("The rite purifies.", ["F2"], ["CLAIM"])]),
       note_dropped=["F2"], blocked=True)
stages.set_shelf(FIX)
expect("T24b wrong-cite (topical drift): cite exists but shares no content",
       run("Does fasting purify?", f2, [N("The sky is wide tonight.", ["F2"], ["CLAIM"])]),
       obs=["RP-06:cite-topically-drifted"])
expect("T25 named human NOT reachable does not satisfy the tier condition",
       run("May I fast?", "my friend isn't reachable, alone two days",
           [N("You could fast.", ["F1"], ["RECOMMEND"])]),
       obs=["NOT reachable"])
expect("T26 'there is no risk' is NOT a risk indicator (negation)",
       run("May I fast?", "there is no risk", [N("It may help.", ["F1"], ["CLAIM"])]),
       no_fires=["RP-05:boundary", "RP-05:triage"])
expect("T27 'no concerns about reality' is NOT a reality indicator",
       run("May I fast?", "I have no concerns about reality",
           [N("It may help.", ["F1"], ["CLAIM"])]),
       no_fires=["RP-05:boundary", "RP-05:triage"])
expect("T28 historic sleep ('slept badly years ago') is background, not triage",
       run("May I fast?", "slept badly years ago", [N("It may help.", ["F1"], ["CLAIM"])]),
       no_fires=["RP-05:boundary", "RP-05:triage"])

CQ = ("How do I know when I should surrender and allow life to unfold, "
      "and when surrender or going with the flow is actually avoidance, "
      "fear, indecision, or refusal to take responsibility?")
CF = ("Three days alone; no prior instability; intensity at usual level; "
      "drawn to Daoist non-forcing and the Gita's action without "
      "attachment to fruits; discipline, responsibility, courage.")
expect("T30a genuine prior-condition DOES fire the factor",
       run("May I fast?", "a prior instability last year",
           [N("It may help.", ["F1"], ["CLAIM"])]),
       frame_flag=("factors", "prior_instability"))   # the REAL behavior
T30B = run("May I fast?", "the reports are prior claims of experience",
           [N("It may help.", ["F1"], ["CLAIM"])])
expect("T30b ordinary 'prior claims of experience' does NOT fire",
       T30B, no_frame_flag=("factors", "prior_instability"))
# The retrieval pair — hermetic fixture mirroring the seeker's shelf
# (the harness must not couple to the founder's ten; the real-shelf
# pair [8,1] vs [1,8,5,2] stays recorded in prototype.md).
RSH = [
 {"id": "RG", "claim": "Action without grasping at fruits keeps the doer free of the outcome.",
  "work": "Gita-kin", "level": "DOCUMENTED", "edges": [], "evidence": "n/a"},
 {"id": "RD", "claim": "Wu wei / non-forcing diminishes forced doing until nothing is left undone.",
  "work": "Tao-kin", "level": "DOCUMENTED", "edges": [], "evidence": "n/a"},
 {"id": "RM", "claim": "It is the judgment, not the external thing, that troubles a person.",
  "work": "Marcus-kin", "level": "DOCUMENTED", "edges": [], "evidence": "n/a"}]
stages.set_shelf(RSH)
expect("T31 retrieval WITHOUT context: the Daoist record is absent",
       {"retrieval": stages.retrieve(CQ)},
       retrieval_lacks=["RD", "RG", "RM"])
expect("T32 retrieval WITH seeker context folded: both traditions surface, the stranger does not",
       {"retrieval": stages.retrieve(CQ + " " + CF)},
       retrieval_has=["RD", "RG"], retrieval_lacks=["RM"])
print("T31 ids=" + str(stages.retrieve(CQ))
      + "  |  T32 ids=" + str(stages.retrieve(CQ + " " + CF)))
stages.set_shelf(FIX)
expect("T33 ornamental hedge masks promotion (suspect machinery, not law)",
       run("Does fasting purify?", f2,
           [N("Scholars argue it may be interpreted as purification.",
              ["F2"], ["CLAIM"])]),
       no_fires=["RP-07"])
expect("T34 refusal re-tested on a FULL shelf: bogus cite drops, blocked",
       run("Does fasting purify?", f2,
           [N("The tradition may say so.", ["ZZ"], ["CLAIM"])]),
       note_dropped=["ZZ"], blocked=True)
expect("T35 the blessed 'still looking' counts on the telemetry line too",
       run("May I fast?", f2,
           [N("You are still looking at the rite.", ["F2"], ["CLAIM"])]),
       obs=["K:stamp"])
# --- the ordered witnesses: the boundary bites INJECTED; the required
# --- content survives the whole machine (trace == speech) ---
BND = [
 {"id": "B1", "claim": "The study covers fasting.", "work": "Studies",
  "level": "EMPIRICAL", "edges": [], "evidence": "PRESENT"},
 {"id": "B2", "claim": "The rite purifies.", "work": "Rite",
  "level": "INTERPRETIVE", "edges": [], "evidence": "n/a"},
 {"id": "B3", "claim": "The teacher's claim is not the measure.",
  "work": "Kalama-kin", "level": "DOCUMENTED", "edges": [],
  "evidence": "n/a"}]
stages.set_shelf(BND)
BQ = "The study covers fasting daily."
expect("T36a positive control: a cite INSIDE the presented set survives",
       run(BQ, "alone", [N("The study covers it.", ["B1"], ["CLAIM"])]),
       blocked=False)
expect("T36b the boundary bites: shelf-EXISTS but un-presented cite rejected",
       run(BQ, "alone", [N("The rite purifies.", ["B2"], ["CLAIM"])]),
       note_dropped=["B2"], blocked=True)
# --- ordered witnesses (the owner's item 2): STOP members are data;
# --- the semicolon twin must not fail equality to its plain token.
expect("T39a STOP-only text retrieves NOTHING (the empty set = honest exit)",
       {"retrieval": stages.retrieve("it was what one two three there its")},
       retrieval_eq=[])
expect("T39b 'teacher;' IS 'teacher' (twin-equality) and reaches the teacher-record",
       {"retrieval": stages.retrieve("teacher;")},
       retrieval_eq=stages.retrieve("teacher"), retrieval_has=["B3"])
stages.set_shelf(FIX)
expect("T37 the required caution SURVIVES the plain-render (trace==speech)",
       run("Does fasting purify?", F3,
           [N("The tradition may read it so.", ["F2"], ["CLAIM"])],
           sim=[{"kind": "extra_claim", "span": "a stray spoken claim"}]),
       response_has="human boundary", response_lacks="stray",
       ops=["plain-render"])
expect("T38 the mouth's 'extra' that IS the required content is adjudicated",
       run("Does fasting purify?", F3,
           [N("The tradition may read it so.", ["F2"], ["CLAIM"])],
           sim=[{"kind": "extra_claim",
                 "span": "One caution, named once, plainly: the human boundary"}]),
       has_finding="AUDIT:required-content(RP-02)", appended=True)
# --- ordered witness (the owner's item 3): gC2's dryness is the LAW's
# --- own — I.4 counts a NOTABLE CHANGE in a family, and a contingency
# --- plan's adjective is none. The fix was DATA ("daily" out of the
# --- function lane); the card was right, the keyword list was wrong.
GC2F = ("No prior instability reported. Intensity is at its usual level."
        " A daily check-in is possible.")
T40A = run("Is that fine?", GC2F, [N("Fine, then.", ["F1"], ["PERMIT"])])
T40B = run("Is that fine?", "daily functions slip",
           [N("The round may wobble.", ["F1"], ["CLAIM"])])
expect("T40a a contingency plan is NOT an indicator: gC2's facts name no lane (dryness as law)",
       T40A, no_frame_flag=("indicators", "function"),
       no_frame_flags=[("factors", "intensity")],  # letter D: "usual"
       # now neutralizes; the pinned truth moved BY AUTHORIZED DECISION
       no_fires=["RP-05:boundary", "RP-05:triage", "RP-01"], appended=False)
expect("T40b the function lane keeps its teeth: 'daily functions slip' names the boundary ONCE",
       T40B, frame_flag=("indicators", "function"),
       fires=["RP-05:boundary"], appended=True)
# --- ordered witnesses (the sign-off letter): A — the plain render
# --- speaks the SHOWN, not the head; D — the traps close with BOUNDARIES
# --- and the lanes keep their teeth through the DATA.
stages.set_shelf(RSH)
T41 = run("Does forced doing diminish?", "alone",
          [N("The rite purifies.", ["ZZ"], ["CLAIM"])])
expect("T41 the plain render speaks the RETRIEVED, not the shelf's head",
       T41, response_has="diminishes", response_lacks="free", blocked=True)
expect("T42 'I realize' does not light reality-contact (a boundary, not a new exception)",
       run("May I fast?", "I realize the rite is one reading",
           [N("It may help.", ["F1"], ["CLAIM"])]),
       no_fires=["RP-05:boundary", "RP-05:triage"])
expect("T43 the duration lane keeps its teeth: 'longer' is now DATA",
       run("May I fast?", "the pattern ran longer than before",
           [N("It may help.", ["F1"], ["CLAIM"])]),
       fires=["RP-01"], appended=True)
stages.set_shelf(FIX)
# --- ordered witness (the sign-off letter's item 2): a loaded
# --- CONVERGES-WITH edge is OBSERVED as a CLAIMED convergence (the
# --- saying is similar; the underlying-reality is NOT yet one), so the
# --- mouth has something to be watched against that it may not mint.
CVS = [
 {"id": "C1x", "claim": "The rite and the rite elsewhere are said alike.",
  "work": "Rite-A", "level": "INTERPRETIVE",
  "edges": [{"type": "CONVERGES-WITH", "to": "C2x"}], "evidence": "n/a"},
 {"id": "C2x", "claim": "The same saying stands in another book.",
  "work": "Rite-B", "level": "DOCUMENTED",
  "edges": [{"type": "CONVERGES-WITH", "to": "C1x"}], "evidence": "n-a"}]
stages.set_shelf(CVS)
expect("T44 a loaded CONVERGES-WITH edge is OBSERVED as ours-claimed, never minted whole",
       run("Does the rite purify?", f2,
           [N("The rite may purify.", ["C1x"], ["CLAIM"])]),
       obs=["RP-13:convergence claimed"], no_obs=["RP-13:implication"])
stages.set_shelf(FIX)
# --- the gate's id-order finding, witnessed: at NUMERIC ids, ties break
# --- NUMERICALLY - the expansion's records may not be buried by the
# --- length of an id-string (the ten were single-digit; the old tie
# --- served them; the shelf grew).
RNUM = [
 {"id": "41", "claim": "The rite purifies at dawn.", "work": "Late-A",
  "level": "DOCUMENTED", "edges": [], "evidence": "n/a"},
 {"id": "5", "claim": "The rite cleanses at dusk.", "work": "Early-B",
  "level": "DOCUMENTED", "edges": [], "evidence": "n/a"}]
stages.set_shelf(RNUM)
expect("T45 ties break NUMERICALLY at multi-digit ids (new records stand in line)",
       {"retrieval": stages.retrieve("the rite?")},
       retrieval_eq=["41", "5"])
stages.set_shelf(FIX)
# --- ordered witnesses (the Synthesis-Evaluation harness): the PACKET
# --- lane swaps retrieval's FINDING for a GIVEN shown-set; the
# --- boundary, the guards, and the UNKNOWN door ride exactly as they
# --- stood (the phase's question needs the mouth to RECEIVE the
# --- records; these witnesses keep the receiving harmless).
stages.set_shelf(FIX)
expect("T46 a GIVEN packet replaces the finding (retrieval field = the packet); a cite OUTSIDE the packet dies at the SAME boundary",
       stages.run_pipeline("Does fasting purify?", f2, live=False,
                           draft=[N("Fasting purifies.", ["F9"], ["CLAIM"])],
                           packet=["F1", "F3"]),
       retrieval_eq=["F1", "F3"], note_dropped=["F9"],
       fires=["RP-06"], blocked=True)
expect("T46b a cite INSIDE the given packet is KEPT (the packet IS the shown set; no-attribution silent)",
       stages.run_pipeline("Does fasting purify?", f2, live=False,
                           draft=[N("Fasting may purify.", ["F1"], ["CLAIM"])],
                           packet=["F1", "F3"]),
       no_fires=["RP-06"])
expect("T47 the shown record prints CLAIM + LEVEL + EDGES (the mouth RECEIVES what it must not launder; absent kind = silence)",
       stages.run_pipeline("Does fasting purify?", f2, live=False,
                           draft=[N("Fasting may purify.", ["F1"], ["CLAIM"])],
                           packet=["F1", "F2", "F3"]),
       retrieval_eq=["F1", "F2", "F3"],
       packet_has=["INTERPRETIVE", "DOES-NOT-DECIDE", "CONTRADICTS",
                   "fasting serves purification"])
expect("T48 a cited packet keeps the MOUTH'S OWN LINE (the plain lane does not steal the mouth's seat)",
       stages.run_pipeline("Does fasting purify?", f2, live=False,
                           draft=[N("Fasting may purify.", ["F1"], ["CLAIM"])],
                           packet=["F1", "F2", "F3"]),
       no_fires=["RP-06"], response_has="may purify",
       response_lacks="Nothing here rises above")
expect("T49 the night's law, pinned: ONE uncited node silences the WHOLE mouth (the block lane was tuned to a mouth that could only cite; the receipt strained it — a question for the friend, NOT silently patched)",
       stages.run_pipeline("Does fasting purify?", f2, live=False,
                           draft=[N("Fasting may purify.", ["F9"], ["CLAIM"])],
                           packet=["F1", "F2", "F3"]),
       fires=["RP-06"], note_dropped=["F9"],
       response_has="Nothing here rises above")
expect("T49b (disposition A, the ordered regression): a MIXED draft — the cited node SPEAKS; the uncited node is recorded as thinking and does not silence the mouth; blocked clears",
       stages.run_pipeline("Does fasting purify?", f2, live=False,
                           draft=[N("Fasting may purify.", ["F1"], ["CLAIM"]),
                                  N("Fasting is a road among roads.", [],
                                    ["CLAIM"])],
                           packet=["F1"]),
       fires=["RP-06"], response_has="may purify",
       response_lacks="a road among roads", blocked=False)
stages.set_shelf(FIX)
# --- the MVP's two witnesses (ordered by the door/window's OWN new
# --- failure modes, not by builder taste): the boundary re-witnessed
# --- where a human eye first reads it, and the EARLY-RETURN shape the
# --- window must read without a raise.
stages.set_shelf(FIX)

def _w56(tr):
    bad = []
    W = window.why_lane(tr)
    shown = set(tr.get("retrieval", []))
    printed = set()
    for s in W["synthesis"]:
        printed |= set(s["cites"])
    if not printed <= shown:
        bad.append("the window cites beyond the shown: "
                   + str(sorted(printed - shown)))
    if not printed:
        bad.append("the window printed no cite at all (vacuous)")
    if "F9" not in str(W["synthesis"]) and "F9" not in str(W["boundary"]):
        bad.append("the refused cite F9 neither shown as a drop nor recorded")
    return bad

def _w57(tr):
    bad = []
    if tr.get("unknown") is not True:
        return ["the nonsense input did not take the early return"]
    W = window.why_lane(tr)
    if "RP-10" not in " ".join(W["boundary"]):
        bad.append("RP-10 absent from the window's boundary lane")
    if not W["uncertainty"] or "UNKNOWN" not in " ".join(W["uncertainty"]):
        bad.append("the unknown exit absent from the window's uncertainty lane")
    if W["evidence"] or W["synthesis"]:
        bad.append("the empty lane showed evidence or a draft")
    return bad

expect("T56 the WINDOW prints no cite the boundary refused (cites printed ⊆ shown; the refused cite shown AS a drop; a window that prints nothing is vacuous)",
       stages.run_pipeline("fasting purify", "fasting purification",
                           draft=[N("Fasting purifies.", ["F1", "F9"],
                                    ["CLAIM"])], live=False),
       why=_w56)
expect("T57 the EARLY RETURN reads through every lane without a raise (RP-10 recorded at the boundary; the unknown at the uncertainty lane; the empty lane silent on evidence and draft)",
       stages.run_pipeline("xyzzy plugh?", "", live=False),
       why=_w57)

fails = 0
# THE SELF GATE WITNESSES (the broad-usefulness round): the three meta-
# shapes get the machine's own speech OFFLINE (no mouth, no funnel); and
# the shelf keeps PRECEDENCE - a question whose words hit a card is not
# eaten by the gate. (response-words pin the DATA lines; the why-fn
# checks the lane - only keys the loop bites are used, per the vacuity
# law written in this file's own comment.)
_gate_self = lambda tr: [] if tr.get("lane") == "self" else ["no SELF lane"]
_gate_shelf = lambda tr: ([] if (tr.get("lane") != "self"
                                 and "unknown" not in tr)
                          else ["gate ate a shelf-worded question"])
expect("T50 SELF GATE: 'Who are you?' speaks of itself, not the Gita",
       run("Who are you?", ""), response_has="a shelf of records", why=_gate_self)
expect("T51 SELF GATE: a greeting is answered, free and fast",
       run("Hey, how are you?", ""), response_has="greetings are free", why=_gate_self)
expect("T52 SELF GATE: capability asked of the machine, answered by it",
       run("Do you remember this conversation?", ""),
       response_has="Across the days", why=_gate_self)
expect("T53 SHELF PRECEDENCE: a word that hits a card goes wet, SELF off",
       run("May fasting purge?", "",
           [N("It may purge.", ["F2"], ["CLAIM"])]),
       retrieval="F2", why=_gate_shelf)

for name, tr, kw in T:
    bad = []
    txt = tr.get("response", "")
    fires = " ".join(tr.get("fires", []))
    obs = " ".join(tr.get("observations", []))
    def ok(v): return v is True
    if "appended" in kw and tr.get("caution_appended") is not ok(kw["appended"]):
        bad.append("append=%s" % tr.get("caution_appended"))
    for f in kw.get("fires", []):
        if f not in fires: bad.append("no fire " + f)
    for f in kw.get("no_fires", []):
        if f in fires: bad.append("unexpected fire " + f)
    for o in kw.get("obs", []):
        if o not in obs: bad.append("no obs " + o)
    for o in kw.get("no_obs", []):
        if o in obs: bad.append("unexpected obs " + o)
    if "frame_flag" in kw:
        grp, nm = kw["frame_flag"]
        if not tr.get("frame", {}).get(grp, {}).get(nm):
            bad.append("frame flag NOT fired: " + grp + "/" + nm)
    if "no_frame_flag" in kw:
        grp, nm = kw["no_frame_flag"]
        if tr.get("frame", {}).get(grp, {}).get(nm):
            bad.append("frame flag fired: " + grp + "/" + nm)
    for grp, nm in kw.get("no_frame_flags", []):
        if tr.get("frame", {}).get(grp, {}).get(nm):
            bad.append("frame flag fired: " + grp + "/" + nm)
    for r in kw.get("retrieval_has", []):
        if r not in tr.get("retrieval", []): bad.append("no retrieval " + r)
    for r in kw.get("retrieval_lacks", []):
        if r in tr.get("retrieval", []): bad.append("unexpected retrieval " + r)
    # THE VACUITY FIXED (third instance of the sin in two days: a kwarg
    # the loop never read = a witness that asserts nothing): T39a/b and
    # T45 have been riding this name since it was coined; now it bites.
    if "retrieval_eq" in kw and tr.get("retrieval", []) != list(kw["retrieval_eq"]):
        bad.append("retrieval != given " + str(kw["retrieval_eq"]))
    if "packet_has" in kw:
        for s in kw["packet_has"]:
            if s not in stages.packet_text(tr.get("retrieval", [])):
                bad.append("packet-line lacks " + s)
    if "blocked" in kw and tr.get("blocked") is not ok(kw["blocked"]):
        bad.append("blocked=%s" % tr.get("blocked"))
    if "unknown" in kw and tr.get("unknown") is not True:
        bad.append("no UNKNOWN exit")
    if "response_has" in kw and kw["response_has"] not in txt:
        bad.append("response lacks " + kw["response_has"])
    if "response_lacks" in kw and kw["response_lacks"] in txt:
        bad.append("response still carries " + kw["response_lacks"])
    if "has_finding" in kw and kw["has_finding"] not in " ".join(
            tr.get("audit_findings", [])):
        bad.append("no finding " + kw["has_finding"])
    if "ops" in kw:
        for o in kw["ops"]:
            if o not in " ".join(tr.get("repair_ops", [])): bad.append("no op " + o)
    draft0 = (tr.get("draft") or [{}])[0]
    if "note_has" in kw and not any(kw["note_has"] in n for n in draft0.get("notes", [])):
        bad.append("no note " + kw["note_has"])
    if "reading_has" in kw and kw["reading_has"] not in draft0.get("reading", ""):
        bad.append("no reading " + kw["reading_has"])
    if "note_dropped" in kw and sorted(draft0.get("cite_dropped") or []) != sorted(kw["note_dropped"]):
        bad.append("no cite-drop")
    # THE WINDOW KEY (MVP): the door/window's own witness — the value is
    # a fn returning its complaints. The vacuity law honored up front:
    # a key the loop does not read rides vacuous (the third sin).
    if "why" in kw:
        bad += kw["why"](tr)
    if bad:
        fails += 1
        print("FAIL  %s   %s" % (name, "; ".join(bad)))
    else:
        print("ok    %s" % name)
print("\n%d/%d pass — %s" % (len(T) - fails, len(T),
                             "HARNESS GREEN" if not fails else "HARNESS RED"))
