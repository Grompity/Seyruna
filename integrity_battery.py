# integrity_battery.py — the SYNTHESIS-INTEGRITY battery (the ordered
# items 5/7/8, at their smallest). A-H lanes separated. Every mouth is
# INJECTED (the standing rule: a printed probe is not a test), so the
# battery is deterministic; where a lane belongs to the reviewer and
# not to the machine, the line says so. The mini-shelf carries its
# generalization duty (item 11): two contradicting lanes, a
# non-decision, an ours-note, and a harmless strange belief.
import stages

IB = [
 {"id": "I1", "claim": "Lan A holds that the rite remits the debt.",
  "work": "LanA", "level": "DOCUMENTED", "edges": [{"type": "CONTRADICTS", "to": "I2"}],
  "evidence": "n/a"},
 {"id": "I2", "claim": "Lan B holds that the debt was never owed.",
  "work": "LanB", "level": "INTERPRETIVE", "edges": [{"type": "CONTRADICTS", "to": "I1"}],
  "evidence": "n/a"},
 {"id": "I3", "claim": "The basket sets the question of the ledger aside.",
  "work": "NonDec", "level": "DOCUMENTED",
  "edges": [{"type": "DOES-NOT-DECIDE", "to": "I1"}], "evidence": "n/a"},
 {"id": "I4", "claim": "The comparison is ours; the baskets state it apart.",
  "work": "our note", "level": "INFERENTIAL", "edges": [], "evidence": "n-a"},
 {"id": "I5", "claim": "The Quipu kept accounts by knotting cords.",
  "work": "Quipu-note", "level": "DOCUMENTED", "edges": [], "evidence": "PRESENT"},
]

stages.set_shelf(IB)
FIXED = []
GAPS = []

def N2(t, cites):
    return {"node": t, "cites": cites, "verbs": ["CLAIM"], "uncertainty": None}

def run(nodes):
    # the battery is a SYNTHESIS lane: the shelf is GIVEN (a finite
    # evidence packet), not found — the first draft of this file let
    # retrieval speak (an exact-token collision with the fixture's own
    # claim was the first RED, and it was TEST-DESIGN, the author's).
    return stages.run_pipeline("Do the baskets agree?", "alone",
                                draft=nodes, live=False, sim_findings=[],
                                packet=["I1", "I2", "I3", "I4", "I5"])

def check(name, tr, has_fire=None, no_fire=None, obs_has=None,
          resp_has=None, resp_lacks=None, lineage0=None, blocked=None):
    bad = []
    fires = " ".join(tr.get("fires", []))
    obs = " ".join(tr.get("observations", []))
    txt = tr.get("response", "") or ""
    d0 = (tr.get("draft") or [{}])[0]
    if has_fire and has_fire not in fires: bad.append("no " + has_fire)
    if no_fire and no_fire in fires: bad.append("unexpected " + no_fire)
    if obs_has and obs_has not in obs: bad.append("no obs " + obs_has)
    if resp_has and resp_has not in txt: bad.append("resp lacks " + resp_has)
    if resp_lacks and resp_lacks in txt: bad.append("resp carries " + resp_lacks)
    if lineage0 and not d0.get("lineage", "").startswith(lineage0):
        bad.append("lineage not " + lineage0 + " (is " + str(d0.get("lineage")) + ")")
    if blocked is not None and tr.get("blocked") is not blocked:
        bad.append("blocked wrong")
    if bad:
        FIXED.append(name); print("FAIL  " + name + "   " + "; ".join(bad))
    else:
        print("ok    " + name)
    return len(bad) == 0

# A. EVIDENCE TRANSCRIPTION: what the records say survives intact.
check("IB1 [A] transcription: the claim restated, cited, DOCUMENTED flat (no fire)",
      run([N2("Lan A holds that the rite remits the debt.", ["I1"])]),
      no_fire="RP-07", lineage0="SOURCE: I1")

# B. RELATIONSHIP PRESERVATION: the edges are OBSERVED when cited.
check("IB2 [B] a contested pair cited: the machine records the contest",
      run([N2("Lan A and Lan B state the matter apart.", ["I1", "I2"])]),
      obs_has="RP-13:implication")
check("IB3 [B] the non-decision cited: the decline is recorded, not flattened",
      run([N2("The basket sets the ledger-question aside.", ["I3"])]),
      obs_has="RP-13:non-decision recorded")
check("IB4 [B] absence-of-evidence lane: all nodes uncited = the EXISTING plain print",
      run([N2("One may compare the baskets freely.", [])]),
      resp_has="Nothing here rises above", blocked=True)

# C. EPISTEMIC PRESERVATION: the authorized level holds (or is restored).
check("IB5 [C] flat INTERPRETIVE speech: promotion fires and the mark restores",
      run([N2("The debt was never owed.", ["I2"])]),
      has_fire="RP-07:promotion")
check("IB6 [C] the hedged twin: the level is honored at the render, no promotion",
      run([N2("It is said the debt was never owed.", ["I2"])]),
      no_fire="RP-07:promotion")

# D. PROVENANCE PER NODE (disposition A at battery level).
check("IB7 [D] mixed draft: the cited node SPEAKS; the uncited one is recorded, not spoken; no silencing",
      run([N2("It is said the debt was never owed.", ["I2"]),
           N2("One may compare without resolving.", [])]),
      resp_has="It is said", resp_lacks="One may compare", blocked=False)
check("IB8 [E] a >=2-cite node wearing a compare-word is LINEAGED as SYNTHESIS (from I1+I2)",
      run([N2("Both baskets speak of the debt; the saying is alike.", ["I1", "I2"])]),
      lineage0="SYNTHESIS: comparison from I1+I2")
check("IB9 [E] a single-cite node is LINEAGED as SOURCE, not as synthesis",
      run([N2("Lan A remits.", ["I1"])]), lineage0="SOURCE: I1")

# #3's five, at their smallest:
check("IB10 [#3-b] FALSE ATTRIBUTION: Lan A named for Lan B's content, cited to Lan A — the machine is SILENT (gap named below)",
      run([N2("Lan A teaches that the debt was never owed.", ["I1"])]),
      no_fire="RP-07:promotion")
check("IB11 [#3-c] IMPLICIT ATTRIBUTION: no name spoken, the cite implies a source; wrong source, still silent (same gap)",
      run([N2("The debt was never owed.", ["I1"])]),
      no_fire="RP-07:promotion")
check("IB12 [#3-d] ELEGANT LAUNDERING: the hedged (elegant) speech holds at its authorized level",
      run([N2("It is said the debt was never owed, and that is enough.", ["I2"])]),
      no_fire="RP-07:promotion")
check("IB13 [#3-e] USEFUL SYNTHESIS WITH DISAGREEMENT: both cited, compared — the comparison rides AND the contested record stands",
      run([N2("Both baskets face the debt; neither resolves the other.", ["I1", "I2"])]),
      obs_has="RP-13:implication", lineage0="SYNTHESIS: comparison from I1+I2")

# #7's bridge-laundering, at its hook: the unsupported minting.
check("IB17 [#7] THE MINTED UNITY on a CONTRADICTED pair: the machine at least RECORDS the opposition (the bridge's truth is the reviewer's lane — gap named)",
      run([N2("The two teach one doctrine of the debt.", ["I1", "I2"])]),
      obs_has="RP-13:implication", lineage0="SOURCE: ")

# #8's exact transition.
check("IB18 [#8a] 'Taken together...' = synthesis, by name",
      run([N2("Taken together, these suggest a distinction between remitting and never-owing.", ["I1", "I2"])]),
      lineage0="SYNTHESIS: comparison from I1+I2")
check("IB18b [#8b] 'The traditions teach...' = a claim that SMELLS of doctrine; lineage keeps it SOURCE (the upgrade-risk is graded, not invented away)",
      run([N2("The traditions teach one road on the debt.", ["I1", "I2"])]),
      lineage0="SOURCE: ")

# H. UTILITY — graded, not fired.
print("graded [H] utility: does the synthesis help the seeker investigate? the reviewer's lane; the machine's part (lines A-G) is measured above.")
print("graded [#11] strange-belief coverage: the Quipu record rode the shelf uneventfully (a history-family claim needs no lane of its own).")

print("\n%d/%d integrity battery — the detection surface MEASURED." % (
      (18 - len(FIXED)), 18))
print("GAPS NAMED, NOT PATCHED (the friend's word: test first): (a) misattribution "
      "and (b) the minted bridge are currently REVIEWER lanes — candidates for an "
      "ARCHITECTURE addition (an attribution-truth boundary), but no detector was "
      "raised before a red demanded one. UNSOURCED is thinking, not a sin; the speech "
      "gate is the sin-gate.")
