# River Valley Vikings Defensive Playbook — Multi-Perspective Audit

**Date:** 2026-02-25
**Scope:** Full playbook analysis from four perspectives: Defensive Coordinator (contradictions), Offensive Coordinator (vulnerabilities), Head Coach (completeness/implementation), Position Coach (key recognition/reaction clarity)

---

## TABLE OF CONTENTS

1. [Executive Summary](#1-executive-summary)
2. [DC Perspective: Contradictions & Internal Consistency](#2-dc-perspective-contradictions--internal-consistency)
3. [OC Perspective: Exploitable Vulnerabilities](#3-oc-perspective-exploitable-vulnerabilities)
4. [Head Coach Perspective: Volume, Implementation & Program Gaps](#4-head-coach-perspective-volume-implementation--program-gaps)
5. [Position Coach Perspective: Key Recognition & Reaction Clarity](#5-position-coach-perspective-key-recognition--reaction-clarity)
6. [Consolidated Action Items](#6-consolidated-action-items)

---

## 1. EXECUTIVE SUMMARY

The playbook is schematically excellent — modern, well-structured, internally consistent in most areas, and backed by thorough pressure cards, legality matrices, and situational menus. The football is sound.

The audit identified **6 critical contradictions**, **10 major teaching-confusion risks**, **10 minor cleanup items**, **5 structural offensive vulnerabilities**, and **significant implementation concerns** around volume, cognitive load, and the Bandit (B) position.

**Top 5 findings (must-address before camp):**

1. **SHADE + SLANT is used as the first example call in the playbook — but it's illegal per the legality matrix.** (Section 2, C1)
2. **The Bandit (B) has 12+ distinct roles with no unified read key.** He needs a position-specific wristband/helmet card. (Section 5)
3. **The 10-day camp install targets 26+ concepts — roughly 2x what an elite HS program can absorb.** Reduce Day 10 checkpoint to ~15 concepts. (Section 4)
4. **CRASH + Zorro creates a QB/RB assignment conflict for B.** Who has the QB vs. the RB needs explicit resolution. (Section 2, C2)
5. **Signals are undefined for ~50 of 56 concepts, yet the playbook says "no wristbands."** Adopt the wristband system (numbers 01-76 already designed). (Section 4)

---

## 2. DC PERSPECTIVE: CONTRADICTIONS & INTERNAL CONSISTENCY

### CRITICAL (Game-Day Bust Risk)

#### C1. SHADE + SLANT Used as Example Call — But It's Illegal

**Location:** CLAUDE.md and Playbook.md Section 16 (Call Grammar Examples)

The first example call is "SHADE + SLANT + BoW + NINJA." Section 5 and Section 21 both state SLANT is **NOT legal with SHADE**. This is the first example a coach reads — and it's an illegal combination.

**Fix:** Change to "UNDER + SLANT + BoW + NINJA" (UNDER + SLANT is a BEST pairing).

---

#### C2. CRASH + Zorro Creates Unresolvable QB/RB Conflict for B

**Location:** Playbook Section 5 (CRASH) and Section 9 (Zorro)

In CRASH: B = field contain → B has QB (per CAMP). In Zorro: B has RB (man). CRASH + Zorro is listed as a "best pairing," but B cannot have both the QB and the RB simultaneously.

The playbook notes B and M switch alignments (B goes to ~8 yds middle for RB, M moves to field force/contain area), which implies M takes contain (and therefore the QB). But this contradicts the explicit CRASH rule "B = field contain."

**Fix:** Add explicit CRASH + Zorro resolution: "When CRASH is paired with Zorro, M takes field contain (and therefore the QB per CAMP). B keys the RB from ~8 yds middle. M aligns at field force/contain position."

---

#### C3. BoW + Zeus Creates 7-Man Rush with Unaccounted RB

**Location:** Playbook Section 20.7 (BoW Pressure Card)

BoW sends B + W. In Zeus, M already rushes on pass read. Result: B, W, and M all rush = 7-man rush. Only FS, D, FC, BC remain in coverage — all four on receivers. The RB has zero coverage.

Unlike Eat (which explicitly acknowledges "RB unaccounted — DL must get home"), BoW + Zeus has no such disclaimer.

**Fix:** Either mark BoW + Zeus as "RB unaccounted — DL must get home" (like Eat), or note that W should check RB before rushing (converting to a 6-man rush with W as RB player).

---

#### C4. Freebird Defined as "Cover 1 Only" But Pressure Card Shows NINJA/Viking Entries

**Location:** Section 6 says "Freebird — Cover 1 only." Section 20.12 defines Freebird assignments for NINJA and Viking.

The quick pairing guide lists NINJA/Viking under "Use Caution" rather than "NOT LEGAL." This creates ambiguity: is Freebird strictly Cover 1, or can it be used with NINJA/Viking?

**Fix:** Either (a) remove NINJA/Viking rows from the Freebird pressure card and enforce "Cover 1 only," or (b) remove the "Cover 1 only" restriction and formalize the NINJA/Viking assignments as legal-but-risky.

---

#### C5. SLIP + Man Coverage (C0/C1) Has No Contain Entry in the Contain Matrix

**Location:** Section 4 (Contain Matrix)

The matrix lists SLIP + NINJA/VIKING (A and E contain, B plays clean) but omits SLIP + Man (C0/C1). If a DC calls SLIP + Oregon, the contain rule is undefined. Every other package has entries for both man and zone.

**Fix:** Add row: "SLIP + Man (C0/C1): A and E contain. B plays coverage clean (same as zone — SLIP always keeps B in coverage regardless of coverage family)."

---

#### C6. Eat + Viking Described as "Do Not Pair" But Not Marked Illegal

**Location:** Section 20.9 says "Do not pair with Viking." Quick pairing guide lists Viking under "Use Caution."

Compare with sWarM + Cover 1 and Eat + Cover 1, both marked "NOT LEGAL." Eat + Viking leaves zero underneath defenders — any short route is an easy completion.

**Fix:** Change Eat + Viking from "Use Caution" to "NOT LEGAL" in the quick pairing guide.

---

### MAJOR (Teaching Confusion Risk)

#### M1. CLAUDE.md Lists Viking RIP/LIZ as Active; Playbook Shows Them as Dropped

CLAUDE.md describes Viking RIP/LIZ with full detail. Playbook.md marks them ~~DROPPED~~ with strikethrough.

**Fix:** Update CLAUDE.md to show dropped status.

---

#### M2. 10-Tech Definition Inconsistent Between CLAUDE.md and Playbook.md

CLAUDE.md: "head up on center at LB depth (no TE)." Playbook.md: "head up over C gap at LB depth." These are different alignments. The GRIZZLY front table matches CLAUDE.md's definition.

**Fix:** Update Playbook.md technique chart to match CLAUDE.md: "Off LOS, head up on center at LB depth (GRIZZLY M, no TE); head up on guard to TE side at LB depth (TE present)."

---

#### M3. NINJA POACH Destination Marked "Tabled" in CLAUDE.md But Fully Defined in Playbook.md

CLAUDE.md deferred items: "POACH destination rules — tabled." Playbook.md defines it: "10-12 yds deep, splitting #2/#3 trips side."

**Fix:** Remove from CLAUDE.md deferred items or mark complete.

---

#### M4. NINJA Empty Rules Marked "Tabled" in CLAUDE.md But Defined in Playbook.md

Same stale-deferred-items issue. Both 3x2 and 2x3 empty rules are defined in the playbook.

**Fix:** Remove from CLAUDE.md deferred items or mark complete.

---

#### M5. ACE DL 2-Gap Play Still Tabled — LB Run Fits Undefined

ACE is installable (in-season Weeks 3-4) but M/W gap fits are "tabled: define DL 2-gap play first." If ACE is called against a running team, M and W have no defined gap fits.

**Fix:** Either (a) define the 2-gap LB fits, or (b) explicitly restrict ACE to passing situations only until the fits are defined.

---

#### M6. W's NINJA Role Changes Between CLAMP and Boundary MOD — Crosser Rules Only Address CLAMP

The crosser handling summary assumes W is always in CLAMP (hook/curl #3). If boundary MOD is called, W becomes the flat player — but the crosser rules don't address this configuration.

**Fix:** Add crosser handling rules for W-as-flat-player in boundary MOD configuration.

---

#### M7. GRIZZLY + CRASH Appears in Same Situational Recommendation Tables Despite Being Illegal

Sections 23.1, 23.4, and 23.5 all list GRIZZLY as a front and CRASH as a stunt in the same recommendation block. Notes say "CRASH NOT legal with GRIZZLY" but a coach scanning quickly could pair them.

**Fix:** Separate GRIZZLY calls and CRASH calls into distinct recommendation rows.

---

#### M8. Cobra Coverage Chain (Section 20.13) Contradicts Cobra Definition (Section 6)

Section 6: "B takes #2 boundary, FS takes #2 field." Section 20.13 chain-of-replacement: "B assumes FS's rules" (which in Zunnel = #2 field) and "FS assumes D's rules" (= #2 boundary). The chain produces the opposite assignment from what Section 6 explicitly states.

**Fix:** Align Section 20.13 chain with Section 6's explicit assignments. The chain should read: "D takes #1 bnd (replaces BC). FS stays on #2 field (unchanged). B takes #2 boundary (from Zorro-depth alignment)."

---

#### M9. Zeus Quick Reference Lists "5-7 Rushers" — Base Zeus is 4-Man Rush

Coverage family quick reference says Zeus has "5-7" rushers. Base Zeus is 4 DL + M on pass read = 5, with B/W conditional.

**Fix:** Change to "4 (+ M on pass; B/W conditional)" or "4-5 base, up to 7 with pressure."

---

#### M10. NINJA 3x1 Does Not Explicitly State Trips-Side Technique

The 3x1 section defines the poach safety's role but doesn't explicitly say the trips side plays MOD/CLAMP. A player on the trips side must deduce this.

**Fix:** Add one line: "Trips side plays its normal MOD/CLAMP triangle. Poach safety adds to coverage from the backside."

---

### MINOR (Cleanup Items)

| # | Finding | Fix |
|---|---------|-----|
| m1 | Signals undefined for ~50 of 56 concepts | Define signals or adopt wristband system |
| m2 | Anchor/Edge Attack "OK" with every front including GRIZZLY (4i alignment) | Mark GRIZZLY as "Caution" for both attacks |
| m3 | SLIP stunt catalog says "stunts are legal"; legality matrix says "stunts are not run with SLIP" | Resolve contradiction — recommend: stunts ARE legal with SLIP per stunt catalog and CLAUDE.md |
| m4 | BOSS/BOSS UNDER + TE SET behavior undefined (no examples) | Add TE SET examples for BOSS/BOSS UNDER |
| m5 | Option appendix: "B (QB player in man)" — ambiguous phrasing | Rewrite: "B (in man coverages) or M (in NINJA/VIKING)" |
| m6 | Dawg + Zeus: #2 boundary uncovered with no resolution | Mark as known risk or define FS help rule |
| m7 | B's NINJA MOD role described differently in CLAUDE.md vs Playbook.md | Align descriptions — playbook's "flat player" definition is authoritative |
| m8 | 3-down common ILB fits (stack/inside-out) vs Section 13 specific gap fits — relationship unclear | Add note: "Common rules describe philosophy; Section 13 assigns specific gaps" |
| m9 | Wristband numbers exist (01-76) but playbook says "no wristbands" | Resolve — recommend adopting wristbands |
| m10 | DEUCES "M/W become gap players only if stunt creates it" contradicts reactive fit rule | Clarify: "In DEUCES, M/W read DL movement to determine gap (reactive fit)" |

---

## 3. OC PERSPECTIVE: EXPLOITABLE VULNERABILITIES

### 3.1 STRUCTURAL VULNERABILITIES

#### V1. Field-Strength Tendency is Exploitable

Strength always set to field. A/T default field, N/E default boundary. An OC who knows this can:
- Align trips boundary to force unfamiliar adjustments on D, BC, E, N
- Motion from 2x2 to trips-boundary to force a POACH re-check with FS sliding away from his natural side
- Run to the boundary where N (often a lighter DT at 2i) is the interior defender

**Mitigation:** The UNDER front exists as a tendency-breaker (shifts DL strength to boundary). Call UNDER 25-30% of the time to prevent boundary tendencies.

---

#### V2. 6-Man Light Box is Vulnerable to Heavy Personnel Gap Schemes

Default 6-man box vs 21/22 personnel running power/counter creates a numbers disadvantage. B is "first insert for 7th hat" but must recognize and trigger fast.

**Mitigation:** Game-plan to GRIZZLY automatically vs 21/22 personnel. Don't wait for B to insert — give him a box assignment pre-snap.

---

#### V3. B (Bandit) is THE Conflict Player — RPO Reads Exploit Him

In NINJA, B is the flat player. If he bites on run, the RPO throw behind him is open. If he stays in coverage, the run hits an undermanned box.

**Mitigation:** SLIP package removes B from the run/pass conflict entirely. In base, B must be coached to "read, don't react" — max 1 step before identifying run vs pass.

---

#### V4. Single-High Coverages Vulnerable to MOF Attacks

Oregon/Oklahoma have one post safety. 4 verticals and double posts force that safety to choose a side.

**Mitigation:** Lean on NINJA and VIKING when facing teams that run heavy 4-verts or double posts (see concept vs coverage matrix, Section 15). Save Cover 1 for quick-game/RPO opponents.

---

#### V5. Tempo is the #1 Weapon Against This Defense

The call grammar (Front + Stunt + Blitz + Coverage/Tags) requires up to 4 signal components. NINJA requires safety re-checks on motion. Oklahoma requires a pre-snap safety swap. At 15-second tempo:
1. Signal relay from sideline may not complete
2. Safety checks may not communicate
3. Formation adjustments (TE SET, trips, bunch) may not trigger

**Mitigation:** Designate a "tempo call" — one base call (SHADE + NINJA) that requires zero communication beyond a single signal. When the offense goes fast, default to the tempo call.

---

### 3.2 SCHEMATIC ATTACK PLAN (What an OC Would Run)

#### Run Concepts

| Concept | Target | Why |
|---------|--------|-----|
| Inside Zone weak (boundary) | W, N | SHADE puts 3-tech field — boundary A gap is W's fit. IZ to boundary attacks this directly. |
| Power/Counter to field | M, B's insert speed | 6-man box, B must insert as 7th hat. If B is late, M is outnumbered. |
| Split Zone | E, D's run support | Slicer seals E, cutback opens. D is 10-12 yds deep pre-snap — slow to fill. |
| Jet Sweep + RPO | B's conflict | B must choose: set edge (give up throw) or stay coverage (give up corner). |
| QB Draw after Zeus shows | M's PA rule | Zeus has M reading run-first. QB draw after 1-3 Zeus shows exploits the PA transition window. |

#### Pass Concepts

| Concept | Target | Why |
|---------|--------|-----|
| Mesh/Crossers vs Cover 1 | D, B in man | Picks/rubs give man defenders trouble. No zone pass-off help. |
| 4 Verticals vs Oregon/Oklahoma | Post safety | Single post must choose side. Two seams split him. |
| Flood/Sail to field vs NINJA | B's flat responsibility | 3-level stretch. B can't cover flat and carry #2 vertical simultaneously. |
| Slant/Flat vs VIKING | FC/BC bail | Corners bail to deep 1/3. Slants break underneath at 5-6 yds. |
| Double Post vs any single-high | Post safety | Designed to beat Cover 1. Two posts converge on MOF. |

#### Motion / Formation Attacks

| Tactic | Exploit |
|--------|---------|
| 2x2 → Trips motion at tempo | Forces NINJA re-check. Snap before re-check = poach safety out of position. |
| Bunch field | BANJO alert changes assignments. Communication failure = bust on IN/OUT sort. |
| Empty with late RB motion | Cover 1: both funnel players lose assignment. Zeus: "nearest B or W takes" — ambiguous timing. |
| Quads (4x1) | Only partially defined ("M or W must expand to #4" — which one?). |
| Trips boundary | Forces defense into less-practiced adjustments. |

#### Pre-Snap Tells to Exploit

| Tell | Reveals | Attack |
|------|---------|--------|
| FS/D swap sides | Oklahoma | Double posts to MOF. FS is now boundary — may be uncomfortable. |
| B walks to ~8 yds | Ohio or Zorro | Field flat undefended by B. Quick screens to #2 field. RPO. |
| Two-high shell holds | NINJA or Viking | Flood/sail to stress flat. Slant/flat vs Viking bail. |

---

### 3.3 SITUATIONAL VULNERABILITIES

**Red Zone:** GRIZZLY + ZEUS + Eat is all-out blitz with zero RB coverage. PA + RB flat is a touchdown if DL doesn't get home immediately.

**2-Minute:** Conservative calls (SHADE + NINJA, Mike only). Quick intermediate routes to the middle (dig, stick, curl at 8 yds) will move chains. The defense wants you on the sideline — take the middle instead.

**3rd & Long:** Heavy pressure (Eat, sWarM, BooM) with zone behind it. Screen game kills this — the playbook has VIKING SCREEN but DL must recognize and redirect. Draw play after 2 pass sets will also gain chunk yardage.

---

## 4. HEAD COACH PERSPECTIVE: VOLUME, IMPLEMENTATION & PROGRAM GAPS

### 4.1 VOLUME / COGNITIVE LOAD

#### Raw Inventory

| Category | Count |
|----------|-------|
| 4-Down Fronts | 8 |
| 3-Down Packages | 4 |
| Stunts | 10 |
| Single Pressures | 4 |
| Combo Pressures | 5 |
| Packaged Pressures | 2 |
| Special Pressures | 3 |
| Coverage Calls | 10 |
| Tags | 6+ |
| Alerts/Autos | 4 |
| **Total named concepts** | **~56** |

#### High School Capacity Benchmarks

- **Average HS varsity:** 8-12 concepts reliably (≤15% bust rate)
- **Elite HS programs:** 15-20 concepts
- **This playbook:** ~56 named concepts

**The volume is approximately 3x typical and 2x elite.** The install plan and in-season progression show the DC intends to layer it, but the risk is surface-level learning across everything rather than deep mastery of a few things.

#### Combinatorial Explosion

Front (12) x Stunt (~6 legal avg) x Pressure (~10) x Coverage (10) = thousands of theoretical combinations. The game-day call sheet wisely limits to 20-25 calls, but the mental database required to handle any of those calls requires understanding the full system.

---

### 4.2 INSTALL PLAN ASSESSMENT

#### Day 10 Checkpoint (Current) — 26+ Concepts

Shade, Under, Grizzly, Eyes, TE SET, Slant, Angle, Pinch, Jacks, Crash, Mike, Will, Bandit, sWarM, BooM, BoW, Hammer, Eat, NINJA (2x2 + 3x1), Oregon, Oklahoma, Ohio, Zeus, Zorro, Viking, Mint.

**This is not realistic for 10 HS camp days.** Each day yields ~60-90 minutes of meaningful install time. At 26 concepts requiring ~40 reps each, the math barely works with zero margin for re-teaching.

#### Recommended Day 10 Checkpoint — 15 Concepts

| Concept | Priority |
|---------|----------|
| SHADE front + base run fits | Must |
| TE SET adjustment | Must |
| UNDER front | Must |
| SLANT stunt (pairs with Under) | Must |
| PINCH stunt (versatile) | Must |
| Mike pressure | Must |
| Will pressure | Must |
| Bandit pressure | Must |
| NINJA 2x2 (MOD/CLAMP) | Must |
| NINJA 3x1 (POACH) | Must |
| OREGON (Cover 1) | Must |
| ZEUS (identity play) | Must |
| VIKING (Zeus call-off) | Must |
| CAMP rule | Must |
| BANJO / EXCHANGE alerts | Must |

**Moved to in-season:** Ohio, Oklahoma, Zorro, Mint, Grizzly, Eyes, Angle, Jacks, Crash, sWarM, BooM, BoW, Hammer, Eat.

#### Week 1 vs Week 10 Game Plan

**Week 1 (12-15 calls):**
1. SHADE + NINJA (base)
2. SHADE + ZEUS (identity)
3. SHADE + NINJA (Zeus call-off)
4. SHADE + OREGON (man)
5. SHADE + Mike + NINJA
6. SHADE + Mike + OREGON
7. SHADE + VIKING (zone)
8. UNDER + NINJA
9. UNDER + SLANT + NINJA
10. UNDER + SLANT + Will + OREGON
11. SHADE + PINCH + NINJA
12. SHADE + Bandit + NINJA
13. SHADE + PINCH + Mike + ZEUS (short yardage)

**Week 10 (20-25 calls):** Add Grizzly (red zone), Oklahoma/Ohio (man variety), sWarM/BooM/BoW/Hammer (pressure variety), Angle/Jacks/Crash stunts, Viking tags, situational calls.

---

### 4.3 CRITICAL PROGRAM GAPS

#### Gap 1: Communication System — Wristbands vs Signals

The playbook says "All calls are signaled — no wristbands" (Section 16). But:
- Signals are defined for only 6 of 56 concepts (Mint, Ace, Jet, Slip, Anchor Raven, Edge Raven)
- A wristband numbering scheme (01-76) already exists
- At the HS level, signal systems fail regularly (noise, glare, wrong coach, player not looking)

**Recommendation: Adopt wristbands as primary. Use signals as backup.** The numbers are already designed. Print them.

#### Gap 2: No Individual Drill Scripts

The playbook tells coaches WHAT to teach but not HOW to teach the physical skills. Missing:
- DL drills: get-off, stunt timing, pass-rush moves, contain/cage
- LB drills: read key, open gap fit, RB funnel, blitz timing, crosser carry
- DB drills: inside leverage jam, MOD technique, CLAMP technique, top-down, poach, bail
- B drills: apex read, flat player technique, man from apex, edge rush, force

**Recommendation:** Create a 1-page daily drill menu for each position group.

#### Gap 3: No Backup / Injury Protocols

If the starting B goes down, the backup faces 12 roles. The playbook should define:
- Two-deep chart with simplified call sheets per backup
- "If backup B enters: drop Ohio, Zorro, Cobra, Hammer. Run NINJA and Oregon only."
- Fatigue call: one call everyone can execute when gassed (SHADE + NINJA)

#### Gap 4: No Sideline Organization

Undefined: Who signals? DC in press box or on field? Who relays? Who manages sub packages? Who tracks Zeus show count? Who charts opponent tendencies in real time?

#### Gap 5: No Film Study Protocol

The playbook is beautifully organized for film study (concept vs coverage matrix, run scheme specifics), but no protocol exists for: when staff watches film, scouting report format, how tendency data feeds the call sheet, player film study requirements.

#### Gap 6: No Special Teams Integration

B is likely also a punt/kick returner or coverage player. Special teams competes for practice time (~15-20 min/day) and reduces defensive install time.

---

### 4.4 CONCEPTS TO CONSIDER DROPPING PERMANENTLY

| Concept | Reason |
|---------|--------|
| ACE | 2-gap is not viable at HS. LB fits still undefined. |
| BOSS / BOSS UNDER | Exotic overloads that create as many problems as they solve. TE SET behavior undefined. |
| Cobra | Too specific: hash-only, Zunnel-only, Cover 0 only. |
| Freebird | No post safety is extremely risky at HS. |
| Zill / Zike | Zunnel already handles the RB problem more cleanly. |

Dropping these reduces the playbook from ~56 to ~45 concepts — still ambitious but more manageable.

---

## 5. POSITION COACH PERSPECTIVE: KEY RECOGNITION & REACTION CLARITY

### 5.1 POSITION COMPLEXITY RANKING

| Rank | Position | Complexity | Distinct Roles | #1 Gap |
|------|----------|-----------|----------------|--------|
| 1 | **B (Bandit)** | Extreme | 12+ | No unified read key across coverages |
| 2 | FS | Very High | 7 | Oklahoma pre-snap swap; POACH at tempo |
| 3 | M | High | 6+ | MINT contain awareness undefined; NINJA crosser progression |
| 4 | W | High | 6+ | CLAMP vs MOD role switch; CRASH contain role change |
| 5 | D | Medium-High | 6 | Oklahoma swap; Viking seam-curl-flat 3-priority read |
| 6 | FC | Medium | 5 | CLAMP "jump #2 out" technique |
| 7 | T | Low | Alignment varies | DEUCES decisiveness |
| 8 | N | Low | Alignment varies | Same as T |
| 9 | A | Low | 4 | None significant — CAMP rule is simple |
| 10 | E | Low | 4 | Counter discipline (don't chase flow) |
| 11 | BC | Low | 4 | None significant |

---

### 5.2 POSITION-BY-POSITION KEY ANALYSIS

#### B (BANDIT) — HIGHEST PRIORITY

B's read key changes by coverage with no unifying thread:

| Coverage | Alignment | Primary Key | Run Action | Pass Action |
|----------|-----------|------------|------------|-------------|
| NINJA MOD | Apex | #2 | Field force | Flat player. Cover down #2. Push vertical. First to flat. |
| NINJA CLAMP (field) | Apex | #2 | Field force | Hook/curl #3. Late push drop. |
| Oregon | Apex | #2 field | Force | Man #2 field. |
| Ohio | ~8 yds middle | — | — | Post/MOF. |
| Zeus | Apex | EMOL | Fit run gap | RB funnel (RB to B = take; away = rush). |
| Zorro | ~8 yds middle | RB | — | Man RB. |
| Zunnel | Apex | — | Fit run gap | Green-light rusher. |
| Viking | Apex | #2 | Support | Curl/flat field. |
| Hammer | Apex | — | — | Edge blitz. |
| Cobra | Zorro depth | #2 bnd | — | Takes #2 boundary. |
| 3-down (OLB) | Field OLB | EMOL | Contain/Force | Per coverage. |
| CRASH | Field contain | — | Replaces A contain | B has field QB (CAMP). |

**This is unteachable without a reference card.** A HS player cannot carry 12 role switches in memory.

**Recommendation:** Create a B-specific wristband/helmet card:
```
NINJA:  Apex → key #2 → Run: force / Pass: flat (MOD) or hook (#3 CLAMP)
OREGON: Apex → key #2F → Run: force / Pass: man #2F
OHIO:   8yds mid → Post/MOF
ZEUS:   Apex → key EMOL → Run: fit gap / Pass: RB funnel
ZORRO:  8yds mid → key RB → Man RB
ZUNNEL: Apex → Run: fit gap / Pass: RUSH
VIKING: Apex → key #2 → Run: support / Pass: curl/flat
```

---

#### FS (FIELD SAFETY) — 2ND HIGHEST COMPLEXITY

| Coverage | Pre-Snap | Post-Snap Key | Action |
|----------|----------|--------------|--------|
| NINJA MOD | 10-12 on #2 field | #2, read to #1 | #2 vertical = match. #2 out = high hole/rob #1. |
| NINJA POACH (trips bnd) | 10-12 on #2 field | Slide to #3 bnd | Split #2/#3 trips. #3 vertical = match. |
| Oregon | 10-12 on #2 field | — | Post/MOF. Rotate to middle. Fixer. |
| Oklahoma | **Boundary side** (swap) | #2 boundary | Man #2 bnd. |
| Ohio | 10-12 on #2 field | #2 field | Man #2 field. |
| Zeus | 10-12 on #2 field | #2 field | Man #2 field. |
| Viking | 10-12 on #2 field | — | Rotate to deep middle 1/3. |

**#1 bust risk: Oklahoma pre-snap swap.** If FS forgets to move to boundary, every downstream assignment breaks. Needs a physical cue (D taps FS, or FS taps his own helmet) every time Oklahoma is called.

**#2 bust risk: POACH timing at tempo.** Identifying trips-boundary and sliding over requires pre-snap communication that may not complete if the offense snaps fast.

---

#### M (MIKE) — KEY GAPS

**Gap 1: MINT + NINJA/VIKING — "M has contain awareness"**

The playbook says M is the QB contain player in MINT + zone coverage. But M is at ILB depth behind a 4i/0/4i DL. How does M play contain from there? Does he scrape over the top to the edge? Does he squeeze to C gap? "Contain awareness" is not a technique — it needs to be defined as a specific action.

**Recommendation:** Define: "MINT + zone: M scrapes to C gap on QB run read. M is the edge player if A (at 4i) gets washed inside. M does NOT sit in his gap — he must get outside A's alignment on QB keep."

**Gap 2: NINJA crosser rules — 4-step progression**

M must: (a) sit in hook zone, (b) wall first crosser entering zone, (c) carry crosser all the way through to boundary calling "CROSS!", (d) on mesh, take the deeper crosser while B relates back to the shallow one.

This is correct but requires a teaching progression:
1. Week 1: Hook zone only. No crosser carry.
2. Week 2: Add single crosser carry (wall and carry, call "CROSS!").
3. Week 3: Add mesh read (deeper crosser).
4. Week 4: Full rules.

**Gap 3: Zeus PA — "Max 2 steps downhill"**

This is the single most important coaching point for M. If M takes 3 steps on PA, the hook zone is vacated for the call-off (NINJA/Viking). Needs a daily PA read drill with a 2-step counter.

---

#### W (WILL) — KEY GAPS

**Gap 1: CLAMP vs MOD role switch**

Default NINJA: W is hook/curl #3 (CLAMP). If boundary MOD is called, W becomes the flat player. These are fundamentally different techniques from the same alignment — one is a passive drop, the other is an aggressive push. W must hear the check and change his entire approach.

The crosser handling summary only addresses W in CLAMP. When W is in boundary MOD (flat player) and a crosser comes through, his rules are undefined.

**Recommendation:** Add: "W in boundary MOD: push to flat. If crosser enters zone, relay to M. Do not chase crosser — stay in flat."

**Gap 2: CRASH contain**

W goes from ILB to boundary edge player (replacing E's contain). This is a major role change requiring specific drill work — W must practice setting an edge from LB depth.

**Gap 3: Zeus RB tiebreaker**

W has a unique rule: "RB middle = W takes." M does not have this tiebreaker. W must know he owns the middle release.

---

#### D (DAWG) — KEY GAPS

**Oklahoma pre-snap swap:** Same bust risk as FS. D moves from boundary to field pre-snap, then rotates from field to MOF post-snap. The physical movement is longer than any other position's and requires the most pre-snap time.

**Viking seam-curl-flat:** D must wall #2 vertical seam → settle in curl → rally to flat. This is a 3-priority read that requires more drill time than B's curl/flat.

---

#### FC (FIELD CORNER)

**One gap: CLAMP technique.** When field CLAMP is called (tight #2 split), FC must jump #2 out if #2 breaks to the flat — while FS flips to #1 deep. If the timing is off, #1 is uncovered deep. This requires extensive paired rep work between FC and FS.

---

#### T, N, A, E, BC — GOOD CLARITY

These positions have consistent, well-defined responsibilities. Key teaching points:
- **T/N in DEUCES:** Must attack a gap decisively. If T/N hesitate, M/W freeze.
- **E on counter:** Must NOT chase initial backfield flow. Discipline repetitions.
- **A:** CAMP rule is brilliantly simple. No significant gaps.
- **BC:** Simplest position. Cobra blitz is only exotic responsibility.

---

### 5.3 UNDEFINED READ KEYS BY POSITION

| Position | Situation | What's Missing |
|----------|-----------|---------------|
| B | Coverage changes | No unified read key — changes every coverage |
| M | MINT + zone coverage | "Contain awareness" not defined as a technique |
| M | NINJA crosser mesh | When to take deeper vs shallower crosser (both look deep?) |
| W | Boundary MOD + crosser | Crosser handling rules in flat-player configuration |
| W | CRASH | Edge-setting technique from LB depth |
| D | Viking | Seam-curl-flat priority order when all 3 happen simultaneously |
| FS/D | Oklahoma | Physical cue for pre-snap swap (no verbal mechanism defined) |

---

## 6. CONSOLIDATED ACTION ITEMS

### Tier 1 — Must Fix Before Camp

| # | Item | Source | Action |
|---|------|--------|--------|
| 1 | SHADE + SLANT example is illegal | C1 | Change to UNDER + SLANT |
| 2 | CRASH + Zorro QB/RB conflict | C2 | Add explicit resolution: M takes contain, B keys RB |
| 3 | Adopt wristband system | HC Gap 1 | Print wristbands using existing 01-76 scheme |
| 4 | Create B-specific wristband/helmet card | Position 5.2 | Coverage → alignment → key → run → pass for every call |
| 5 | Reduce Day 10 checkpoint to ~15 concepts | HC 4.2 | Move Ohio, Oklahoma, Zorro, Grizzly, etc. to in-season |
| 6 | Define MINT + zone M contain technique | Position 5.2 | "M scrapes to C gap on QB run read" |
| 7 | Write individual drill scripts (1-page per position) | HC Gap 2 | DL, LB, DB, B daily drill menus |
| 8 | Designate a "tempo call" | OC V5 | SHADE + NINJA — requires zero communication beyond one signal |
| 9 | Designate a "fatigue call" | HC Gap 3 | Same as tempo call — SHADE + NINJA, no stunt, no pressure |

### Tier 2 — Fix During Camp / Week 1

| # | Item | Source | Action |
|---|------|--------|--------|
| 10 | BoW + Zeus: mark RB as unaccounted | C3 | Add disclaimer like Eat |
| 11 | Freebird: resolve "Cover 1 only" vs pressure card | C4 | Remove NINJA/Viking rows or remove restriction |
| 12 | SLIP + Man: add contain matrix entry | C5 | Add row: A and E contain regardless of coverage |
| 13 | Eat + Viking: mark NOT LEGAL | C6 | Change from "Use Caution" to "NOT LEGAL" |
| 14 | Update CLAUDE.md: Viking RIP/LIZ = dropped | M1 | Strikethrough or remove |
| 15 | Fix 10-tech definition in Playbook.md | M2 | Match CLAUDE.md definition |
| 16 | Remove stale deferred items in CLAUDE.md | M3, M4 | Mark POACH destination and NINJA Empty as complete |
| 17 | Fix Cobra coverage chain in Section 20.13 | M8 | Align with Section 6 explicit assignments |
| 18 | Fix Zeus rusher count in quick reference | M9 | "4 (+ M on pass; B/W conditional)" |
| 19 | Add Oklahoma pre-snap cue | Position 5.2 | Define physical signal (helmet tap, partner tap) |
| 20 | SLIP stunt legality: resolve contradiction | m3 | Stunts ARE legal per stunt catalog — update legality matrix |

### Tier 3 — Fix In-Season

| # | Item | Source | Action |
|---|------|--------|--------|
| 21 | Add W crosser rules for boundary MOD | M6 | Define W's crosser behavior as flat player |
| 22 | Separate GRIZZLY and CRASH in situational tables | M7 | Distinct rows in Sections 23.1, 23.4, 23.5 |
| 23 | NINJA 3x1: state trips-side technique explicitly | M10 | "Trips side plays normal MOD/CLAMP triangle" |
| 24 | Add BOSS/BOSS UNDER + TE SET examples | m4 | Work through DL shifts with examples |
| 25 | Define ACE as pass-situations-only until 2-gap fits defined | M5 | Explicit restriction |
| 26 | Create backup/injury simplified call sheets | HC Gap 3 | Per-position backup protocols |
| 27 | Write sideline organization document | HC Gap 4 | Signal relay, sub management, tendency tracking |
| 28 | Write film study protocol | HC Gap 5 | Weekly schedule, scouting report format |
| 29 | Define signals for all concepts OR finalize wristband-only | m1 | One system, not both |
| 30 | M NINJA crosser teaching progression | Position 5.2 | 4-week progression: hook → carry → mesh → full |

### Tier 4 — Consider for Long-Term Program

| # | Item | Action |
|---|------|--------|
| 31 | Drop ACE permanently (2-gap not viable at HS) |
| 32 | Drop BOSS/BOSS UNDER (exotic, TE SET undefined) |
| 33 | Drop Cobra (too specific for HS) |
| 34 | Drop Freebird (no post safety too risky at HS) |
| 35 | Drop Zill/Zike (Zunnel handles RB cleaner) |
| 36 | Create JV playbook subset (6 concepts: Shade, TE SET, NINJA 2x2, Oregon, Zeus, Mike) |
| 37 | Create spring/summer install calendar for incoming sophomores |
| 38 | Create weekly scouting report template that feeds call sheet |

---

*Generated: 2026-02-25 — Multi-Perspective Playbook Audit*
