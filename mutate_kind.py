# mutate_kind.py — the mutation family the sign-off letter ordered:
# KIND says what SORT of content a record is; LEVEL says its epistemic
# RANK; neither may serve for the other, and the new field may not move
# level, authority, or constitutional behavior by itself. All runs are
# offline (injected drafts): the family is deterministic and as
# reproducible as the rest of the testing.
import copy
import stages

KFIX = [
 {"id": "K1", "claim": "The rite is said to purify.", "work": "Rite-Text",
  "level": "INTERPRETIVE", "edges": [], "evidence": "n/a",
  "kind": "METHODOLOGY"},
 {"id": "K2", "claim": "The study notes the rite.", "work": "Studies",
  "level": "EMPIRICAL", "edges": [], "evidence": "PRESENT",
  "kind": "PSYCHOLOGY"},
 {"id": "K3", "claim": "A saying stands in another book.",
  "work": "Elsewhere", "level": "DOCUMENTED", "edges": [],
  "evidence": "n/a"}]                       # kind ABSENT: silence itself

def N(t, cites):
    return {"node": t, "cites": cites, "verbs": ["CLAIM"],
             "uncertainty": None}

def run(node, cite):
    return stages.run_pipeline("Does the rite purify?", "alone",
                                draft=[N(node, cite)], live=False,
                                sim_findings=[])

def view(tr):
    return (str(tr.get("fires")), str(tr.get("observations")),
            str(tr.get("response")), str(tr.get("blocked")))

fails = 0
stages.set_shelf(copy.deepcopy(KFIX))
base = view(run("The rite purifies.", ["K1"]))     # INTERPRETIVE, flat

# K1: flip the KIND ALONE (METHODOLOGY -> METAPHYSIC): the whole trace
# identical, or the field is already secretly doing work it was not
# given. (The mutation doctrine, applied to the NEW field the day it
# enters.)
shelf = copy.deepcopy(KFIX)
shelf[0]["kind"] = "METAPHYSIC"
stages.set_shelf(shelf)
flip = view(run("The rite purifies.", ["K1"]))
if flip == base:
    print("ok    K1 the kind flipped ALONE moves nothing (the rank is the level's)")
else:
    fails += 1; print("FAIL  K1 the kind moved behavior before any check earned it")

# K2: STRIP the field everywhere: absence is SILENCE, not an
# UNKNOWN-inference, and silence moves nothing.
shelf = copy.deepcopy(KFIX)
for rec in shelf:
    rec.pop("kind", None)
stages.set_shelf(shelf)
strip = view(run("The rite purifies.", ["K1"]))
if strip == base:
    print("ok    K2 absence of kind = silence; stripping moves nothing")
else:
    fails += 1; print("FAIL  K2 absence was read as a fact")

# K3: the SAME kind set on two levels: behavior follows the LEVEL
# ALONE — INTERPRETIVE flat promotes, EMPIRICAL flat does not.
shelf = copy.deepcopy(KFIX)
shelf[1]["kind"] = "METHODOLOGY"          # now BOTH records PSYCHOLOGY-adjacent?
shelf[0]["kind"] = "PSYCHOLOGY"; shelf[1]["kind"] = "PSYCHOLOGY"
stages.set_shelf(shelf)
tr_a = run("The rite purifies.", ["K1"])          # INTERPRETIVE + flat
tr_b = run("The study notes it.", ["K2"])         # EMPIRICAL + flat
fa = " ".join(tr_a["fires"]); fb = " ".join(tr_b["fires"])
if "RP-07:promotion" in fa and "RP-07:promotion" not in fb:
    print("ok    K3 one kind, two levels: the rank follows the LEVEL, never the kind")
else:
    fails += 1; print("FAIL  K3 the kind touched the rank")

# K4: NON-DECISION does NOT make a claim into evidence: an INFERENTIAL
# record kinded NON-DECISION, spoken flat, still promotes. (Cite-shown
# note, learned the hard way at first run: a cite on a record the gate
# did not SHOW is DROPPED, promotion never runs, and the check sits
# vacuous - the boundary bites even inside the kind family, so K4/K4b
# speak through the SPOKEN-SHOWN K1 and state their level on it.)
shelf = copy.deepcopy(KFIX)
shelf[0]["level"] = "INFERENTIAL"; shelf[0]["kind"] = "NON-DECISION"
stages.set_shelf(shelf)
tr_c = run("The rite purifies.", ["K1"])
if "RP-07:promotion" in " ".join(tr_c["fires"]):
    print("ok    K4 NON-DECISION does not dignify: INFERENTIAL still promotes")
else:
    fails += 1; print("FAIL  K4 the kind smuggled rank")

# K4b: WITNESS-STATE at DOCUMENTED, spoken flat, promotes nothing and
# confers nothing: the DOCUMENTED flat stands (the founder's clause —
# a witnessed state is no evidence just because it is on the shelf).
shelf = copy.deepcopy(KFIX)
shelf[2]["level"] = "DOCUMENTED"; shelf[2]["kind"] = "WITNESS-STATE"
shelf[0]["level"] = "DOCUMENTED"; shelf[0]["kind"] = "WITNESS-STATE"
stages.set_shelf(shelf)
tr_d = run("The rite purifies.", ["K1"])
if "RP-07:promotion" not in " ".join(tr_d["fires"]):
    print("ok    K4b WITNESS-STATE confers no rank: the level alone spoke")
else:
    fails += 1; print("FAIL  K4b the kind conferred an authority")

print("\n%d/5 kind family — %s" % (5 - fails,
      "THE TWO AXES HOLD APART" if not fails else "FAMILY RED"))
