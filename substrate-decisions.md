# ASCENDED AI — SUBSTRATE DECISIONS

*An audit's three decisions, tested against the bytes — validated, not implemented.*

## 0. Status

This document validates the three architectural decisions that `substrate-audit.md` named as
the gate before the next implementation phase (rung location; run-state location;
provenance/counter-example, split into two decisions). It is a **decision-validation pass**:
every claim below cites an artifact, no artifact moved, no test moved, the shelf stayed at
twenty-six, and nothing was built, renamed, or reconciled.

Classifications used: **ACCEPTED / ACCEPTED — MINIMAL OPERATIONAL SCOPE / DEFERRED /
REJECTED**, with **UNKNOWN** reserved for what the artifacts cannot ground. The four
hard-stop conditions were checked per decision: a Constitution conflict would STOP the branch;
insufficient evidence says UNKNOWN; a branch that would need to resolve six-vs-nine would stop;
a branch that would invent constitutional authority would be marked governance. The git state
is reported, not repaired (see §7).

The order held as ordered: rung location → run-state location → provenance → counter-example.
No decision borrowed another's unfinished conclusion, and no future architecture was used as
evidence that current machinery exists.

## 1. Decision 1 — Rung location

**Proposal:** *Epistemic rung is a property of the claim/card and belongs on Axis B.* Location
of the rung is decided; the **enumeration is not**.

### Evidence (for)

1. **Foundation II.1, `foundation.md:171`** — *"One document holds claims at every level.
   **The unit of storage is the CLAIM, with its level**, its source chain, and its witnessed
   disagreements."* The location was already the Foundation's own doctrine: the level rides the
   claim, and one document's uniformity is explicitly refused.
2. **Foundation II.2, `:173`** — *"Promotion is gated; demotion is instant. **A claim** may be
   re-tagged upward…"* Every rung-verb the Foundation prints takes the claim as patient.
3. **XIII.1, `:626–627`** — the claim record carries `{text, provenance-class, **claim-status**,
   confidence, counter-example, falsifier, level-history}` on one row — the rung's semantics
   (claim-status) is a field of the claim. **Axis B is defined as *"claim status (how to hold
   this claim)"*** — and the split that makes Axis B the only candidate is the paper's own quote
   of XIII.1 (`promotion.md:87–89`): *"'primary source' answers WHO SAID IT (Axis A — provenance
   is a fact), while 'speculation' answers HOW TO HOLD IT (an epistemic status)"*.
   The paper then demonstrates the separation from the substrate side (`promotion.md:136–139`):
   attestation *"runs on the **origin axis**, so an echo-cycle fails attestation and does not
   fall in rung — **the rung was never at stake**."* A rung that is never at stake where provenance
   is at stake is, by the paper's own arithmetic, on the other axis. **Axis B confirmed.**
4. **The law uses the slot this way** — II.3, `constitution.md:176`: *"Sequence follows the old
   maps — **at claim-status `INTERPRETIVE`**, not as a law of the mind"*; III, `:199`: equivalence
   *"judged on claim-status and scope."* (Recorded, unreconciled: the law's example-word here is a
   SPINE-six word, while III's drift example at `:204` speaks `SPECULATIVE` — a nine-only word. The
   law's own examples lean on **both** enumerations; this is evidence that the six-vs-nine drift
   reaches past the machinery, and this decision refuses to touch it.)
5. **The paper's grant-shape fits the claim** — `promotion.md:38,44`: *"the substrate's two
   grants — rung and membership… A rung is granted, never walked into."* And `:82–85`: a Report
   *"carries origin (Axis A), a source-claimed status, and lineage — and **the rung is absent,
   NOT rung=UNKNOWN(−1)**"*. An absent-but-named slot is only meaningful on the object the grant
   could have landed on — the claim-record. The Bench is barred from the slot (`:126–127`: a
   Bench-granted rung *"would be an un-assented JUDGMENT, the keeper's sin"*), and
   `:115` files *HYPOTHESIS as a status, not a rung* — the paper keeps run-states out of the slot
   exactly as this decision wants run-states out of the claim.
6. **The shelf's own header** (`shelf.jsonl:18–20`) declares every expansion card *"carries
   provenance/level/kind"* — the data already treats the level as a card-constituent (documented
   practice, as ever: a practice recorded, not a law minted).

### Evidence (against / contradictions searched)

- **XIII.1's rendering line** (`foundation.md:628–629`): *"The old Nine-Rung Ladder survives as
  the RENDERING — how a claim's status is shown to a seeker — while storage stays multi-field."*
  Read against the proposal this is **not a contradiction but a division of labor**: the rung is
  *stored* as the claim's claim-status (Axis B), and the ladder is its *display*. The proposal
  decides location; it does not collapse storage to the ladder. Recorded.
- **The law's rung-family word applied to persons** (IV, `constitution.md:216`: *"weighed as
  evidence, never scored into rank"*) — the keeper ranks a **seeker**; that is the Gate's patient,
  never a card's, and it stands untouched by this decision. Boundary note, not contradiction.
- **VI.3's five-and-sixth held at `UNKNOWN`** (`:259`) — the patient there is the **system's
  self-claims** ("recorded as evidence-and-interpretation"), claim-shaped, so the law's own rung
  talk is claim-patiented too. Confirms rather than contradicts.
- **The promotion paper's report-rung-absence** (`:82–85`) — consistent: the slot exists with the
  claim and may go unassigned; absence ≠ −1. Confirms.

### Machinery location (does the current code assume somewhere else?)

`LEVEL_RANK` (`stages.py:79–80`) is the installed enumeration; the **`level` rides the shelf
row** (`BY_ID`), i.e. the claim-row — the machinery already assumes exactly the proposed
location. The one run-side rung-byte is the **node's derived level** (`:328–329`,
*"weakest governs; split"* — `min` over cited cards' ranks): a computed *transcription* of
claim-rungs onto the mouth's node, riding the trace, which is precisely where Decision 2 says
run-bytes live. It is not a second home; it is the claim's rung doing its job once at the node.
The window reads level from `BY_ID` (`window.py:29`) — the claim-row, again.

### Constitutional implications

The decision places a **grant that is already documented practice** (the KS-0.1 carding
"the founder's word"); it **creates no new constitutional authority** and therefore raises no
governance stop. It also does not touch the rung's *motion*: the paper's verdict stands untouched
(`promotion.md:184–185`) — *"rung-HELD has precedent (VI.3); rung-MOVED has none."* Location ≠
movement: the location is decided here, the movement stays in the one novel D-bucket (assent
shape, new patient) with its four open governance questions.

### Verdict

> **DECISION 1: ACCEPTED.**

The rung's location is the **claim/card**, and its axis is **Axis B (claim status)** — by the
Foundation's own unit-of-storage clause (`foundation.md:171`), by XIII.1's axis definitions
(`:614–628`), by the law's claim-status usage (`constitution.md:176,:199`), by the paper's
two-grants architecture (`promotion.md:38–44`), and by the installed data shape. No artifact
contradicts it; two lines of nuance recorded (the rendering-division at `:628–629`; the law's
person-patient rank at IV). **The six-vs-nine remains unresolved and this decision touched it
zero times:** the enumeration (six installed vs nine drafted vs the field's A/B axis-mix) is
untouched, and the fresh finding — the law itself speaks one word from each list (`:176` vs
`:204`) — says the drift runs deeper than the machine, which is the audit's §12 finding,
preserved verbatim, not reconciled.

## 2. Decision 2 — Run-state location

**Proposal:** *Visibility, relevance, and answerability live in the run trace* — the trace is
the canonical address for ephemeral run-state; the trace is **not** a general database and
**not** a second claim-store; the states die with the run; the future Bench is the different
question ("what does one inquiry carry across turns?").

### Current trace representation (the canonical trace exists? — yes)

`run_pipeline` (`stages.py:585–586`) builds exactly **one dict per run** (`versions` stamped
first) and returns it in all three arms:

- **self-lane early return** (`:598–606`) — `lane`, `fires`, `response` (the self-gate's exit;
  no states computed, none needed);
- **RP-10 arms** (`:607–610` and the NOTHING-sibling `:619–629`) — the second arm **already
  carries `grades`, `grade_notes`, `answerability`** — the three states are present in the
  minimal trace where they were computed;
- **full arm** (`:644–663`) — `trace.update({...})` carries `frame`, `analysis`,
  **`grades`, `grade_notes`**, **`answerability`**, `draft`, `fires`, `observations`,
  `blocked`, `caution_appended`, `audit_findings`, `narrow_mouth`, `repair_ops`,
  `required_content`, telemetry, `response`.

The three states' canonical keys, as decided: **visibility** = `retrieval` (+ `lane`,
`retrieval_count`, `context_size`), decided at RETRIEVE (`:592`); **relevance** = `grades` (+
`grade_notes`), decided at GRADE; **answerability** = `answerability`, decided at ANALYZE
(`:647`; and the sibling arm's pinned value `:624`). Nothing is stored outside the dict.

### Evidence the proposal is compatible with the actual machinery

1. **`window.py` already governs the trace as canonical** — header line 1: *"the WINDOW. One
   pure reading of the trace: no second reasoning system, no new truth, no reading back of
   the response text to find reasons (**the trace's own protocol applies to the product**)."*
   The door's own constitution already makes the trace the single address the seeker-side reads;
   naming run-state as trace-property **ratifies** this, and adds zero machinery.
2. **The states already live there** — the door reads `retrieval` (EVIDENCE),
   `grades`/`grade_notes`/`answerability` (the `relevance` key, `:54–58`), and the full-arm trace
   carries them. The decision does not MOVE bytes; it names their home and bars the drift:
   visibility/relevance/answerability may not be promoted into shelf-fields, and (the proposal's
   own guard) the trace is not a store.
3. **Ephemeral nature preserved** — the dict is constructed fresh per call, returned, and
   **nothing persists it**: no file, no second state, no store; the window reads it; the tests
   read it; then it is garbage. The proposal's "states die with the run" is byte-true, and the
   door's `T57` (early-return trace reads all six lanes without raising) is a witness that the
   trace's SHAPE may be incomplete across arms while its PROTOCOL stands — the three keys exist
   wherever their stage runs; the self-lane simply never computes them.
4. **Nothing treats them as durable claim-fields** — `shelf.jsonl` was read whole: across all 26
   rows the fields in use are id/claim/work/who/date/provenance/level/edges/counterexample/
   evidence/locus/kind/note (+card-26's facts/indicators) — **no card carries a
   visibility/relevance/answerability field**. The data itself abstains. promotion.md's class-C
   already ruled the run-states run-scoped and left Bench-location *undecided*, which this
   decision does not change (it names the run's home; it does not name the inquiry's).
5. **Does the future Bench get cleaner or harder?** Cleaner. The decision draws the line the
   Bench needs before it is designed: the **run** already has its home (the trace); the
   **inquiry** (Bench) does not and its design question ("what does one inquiry carry across
   turns?") stays open, unburdened — and, decisively, the decision **prevents the easy
   misstep** of calling the trace the future Bench: *"This does NOT mean the trace becomes a
   general database or second claim-store,"* so a trace that dies with the run is the correct
   *negative example* the Bench must be designed against, not its accidental host.
6. **Would a separate run-state address solve a demonstrated problem?** No demonstrated
   problem. The audit's only recorded run-state findings were **presentation** (the window's one
   `relevance` key bundling grades+answerability+notes — `:54–58`; and the one recorded shape-
   asymmetry: the self-lane trace carries no states because it computes none, which T57 already
   blesses as lane-legal). One duplication to record, not to fix: `grades` rides the full trace
   **twice** (`:646` top-level and `:645` inside `analysis` — the analyze return `:278` puts it
   there); the canonical address is `trace["grades"]` (what the door reads); the decision's word
   "canonical" covers it: the twin key is a redundancy, not a second home. A separate run-state
   *address-object* (a new structure) would be second-state machinery bought for decoration.

### Implications for future Bench

The trace stays ephemeral by ruling; the Bench's address (store? trace-successor? new?) is a
**future design decision, not a gap** (audit §8; paper §4.C-D left it *undecided deliberately*).
One recorded adjacency so it cannot drift later: the window's `lane`-marker (`:86`) and the
UNKNOWN arms already answer "why did this run fall quiet?" — a future cross-turn history of
those answers (one record per question) is a **Bench-side need**, and this decision's
"die with the run" is the boundary that keeps it a need rather than a contradiction.

### Constitutional implications

None needed. A trace-state has no standing: **run-states cost no assent** (the paper's own
criterion, which the audit upheld at §9), so an address inside a run cannot raise a law
question. The decision therefore raises **no new constitutional authority** (no governance
stop) and no hard-stop fires: the Constitution neither commands nor forbids where a run keeps
its notes; the machinery already did this; the tests (T57, the `T58–T66` why-family) already
read it this way.

### Verdict

> **DECISION 2: ACCEPTED.**

The trace is canonical for the three run-states; it stays ephemeral; it is explicitly not a
store and explicitly not the Bench; the one recorded redundancy (grades at the trace top
inside `analysis`, `:645–646`) is a recorded byte, not a moved byte; the six-vs-nine was
untouched. What the acceptance forbids to arrive unnoticed later: any implementation that
stores the trace (a soul-log row, a Bench) must **rename the act** — storing a trace is an act
of the future, and per §8 of the audit the FOUNDATION's soul-log clause (`:266`,
the provenance-composition report *"attached in the soul-log so the drift is MEASURED"*) is
the named home for any durable note about *retrieval's composition* — not an open invitation.

## 3. Decision 3A — Provenance

**Proposal:** *Make provenance operational next.* The field is on every card, read by zero
stages — the audit's G1. The pass was ordered not to design a research provenance system and
not to build chain-walking unless already required.

### Current consumers (verified fresh, this pass)

- `stages.py`: **zero readers.** Every "provenance" token in the spine is a **comment**
  (`:195, 335, 435, 438, 446, 462`) — and the comments' own content is the point: *"No second
  provenance system was raised"*; *"a node that cannot carry its provenance is not ready to
  become speech"* — prose that invokes the word for the **cite**, never reads the **field**.
- `window.py`: zero readers. The EVIDENCE row prints `id, claim, level` (+`kind` when present,
  `:28–31`) — the card's `provenance` never reaches the seeker-side print either.
- `tests.py`: one byte — F4's fixture field `"provenance": "attributed"` (`:24`); **no witness
  asserts on it.** `rule_pack.json`: zero tokens.
- The data, however, is fully loaded: all 26 rows carry it — 21 `primary`; 5 `ours-*`
  (10/14/16/19 `ours-synthesis`; 26 `ours-comparison; web-corroborated 2026-10-01 (… 3/10
  relevant, HIGH)` — corroboration, DATE, and a COUNT welded into one STRING, the audit's G1
  finding verbatim). And the shelf's own header already legislates the shape as practice:
  *"every one carries **provenance**/level/kind"* (`shelf.jsonl:18–19`).

### The sharpest existing need (what behavior touches the field today)

Not decorative, and the byte to prove it is card **10**: its `work` reads *"Goyal et al., JAMA
Internal Medicine (meta-analysis…)"* — a primary-looking citation — while its `provenance`
says **`ours-synthesis`** (our digest of a literature, the bridge-card between
*"this tradition says"* and *"observed evidence"*). Today the mouth receives
`[10] (Goyal et al… | EMPIRICAL)` (`packet_text`, `:543–544`) — the authorship fact that the
whole *"the shelf is evidence-with-an-author"* clause and the paper's *"a reported rung is
read, never adopted"* hinge on is **invisible at cite-time**. The node-level `lineage` label
(`SOURCE / SYNTHESIS / UNSOURCED`, `:330–343`) records only the mouth's *fresh* comparisons; a
**carded** comparison (26) or carded synthesis (10/14/16/19) loses the fact the moment it is cited.
The compare-word detail confirms the direction of the risk: lineage's SYNTHESIS half is gated by
`compare_words` — "the words are DATA" — and T66's own node (*"pull apart"*) misses the listed
*"pulls against"*, computing the **conservative** `SOURCE` (`:340–343`). The word-list is a
floor, never a ceiling — and a card's own `provenance` word would not need to be re-inferred by
words at all.

### Minimum operational scope (what "operational next" must mean, no more)

1. **Reader/stage: SYNTHESIZE's packet rendering** — `packet_text` prints the card's
   `provenance` **when present, silence when absent** (the K2-shaped law of presence the packet
   already runs for `kind`), beside `work | level`. One line, inside the renderer's own
   charter (`:534–536`: *"A RENDERING inside stage 4, not a subsystem: the same spine, the same
   boundary, the same guards"*).
2. **The door mirrors it** — the window's EVIDENCE row gains the field (`window.py:28–31`), so
   mouth-side and seeker-side see the same authorship byte.
3. **Witness route:** a `T47`-pattern extension (`packet_has` pinning the printed token) when
   implementation runs — a lane-side witness over bytes that already exist; no new lane.
4. **What does NOT move:** the cite-boundary (id-based); the NON-DECISION demote (kind-based);
   the promotion-catch (node-rank + hedge); answerability (grades+edges); the rung (still
   inert to all machinery — Decision 1 placed it, nobody moves it). The change's whole blast
   radius is *the bytes the mouth receives*.

**Honest reading of "operational":** no *current frozen behavior* is false without this field —
every named gate (attestation, echo-detection, chain-walk) is future design. The minimum scope
accepted here makes the field **read by machinery and visible to the mouth**, so the word
"authoritative field" stops being a comment's claim and starts being a rendered byte. If the
founder reads "operational" as *"gates something,"* the truthful answer is: the need is
prospective, and this print-role is the smallest thing that makes the field not-dead — with the
gating uses deferred below, and **no parse, no enum, no walker built.**

### Deferred capabilities (explicit, with owners)

chain-walking itself (the FOUNDATION's Casaubon line the paper quotes — *"lineage-provenance
as part of the data… or we dig our own echo-chamber"* — the walker's purpose); the Attestation
gate proper (`promotion.md:136–139` — it *"runs on the origin axis"*, Axis A, not the rung's);
**self-echo detection** (needs a Report to detect; none exists); card-26's welded corroboration-
string parse (date+count — DATA-grammar, a future actuation of it); the Axis-A five-name enum
mapping (`PRIMARY_TEXT → TRANSMISSION/EDITION → SCHOLARLY_READING → PRACTITIONER_READING →
STUDY` at `foundation.md:609–611` vs the data's words `primary/ours-synthesis/ours-comparison/
attributed` — **printing verbatim needs no mapping, and none is invented here**); the RETRIEVE-
side provenance-**composition-report** (G9 — the FOUNDATION's bigger station, `:285`, whose NAME
is already taken by the door's shown-set lane); and the REPORT's own provenance-as-origin
(`promotion.md:82` — no report yet).

### Verdict

> **DECISION 3A: ACCEPTED — MINIMAL OPERATIONAL SCOPE.**

Printed where the mouth already receives (SYNTHESIZE's packet), mirrored where the seeker
already looks (the door's EVIDENCE row), one witness-extension at implementation. **WALK
nothing, gate nothing, map nothing** — the walker, the echo-detection, the enum-mapping, the
corroboration-parse, and the gate's machinery all stay on the deferred ledger. No constitutional
authority is created by printing a claim's own word about who speaks through it (VI.5's
quarantine-clause already shows the law thinks provenance as *constraining*, which is future —
*"quarantined sources are CONSTRAINED, never CLEARED"*).

## 4. Decision 3B — Counter-example

**Proposal:** *Keep the field in the schema; explicitly defer making it operational.*

### Current consumers (verified fresh)

**Zero.** `grep` across the spine/door/tests/pack: the ONLY tokens are fixture and shelf *data* —
and the lane's four fixtures carry the field **empty** (`tests.py:13,17,21,25:
"counterexample": ""` — shape compliant, content empty; the data already practices the
deferral). No stage reads it; no witness asserts it. The near-miss, searched for
specifically, fails to make it a consumer: the only convergence-behavior in the spine —
`RP-13:convergence claimed (ours — the similar saying is not yet the same underlying reality)`
(`stages.py:427–430`) — speaks a **hard-coded literal**, not the field; T44 pins the literal.
So even the closest current behavior is edge-driven and word-fixed.

### Why the deferral is right, and what "required" still commands

The Foundation names Axis D **required** (`:623`: *"the claim's best counter-example (P10 as a
schema field, not a virtue)"*) and P10 scopes the obligation: *"Every **convergence report**
must name its best counter-example — a requirement, not a disclaimer"* (`:143`), which the
founder's own note sharpens: *"P10 was already convergence-scope"* (`:907`) with the eval
guardrail *"L3 convergence/generalization → mandatory counter-example"* (`:915`). P10 lives
where a REPORT and a convergence station exist; the spine runs neither. We do not build
machinery because a field exists — and the shelf is frozen, so there is no carding at risk.

### Future consumers (what would eventually consume it, named precisely)

1. the **convergence-report station** (the Foundation's own pipeline `:200` — *"SYNTHESIS
   (labeled; always paired with its best counter-example, P10)"* — and its BEST-COUNTER-EXAMPLE
   station `:288`) — the field's first natural reader;
2. the **promotion's Boundary gate** (`promotion.md` §5 — *"what the card does not say, what the
   counter-example constrains"*);
3. a **research/evaluation loop's TEST→RESULT→EVAL** — the endorsement's outliver-clause
   (`:737`: *"its reason (the counter-example it survived, the falsifier it met) must outlive
   them"*) and the eval-row's *"explicit falsifier each"* (`:326`) — with the precision that
   **`falsifier` is a SEPARATE field of the seven** and absent from every shelf row (audit
   G4-family; recorded, not repaired);
4. and the FOUNDATION's self-cert clause (`:406`) — a piece must *"pass its own falsifier (what
   would show this piece misled someone?)"* — the evaluation shape the counter-example
   eventually rides.

### Verdict

> **DECISION 3B: DEFERRED.**

No current behavior requires it; the deferral is documented, so the field is not misread as
dead weight: **the obligation to CARRY it stays** (XIII.1 required it; the shelf-freeze means
no carding risks it; a future card that dropped it would break the Foundation regardless of
this deferral — a data-obligation, not machinery), and the **operational** half waits for its
first real consumer (the convergence station or the Boundary gate), whichever arrives first.
The empty-string fixtures are the lane's own quiet witness: the schema shape is respected
today; the content waits for its machinery, exactly as deferred.

## 5. Decision interaction

All four proposals survived; nothing here adds machinery. The intended result, now byte-
located rather than merely intended:

```
CLAIM  (shelf.jsonl rows / BY_ID)
├── Axis B — epistemic rung            [LOCATION SET; enumeration OPEN — untouched]
│     stages.py:79–80 LEVEL_RANK (six, strict)      foundation :616–619 (nine, printed)
├── provenance (Axis A)               [FIELD PRESENT; readers zero]
│     21 "primary" / 5 "ours-*"; 5 readers = comments only (stages :195…:462)
└── durable claim properties
      edges (3 of 6 in use; targets unchecked — G7) · evidence (n/a|n-a drift)
      · locus · counter-example (REQUIRED-CARRIED, deferred-operational)
      · ABSENT: confidence · falsifier · level-history (3 of the mandated 7)

RUN
└── TRACE  (stages.py:585–663, fresh per run, garbage after the door — NOT a store)
├── visibility     = trace["retrieval"] (+ lane)       [decided at RETRIEVE]
├── relevance      = trace["grades"] (+ grade_notes)  [decided at GRADE]
└── answerability  = trace["answerability"]            [decided at ANALYZE]
      (both early-return arms that COMPUTE states carry them; the self-lane computes none)
      (one recorded redundancy: grades also rides trace["analysis"]["grades"] — :645–646)

INQUIRY
└── future BENCH — its ADDRESS is a design decision, not a gap (paper §4.C–D left it so)

COUNTER-EXAMPLE
└── deferred until an actual evaluation/test consumer arrives (convergence station / Boundary gate)

SIX VS NINE RUNG ENUMERATION
└── unresolved — all four decisions passed through it without touching it;
      the law's OWN examples lean on BOTH lists (II.3 "INTERPRETIVE" :176; III "SPECULATIVE" :204)
```

**How they fit without new architecture:**

- **D1 ⊥ D2** by the paper's criterion (free-to-mint = free-to-lose; what stands costs assent):
  the rung is durable and GRANTED → the claim's property; the three states are freely minted
  per run → the trace's. The claim-row carries the rung and **carries no state-field** (26 rows
  read: none does); the grades-map is per-id but lives **inside the trace**, never in `BY_ID` —
  the two addresses do not overlap at one byte.
- **D3A rides inside D1's tree without colliding:** provenance and rung are **different axes on
  the same row** (A prints *"who speaks"*, B prints *"how to hold"*), and the print-role
  prints BOTH (`work | level` gains `provenance`) — so **no decision needs the axis-to-enum
  mapping to exist first**, and none was invented (the mapping itself stays on the deferred
  ledger). D3A's single interaction with D1, recorded in advance: printing both axes together
  makes the **axis-contaminated word** (`DOCUMENTED` — a provenance-shaped name inside the
  status-ladder) visible as such; that is an observation *about the unresolved enumeration*,
  not a resolution, and D1's firewall (§"the qualification") keeps it so.
- **D3B attaches to the claim (required-carried) with its consumer parked in the future,** and
  its deferral moves neither D1's rung (the location stands regardless) nor D2's trace (the
  states' home stands regardless) — the ordered pass kept every firewall: no decision borrowed
  another's conclusion; the six/nine was not needed by any of the four, so **no branch stopped**
  for it (the stop-condition reserves the stop for a branch that *needs* the choice).
- **No proposal touched a hard-stop:** no constitutional contradiction found for any of the four
  (all four are placement/rendering/data moves in the machinery's own territory); no branch
  *required* a six-vs-nine resolution; **no new constitutional authority is proposed** (the
  rung's *movement* stays inside the paper's one novel D-bucket; the *location* is older than
  every one of these documents) — so the governance stop never fires and the four open
  governance questions stay exactly as the audit left them, uncounted-as-blockers.

## 6. Implementation boundary

What these decisions now **authorize** — listed, not done:

- **Immediate** (D3A's scope; all inside existing contracts; lane-compatible):
  1. `packet_text` prints `provenance` when present, beside `work | level` (one rendering-line
     inside stage 4 — the presence/silence shape borrowed from K2's-law usage, **not** re-homed);
  2. the window's EVIDENCE row gains the field (the door already reads the shelf rows);
  3. one witness-extension of the `T47` pattern (a `packet_has` pin — the loop must READ the
     key it is given: the vacuity-law discipline; a kwarg that enters a witness must enter the
     print-loop's key-list too, or the witness rides vacuous).
- **Future, not now** (decisions placed, machinery waits): the rung-MOVE's call site
  (D1 settled *where* a rung sits; the paper's no-precedent bucket still governs *whether* and
  *by whom* it moves; `promotion.md:162` — *"grants… and, untested, may move a rung"*); the
  Bench's address (D2 left it open by ruling); the convergence-report station (P10, the
  counter-example's first real reader); the second AUDIT (post-repair — audit G12); the
  mode-switch (audit G8 — *"the mode never self-licenses"* is a comment's promise and still
  is).
- **Explicitly deferred** (owners named): the counter-example's operationalization (3B —
  consumer-gated); the chain-WALK, self-echo detection, card-26's welded corroboration-parse
  (date+count in one string); the Axis-A enum mapping; the FOUNDATION's provenance-composition
  REPORT at RETRIEVE (G9 — and its NAME is already taken by the door's shown-set lane, a
  §10 collision awaiting its "clarify"); the one sentence (App. B.4, on purpose); the Gate
  proper; the R0–R4 tiers; SANCTION/JUDGMENT/ACT classes.
- **Unresolved, preserved by order** (none is this pass's work): **six vs nine** (the law's own
  examples lean on both lists — recorded, not reconciled); **[Closure — founder ruling,
  2026-10-05: the relation is SETTLED AS DECLARED** — the law's six + the door are the ranks
  (CONSTITUTION XI); the data's nine are the working set (II.5/XII.1); never a merge, never a
  new enum (XII.1; XIV). What remains deferred in this entry is implementation **ownership
  only** — which list the future rung-held rule governs, and which list a future rung-table
  reads — both non-operative while the machinery is rung-blind (no code writes `level`; the
  rungs do not move). This is a record, not a reconciliation (XIII.0)**]; the four governance
  questions
  (Hand/Rotation; whose assent licenses a card's rung-move; the sealing ruling; first-person as
  a Foundation line); `K2`'s home (statement located — `golden-set.md` A–K batteries; the
  **specific citation** of "K2" remains not located in any artifact read this pass — UNKNOWN
  kept); `"n/a"` vs `"n-a"`; the "gate" word's future owner (IV's human room vs the machine's
  self_gate/relevance-gate — **the DANGEROUS row**; and the door's own line, *"the gate spoke;
  the mouth did not,"* which means the MACHINE's gate today); the window header's six-lanes vs
  eight-keys drift; the dead `mint` lane; the twin "plain" lanes (G6); the ANSWER-state's
  unwitnessed positive (G5); the edge targets (G7).

## 7. Final verdict

1. **Which proposed decisions survived?** **All four** —
   **DECISION 1: ACCEPTED** (rung = the claim's property on Axis B — Foundation `:171/:173/:626`,
   law `:176/:199`, paper `:38–44/:82–85/:136–139`, machinery agrees byte-wise);
   **DECISION 2: ACCEPTED** (the three run-states = the run trace's — `stages.py:585–663` already
   holds them; `window.py`'s header already makes the trace canonical; the shelf's 26 rows carry
   no state-field; a separate address would solve nothing demonstrated);
   **DECISION 3A: ACCEPTED — MINIMAL OPERATIONAL SCOPE** (print at SYNTHESIZE, mirror at the
   door's EVIDENCE row, one T47-pattern witness; walk/gate/map all deferred);
   **DECISION 3B: DEFERRED** (zero readers; convergence literal hard-coded; consumers named —
   convergence station, Boundary gate, TEST→RESULT's falsifier-meeting; the data-obligation to
   CARRY the field survives the operational deferral).

2. **Which failed?** None of the four proposals. Two *assumed* extensions died instead: 3A's
   scope was cut from "a provenance system" to a print-role (the gates stay future), and
   2's possible second address ("run-state address" as a NEW object) was declined — the trace
   already is the canonical address, and the proposal's own text forbids it becoming a store.

3. **What evidence changed the mind?** Four bytes, all named: (i) Foundation `:171` —
   *"the unit of storage is the CLAIM, with its level, its source chain…"* and `:173` (every
   rung-verb's patient is *a claim*) — Decision 1 was **latent in the Foundation already**; the
   decision ratifies, it does not invent; (ii) the window's header — *"One pure reading of the
   trace… (the trace's own protocol applies to the product)"* — Decision 2 likewise ratifies
   the door's own constitution; (iii) **card 10** — a `work` that reads like a primary and a
   `provenance` that says `ours-synthesis` — which converted the 3A print-role from decoration
   to **correction** (a fact no other field carries; the five `ours-*` rows size the need
   without inventing it); (iv) the **empty-string fixtures** (`tests.py:13,17,21,25`) — the lane
   already carries the counter-example's SHAPE with empty CONTENT, which is the deferral
   witnessed from inside the tests. And the one finding that touched no decision but must be
   said: the law's own examples name one word from **each** enumeration (`II.3 "INTERPRETIVE"`;
   `III "SPECULATIVE"`) — evidence that the six-vs-nine fork runs *past* the machinery into the
   law's illustrations, and that none of these four decisions may — per the founder's own order —
   presume to resolve it.

4. **The smallest next implementation step?** Exactly Decision 3A's scope: **one rendering-line**
   in `packet_text` (print `provenance` when present, beside `work | level`) **+ one field** on
   the window's EVIDENCE row **+ one `T47`-pattern witness** (its key admitted to the print-loop,
   vacuity-law clean) — a change that moves **no state, no gate, no rung, and no word of the
   law**, runnable atop the frozen lane and falsifiable in the lane itself. Everything else these
   decisions placed waits, by these decisions' own order, for the founder's implementation word.

**Repository/provenance note (reported, not touched, per the order):** the git tree still shows
`?? promotion.md` — untracked — together with `?? substrate-audit.md` and the repair footprint
(`opencode.json`, `stages.py`, `tests.py`, `window.py` modified). The word says the Promotion
Paper is committed; the tree has not been told. No git state was modified by this pass; the only
artifact created here is this one file.

**HARD STOPS, final tally:** constitutional contradictions found — **zero** (every branch
lands in machinery's own territory); six-vs-nine resolutions forced — **zero** (the discrepancy
was untouched and remains open on order); new constitutional authority demanded — **zero** (the
D-bucket's *movement* stays exactly as the paper committed it — this pass fixed only where
things sit and what a printer may print; **admission** and **rung-move** ride unchanged, both
un-promoted). **No decision stopped.** The founder's implementation word is the next and only
required next thing.
