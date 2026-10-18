# coral.py — the HANDOFF BOUNDARY to the CORAL lab (A2). Ascended's side ONLY:
# the lab keeps its own law at its own bytes; this module READS the lab and
# WRITES only into the holding area (research.hold is still the one pen — the
# A1 law stands whole). Zero new dependencies; zero network; a read that cannot
# be made answers as a lane, never as a raise.
# What the boundary witnesses and what it merely RECORDS (the probes run at
# the shell, and the report quotes their bytes):
#   * the pin scale — the lab's recorded digest scale is shasum -b (SHA-1, first
#     ten hexits), NOT sha256 (the first weighing here guessed wrong until the
#     lab's own record corrected the scale);
#   * the lab's committed bytes (its test file is named, never executed FROM
#     this repo — the O1 controller imports runner and planner, which exist at
#     the lab's root only; running the lab's own battery from here means
#     running IT there, which A2 does not do);
#   * a candidate in the lab's OWN shape, handed here, has never been walked by
#     the lab's controller and its own evaluator (the lab's O2 report names that
#     road NOT TESTED); evaluated_by_lab rides False until the lab says otherwise.
# Transcribed from the lab at the A2 checkpoint (its bytes own the record; the
# recomputed pins below are the check): branch o1-controller @ 0910554; main at
# 0d28afb; protected docs pinned at af3117a6ca/d7724cb793/be650831cf; the frozen
# law, quoted verbatim from its committed orchestrator header.
import hashlib
import os
import subprocess

import research
import stages

LAB_DEFAULT = os.environ.get("CORAL_LAB") or os.path.join(
    os.path.dirname(stages.BASE_DIR), "ascended-coral-p1", "loop")
EVAL_FILES = ("test_loop.py", "o1_probes.py")      # the lab's evaluator, committed
PATTERN = "test*.py"                              # the lab's discovery pattern
PINNED_TIP = "0910554"
PINNED_BRANCH = "o1-controller"
PINNED_MAIN = "0d28afb"                            # the recorded baseline ref
PINNED_DOCS = {"constitution.md": "af3117a6ca",
               "foundation.md": "d7724cb793",
               "golden-set.md": "be650831cf"}
LAW = ("tests are never edited to pass, and the baseline is measured, "
       "never assumed",
       "the evaluator (test_loop.py, o1_probes.py, evidence dirs, .gitignore) "
       "is PROTECTED",
       "zero rerolls: one POST per cycle; a rejection is a class, recorded")
KEY_ORDER = ("changed", "evaluated_by_lab", "lab", "law", "notes", "pins",
             "proposal", "status", "task_id")        # sorted — the frozen shape


def scale(path):
    """the lab's scale, recomputed here (shasum -b: SHA-1, first ten hexits)."""
    try:
        return hashlib.sha1(open(path, "rb").read()).hexdigest()[:10]
    except OSError:
        return None


def pins():
    """the three protected docs, weighed on the lab's scale vs the lab's
    recorded pins. Ascended's side of the boundary — no lab call."""
    out = {}
    for doc, pinned in PINNED_DOCS.items():
        now = scale(os.path.join(stages.BASE_DIR, doc))
        out[doc] = {"now": now, "pinned": pinned, "match": now == pinned}
    return out


def lab_refs(lab=None):
    """the lab's own .git bytes — no subprocess, no lab write."""
    lab = lab or LAB_DEFAULT
    head = os.path.join(lab, ".git", "HEAD")
    try:
        raw = open(head).read().strip()
    except OSError:
        return {"present": False, "lab": lab, "branch": None, "tip": None,
                "main": None}
    if raw.startswith("ref: "):
        branch = raw[5:]
        tip = ""
        try:
            tip = open(os.path.join(lab, ".git", branch)).read().strip()
        except OSError:
            pass
    else:
        branch, tip = "(detached)", raw
    main = ""
    try:
        main = open(os.path.join(lab, ".git", "refs", "heads", "main")).read().strip()
    except OSError:
        pass
    return {"present": True, "lab": lab, "branch": branch, "tip": tip, "main": main}


def lab_clean(lab=None):
    """git status --short at the lab — READ-ONLY; git's absence is a lane, not
    a raise (the bridge's own lesson)."""
    try:
        r = subprocess.run(["git", "-C", lab or LAB_DEFAULT, "status", "--short"],
                           capture_output=True, text=True, timeout=30)
    except (OSError, subprocess.SubprocessError):
        return "git-absent"
    return not (r.stdout + r.stderr).strip()


def proposal(changed, task_art=None, notes=(), to=None, lab=None):
    """the handoff record: FROZEN KEYS at build (the lab's G7 bug-class,
    adopted whole — a verdict-shape slip must never look like an experiment
    fault), held by the one pen into the holding area."""
    art = {"proposal": "A2: the founder's menu file + a bounded multi-pass campaign on the existing auto() road",
           "task_id": (task_art or {}).get("task_id"),
           "status": (task_art or {}).get("status"),
           "changed": list(changed),
           "law": list(LAW),
           "evaluated_by_lab": False,
           "pins": pins(),
           "lab": lab_refs(lab),
           "notes": ["the lab's suite gate over an Ascended-shaped tree is VACUOUS (its evaluator is a unittest suite; Ascended answers with a custom harness): a green there must never be read as acceptance"] + list(notes)}
    if tuple(sorted(art)) != KEY_ORDER:
        raise ValueError("coral: the handoff's keys moved (the G7 class)")
    return research.hold(art, "a2-handoff.json", to=to)
