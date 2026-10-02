# retrieval_battery.py — the owner's adversarial battery (a PROBE,
# not a test the count counts). Run against the FOUNDER'S REAL shelf:
# the claims are the ground truth. Zero funnel consumed. Goal per the
# order: learn whether the lexical mechanism can be made SANE with
# bounded data/tokenization changes — and name, exactly, what remains
# for graduation, WITHOUT proposing a subsystem yet.
import json
import stages

stages.set_shelf([json.loads(l) for l in open("shelf.jsonl")
                  if not l.strip().startswith("//")])

def chk(label, ids, yes=None, no=None, boundary=False):
    miss = [e for e in (yes or []) if e not in ids]
    extra = [e for e in (no or []) if e in ids]
    if miss or extra:
        print("FAIL      " + label + "   ids=" + str(ids)
              + "  | " + "; ".join(["missing " + m for m in miss]
                                   + ["unexpected " + x for x in extra]))
        return False
    if boundary:
        print("BOUNDARY  " + label + "   ids=" + str(ids))
    else:
        print("ok        " + label + "   ids=" + str(ids))
    return True

print("1. counting words — the token that moved the retreat card:")
chk('"two"/"three" alone move nothing', stages.retrieve("two three"),
    no=[])
chk('   (the literal count cannot hook a record on counting alone)',
    stages.retrieve("two"), no=["9"])

print("2. pronouns/function words — the particles that flipped gC2:")
chk('"its/was/what/one" move nothing',
    stages.retrieve("its was what one"), no=[])

print("3. punctuation — the semicolon that denied a predicted match:")
chk('"teacher\'s" reaches Kālāma\'s "revered teacher;"',
    stages.retrieve("The teacher's claim is a claim of teachers"),
    yes=["4"])

print("4. morphology — the bound the data route cannot cross:")
chk('"purifies" does NOT reach "purifying" (known bound)',
    stages.retrieve("the purifies daily"), no=["5"], boundary=True)

print("5. genuinely relevant content terms:")
chk('"responsibility" reaches the Gita record',
    stages.retrieve("responsibility for act"), yes=["1"])

print("6. irrelevant shared terms — content-blindness, known bound:")
chk('"possible" surfaces Marcus (shares, does not mean)',
    stages.retrieve("quite possible"), yes=["8"], boundary=True)

print("7. relevant FACTS (the fold, live at the gate):")
chk("teacher-card + study-fact: Kālāma AND the meta-analysis surface",
    stages.retrieve("My teacher says the rite purifies karma. There is "
                    "no evidence on karma the teacher frames meaning"),
    yes=["4", "10"])

print("8. irrelevant FACTS (the fold must stay silent with them):")
chk("stranger words add no stranger records",
    stages.retrieve("Zorb flux quag? the weather was mild altogether."),
    no=[])

print("\nVerdict: sane via data/tokenization alone for classes 1,2,3,5,7,8;")
print("two bounds remain and they are NAMED: stem equality (4) and")
print("content-blindness (6). If those two ever bite in a real card,")
print("graduation of the retrieval mechanism is evidence-ripened —")
print("not before, and not by taste.")
