# River Valley Vikings Defensive Playbook

## Project Overview
Defensive playbook for the River Valley Vikings Varsity Football team. DC builds the playbook from chat exports and iterates on documents and diagrams.

## Team Colors
- Columbia blue (#6CACE4)
- Gold (#CFA700)
- White
- Navy blue (#002D62) for accents

## Files
- `Chat_Export_River_Valley_Vikings_Defense_Playbook.txt` — 7,789-line source chat export
- `create_playbook_docx.py` — generates text-only playbook .docx
- `create_playbook_diagrams.py` — generates diagram edition .docx (matplotlib diagrams embedded)
- `create_coverage_rules.py` — generates pre-snap disguise & coverage rules .docx (60 diagrams: 10 coverage diagrams + 50 concept×coverage diagrams)
- `River_Valley_Vikings_Defensive_Playbook.docx` — text-only output
- `River_Valley_Vikings_Defensive_Playbook_DIAGRAMS.docx` — diagram edition output
- `River_Valley_Vikings_PreSnap_Disguise_Coverage_Rules.docx` — pre-snap disguise, coverage rules, and pass concept breakdowns

---

## DEFENSIVE IDENTITY

**Base Personnel:** 4-2-5; 3-4 packages (Mint/Ace/Jet/Slip) based on offensive personnel.
**Strength:** Field ("protect space").
**Shell:** Two-high.
**Box:** 6-man (light box default).
**Call Format:** Front + Stunt + Blitz tag(s) + Coverage/Tags.
**Communication:** Signals with rules/adjustments per formation.

### Philosophy
"We play fast, physical, and disciplined football. Our job is to remove explosive plays, control the box, and force the offense to execute perfectly for an entire drive. We will pressure and change the picture, but never at the cost of leverage, gap integrity, or effort."

### Non-Negotiables
- No explosives. Make them snap it again.
- Aggressive with discipline. Attack without losing leverage or committing penalties.
- Box the run. Set hard edges, compress gaps, keep ball in help.
- Relentless pursuit. 11 to the ball, correct angles, swarming tackles.
- Win leverage. Outside vs perimeter/QB run; inside vs quick game/crossers.
- Win situations. 1st down sets the series; 3rd down/red zone = get off the field.
- Smart aggression. Pressure to take away something; call off the horses when needed.
- Communication standard. Simple, loud, early. Safeties are fixers. Alerts: BUMP / BANJO / EXCHANGE / UNDER.

### Grading Non-Negotiables
- No lost edges — contain player keeps QB and ball inside
- No uncovered gaps — adjust instantly if gap changes with stunt/pressure
- No free releases — collision/deny access; communicate stack/bunch
- No missed tackles — leverage + near foot + wrap; eliminate YAC
- No penalties that extend drives
- No loafs — pursuit is mandatory on film

---

## POSITION DESIGNATIONS

| Letter | Name | Role |
|--------|------|------|
| FC | Field Corner | Inside leverage, 6 yds (NINJA default) |
| FS | Field Safety | 2-high; NINJA field-side caller; 10-12 yds deep; align off #2 |
| B | Bandit (Nickel) | Field force/contain; hybrid DB/OLB; Field OLB in 3-down |
| A | Anchor (Field DE) | Box edge; CAMP QB player; default field side |
| T | Tackle (Field DT) | 3-tech to field in Shade; default field side |
| N | Nose (Boundary DT) | 2i boundary in Shade; default boundary side |
| E | Edge (Boundary DE/LB) | Boundary edge; Boundary OLB in 3-down |
| M | Mike (Field ILB) | Open A gap (field) in base |
| W | Will (Boundary ILB) | Open B gap (boundary) in base |
| D | Dawg (Boundary Safety) | Boundary force/contain; NINJA boundary-side caller; 10-12 yds deep |
| BC | Boundary Corner | Inside leverage, 6 yds (NINJA default) |

**Default Sides:** A, T = field. N, E = boundary (unless called out).

## TECHNIQUE CHART

| Tech | Alignment |
|------|-----------|
| 0 | Head up on Center |
| 1 | Shade on Center |
| 2i | Inside shade on Guard |
| 2 | Head up on Guard |
| 3 | Outside shade on Guard |
| 4i | Inside shade on Tackle |
| 4 | Head up on Tackle |
| 5 | Outside shade on Tackle |
| 6i | Inside shade on TE |
| 6 | Head up on TE |
| 7 | Outside shade on TE |
| 9 | Outside shade on Wing |

---

## 4-DOWN FRONT CATALOG

### Global Rules (no stunts)
- M fits the open gap to the field side
- W fits the open gap to the boundary side
- Open gap: 3-tech closes B → open A; 2/2i/1 closes A → open B
- A and E = contain (set edge, no wrong-arm)
- B = field force. D = boundary force
- 2-back (20/21): 6-man box default; B is first insert if adding 7th hat
- Puller rule (Power/Counter/Wing-T): Box + overlap; edge outside, M/W inside-out off pull path
- QB run (CAMP): DE (A) is QB player

### TE SET — Default 4-Down Adjustment
Overrides ALL fronts EXCEPT GRIZZLY when TE/Y-off surface.
- Set front to TE: 3-tech to TE, 2i away
- B inserts into box at LB depth over C gap
- End to TE aligns 7-tech and plays contain
- Example: TE to field → A goes to 7-tech on TE, E stays 5 boundary

### Front Alignments

| Front | A | T | N | E | M Fit | W Fit |
|-------|---|---|---|---|-------|-------|
| SHADE (base, set field) | 5 | 3 | 2i | 5 | Open A (field) | Open B (boundary) |
| UNDER (set boundary) | 5 | 2i | 3 | 5 | Open B (field) | Open A (boundary) |
| EYES (balanced) | 5 | 2i | 2i | 5 | Open B | Open B |
| WIDE | 5 | 3 | 3 | 5 | Open A | Open A |
| DEUCES | 5 | 2 | 2 | 5 | Make T/N right | Make T/N right |
| GRIZZLY | 4i | 2i | 2i | 4i | 10-tech; no gap (C to TE) | OLB |
| BOSS (bigs field) | 5 | 3(F) | 1(F) | 5 | A gap (boundary) | B gap (boundary) |
| BOSS UNDER (bigs bnd) | 5 | 1(B) | 3(B) | 5 | A gap (field) | B gap (field) |

**When to call:**
- SHADE: Base vs spread/RPO; stable vs Air Raid
- UNDER: Tendency breaker; boundary-run weeks; pairs with SLANT
- EYES: Vs zone/duo; square interior
- WIDE: Force bounce; vs B-gap heavy / gap schemes
- DEUCES: Vs Wing-T / pullers; M/W become gap players only if stunt creates it
- GRIZZLY: Vs power/counter; red zone; short yardage; B and W are OLBs; TE SET does NOT override
- BOSS: Overload field bigs; pressure setup
- BOSS UNDER: Overload boundary bigs

---

## 3-DOWN PACKAGES (MINT / ACE / JET / SLIP)

### Common Rules
- Field OLB = B. Boundary OLB = E.
- T/N may swap by personnel.
- Slice rule: backside OLB has slicer.
- Strength = Field.

### ILB Fits (Locked)
- Play-to (toward strength): STACK B → D (inside-out)
- Play-away (away from strength): SLOW PLAY A (patient shuffle, hunt cutback)

### MINT (4i / 0 / 4i)
- Signal: "M" on thigh
- A=4i, T=0, N=4i. B/E = OLBs.
- Contain: Man (C0/C1) = B. NINJA/VIKING (MINT only) = M is QB contain.

### ACE (4 / 0 / 4)
- Signal: 1 finger up (optional chest tap)
- A=4, T=0, N=4. B/E = OLBs.
- A, T, N ALL 2-gapping (no stunt). Contains = OLBs (B and E).

### JET (5 / 0 / 5)
- Signal: whoosh forward (hand flat)
- A=5, T=0, N=5. B/E = OLBs.
- T is 2-gapping. A and N are contain (C-gap edges).

### SLIP (5 / 0 / 4i)
- Signal: mime pushing a wall to the side (two hands)
- A=5, T=0, N=4i. B/E = OLBs.
- 1-gap penetrating. A and E are contain.
- Use: 3-down vs spread with NINJA or VIKING. Takes B out of conflict — B plays coverage clean.

### Contain Matrix
| Package + Coverage | Contain |
|--------------------|---------|
| MINT + Man (C0/C1) | B |
| MINT + NINJA/VIKING | M is QB contain |
| ACE/JET + Man | B |
| ACE/JET + NINJA/VIKING | B contain-first, then match on pass read |
| SLIP + NINJA/VIKING | A and E (B plays coverage clean) |

### TE Adjustment (3-Down)
OLB-only adjust: bump B/E alignments to TE/Y-off surface. Keep Mint/Ace/Jet/Slip interior intact.

---

## STUNT CATALOG

DL coaching point: read run/pass; on run read get heel depth. Edges play normal unless noted.

### SLANT (to field)
- 4-down: T+N slant to field. 3-down: A+T+N slant.
- NOT with Shade. Best fronts: Under, BOSS Under.
- Best pressures: Mike, Will, Bandit, sWarM, BooM, BoW.

### ANGLE (to boundary)
- Same as Slant but to boundary.
- NOT with Under/BOSS Under. Best fronts: Shade, BOSS.

### PINCH
- 4-down: T+N pinch A gaps (if already in A, play base). 3-down: A+N pinch B gaps.
- A and E normal. Best fronts: Shade, Under, Wide, Deuces.

### JACKS
- 4-down: T+N shoot B gaps. 3-down: A+N expand to C gaps (NOT pinch).
- A and E contain. NOT with Wide. Best fronts: Eyes, Shade, Under. Best pressure: sWarM.

### SPLIT
- With BOSS: 1-tech crosses C face to opposite A. With GRIZZLY: field gap-out.
- A and E contain. Looks weird with BOSS but plays like Shade. Best: Mike, sWarM.

### ANCHOR ATTACK
- A attacks OL closing one inside gap (washes OL inside). NOT paired with Cobra.

### EDGE ATTACK
- E attacks OL closing one inside gap. CAN pair with Cobra.

### CRASH
- A+E shoot B gaps. T+N shoot A gaps. B/M/W contain.
- NOT with Grizzly or Freebird. Best fronts: Wide, Shade, Under. Best pressure: BoW.

### ANCHOR RAVEN (A 5→B)
- A shoots B gap from 5. Signal: point field → flap flap.
- Not with Hammer or staB. If + Bandit = BANDIT RAVEN.

### EDGE RAVEN (E 5→B)
- E shoots B gap from 5. Signal: point boundary → flap flap.

---

## BLITZ / PRESSURE TAGS

Rule: All blitzes hit your gap responsibility unless noted.

### Single Add-Ons
- **Mike** — M blitzes his gap
- **Will** — W blitzes his gap
- **Bandit** — B blitzes his gap
- **Dawg** — D blitzes his gap

### Special Tags
- **staB** — B one gap inside EOL (normally B or C gap)
- **Freebird** — MOF safety (per coverage) blitzes
- **Cobra** — Boundary corner blitz. In 0-family: D takes #1 boundary, FS assumes D rules, B assumes FS rules, RB funneled by M/W.

### Combination Pressures
| Call | Who Blitzes |
|------|-------------|
| sWarM | M + W |
| BooM | B + M |
| BoW | B + W |
| MaD | M + D |
| Eat | M + W + B |

### Packaged Pressures (Married to Stunts)
- **Hammer** — B edge blitz + Anchor Attack (A washes OL inside, creating edge for B)
- **Shave** — W edge blitz + Edge Attack (E attacks OL)

### Weekly Called Pressures (Locked Friday Menu)
Mike, Will, Bandit, sWarM, BooM, BoW, Hammer, Eat.
Zeus/Z-family featured separately.

---

## COVERAGE: NINJA (COVER 7 FAMILY)

Coach calls "NINJA." DBs auto-check. FS owns field checks. D owns boundary checks. Safeties are fixers.

### Alignments
- **Corners (FC/BC):** Inside leverage, 6 yards on #1.
- **Safeties (FS/D):** 10-12 yds deep. Inside foot on #2 (~1 yd inside #2). No #2: poach/post posture, hash-to-middle. Compressed/stack: tighten 1-2 steps, be ready to BANJO.
- **B (Bandit):** Apex to field.

### NINJA vs 2x2 — MOD (Field) / CLAMP (Boundary)
**Field (MOD: FS + FC + B):**
- FC: man-match #1. Stay on top, deny explosives.
- FS: top-down on #2. #2 vertical = match. #2 out/flat = drive with control.
- B: apex rules to #2/#3. Eliminate RPO access. Carry seams for safety help.

**Boundary (CLAMP: D + BC):**
- BC: clamp technique. Physical, deny release, protect outside leverage.
- D: control #2 and help corner. #2 vertical = match.

### NINJA vs 3x1 — POACH
- **Trips to field: D is the poach safety.**
- **Trips to boundary: FS is the poach safety.**
- #3 vertical: poach player takes it.
- #3 shallow/under: poach player overlaps crossers.
- Backside stays sound.

### NINJA Motion Rule
- BUMP is for MAN coverages ONLY, NOT NINJA.
- Motion creates/removes trips → re-check:
  - 2x2 → 3x1: "POACH! POACH!"
  - 3x1 → 2x2: "MOD/CLAMP!"
  - No trips change: keep original.
- Nearest safety calls re-check; other echoes.

### NINJA Special Formations
- **Bunch/Stack/Tight Splits:** BANJO alert. Corner = first OUT; near safety = first IN; opposite safety = deeper fixer.
- **Rub/Pick:** EXCHANGE automatic. Switch on contact.
- **Empty:** Stay split-field. DBs identify #3 threats.
- **Nub TE/Y-off:** Treat nub as #1. Safety communicates if nub goes vertical.

---

## COVERAGE: COVER 1 FAMILY

### CAMP Distribution (All 3)
- FC/BC: man #1 to your side.
- Non-post safeties: #2 to their side, or #3 away if no #2.

### RB Funnel / RAT (All 3)
- M and W funnel RB.
- RB to your side → take RB. RB away → rush.
- TAMPA tag: LB away from RB becomes RAT.

### OREGON (Post = FS)
FS = Post/MOF. D = man #2 bnd or #3 away. B = man #2 field or #3 away. M/W = RB funnel.

### OKLAHOMA (Post = D)
**Pre-snap: FS and D switch sides.** D aligns to field, FS aligns to boundary.
D = Post/MOF (rotates from field). FS = man #2 bnd (already on boundary). B = man #2 field or #3 away. M/W = RB funnel.

### OHIO (Post = B) — EXCEPTION
B aligns at ~8 yds deep in the middle of the formation (not at apex). B = Post/MOF. FS = man #2 field or #3 away. D = man #2 bnd or #3 away. M/W = RB funnel.

### ZORRO — EXCEPTION
B aligns at ~8 yds deep in the middle of the formation to key the RB (not at apex). Changes pre-snap look.

---

## COVERAGE: COVER 0 / Z-FAMILY

All Z-calls = Cover 0. No deep safety help.

### CAMP DB Rules (0-Family)
- FC: man #1 field. BC: man #1 boundary.
- FS: man #2 field (or #3 away). D: man #2 boundary (or #3 away).

### Universal Tags
- **TAMPA:** 2nd-level players become droppers/RAT.
- **SPY:** Tagged player spies QB.

### ZEUS (Run-First / Pass-Read Delayed Pressure)
**Rush on pass (always):**
- A & E: cage/contain (don't run past QB depth, force step-up)
- T & N: vertical push / collapse pocket
- M: primary add-on rusher

**B and W (conditional — run first, then RB check):**
- RB to your side → take RB. RB away → rush. RB middle → W takes.

**Call-off:** After showing Zeus 1-3 times, bail to NINJA or VIKING.

### ZORRO
- B has RB. M/W no pass responsibility unless tagged (TAMPA = droppers, SPY = spy QB).

### ZUNNEL
- M and W funnel RB. RB to your side → take. Away → rush. TAMPA: away = RAT.

### ZILL
- W has RB (man).

### ZIKE
- M has RB (man).

### Z-Family RB Player Reference (for UNDER alert)
| Z-Call | RB Player |
|--------|-----------|
| Zeus | B or W (funnel) |
| Zorro | B |
| Zunnel | M or W (funnel) |
| Zill | W |
| Zike | M |

### 0-Family Motion Rules
- Receiver motion: safeties travel. Underneath does NOT.
- Safeties do NOT cross.
- RB motion out (empty): nearest B or W takes.

---

## COVERAGE: VIKING (COVER 3 FAMILY)

### VIKING (Base) — Spot-Drop Cover 3
Intent: safe, anti-explosive, low bust. Primary Zeus call-off.

**Deep 3:** FC = 1/3 field. FS = 1/3 middle. BC = 1/3 boundary.
**Underneath:** B = curl/flat (field). D = seam-curl-flat (boundary). M = hook. W = hook.

**Tags:** VIKING SEAM, VIKING PUSH (trips), VIKING CROSS, VIKING SCREEN.

### VIKING RIP / VIKING LIZ (True Match 3)
Single-side call sets seam-match distribution. Use: verts, sail/flood, switch releases, glance RPO.

### VIKING Fire Zone
Status: DEFERRED ("forget the fire zone Viking for now").

---

## AUTOS & ALERTS

### BUMP-BUMP (Man Coverages Only — C0/C1)
- Safeties travel. Underneath does NOT. Safeties do NOT cross.
- BUMP 1 (Safety → Safety): traveling safety hands off because he won't cross.
- BUMP 2 (Safety → Corner): if motion becomes new widest #1, safety bumps to corner.
- Corner takes ONLY when motion is new widest #1 to that side.

### BANJO (Safety Alert — NOT Signaled In)
- Trigger: stack, tight/close splits, bunch.
- Corner = first OUT. Near safety = first IN. Opposite safety = deeper fixer.

### EXCHANGE (Automatic)
- Trigger: rub/pick route concepts. Switch on contact. Communicate early.

### UNDER (On-Field Alert — Fixer-Driven)
- Trigger: receiver runs UNDER to pick RB-responsible defender AND RB releases fast out.
- Rule: RB player takes UNDER (replaces pick). UNDER defender takes RB (swap).
- Call: "UNDER! UNDER!" (no numbers). Fixer safety calls it.
- RB player by coverage: Cover 1 = M or W. Zeus = B or W. Zorro = B. Zunnel = M or W. Zill = W. Zike = M.

---

## RUN-FIT RULES

### Goals
No explosives. Box it. Relentless pursuit. Force ball to help.

### Base (4-Down, Non-Grizzly)
- Edges: A/E contain. Force: B = field, D = boundary.
- ILBs: M = open gap field, W = open gap boundary.

### Special
- **Pullers:** Box + overlap; edge outside, M/W inside-out.
- **QB Run (CAMP):** A is QB player.
- **2-Back:** 6-man box; B first insert.
- **Slice:** Backside OLB has slicer.

### 3-Down ILB Fits
- Play-to: STACK B → D. Play-away: SLOW PLAY A.

---

## CALL GRAMMAR & SIGNALS

**Order:** Front + Stunt + Blitz + Coverage/Tags

**Examples:**
- SHADE + SLANT + BoW + NINJA
- GRIZZLY + PINCH + Mike + OREGON
- BOSS + SPLIT + Cobra + ZEUS
- ZEUS (show) → call-off to NINJA/VIKING

### Signals
- MINT: "M" on thigh. ACE: 1 finger up. JET: whoosh forward.
- Anchor Raven: point field → flap flap. Edge Raven: point boundary → flap flap.
- Grammar: front sign, then stunt sign.

### Wristband Menu
| Category | Codes |
|----------|-------|
| Fronts (01-20) | 01 Shade, 02 Under, 03 Eyes, 04 Wide, 05 Deuces, 06 Grizzly, 07 Boss, 08 Boss Under |
| Stunts (21-35) | 21 Slant, 22 Angle, 23 Pinch, 24 Jacks, 25 Split, 26 Crash, 27 Anchor Raven, 28 Edge Raven |
| Pressures (36-50) | 36 Mike, 37 Will, 38 Bandit, 39 sWarM, 40 BooM, 41 BoW, 42 Hammer, 43 Eat, 44 Zeus |
| Coverages (51-65) | 51 Ninja, 52 Oregon, 53 Oklahoma, 54 Ohio, 55 Viking |
| Tags (66-75) | 66 Tampa, 67 Spy |

---

## DEFERRED / PENDING ITEMS
- ~~Viking fire zone~~ — dropped (pressure packages cover this)
- ~~Viking RIP/LIZ match-3~~ — dropped (NINJA already provides route-matching)
- Install plan (week-by-week)
- Blitz/pressure drill progressions

## COMPLETED SECTIONS (in MD playbook)
- Section 18: Formation Recognition & Adjustment Rules
- Section 19: Personnel Grouping ID
- Section 20: Pressure Cards (Rush/Drop Assignments) — all pressures × all coverages
- Section 21: Front-Stunt Legality Matrix
- Section 22: Run Scheme Specifics (IZ, OZ, Power, Counter, Draw, QB Run, Jet Sweep)
- Section 23: Situational Defense (3rd down, red zone, goal line, 2-min, backed up, 4-min)
