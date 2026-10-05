# ASCENDED AI — SUBSTRATE AUDIT

*An audit, not a redesign. Nothing was fixed while performing it. Classifications carry their
evidence; where evidence runs out, the word is UNKNOWN. The governing order held throughout:
**Constitution → Foundation → machinery/data/tests**.*

## 0. Scope and governing rule

This audit maps what is IMPLEMENTED, TESTED, SPECIFIED, DEFERRED, or UNRESOLVED across the
substrate as it stands at Draft 4 rev a / RP-0.4 / KS-0.1 / VB-0.3, with the Promotion Paper
committed as design and not implementation. It does not add machinery, build web/research/
autonomy/agents, expand the shelf, or reconcile contradictions silently. Documented practice was
not promoted into law anywhere below — and one observation is recorded without reconciliation:
the founder's word says `promotion.md` is committed, and the git tree still shows it as
**untracked** (`?? promotion.md`; log shows one commit, `f5479ec baseline`). The repair footprint
(opencode.json, stages.py, tests.py, window.py modified; gpt-reviewer.md, reviewer/ untracked) is
likewise still uncommitted. Words and trees were both recorded; neither was touched.

## 1. Executive map

| Area | Current state | Evidence | Gap | Disposition |
|---|---|---|---|---|
| Cite-authority (no laundering) | **IMPLEMENTED** | stages.py:319–327 (`cites ⊆ shown ∧ in BY_ID`); T36a/b, T46, T49/T49b | none known | solid |
| UNKNOWN exit (two arms, one door) | **IMPLEMENTED + TESTED** | stages.py:595–629; window.py:48–53 names the arm; T23/T57/T63 | verbatim's "no yet / no count" data-only, not asserted | solid |
| Promotion-catch (render-level) | **IMPLEMENTED + TESTED** | stages.py:388–392 (RP-07, hard); T11/T12; T33 self-flags false-negative class | card-rungs never move (no site) | solid, narrow |
| NON-DECISION cannot answer | **IMPLEMENTED** (the one enforcement of law over a card's own field) | stages.py:239–242; T64 | real card 13 has never run (lane runs borrowed CUSTOM) | lane solid; data untested |
| Required caution reaches speech | **IMPLEMENTED + TESTED** | stages.py:453–457, 471–473, 513–519; T37/T38 | card-seeded caution (`caution_src`, :261) unasserted | solid, one lane unwitnessed |
| Self-gate + shelf precedence | **IMPLEMENTED + TESTED** | stages.py:558–573, 591–606; T50–T53 | the two-word-AND patterns are data; wet phrasings untested | solid |
| Bounded repair | **IMPLEMENTED**; bounded by closed op-set | stages.py:499–521 | second AUDIT (intended spine) uninstalled; block-lane overrides post-repair | solid with two recorded divergences |
| Relevance-state (2b) | **IMPLEMENTED + TESTED (dry)** | stages.py:182–243; T58–T61, T63 | wet semantics ride `sim` — CHOSEN, not judged (frozen) | solid dry; wet a probe |
| Answerability-states | **IMPLEMENTED**; 3 of 4 pinned (ANSWER not) | stages.py:266–274; T63/T65/T66 | ANSWER-state has no witness | fragile-by-omission |
| Five verbs (VII.1) | **PARTIAL by design** — 3 offered; IMPLY detected-never-emitted; DO = bug-flag | SYNTH_SYS contract (stages.py:296); RP-13/RP-12; T20 | none — deferral defended | by design |
| Stair machinery (WHERE-IS-THE-SEEKER) | **NOT YET ADDRESSED** | law Art. II; foundation pipeline 283; code has no station | the knowledge lane runs flat | intentionally deferred |
| R0–R4 proposal economy | **SPECIFIED ONLY** (law I.2; table = foundation XIII.2) | constitution 89–101; R0-exit = data-recorded (XIII.2) | no R3/R4 in force | intentionally deferred |
| Provenance (card-level) / attestation | **FIELD EXISTS, UNWIRED** | shelf.jsonl (every card); stages.py reads: claim/work/level/kind/edges/caution — never provenance | Axis-A vocabulary unmapped; ad-hoc data strings | G1 |
| Counter-example | **FIELD EXISTS, UNWIRED** | shelf.jsonl (every card + FIX); XIII.1 "schema field, not a virtue" | read by no stage, printed to no mouth | G2 |
| Report / Bench / Promotion | **DESIGN** (terms exist in promotion.md alone, save one) | grep: no noun Report/Bench in law/foundation; foundation 173 has *its own* "Promotion is gated" | integration into Foundation pending | proposed |
| TEST / RESULT / research loop | **NOT INSTALLED** | no stage; "test"/"result" appear only as health-data keys | — | confirmed |
| Golden-set (the law's own test-form) | **SPECIFIED; UNINSTALLED as machinery** | law preamble rule ("every commandment… a test… a wish, not a safeguard"); golden-set.md A–N | no runner in the spine; devices (held-out/surprise/mutation) unenforced | G11-family / deferred |
| Ladder: six vs nine | **UNRESOLVED — preserved** | stages.py:79–80 vs XIII.1 Axis-B; overlap measured = 3 names | see §12 | unresolved arch/data |
| The mouth (model) | **UNFALSIFIABLE IN-LANE** | tests.py:4 ("runs WITHOUT the funnel") | no frozen witness can be the law's dialog | structural, known |

**The audit's question, answered (which constitutional promises are enforced by *machinery*):**
six, exactly: the cite-boundary; the UNKNOWN door (an un-skippable return, both arms truthful at
the window); the render-level promotion-catch (demote-only — no code line can silently promote);
NON-DECISION cannot-answer (code over the card's own kind-field); the owed caution reaching the
speech (and surviving the plain-render); the shelf's precedence over the self-gate; and repair's
closed op-set (it *cannot* loop). Everything else in the law is, today: guard-observation (RP-04/08/
13 are *named* guard-observe), a deferred class (JUDGMENT/SANCTION never minted in the knowledge
lane), or a mouth's duty awaiting a mouth the lane cannot call.

## 2. Constitution → implementation

Classifications use the ordered set; each carries its exact support.

| Concept | Class | Support |
|---|---|---|
| **Floor (Art. I)** | PARTIALLY IMPLEMENTED | precedence is law (VI.6, :288) but no code site *uses* precedence; operational force arrives via RP-07/02/10 — machinery over rule-pack data; T11–T12 |
| **I.1 harmlessness / disclosed deferral** | PARTIAL — the disclosure half enforced (RP-02 append, T01/T08; window's caution line); the deferral-halves (may-not-treat/discourage/interpret) are Application doctrine awaiting the health-mode | constitution :67–78; rule_pack RP-02 |
| **I.2 proposal / named-human (R2)** | PARTIAL — RECOMMEND±human witnessed both ways (T05/T06; T25 unreachable-variant); RP-11's "*field from the card*" half is not installed — human detection reads FACTS only (stages.py:125–141) | constitution :91; rule_pack RP-03/11 |
| **I.3 grandiosity refusal; "decline to promote"** | PARTIAL, observe-by-name — status-word ⇒ **DEMOTE, never promote** (rule_pack RP-04 verbatim: "demotion is ordered, never promotion"); T18; VB-0.3 status-verbs-vs-nouns guard the mouth | constitution :103–116 |
| **I.4 indicators, not vibes** | IMPLEMENTED in the health-lane + TESTED dense (conjunction ≥2; sleep-alone no-crisis; T07–T09, T26–T28, T40a/b) | constitution :118–130 |
| **I.5 dependency** | PARTIAL, observe-by-name (exclusivity ⇒ "I.5 dependency WATCH — pattern, not sentence"; T19) | constitution :132–146 |
| **Stair (Art. II)** | SPECIFIED ONLY (governs Application; the installed knowledge-lane runs flat; II.2's early-mount = Access, which the shelf already is) | constitution :150–181 |
| **II.1 "fully" = four heads** | PARTIAL — trace holds the heads (grades/fires/obs/uncertainty/answerability; RP-06 "holdable in the trace, answerable on demand"); "answerable on demand" = a door's claim, witnessed at the window's lanes (T56/T57) | constitution :156–165 |
| **III Voice / register law / drift** | PARTIAL — validate's double-reading (T14/T15), RESTORE's marks, coverage-words; drift *observed* (wet narrow-mouth; simmed in lane); no silent status-upgrade (a) and hedge-drop (b) both have witnesses (T11/T12) | constitution :185–206 |
| **IV Community Gate** | SPECIFIED ONLY — a human institution ahead of its substrate; "guide never *pitches*" operationalized (RP-08 observe; T21/T35-family) and the golden word stands: the guide never *mentions* it | constitution :210–224; golden-set P15 |
| **V Obsolescence** | NOT YET ADDRESSED (measurable half only: K-stamp "counted, not sentenced," T22/T35; flourishing = the panel's, uninstalled) | constitution :228–237 |
| **VI.2 behavior-inference refusal; four sentences** | LAW'S OWN RESTRICTION; the four names never issued (no code path mints them) | constitution :247–254 |
| **VI.3 six-level line; held at UNKNOWN** | PARTIAL — held-rungs are the *law's* act; operationalized at data-scale by the self-gate's three lines (T50–T52) — and the self-gate covers only the zero-retrieval case | constitution :255–260 |
| **VI.4 taxonomy; demote-only economics** | the cheap tier is ALL the spine ever mints; JUDGMENT/SANCTION uninstalled; re-open (the law's only reversal-mechanism) uninstalled and future-patientless | constitution :261–280 |
| **VI.5 preservation ≠ endorsement; quarantined = constrained, never cleared** | NOT YET ADDRESSED — nearest shape to the paper's Attestation/assent-family; the law's patient here is SOURCES, not cards — recorded as adjacency, not identity | constitution :281–287 |
| **VI.6 precedence; capability-of-the-tool** | PRECEDENCE SPECIFIED (no site); the tool-clause operationalized as doctrine at VI.6 ("instruments, not seats" — the paper's §7.A) | constitution :288–296 |
| **VI.7 ACTUATION** | INTENTIONALLY DEFERRED — and its sentinel is installed: DO ⇒ RP-12 "a door, not a tenant" (T20) | constitution :297–310 |
| **VII.1 five verbs; compliance by what a response CAUSED, never by recital** | PARTIAL by design: 3 offered (SYNTH_SYS contract), IMPLY detected-never-emitted (RP-13 — the special verb), DO bug-flagged (RP-12); the pointer reads "V special verb" while law Art. V = *Obsolescence* and the verbs live at VII.1 — a pointer drift, recorded unreconciled | constitution :321–325; rule_pack RP-12/13 |
| **VII.2 no test-history deleted; held-out/surprise/mutation** | SPECIFIED ONLY (no runner; the devices are law's own, awaiting machinery) | constitution :326–333 |
| **VII.5 two seats** | NOT YET ADDRESSED as machinery; listed in the rule-pack's own *uncompiled* inventory — the house records its own deferrals in DATA | constitution :340–347; rule_pack line 73 |
| **Consciousness-status (VI.2/VI.3)** | PARTIAL — as above: the restriction general, the gate narrow, the wet mouth free to opine (architecture.md: "the mouth always had opinions about its own rank") | constitution :247–260 |
| **Provenance** | PARTIAL: node-lineage IMPLEMENTED (SOURCE/SYNTHESIS/UNSOURCED, rule-based, "no second provenance system"); card-field unwired (G1); chain-walk uninstalled; Axis A unmapped | stages.py:330–343; XIII.1 |
| **Authority movement** | NOT YET ADDRESSED at the card: drift *observed*; rung-move has no site to fire in (see §9) | III; II.2; §9 |

## 3. Foundation → spine

The founder's intended spine, stage by stage, against `stages.py`:

| Intended stage | In code? | Where | What it actually does | Foundation says | Material gap |
|---|---|---|---|---|---|
| USER | — (input, not a stage) | run_pipeline | question + facts **folded** into retrieval (:588–590) | UNDERSTAND ("the human question under the words") is a station | UNDERSTAND uninstalled — the fold is its machinery-shadow |
| INTENT | yes | :89–151 | frame; factors/indicators w/ metamorphic guards (neg/hist/neutralizer/reach); **mode pinned "knowledge"** (:149) | WHERE-IS-THE-SEEKER is the second missing station | no mode-switch exists — see §4/G8 |
| RETRIEVE | yes | :153–180 | symmetric tokenization; STOP as data; top-K=**4** (config); ties break NUMERICALLY (T45) | "RETRIEVE (with provenance-composition report)" | the composition-report half is uninstalled (G9) |
| *(2b GRADE — installed, not in the intended list)* | yes | :182–243 | the relevance STATE; four kinds; enforcement over the kind-field; notes | — (added by the relevance round) | the founder's list omits it; the code runs it — recorded, unreconciled |
| ANALYZE | yes | :254–278 | conjunction arithmetic + **answerability arithmetic** (contested only when an edge's TARGET is in the ANSWER set) | — | ANSWER-state has no witness |
| SYNTHESIZE | yes (mouth 1; bypassed dry) | :280–346 | cite-authority; weakest governs; LINEAGE rule; DO-flag | SYNTHESIS "(hypotheses stay hypotheses)" + mandatory counterexample pairing (P10/XIII.1) | lineage computed, value asserted by no witness; counterexample never paired (G2) |
| TYPE VALIDATION | yes, **as VALIDATE** | :348–364 | code watch-lists, "doubles only"; sets report_frame/rec_word; readings loosens/strict | red-team's validation stage w/ double-reading (architecture.md §1) | name overstates: it FLAGS, it does not TYPE-check |
| CHECK | yes | :366–441 | the rule-pack runs; edges OBSERVED (RP-13 trio); blocked = all-uncited (Disposition A) | — | none known |
| SPEAK | yes, as COMPOSE | :443–457 | deterministic; only cited nodes speak; RP-02 append ONCE | "UNCERTAINTY SPOKEN… tested for frequency" | spoken-uncertainty testing (frequency) is a golden-side instrument, uninstalled |
| AUDIT | yes | :459–497 | findings only; wet mouth-2 ONLY when the speech carries no hedge (narrow); adjudicates required content | — | **the `mint` variable is computed and never rides — RP-04's audit-side watch is dead code; the live lane is check's observation** |
| BOUNDED REPAIR | yes | :499–521 | two named ops; one pass; RESTORE from fields; plain-render re-renders nodes + survives required | terminating fallback / op-set / claim-inventory (architecture.md §1) | see §7 (two divergences) |
| AUDIT (second) | **NO** | — | repair's output is never re-audited | (intended spine) | G12 |
| RESPONSE | trace + lane | :644–663 | under block, plain_render REPLACES the response — **after repair ran** | — | repair's work can be overridden under block (T49's pin shows the replacement, not the repair) |

**Foundation concepts with NO installed machinery** (each a station the Foundation named; none is a
proposal of this audit): UNDERSTAND; WHERE-IS-THE-SEEKER; the provenance-composition report;
IDENTIFY TRADITIONS/CLAIMS (at level, from the claim-graph); COMPARE → RECURRING PATTERNS;
**BEST COUNTER-EXAMPLE (mandatory, P10)**; DIFFERENCES (load-bearing, not footer); EVIDENCE ASSESS
(falsifiability per claim); FACT/INTERPRETATION/SPECULATION separated; hypotheses-stay-hypotheses
(XIII.1's HYPOTHESIS as a stored status — no card on the shelf carries it); **SOURCES LINK-RESOLVE
or the answer does not ship (P8)**; UNCERTAINTY SPOKEN (tested for frequency); HUMAN-WORLD NEXT STEP
(P6); the conflict **ledger table** ("first-class, not an absence" — the shelf's edges exist; a
table has no file); the six drafted edge-types (printed, unshipped); the provenance-chain WALK;
first-person (the four sentences — the Foundation line the founder has not ruled); and the rule-pack's
own *uncompiled* list (IV-Gate proper; VI.4 floor-vs-arrangements; Rotation Question; App.B.4 the
one sentence; VII.5 two seats; naming; VI.7 application-tonight; K stamp watch; diction fix) — the
house's deferrals, recorded in DATA itself.

## 4. Data / claim model

The Foundation's schema (XIII.1, verbatim): a claim record carries
**`{text, provenance-class, claim-status, confidence, counter-example, falsifier, level-history}``**
— seven fields — "while storage stays multi-field." The shelf's rows carry ONE status field
(`level`) and the data's own words. Field by field:

| Field (Foundation's expectation) | Shelf reality | Code reader? | Test? | Verdict |
|---|---|---|---|---|
| claim / text | every card | RETRIEVE tokens; CHECK drift-proxy; packet; plain_render | dense | **FIELD EXISTS (wired)** |
| provenance (Axis A) | every card — words: `primary`, `ours-synthesis`, `ours-comparison; web-corroborated 2026-10-01 (…3/10 relevant, HIGH)`, `attributed` (F4) | **none** | none | **FIELD EXISTS, UNWIRED** — G1; Axis-A's five drafted names are NOT the data's names |
| epistemic level/rung | every card — six names only | the whole rank-machinery | dense | **FIELD EXISTS (wired)**; it is NOT claim-status-as-designed (see ladder, §12) |
| disagreement edges | many cards; three of the six drafted types in use (`CONTRADICTS`, `DOES-NOT-DECIDE`, `CONVERGES-WITH`); edges carry no target-existence check | CHECK (obs); ANALYZE (contested); window (shown-pairs only) | T17/T44/T66/T47 | **FIELD EXISTS (partial)**; dangling targets silently absent — G7 |
| counter-example (Axis D, "required") | every real card + FIX | **none** | none (carriage only; F-cards show the field rides) | **FIELD EXISTS, UNWIRED** — G2 |
| evidence status | PRESENT / NONE-FOR / n/a / n-a (spelling drift both ways in fixtures and shelf) | **none** | none | **FIELD EXISTS, UNWIRED** — and the door's lane named EVIDENCE is the shown-set (collision, §10) |
| citation locator (`locus`) | most cards | none | none | **FIELD EXISTS, UNWIRED** (the trace cites IDs, not loci) |
| source (`work/who/date`) | all / most / some | `work` IS read (packet; RESTORE's "(as X has it)"); who/date inert | T11 (RESTORE) | **FIELD EXISTS (work wired; who/date implied)** |
| kind | nine rows on the shelf (`NON-DECISION, DEFINITION, COMPARISON, TEACHING, PSYCHOLOGY, METHODOLOGY`); no declared enum anywhere in the artifacts read | GRADE demote; packet/window print (absent = silence — the machinery cites **"K2's law"**; **the statement of K2 was NOT located in any artifact read — UNKNOWN**) | T64; T47/T65 (silence half) | **FIELD EXISTS (partial)**; vocabulary = documented practice, no home |
| status (claim-status) | **no card field** — the axis the Foundation re-pointed storage to; the shelf substituted the six-name `level` | — | — | **FIELD ONLY IMPLIED (G4)** |
| silence / non-decision | the kind field + the enforcement | GRADE | T64 | **IMPLEMENTED (the one law-over-field enforcement)** |
| relevance | no card field — by design (a run-state) | GRADE → trace | T58–T66 | state, not field (design holds) |
| answerability | computed at the trace | ANALYZE | T63/T65/T66 (**not** ANSWER) | state, partially pinned |
| lineage | node-level label | SYNTHESIZE (word-gated; "the words are DATA") | value asserted by no witness | **IMPLEMENTED, UNASSERTED** (and: compare_words has `pulls against`; T66's "pull apart" ⇒ that node's lineage computes SOURCE — conservative direction, recorded) |
| confidence / falsifier / level-history (three of the seven) | **absent from every card** | — | — | **FIELD ABSENT (G4)** — three mandated fields not yet data, fields that exist read by no machinery |
| caution | some cards | ANALYZE (`caution_src`) | unasserted as a card path | **EXISTS, UNASSERTED (G11)** |
| facts/indicators (card-26's empty lists) | one row | none — and RP-11 promises the named-human "from the card" while code reads FACTS | T40a (the permissive half, facts-side) | **FIELD EXISTS, UNWIRED (G8/G9 adjacency)** |

**Talks-as-if list (paper/Foundation speaking of fields the machinery does not read):** Attestation
stands on an unread field (G1); the Boundary gate stands on an unread field (G2); "storage stays
multi-field" describes a schema the shelf has not grown (G4); the provenance-composition report is
cited at the RETRIEVE station and lives nowhere (G9); the conflict ledger is "first-class, not an
absence" as a PLAN — today the ledger's only installed kin are card-edges and observations.

## 5. Run-state model

1. **Visibility** is decided at RETRIEVE (the IDs list; ties numeric; TOP-K = 4) — or replaced by
   the packet arg — and re-decided *narrower* twice for the mouth: the shown set for
   synthesis is `part ∩ first-5` (packet_text's cap; the grade-prompt shares it) and the
   blocked-lane speaks `first-3` (plain_render). With TOP-K = 4 the five-cap cannot bite yet —
   recorded as a latent divergence, not a bug.
2. **Relevance** is decided at GRADE (2b) — wet classifier, `sim` in-lane — *enforced by code over
   data the shelf owns* (the NON-DECISION demote; invalid words frame; misses recorded; total
   silence falls back to the OLD meaning, noted — "the machinery never ends weaker than it was
   found"), and NOT_RELEVANT is filtered (`part`) BEFORE the answerability arithmetic.
3. **Answerability** is decided at ANALYZE — arithmetic over grades and over edges whose targets
   are in the ANSWER set — four states (NOTHING / RELATED-ONLY / CONTESTED / ANSWER).
4. **Distinct operations — yes:** three stages, three mechanisms (set-algebra / wet classification +
   data-enforcement / arithmetic). Nothing is computed twice by the same method.
5. **Collapses:** (i) the dry lane's all-ANSWER default deliberately collapses relevance onto
   visibility ("the frozen fixtures' shown-sets are **CHOSEN, not judged**" — the comment's own
   words; T58–T66 exist precisely to un-collapse); (ii) the window presents `grades +
   answerability + notes` under the ONE key `relevance` (lines 54–58) and its header still says
   "six lanes" where it returns eight keys — a presentation-collapse, recorded not fixed;
   (iii) nothing collapses in code itself.
6. **Enough for the mouth?** For the SURVIVORS, yes: it receives claim/level/kind-when-present/
   edges/grades, plus COVERAGE counts (answers=, related=), plus SYNTH_SYS's permission and its
   three coverage phrasings ("the shelf is thin here; what stands is related, not an answer;
   **the records contend**" — note the third: CONTESTED reaches the mouth's toolkit as a coverage
   phrase). What the mouth cannot see: the rejected records (already filtered), and the card's
   provenance/counter-example (unwired fields) — so scope-words ride as OURS, and the rejects
   exist only in the trace.

## 6. Retrieval / relevance

The historical problems, each classified against what the CURRENT code and tests actually contain.
No old issue re-litigated unless the implementation still carries it.

| Historical problem | Class | What is actually there |
|---|---|---|
| lexical overlap inflating the set | **PARTIALLY FIXED — by doctrine, not machine** | the generator "stands EXACTLY as it was (its lexical noise is its nature, not its fault)" — the fix is the SEPARATE state (2b), not a narrower retrieval; wet defence untested (sim) |
| stop-list repairs (`about`, `can`, `answer`, `who`; battery's "two"/"its") | **FIXED (as data)** | RP-0.4 `stop_words` (rule_pack:9–14; "the debt is paid" — stages.py:154–158); boundaries witnessed T39a/T39b; the real-shelf effect of the members themselves = a wet probe |
| Newton entering through lexical collision ("a stranger bought in") | **FIXED AS DATA; NOT YET TESTED in-lane** | cards 21/22/25 were carded — their own notes record the prior accidents ("Now Opticks can take its own question"); the lane never runs the real shelf |
| prior-answer contamination ("prior claims of experience") | **FIXED** | the metamorphic guards (neg/hist/neutralizer/reach, stages.py:86–141) as DATA+code; the pair T30a/T30b is the witness ("the REAL behavior") |
| anatta / no-self coverage gap | **LANE FIXED; COVERAGE OPEN (DATA)** | the set-aside cannot-answer is installed and witnessed (T64; its own name: "the no-self lane's law"); the missing premise-card remains the Hand's DATA act, not machinery's; law knows the risk-class ("Doctrinal dose — premature no-self…" App. A) |
| "four sources speak here" machinery leaking into voice | **FIXED** | T62's offline witness kills the command ("the count-command is dead"); SYNTH_SYS grants counts as permission ("how many is yours to know, never a sentence you owe") |
| answer-count vs record-count | **PARTIALLY FIXED** | the distinction lives as the four answerability STATES (state, not count; IV/V re-aimed); the counts (COVERAGE answers=/related=) are telemetry for the mouth; a count may not buy a state — dry-untestable by nature |
| the relevance gate | **FIXED (dry) — the six-witness family T58–T63**; wet semantics CHOSEN not judged (the lane's law; "a wet run is a probe, not a witness") | stages.py:182–243 |
| NON-DECISION handling | **FIXED — and it is the only place machinery ENFORCES a law-shaped fact over a card's own field** (demote + note, :239–242); the real card 13 has never run (T64 rides a borrowed CUSTOM shelf) | T64 |
| UNKNOWN after relevance-rejection | **FIXED** — the empty set's SIBLING arm at the SAME door with the SAME words ("no lane is added; the door's MEANING widened") | T63; stages.py:616–629 |

## 7. Audit / bounded repair

**What AUDIT can detect:** deterministically, what CHECK already found for it (RP-07 promotion,
RP-07 hedge-drop); from the mouth (wet, and only when the speech carries NO hedge — the
`narrow_mouth` budget-guard), promotion / extra_claim / minting findings; plus its one own
adjudication — an extra_claim whose span IS the required content is RE-classed
`AUDIT:required-content(RP-02)`. **What it can MODIFY:** nothing — findings only (stages.py:459–497).
**One dead lane:** the status-word minting watch (`mint`, :470) is computed and never rides — the
live RP-04 path is CHECK's observation, as its own class demands (guard-observe).

**Repair's authorization, operation by operation:** `RESTORE-from-field` appends "(as X has it)"
marks — words drawn from the cited card's OWN `work` field, applied only to nodes at or below
INTERPRETIVE rank (the ladder's conservative direction: it may restore a hedge, never mint a rank).
`plain-render` discards the speech and re-renders the RECORDED nodes, and the required content
survives "because it rode in with the rule's authority, not the model's license" (T37/T38 pin both
halves). Therefore: **new reasoning? No** — all text is already recorded (fields, nodes, rule-data).
**New source? No** — no cite is added anywhere in the op-set. **Epistemic status change? No** — no
card's rung is touched; the render's REGISTER moves. **Alters the user's answer? Yes** (the text),
**but** under block the response is replaced by plain_render AFTER repair ran (T49's pin shows the
replacement) — repair's work can be overridden. **Genuinely bounded? Yes** — a closed op-set of two
named ops, one pass, deterministic, terminating; the narrow-mouth gate caps the wet budget.

**The key question, answered:** BOUNDED REPAIR is genuinely repair, not a second synthesis — with
two recorded divergences, neither fixed: (1) its plain-render speaks ALL nodes, **including the
uncited** — while Disposition A and T49b make the uncited node recorded-as-thinking, not speech:
two "plain" lanes (blocked→records-first-3 vs extra-claim→nodes-all) share a name and differ in
material, and no witness pins the mixed case; (2) the intended spine's SECOND AUDIT (post-repair)
has no install site (G12). Neither divergence lets reasoning in; both are name-and-lane drifts.

## 8. Report / Bench / Promotion / TEST / RESULT

Against `promotion.md` as design, and only against code as fact:

- **REPORT.** Today: the PACKET LANE (a real lane — T46–T49b: a given shown-set replaces retrieval's
  FINDING; boundary/guards/door ride) + the cite-drop note + the LINEAGE label (SOURCE/SYNTHESIS/
  UNSOURCED — "the mouth's thinking; no seat in the speech"). Merely conceptual: the Report as a
  DATA TYPE — there is none; an off-shelf shown card cannot be cited (T24a/T46's boundary), so a
  Report's only entry point today is **`set_shelf` — the founder's hand** (the lane's own
  precedent; T64's CUSTOM shelf is that act). The mouth never sees rejected records; it never sees
  provenance/counterexample (fields unwired). Verdict: **lane exists; type does not.**
- **BENCH.** Today: the trace and the window's lanes — bytes that die with the run. No inquiry
  state spans turns; no store; the word appears NOWHERE in constitution/foundation (it is the
  paper's own notation — its class-C item, honestly). Its location (store vs trace) is an
  UNDECIDED design item, not a gap by this audit's license. Verdict: **proposed architecture only.**
- **PROMOTION.** Today: no operation; the only promotion-SHAPE is `set_shelf` — a PLACEMENT by the
  founder's lane-only call, not a passage; `set_shelf` is not called anywhere in code (grep:
  definition + tests' calls only). No Hand/grant mechanism exists (no assent object, no grant site);
  a rung-change is NOT executable (no code line writes a card's `level` — the rung is inert to
  machinery; T64's demotion moved a GRADE, not a rung). The three gates (attestation / status /
  boundary) have no sites — their fields (provenance / counterexample) are the unwired two (G1/G2).
  Verdict: **design; the passage is rehearsed, not installed.**
- **TEST / RESULT.** Confirmed **not installed**: the spine has no TEST stage and files no RESULT;
  the words "test"/"result" live as health-mode data keys and as the harness's own name. The
  research-loop, hypothesis handling (HYPOTHESIS is an Axis-B member no card carries),
  provenance-chain walking, first-person, open knowledge, and future actuation all sit in the
  NO-MACHINERY list of §3. (And the FOUNDATION's "Promotion" — II.2, "promotion is gated; demotion
  is instant… retagged UP only by human review + the golden dialogue; the system may demote freely,
  in view" — already REGULATES the move the paper left precedentless: recorded as adjacency, not
  identity.)

## 9. Governance / authority movement

Every operation that can change a content's standing, classified (states of a run carry no
authority — the paper's ruling, upheld here; governance enters only at the named gates):

| Operation | Class | Where it lives / rests |
|---|---|---|
| become visible | no authority consumed (state of the run) | RETRIEVE (or the packet); rung-BLIND — the rank field rides in but is not read at the door |
| become relevant | no authority consumed; an instrument's act (VI.6) | GRADE; enforcement = data-over-data (the kind-field) |
| become answerable | no authority consumed (a computation's state of the SHELF for the question) | ANALYZE |
| enter the shelf (admission) | **DOCUMENTED PRACTICE — NOT established law** | KS-0.1 carding ("the founder's word"); shelf header "C1–C5 aimed … the loci are the builder's own hand"; law: no admit/membership/curat token exists (grep empty) |
| receive a rung | **DOCUMENTED PRACTICE** | granted at carding; the law's only rung-adjacent force is IV (keeper ranking a SEEKER) and the Foundation's II.2 (re-tag rules) |
| **move a rung** | **PROPOSED FUTURE MECHANISM** with **UNRESOLVED GOVERNANCE QUESTION** | no site in code; law-silent (the paper's ruling, unchanged); Foundation ALREADY has the rule (up = human review + golden dialogue; demote free, in view); law's nearest kin: I.3 "may decline to PROMOTE… only the rank," VI.4's re-open (the only reversal-shape, and it is the SEEKER'S), VI.5's named+revocable endorsement (SOURCES as patient) |
| change status (render-level) | machinery, direction-locked to demote | RP-04 "demotion is ordered, never promotion"; GRADE's demote; no code path can promote |
| become authoritative (promotion proper) | **PROPOSED — the D-bucket itself** | the assent-SHAPE has precedent (VI.4); the patient (a card) is the novel case; the sealing fork awaits the founder's ruling |
| be acted upon (SANCTION; ACT) | **INTENTIONALLY DEFERRED** | VI.7 — "a permission in law is a door, not a tenant"; the sentinel is installed (RP-12/RP-13's "detected, never emitted") |

**Unresolved governance questions (4, named; none solved here):** (1) the **Hand's identity and
selection** — the Rotation Question, law App. B.3 verbatim (who selects keepers, for what term,
removable how — and whether the Gate can EVER be economically coercive), with today's practice
one human in four hats; (2) **whose assent licenses a card's rung-move** (the law's assent-patients
are persons/seekers/arrangements; the seeker's re-open does not fit a card); (3) the **sealing
question** — whether VI.4's five classes are sealed to the seeker's log and cannot take the corpus
as patient (the paper's fork; a RULING, not a bug); (4) **first-person as a Foundation line** — the
four sentences stand at law; the Foundation line is the founder's undecided word (App. B.4's "one
sentence" is its own, on-purpose open item — a deferral, not counted here).

## 10. Vocabulary collisions

Format as ordered. "Clarify" = the collision is real and the fix is words, later; nothing renamed now.

| Term | Layer A meaning | Layer B meaning | Risk | Action |
|---|---|---|---|---|
| membership | community doctrine: the room's ONLY COERCIVE POWER, re-earnable ("lose the room, never the project") | paper §2: shelf-admission of a card | **DANGEROUS** | clarify (the paper already flags "a different head's hat") |
| admission | foundation: ADMITTED ABSENCE ("an absent shelf ADMITTED is honorable") | paper: the act of entry | AMBIGUOUS | clarify |
| assent | law VI.4: the SEEKER's, opens jurisdiction, moves no Floor, one re-open | Stoic DATA (card 12: "the story the assent lets in"); paper: the Hand's (new patient) | AMBIGUOUS | clarify later |
| rung | FOUNDATION: the Nine-Rung Ladder survives as the RENDERING only | spine: the six-name `level` (rank-machinery); LAW says *rank* (IV) and *level*, never "rung" | **DANGEROUS** (it IS the ladder discrepancy) | none — defer (preserve §12) |
| standing | VI.4: the SEEKER's ("at no cost to standing"); Spirit-standing (conflicts list) | paper §2: admission+rung for a card | AMBIGUOUS | clarify |
| shelf | foundation doctrine (a view, not the ground; the honor-clause) | the frozen data (26) | AMBIGUOUS | none |
| report | validate's `report_frame_words` / node `report_frame` flag (a RENDERING frame); foundation's VERB uses ("report those states") | the paper's Report lane (noun) | **DANGEROUS** | clarify |
| evidence | the card's `evidence` field (PRESENT/NONE-FOR/n-a) | the door's EVIDENCE lane = the shown-set | **DANGEROUS** | clarify |
| bench | (no competing use found in law/foundation) | the paper's workspace | SAFE (so far) | none |
| claim | VII.1's verb (a compliance tier); the claim-WORD generator (the retrieval tokens); claim-STATUS (Axis B) | the claim-record object | **DANGEROUS** (four senses, one a verb) | clarify |
| record | VI.4's RECORD class — its patient is the SEEKER ("recorded against") | claim-record; shelf rows ("records"); the trace ("noted/recorded") | **DANGEROUS** (the paper's own "RECORD-shaped" extends it) | clarify |
| status | I.3's status-reading about the PERSON (the forbidden move); `status_words` (the grandiosity trip-wires) | claim-status (Axis B); the paper's "claimed status" | **DANGEROUS** | clarify |
| authority | III's drift-of-authority; I.2's authority-CLAIMED; IV ("its only authority: its members were slower") | the paper's authority-MODEL | AMBIGUOUS | none (context-held) |
| hand | shelf header "the builder's own hand"; idiom "the Hand's" (paper) | colloquial "in modern hands" (card 16) | AMBIGUOUS | defer (paper-habit already rules: name the hat) |
| **gate** (found) | Art. IV: a FUTURE HUMAN INSTITUTION (keepers, roster, friction-not-exam; P15: the guide never mentions it) | `self_gate` + the 2b relevance-gate + the window's "the gate spoke; the mouth did not" (the MACHINE's gate) | **DANGEROUS** (same word, machine-part vs future human room; VB-0.3's charter bars the mouth from it) | clarify later |
| **grade / GRADE** (found) | IV forbids scoring the Gate's behaviors into rank | the 2b four GRADES — four KINDS, not degrees | AMBIGUOUS (the word invites the very reading IV bars) | clarify |
| **frame** (found) | the intent's OBJECT (the frame) | `report_frame` (a word-flag); CONTEXT's own definition ("materially FRAMES, without settling") | AMBIGUOUS | defer |
| **DO / ACT / ACTUATION** (found) | the fifth verb (VII.1); the speech-ladder's rung "actuated" (I.2) | RP-12: an emitted DO is a BUG-FLAG ("door, not a tenant") | SAFE by design (the flag pins the distinction) | none |
| **promotion** (found) | FOUNDATION II.2: a claim's re-tag-up, GATED (human review + golden dialogue) | the paper's PROMOTION: the Bench→Shelf passage | **DANGEROUS** (one word, two operations) | clarify |
| **level** (found) | the six names (`level` = the rung's data) | `level-history` (the absent 7th field); "at level" (II.3's sequence phrasing) | AMBIGUOUS | clarify |
| **mode** (found) | the intent's pinned "knowledge" (the comment's promise: "the mode never self-licenses") | no switch exists anywhere | AMBIGUOUS | defer (with G8) |
| **audit** (found) | stage 8 (findings); the bias audit (IV.3, corpus-side); the voice audit (foundation I.3 area) | the law's own audit QUESTIONS (VII's, VI.7's) | AMBIGUOUS | defer |
| **lane** (found) | the trace's six/eight lanes; the packet lane; the plain lane; the SELF lane; the door's MEANING widened to a sibling ARM — "lane/arm/road" already three words for exit-shapes | — | AMBIGUOUS | defer |

## 11. Test coverage

**Strong (pinned both directions):** the cite-boundary (the largest family — T36a/b, T46/T46b,
T48/T49/T49b, T24a/b, T34); the UNKNOWN door's two arms + early-return (T23, T57, T63); the
self-gate with the shelf's precedence (T50–T53); the named-human tier (T05/T06, plus T25's
unreachable variant); conjunction & triage (T01–T03, T07–T09, T26–T28, T40a/b); the relevance-state
family (T58–T66); repair (T11/T12 RESTORE; T37/T38 plain-render + adjudication; T41 the shown-not-the-
head); edge-observation (T17 non-decision, T44 convergence-as-ours, T66 contested, T47 the mouth
RECEIVES level/edges).

**Tested only indirectly (by name: guard-observe):** status words (T18 — an observation, the demote
is a READING); pitch (T21 — a *candidate*, not a strip); dependency (T19 — "pattern, not sentence");
stamp (T22/T35 — "counted, not sentenced," telemetry named as such); grandiosity (T33 — a witness
that asserts an ABSENCE).

**Weak/fragile:** T33 (an absence-witness: a hedged promotion rides free — the lane's own name
says "suspect machinery, not law"); T62 (an OFFLINE string-witness over the prompt — behavior
could drift elsewhere while it passes); T64 (the real card 13 has never run — the lane borrows a
CUSTOM two-card shelf, the file's own `set_shelf` precedent); the unknown-lane pins assert a
SUBSTRING ("don't know") while the verbatim's own doctrine ("that is an answer, not a failure";
the "yet" that sits there belongs to the SHELF's reach, not to a "not yet") rides as data asserted
by no witness.

**No tests:** the ANSWER-state (the positive case of the four is unpinned); the LINEAGE field's
VALUES (set, carried to the window, asserted nowhere); the card-seeded caution lane (`caution_src`
implemented, never exercised through a shown card); the real shelf's own retrieval (T31/T32 pin the
MECHANISM on the hermetic fixture; the real-shelf pair rides recorded in prototype.md, not frozen);
authority movement (nothing can fire); evictions beyond the required-content survival.

**Two structural facts, recorded without fix:** (i) **all seventy witnesses witness MACHINERY, not
law** — by construction: the lane "runs WITHOUT the funnel," and the law's own rule demands "a
dialogue in the golden set that a MISALIGNED MODEL would fail… a commandment without a test is a
wish, not a safeguard" — the frozen lane cannot in principle be the law's test, and the golden set
(A–N: blind batches, the held-out slice complete, the frozen table, the 37×3 sweep, the five
verdicts) has no runner in the spine; (ii) **the vacuity law** — a kwarg the print-loop does not
read rides vacuous (bitten three times, now written in the file's own comment) — the harness can
hold a witness that asserts nothing, so any new expectation MUST enter through a key the loop reads.

## 12. Ladder discrepancy

Preserved exactly, unreconciled: **spine six vs Axis-B nine.**
- The SIX: `stages.py:79–80` (LEVEL_RANK; DOCUMENTED entered as a KS-0.1 ENUM MEMBER — "the
  taxonomy's content belongs to the foundation"); load-bearing throughout (rank lookups
  `get(name,−1)`); every fixture and every shelf row speaks it; the promotion-catch keys off three
  of its members {INTERPRETIVE, INFERENTIAL, UNKNOWN}; the window's DISTINCTION lane counts it.
- The NINE: `foundation` XIII.1 verbatim (FACTUAL · HISTORICAL · EMPIRICAL · PHILOSOPHICAL ·
  EXPERIENTIAL · SYMBOLIC · HYPOTHESIS · SPECULATIVE · UNKNOWN) + "The old **Nine-Rung Ladder**
  survives as the **RENDERING** … while storage stays multi-field."
- The OVERLAP, measured: **three names** {EMPIRICAL, PHILOSOPHICAL, UNKNOWN}; spine-unique {DOCUMENTED,
  INTERPRETIVE, INFERENTIAL}; Axis-B-unique {FACTUAL, HISTORICAL, EXPERIENTIAL, SYMBOLIC, HYPOTHESIS,
  SPECULATIVE}.
- Machinery depends on the six (strictly); on the nine (not at all). Tests depend on the six (no
  witness names a nine-only word). The LAW speaks a nine-word — its own voice-law example is a
  `SPECULATIVE` claim "sung as scripture" (III) — a word the installed machinery could never see
  (a card carrying it would compute at rank −1 and print to the mouth as itself).
- Behaviorally significant TODAY? No — every installed card speaks the six. Live drift-risk: yes —
  every carding day compounds the fork. **Class: unresolved architectural/data issue. Reconciled
  by nothing here.**

## 13. Deferred by design

Ten items, all cited, none mourned:
1. **ACTUATION** — VI.7: an office, not a present authority; "a permission in law is a door, not a
   tenant"; its SENTINEL is installed (RP-12/RP-13).
2. **JUDGMENT / SANCTION** — the expensive classes are never minted in the knowledge lane (the
   arrangement "e.g., the Gate's" is future).
3. **The Community Gate proper** — the rule-pack's own uncompiled list names it ("IV-Gate proper");
   an institution ahead of its substrate.
4. **The Rotation Question** — App. B.3, open ON PURPOSE (who selects keepers; term; removability;
   whether the Gate can ever be economically coercive).
5. **The Stair's stations + APPLICATION dosing** — WHERE-IS-THE-SEEKER uninstalled; the knowledge
   lane runs flat (Access, not dose).
6. **R0–R4 proposal economy** — I.2's graduated ban; the R0-exit (receive-without-human, recorded as
   data ABOUT THE SYSTEM) is the only tier with a lane at all.
7. **The voice's register spectrum** — the plain/ornate minimum at law; the five registers are
   machinery (XIV.7); VB-0.3 runs diction and the size-cap ("a drift-CONTROL measure, not a
   prevention").
8. **Golden-set's three devices** — held-out set, human-authored surprise tests,
   mutation/revalidation (VII.2: "Three devices, no bureau") — no enforcement installed.
9. **App. B.4 — the one sentence** — "Still open, on purpose" (site candidate: "You were already
   looking," which the machinery already stamps as telemetry).
10. **This phase's own order** — no web, no research lane, no agents, no autonomy, no shelf
    expansion, no new architecture: the audit's own boundary.

## 14. Genuine gaps

Things the substrate NEEDS but nobody has yet designed/decided (distinct from the deferrals above,
which were decided):
- **G1 — attestation has no site.** Every card carries provenance; no stage reads it; the shelf's
  words (`primary`, `ours-synthesis`, `ours-comparison; web-corroborated 2026-10-01 (…3/10
  relevant, HIGH)` — corroboration, DATE, and a COUNT welded into one STRING) are no one's enum.
- **G2 — counterexample has no site.** The Foundation's REQUIRED schema field, on every card, read
  by zero code; the paper's Boundary gate stands on it.
- **G3 — the conflict LEDGER has no home.** "First-class, not an absence" was planned as a TABLE;
  installed today: card-edges + observations. No file, no table.
- **G4 — claim-status STORAGE is undesigned.** Seven mandated fields vs one installed field; the
  enum-overlap is three; DOCUMENTED is a provenance-SHAPED word inside a STATUS ladder.
- **G5 — ANSWER, the positive state, has no witness.**
- **G6 — the repair lane can speak the uncited node** where compose's law bars it; the two "plain"
  lanes share a name, differ in material, and the mixed case rides unwitnessed.
- **G7 — edge targets are not existence-checked.** A dangling edge silently vanishes from the
  DISAGREEMENT lane (the window prints edges only when `to` is in the shown set).
- **G8 — the mode never switches.** "knowledge" is PINNED at :149; "the mode never self-licenses"
  is a comment's promise; the health-lane's arithmetic rides every knowledge run; card-26's empty
  `facts`/`indicators` lists are an inert hook; RP-11 promises the named-human "from the card" and
  the code reads FACTS.
- **G9 — the FOUNDATION's provenance-composition report** (the RETRIEVE station) is uninstalled —
  and its NAME is already taken by the door's shown-set lane.
- **G10 — reproducibility is partial.** versions/model/build stamp the trace; the wet arm is never
  frozen ("a wet run is a probe, not a witness" is a DOCTRINE, not a mechanism); no independent-testing
  runner exists (XIII.0's red-team amendment demands one: the self-model must have predictive pull).
- **G11 — implemented-but-unasserted lanes:** the card-seeded caution (`caution_src`); the lineage
  values; the ANSWER-state (again — it earns its own entry by being the positive case of a
  FOUNDER-named set).
- **G12 — the intended spine's SECOND AUDIT** (post-repair) has no install site; and under BLOCK,
  the response-replacement runs after repair — repair's work can be overridden.

*Observed, not gaps (recorded without reconciliation):* the tree shows `?? promotion.md` while the
word says committed; the machinery cites **"K2's law"** (absent kind = silence) whose statement was
NOT located in any artifact read — **UNKNOWN**; the audit's `mint` watch is a dead lane; the window's
header says "six lanes" while it returns eight keys; RP-13's pointer reads "V special verb" while
law Art. V is *Obsolescence* and the verbs live at VII.1; `evidence` spells both "n/a" and "n-a."

## 15. Audit verdict

1. **What is solid?** The law's cheap-tier spine. The cite-boundary; the UNKNOWN door with its two
   truthful arms; the demote-only promotion-catch; NON-DECISION cannot-answer; the owed caution
   that reaches and survives; the shelf's precedence over the self-gate; and a repair that is
   bounded because its op-set is CLOSED. These are enforced by CODE over DATA — not by the mouth,
   not by observation — and they are witnessed in the frozen lane. The machine keeps the Floor's
   economics exactly as the law drew them: nothing in a run can cost an assent, because nothing in
   a run may MOVE a rung.
2. **What is implemented but fragile?** The relevance-state (its wet semantics are CHOSEN, not
   judged, in every witness that claims to pin it); the answerability set (three of four pinned);
   the two plain-lanes; the observation-class guards (status/pitch/dependency/grandiosity — all
   observe-by-name, and the T33 class shows a hedged promotion can ride through); the harness
   itself (vacuity law — a witness can assert nothing and pass).
3. **What is designed but not implemented?** The entire research substrate: the Report as a type,
   the Bench as a state across turns, Promotion as an operation (the only shape today is the
   founder's hand at `set_shelf`), TEST/RESULT, the chain-walk, the ledger-table, the
   composition-report, the FOUNDATION's own twelve-station pipeline (the spine runs nine stations
   and omits GRADE from the intended list while the code runs it — recorded, unreconciled), and
   the golden-set's devices.
4. **What is genuinely missing?** An ADDRESS for state (a grade dies with the run by design, so the
   Bench has nowhere to live until the trace is ruled a store or a home is designed); a SITE for
   the rung-move (the law is silent, the Foundation's rule is printed, the code has no call point);
   an ENUM home for the kind-vocabulary; a MAPPING from Axis A to the data's own words; and a RUNNER
   for the law's own test-form — today the house proves its law's behavior on a lane that cannot
   speak, while the mouths it fears are governed by a set it does not run.

## 16. Recommended next decision

Three decisions — architectural, not features. Governance is NOT on this list: the four open
questions (§9) stand on purpose and need no decision to keep the audit true.

1. **Where rungs live, and on which axis.** Six in machinery, nine in the schema, one field in the
   shelf, seven in the design — rule the storage question (enum home, mapping, the DOCUMENTED-word
   question) BEFORE any new carding, kind, or edge-work, or every carding day compounds the fork.
2. **Where a run-state may live.** The paper's durations (Shelf outlives inquiries; Bench outlives
   turns and dies at its inquiry; Report outlives not even a turn) are unimplementable while every
   state dies with the run; decide whether the trace is a store or a new address is designed —
   this gates the Bench phase itself.
3. **Whether counter-example and provenance get wired next, or are filed deferred.** The paper's
   first and third gates (attestation, boundary) stand on two fields the machinery reads nowhere;
   the Foundation already called the first REQUIRED (a schema field, not a virtue). Wiring either
   is a commandment and the law already demands its golden dialogue before it ships — so the
   decision is which, when, or explicitly: not-yet.

---
*Colophon. Files inspected: constitution.md (whole, 385 ll.); foundation.md (targeted: I.3/P10/P14/P15
region, II.1–II.2, III.1, IV.3, the pipeline block ~278–296, IX, XIII.0–XIII.2, the conflicts list,
XIV; plus greps); stages.py (whole); tests.py (whole); window.py (whole); shelf.jsonl (whole);
rule_pack.json (whole); config.json (whole); promotion.md (whole); voice_brief.md (whole);
golden-set.md (structure, 385-line scan of A–N); spine.md (head). Tests inspected: 70 frozen
witnesses + the loop's kwarg-contract + the vacuity law. Areas audited: twelve (I–XII). Genuine
gaps: twelve (G1–G12). Intentional deferrals: ten. Unresolved governance questions: four.*
