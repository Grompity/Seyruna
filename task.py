# task.py — the TASK RUNNER (A1): a bounded voyage of research passes, the
# conversational commands on top, and NOTHING else. The division of labor is
# the mission's own: the conversation stays the conversation; this module is
# the runner the conversation may command (kept SEPARATE so a task can be
# issued naturally while the runner manages the bytes).
# Reuses, never re-founds: research.run is one evidence pass (its four
# outcomings are ALL passes; its gap-words become the gap-list); research.live
# is the ONE joining mouthful (the dry law stands: one source does not join);
# stages.call is the ONE seam (never named by a caller); research.hold is the
# single write-path — the holding area stays DISPOSABLE (blowing it away
# forgets the task; that is stated, not hidden).
# The BUDGET is an accumulator, never a wall-clock: spent.secs rides summed
# pass-durations, so an overnight PAUSE costs the voyage nothing and a
# RESUME can never un-spend. The gate is PRE-REQUEST (a pass does not start
# without margin), the safety lanes' shape. ONE mouthful is never re-sent on
# an ambiguity: a pass that settles nothing AND opens nothing is one coin;
# its repeat is STALLED (the anti-reroll law at the task's address).
# Modes: a door-call runs ONE pass (the chat stays responsive at one-to-two
# mouthfuls a turn); Task.auto() runs to a terminal state — the foundation of
# the unattended hour, no daemon, no second pipeline: auto rides the SAME
# pass function. Statuses: resumable OPEN (the crash point) and PAUSED (the
# operator); terminal-for-the-run DONE, BUDGET (caps reached — the open work
# rides the report), STALLED (the ambiguous request), CANCELLED.
# No arbitrary filesystem authority beyond the holding area; the protected
# bytes answer the runner's pen with a refusal (research.hold's own law).
import json
import os
import time

import research
import stages

STATUSES = ("OPEN", "PAUSED", "DONE", "BUDGET", "STALLED", "CANCELLED")
RESUMABLE = ("OPEN", "PAUSED")
STATE_NAME = "task_state.json"
DEFAULTS = {"max_passes": 4, "max_calls": 8, "max_secs": 600.0, "margin_secs": 30.0}

PLAN_SYS = (
    "You are planning ONE research pass. Choose which designated sources the "
    "pass should reach, by their ids from the MENU shown; you may not invent "
    "an id (a choice outside the menu dies, noted - the cite-law's shape). "
    "Name the focus the pass serves in a few words. "
    "Respond ONLY with JSON: {\"designated\": [ids shown], \"focus\": \"...\"}")


def state_path(to=None):
    return os.path.join(to or os.environ.get("TASK_STATE") or research.HOLD_DIR,
                        STATE_NAME)


class _Budget(Exception):
    pass


class _NoProgress(Exception):
    pass


class Task:
    """One record, one file, no registry: the checkpoint IS the ledger."""

    def __init__(self, record=None, to=None, mouth=None, fetch=None, clock=None):
        self.to = to or os.environ.get("TASK_STATE") or research.HOLD_DIR
        self.mouth = mouth                       # stages.call's shape (or a stand-in)
        self.fetch = fetch or research.default_fetch
        self.clock = clock or time.monotonic
        self.r = record
        if self.r is None and os.path.isfile(state_path(self.to)):
            with open(state_path(self.to)) as fh:
                self.r = json.load(fh)

    # ---- persistence: crash-safe (tmp, write, replace), never a re-spend ----
    def _checkpoint(self):
        os.makedirs(self.to, exist_ok=True)
        tmp = state_path(self.to) + ".tmp"
        with open(tmp, "w") as fh:
            json.dump(self.r, fh)
        os.replace(tmp, state_path(self.to))
        return self.r

    def status(self):
        return (self.r or {}).get("status", "NONE")

    def status_line(self):
        r = self.r or {}
        sp, bd = r.get("spent", {}), r.get("budget", DEFAULTS)
        return ("task %s status=%s passes=%d/%s calls=%d/%s secs=%.1f/%s "
                "settled=%d gaps=%d"
                % (r.get("id", "-"), self.status(),
                   sp.get("passes", 0), bd.get("max_passes"),
                   sp.get("calls", 0), bd.get("max_calls"),
                   sp.get("secs", 0.0), bd.get("max_secs"),
                   len(r.get("settled") or []), len(r.get("gaps") or [])))

    # ---- the mouth: counted, laned, NEVER re-raised ----
    def _say(self, system, user):
        sp = self.r["spent"]
        if sp["calls"] >= self.r["budget"]["max_calls"]:
            raise _Budget()
        sp["calls"] += 1
        out = (self.mouth or stages.call)(system, user)
        txt = (out.get("content") or "") if isinstance(out, dict) else str(out)
        if txt.startswith("[MOUTH ERROR"):
            self.r["notes"].append("mouth:unavailable")       # laned, not raised
        return txt

    def _menu(self):
        out = {}
        for i, m in enumerate(self.r.get("menu") or []):
            mid = str(m.get("id") or ("M%d" % (i + 1)))
            out[mid] = dict(m, id=mid)
        return out

    # ---- one pass: plan (by hand the first, by mouth after) then evidence ----
    def _plan(self, first):
        menu, r = self._menu(), self.r
        settled, gaps = set(r.get("settled") or []), r.get("gaps") or []
        if first and r.get("designated"):
            chosen = [m for mid, m in menu.items() if mid in set(r["designated"])]
            if chosen:
                r["notes"].append("designated by hand")       # the first pass
                return chosen                                 # spends no mouth
        shown = ", ".join("%s=%s" % (mid, "settled" if mid in settled else "open")
                           for mid in menu)
        try:
            row = stages.grab_json(self._say(
                PLAN_SYS,
                "OBJECTIVE: " + str(r.get("objective") or "")
                + "\nFOCUS: " + str(r.get("focus") or r.get("objective") or "")
                + "\nOPEN GAPS: " + (", ".join(gaps) or "(none yet)")
                + "\nMENU (id=status): " + (shown or "(empty - nothing to reach)")
                + "\nPrefer sources not yet settled; an id outside the MENU dies."), "{")
        except ValueError:
            r["notes"].append("plan:fell-back")               # laned, never raised
            return []
        picks = [str(c) for c in (row.get("designated") or [])]
        dead = [c for c in picks if c not in menu]
        if dead:
            r["notes"].append("plan dropped: " + "+".join(dead))  # the cite-law
        if row.get("focus"):
            r["focus"] = str(row["focus"])
        return [menu[c] for c in picks if c in menu]

    def _pass(self, items):
        r = self.r
        spec = {"id": "%s-p%d" % (r["id"], r["spent"]["passes"] + 1),
                "designated": items, "bounds": r.get("bounds") or {}}
        # research.live IS research.run plus the ONE joining mouthful (it
        # re-runs the spec itself); the dry law rides INSIDE it: a pass under
        # two rows never mouths to join and spends nothing.
        art = research.live(spec, fetch=self.fetch, mouth=self._say)
        ids = [row["id"] for row in art["rows"]]
        settled = set(r.get("settled") or [])
        moved = bool(set(ids) - settled) or bool(
            [g for g in art["gaps"] if g not in (r.get("gaps") or [])])
        r["settled"] = sorted(settled | set(ids))
        r["gaps"] = sorted(set(r.get("gaps") or []) | set(art["gaps"]))
        r["last_status"] = art["status"]
        if art["status"] == "CONTENDING":
            # the conflict is PRESERVED, never smoothed: the report names it
            # (a cross-check by a FRESH designation is the next milestone's
            # hour — the foundation is that the conflict rode the bytes).
            r["notes"].append("contending preserved (the report names the conflict, never smooths it)")
        r["artifacts"] = (r.get("artifacts") or []) + [art]
        return art, moved

    # ---- the loop: a door-call runs ONE pass; auto() runs to a terminal ----
    def _gate(self):
        r = self.r
        bd, sp = r["budget"], r["spent"]
        if sp["passes"] >= bd["max_passes"]:
            return "BUDGET"
        if sp["calls"] + 1 >= bd["max_calls"]:      # conservative by one mouth
            return "BUDGET"
        if sp["secs"] > bd["max_secs"] - bd.get("margin_secs", DEFAULTS["margin_secs"]):
            return "BUDGET"
        return None

    def _spend(self, t0):
        r = self.r
        r["spent"]["passes"] += 1
        r["spent"]["secs"] = round(r["spent"]["secs"] + (self.clock() - t0), 3)

    def _run_slice(self, passes=1):
        r = self.r
        done = 0
        while r["status"] == "OPEN" and done < passes:
            g = self._gate()
            if g:
                r["status"] = g
                break
            t0 = self.clock()
            try:
                items = self._plan(r["spent"]["passes"] == 0)
                if not items:
                    raise _NoProgress()
                art, moved = self._pass(items)
                self._spend(t0)
                if not moved:
                    r["stall"] = r.get("stall", 0) + 1
                else:
                    r["stall"] = 0
                min_s = (r.get("bounds") or {}).get("min_sources", 1)
                # SERVED, cross-pass: either the shelf spoke CLEAN this pass,
                # or the voyage's own floor is met with nothing left open.
                # (EMPTY rides the gap-lanes: gaps present => never served,
                # so it coins once and takes STALLED or BUDGET honestly.)
                if ((len(r["settled"]) >= min_s and not r["gaps"])
                        or art["status"] == "DONE"):
                    r["status"] = "DONE"
                    if r["gaps"]:
                        r["notes"].append("served, yet gaps ride: the report names them")
                    break
                if r["stall"] >= 2:
                    r["status"] = "STALLED"
                    r["notes"].append("the ambiguous request repeated: no reroll")
                    break
            except _Budget:
                r["status"] = "BUDGET"
                break
            except _NoProgress:
                self._spend(t0)
                r["stall"] = r.get("stall", 0) + 1
                if r["stall"] >= 2:
                    r["status"] = "STALLED"
                    r["notes"].append("the ambiguous request repeated: no reroll")
                    break
            done += 1
            self._checkpoint()
        self._checkpoint()                 # the break paths ride too: a
        if r["status"] not in RESUMABLE:  # terminal state is never unspilled
            self.report()                          # terminal: the durable word
        return r

    # ---- the conversational surface of the runner (all zero-mouth) ----
    def start(self, task_id, objective, menu, designated=None, bounds=None,
              budget=None):
        if self.r is not None and self.status() in RESUMABLE:
            # an afloat voyage is NOT silently restarted (the ALREADY_COMPLETE
            # law, adopted whole): resume it, or cancel, or name it fresh.
            self.r["notes"] = (self.r.get("notes") or []) + \
                ["start refused: a task is afloat (resume it, or cancel)"]
            return self._checkpoint()
        self.r = {"id": task_id, "objective": objective,
                  "deliverable": "the report: settled records, our synthesis, open gaps",
                  "status": "OPEN",
                  "budget": dict(DEFAULTS, **(budget or {})),
                  "spent": {"passes": 0, "calls": 0, "secs": 0.0},
                  "menu": list(menu or []), "designated": list(designated or []),
                  "bounds": dict(bounds or {}),
                  "settled": [], "gaps": [], "notes": [], "stall": 0}
        return self._run_slice(1)

    def resume(self, **raise_budget):
        if self.r is None:
            return {"id": "-", "status": "NONE",
                    "note": "task: none afloat - start one with /task start"}
        if self.status() not in RESUMABLE:
            self.r["notes"] = (self.r.get("notes") or []) + \
                ["resume of a " + self.status() + " task: the caps change, not the past"]
        for k in ("max_passes", "max_calls", "max_secs"):
            if k in raise_budget:
                self.r["budget"][k] = raise_budget[k]
        if self.status() == "PAUSED":
            self.r["status"] = "OPEN"
        out = self._run_slice(1)
        return out

    def pause(self):
        if self.status() in RESUMABLE:
            self.r["status"] = "PAUSED"
            return self._checkpoint()
        return self.r

    def cancel(self):
        if self.r is None:
            return None
        self.r["status"] = "CANCELLED"
        self._checkpoint()
        return self.report()

    def auto(self):
        """The unattended foundation: run to a terminal state on the SAME
        pass function (no daemon, no second pipeline)."""
        if self.r is not None and self.status() in RESUMABLE:
            self.r["status"] = "OPEN"
            return self._run_slice(len(self.r.get("menu") or []) + 1)
        return self.r

    # ---- the report: durable evidence; completed vs unresolved, named ----
    def report(self):
        r = self.r or {}
        arts = r.get("artifacts") or []
        joins = [a.get("synthesis") for a in arts if a.get("synthesis")]
        lines = ["TASK %s %s" % (r.get("id", "-"), self.status()),
                 "objective: " + str(r.get("objective", "")),
                 "deliverable: " + str(r.get("deliverable", "")),
                 "spent: passes=%d calls=%d secs=%.1f of max %s/%s" % (
                     (r.get("spent") or {}).get("passes", 0),
                     (r.get("spent") or {}).get("calls", 0),
                     (r.get("spent") or {}).get("secs", 0.0),
                     (r.get("budget") or {}).get("max_passes"),
                     (r.get("budget") or {}).get("max_calls")),
                 "settled (sourced): " + (", ".join(r.get("settled") or []) or "(none)"),
                 "ours (synthesis, UNSOURCED by kind): "
                     + ("; ".join(j.get("lineage", "?") for j in joins) or "(no joining)"),
                 "open: " + (", ".join(r.get("gaps") or []) or "(no gaps)")
                     + " | notes: " + ("; ".join(r.get("notes") or []) or "(none)"),
                 "the open work rides the gaps and the notes, not the silence."]
        art = {"task_id": r.get("id"), "status": self.status(), "lines": lines,
               "spent": r.get("spent"), "settled": r.get("settled"),
               "gaps": r.get("gaps"), "notes": r.get("notes")}
        if self.status() in ("DONE", "BUDGET", "STALLED", "CANCELLED"):
            research.hold(art, "task-%s-%s.json" % (r.get("id"), self.status().lower()),
                          to=self.to)
        return art


WORDS = ("start", "inspect", "pause", "resume", "cancel")


def handle(q, task=None, clock=None):
    """The conversational command lane: deterministic, ZERO mouthfuls.
    '/task start <objective>' | '/task inspect|status|report|why' (a report
    rides the status line) | '/task pause|resume|cancel'. An unknown word
    answers USEFULLY (the state plus the recognized words) - never a shrug,
    never a model."""
    t = task if task is not None else Task()
    parts = q.split(None, 2)
    word = (parts[1].lower() if len(parts) > 1 else "inspect")
    if word == "start":
        objective = (parts[2] if len(parts) > 2
                     else "(no objective: the last run's shelf rides)")
        t.start(task_id="A1", objective=objective,
                menu=(t.r or {}).get("menu") or [],
                designated=(t.r or {}).get("designated") or [])
        return {"response": "started: " + objective, "why": {"lane": "task"},
                "trace": t.r}
    if word not in WORDS:
        return {"response": ("task: " + t.status().lower()
                             + " - recognized: " + ", ".join(WORDS[1:4]) + ", " + WORDS[4])
                + " (start too)",
                "why": {"lane": "task", "unknown-word": word}, "trace": t.r}
    if word == "pause":
        t.pause()
    elif word == "resume":
        t.resume()
    elif word == "cancel":
        t.cancel()
    line = t.status_line()
    if word in ("inspect", "status", "report", "why"):
        line += "\n" + "\n".join(t.report()["lines"])
    return {"response": line, "why": {"lane": "task", "task": t.r}, "trace": t.r}
