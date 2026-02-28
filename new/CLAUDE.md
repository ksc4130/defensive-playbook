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
**Box:** 6-man.
**Call Format:** Front + Stunt + Blitz tag(s) + Coverage/Tags.
**Communication:** Front/stunt/blitz signaled; coverage is verbal. Safeties echo and relay.

### Philosophy
"We play fast, physical, and disciplined football. Our job is to remove explosive plays, control the box, and force the offense to execute perfectly for an entire drive. We will pressure and change the picture, but never at the cost of leverage, gap integrity, or effort."

### Non-Negotiables
- No explosives. Make them snap it again.
- Aggressive with discipline. Attack without losing leverage or committing penalties.
- Box the run. Set hard edges, compress gaps, keep ball in help.
- Relentless pursuit. 11 to the ball, correct angles, swarming tackles.
- Win leverage. Outside vs perimeter/QB run; inside vs quick game/crossers.
- Win situations. 1st down sets the series; 3rd down/red zone = get off the field.
- Smart aggression. Plus-one rushers to blockers with zero coverage behind it. No-win situation for the offense. Call off the horses when needed.
- Communication standard. Simple, loud, early. Everyone echoes. Alerts: BUMP / BANJO / EXCHANGE / UNDER.

### The Standard
- No lost edges — contain player keeps QB and ball inside
- No uncovered gaps — adjust instantly if gap changes with stunt/pressure
- No free releases — collision every route; reroute, disrupt timing, deny easy access
- No missed tackles — leverage + near foot + wrap; eliminate YAC
- No penalties that extend drives
- No loafs — pursuit is mandatory

---

## POSITION DESIGNATIONS

| Letter | Name | Role |
|--------|------|------|
| FC | Field Corner | Cover #1 field; run support |
| FS | Field Safety | Field-side caller; MOD/CLAMP fixer |
| B | Bandit (Nickel) | Field force/contain; hybrid DB/OLB; Field OLB in 3-down |
| A | Anchor (Field DE) | Field edge; contain; QB player (CAMP) |
| T | Tackle (Field DT) | Interior run control; pass rush |
| N | Nose (Boundary DT) | Interior run control; pass rush |
| E | Edge (Boundary DE/LB) | Boundary edge; contain; OLB in 3-down |
| M | Mike (Field ILB) | Run fit field gap; coverage dropper/blitzer |
| W | Will (Boundary ILB) | Run fit boundary gap; coverage dropper/blitzer |
| D | Dawg (Boundary Safety) | Boundary-side caller; boundary force/fixer |
| BC | Boundary Corner | Cover #1 boundary; run support |

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
| 8i | Inside shade on Wing |
| 8 | Head up on Wing |
| 9 | Outside shade on Wing |

### Gap Names
| Gap | Location |
|-----|----------|
| A Gap | Between Center and Guard |
| B Gap | Between Guard and Tackle |
| C Gap | Between Tackle and TE (or outside Tackle if no TE) |
| D Gap | Outside the TE |
| E Gap | Outside the Wing |
| Alley | Outside contain lane — where the force/contain player operates |

**Contain** = maintain outside leverage, squeeze run inside. **Force** = collision at/behind LOS, turn ball inside.

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
- QB run (CAMP): Whoever has contain has the QB

### TE SET — Default 4-Down Adjustment
Overrides ALL fronts EXCEPT GRIZZLY when TE/Y-off surface.
- Set front to TE: 3-tech to TE, 2i away
- End to TE aligns 7-tech and plays contain
- Example (TE to field): A goes to 7-tech on TE, E stays 5 boundary. B inserts at LB depth over C gap field.
- Example (TE to boundary): E goes to 7-tech on TE, A stays 5 field. B inserts at LB depth over C gap boundary.
- TE SET triggers on alignment, not personnel. If TE splits out as WR (3+ yds from OL), no TE SET.
- **Gap fits (TE to field):** B = C gap, M = A gap, W = B gap.
- **Gap fits (TE to boundary):** B = B gap, M = A gap, W = C gap. SHADE checks to UNDER.

### Front Alignments

| Front | A | T | N | E | M Fit | W Fit |
|-------|---|---|---|---|-------|-------|
| SHADE (base, set field) | 5 | 3 | 2i | 5 | Open A (field) | Open B (boundary) |
| UNDER (set boundary) | 5 | 2i | 3 | 5 | Open B (field) | Open A (boundary) |
| EYES (balanced) | 5 | 2i | 2i | 5 | Open B | Open B |
| WIDE | 5 | 3 | 3 | 5 | Open A | Open A |
| DEUCES | 5 | 2 | 2 | 5 | React to T (T closes A→M fills B; T stays B→M fills A) | React to N (same) |
| GRIZZLY | 4i | 2i | 2i | 4i | Head up center at LB depth (no TE); head up guard to TE side at LB depth (TE present); C gap | OLB |
| BOSS (bigs field) | 5 | 3(F) | 1(F) | 5 | A gap (boundary) | B gap (boundary) |
| BOSS UNDER (bigs bnd) | 5 | 1(B) | 3(B) | 5 | A gap (field) | B gap (field) |

**When to call:**
- SHADE: Base vs spread/RPO; stable vs Air Raid
- UNDER: Tendency breaker; boundary-run weeks; pairs with SLANT
- EYES: Vs zone/duo; square interior
- WIDE: Force bounce; vs B-gap heavy / gap schemes
- DEUCES: Vs Wing-T / pullers; M/W become gap players only if stunt creates it
- GRIZZLY: Goal line; power/counter/zone; edge pressure; short yardage; B and W are OLBs; TE SET does NOT override
- BOSS: Overload field / confuse OL; SPLIT → SHADE post-snap; ANGLE → EYES post-snap; pressure setup
- BOSS UNDER: Overload boundary / confuse OL; SPLIT or ANGLE combos
- DISCO: Week-by-week SHADE adjustment based on the back and offensive tendencies

---

## 3-DOWN PACKAGES (MINT / ACE / JET / SLIP)

### Common Rules
- Field OLB = B. Boundary OLB = E.
- T/N may swap by personnel.
- Slice rule: backside OLB has slicer.
- Strength = Field.

### ILB Fits (Locked)
- Play-to-field: M stacks behind B, inside-out. W stacks behind E.
- Play-away: M/W slow-play A gap (patient shuffle, hunt cutback).

### CAMP QB Player (3-Down)
- Universal rule: whoever has contain has the QB.
- Mint/Ace: B is contain (A is inside at 4i/4). In zone coverage (MINT only), M has contain awareness.
- Jet/Slip: A has contain (A is at 5-tech).

### MINT (4i / 0 / 4i)
- Signal: "M" on thigh
- A=4i, T=0, N=4i. B/E = OLBs.
- Contain: Man (C0/C1) = B. NINJA/VIKING (MINT only) = M is QB contain.
- **MINT + zone contain technique:** On QB run read, M scrapes over the top to the C gap. If A (at 4i) gets washed inside, M becomes the edge player. M does NOT sit in his gap — he must get outside A's alignment on QB keep.

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
- 1-gap penetrating. A and E are contain. M = B gap field. W = A gap boundary.
- Stunts are legal with SLIP (e.g., ANGLE). On stunts, T at 0 goes to slip-side A gap.
- Use: 3-down vs spread with NINJA or VIKING. Takes B out of conflict — B plays coverage clean.

### Contain Matrix
| Package + Coverage | Contain |
|--------------------|---------|
| MINT + Man (C0/C1) | B |
| MINT + NINJA/VIKING | M is QB contain |
| ACE/JET + Man | B |
| ACE/JET + NINJA/VIKING | B contain-first, then match on pass read |
| SLIP + Man (C0/C1) | A and E (B plays coverage clean) |
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
- With BOSS: 1-tech crosses C face to opposite A. With BOSS UNDER: same concept, boundary side. With GRIZZLY: field gap-out.
- A and E contain. Looks weird with BOSS but plays like Shade. Best: Mike, sWarM.
- **SPLIT is only legal with BOSS, BOSS UNDER, and GRIZZLY.** Not called with other fronts.

### ANCHOR ATTACK
- A attacks OL closing one inside gap (washes OL inside). NOT paired with Cobra.
- Best fronts: Under, Eyes, Boss Under, Shade (with Pinch or Angle).

### EDGE ATTACK
- E attacks OL closing one inside gap. CAN pair with Cobra.
- Best fronts: Shade, Eyes, Boss, Under (with Pinch or Slant).

### CRASH
- A+E shoot B gaps. T+N shoot A gaps. B = field contain (replaces A). W = boundary contain (replaces E). M = free LB (no TE); M takes C gap to TE/Y-off/H side (TE present).
- NOT with Grizzly or Freebird. Best fronts: Wide, Shade, Under. Best paired with Zorro (B/M swap alignments so B has RB on pass). Best pressure: BoW.
- **CRASH + Zorro CAMP exception:** M takes field contain (and therefore the QB per CAMP). B keys the RB from ~8 yds middle. W has boundary contain. This is the only CRASH pairing where B does NOT have field contain.

### ANCHOR RAVEN (A 5→B)
- A shoots B gap from 5. Signal: point field → flap flap.
- Not with Hammer or staB. If + Bandit = BANDIT RAVEN.

### EDGE RAVEN (E 5→B)
- E shoots B gap from 5. Signal: point boundary → flap flap.

### VEER (Slant to Motion / Slant to TE)
- Two variants: (1) DL slants toward the motion, (2) DL slants toward the TE.
- 4-down: T+N slant. 3-down: A+T+N slant.
- Reactive stunt — direction determined by offensive alignment/motion.

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
- **Freebird** — Cover 1 only. The post safety per the coverage variant blitzes (Oregon = FS, Oklahoma = D, Ohio = B). Remaining players adjust to Cover 1 distribution minus the blitzer.
- **Cobra** — Cobra + Zunnel only. Two-high shell pre-snap, hash-only call. BC blitzes as 6th rusher. D rotates to #1 boundary. B aligns at Zorro depth but takes #2 boundary. FS takes #2 field. M/W funnel RB (Zunnel rules). **Cobra requires B in coverage — cannot pair with any pressure that sends B.**

### Combination Pressures
| Call | Who Blitzes |
|------|-------------|
| sWarM | M + W |
| BooM | B + M |
| BoW | B + W |
| MaD | M + D |
| Eat | M + W + B |

**Pressure + Coverage Legality Rules:** sWarM + Cover 1 is NOT LEGAL (sends both RB funnel players). BooM (B+M) in Cover 1: W takes RB solo (no funnel). **BoW + Cover 1: NOT LEGAL** (B has #2 field — blitzing leaves #2 uncovered). **BoW + Zeus: NOT LEGAL** (B, W, M all rush — RB unaccounted). Use BoW with Cover 0 family only (Zike is standard call — M has RB). **Eat is Cover 0 family only** — all second-level players rush, defenders play Z-family assignments hot. NOT LEGAL with NINJA, Cover 1, or Viking.

### Packaged Pressures (Married to Stunts)
- **Hammer** — B edge blitz + Anchor Attack (A washes OL inside, creating edge for B)
- **Shave** — W edge blitz + Edge Attack (E attacks OL)
- **Bandit Raven** — B blitzes C gap, A shoots B gap
- **Will Raven** — W blitzes C gap, E shoots B gap

### Weekly Called Pressures (Locked Friday Menu)
Mike, Will, Bandit, sWarM, BooM, BoW, Hammer, Eat.
Zeus/Z-family featured separately.

### MUG (Alignment Tag)
M and/or W walk up to the LOS at their pre-snap gap assignment. Responsibilities do not change — same gap fit, same coverage drop, same read keys. Mug changes the pre-snap picture only.
- **MUG** — both M and W walk up to their gap.
- **M MUG** — only M walks up.
- **W MUG** — only W walks up.
- Pre-snap gap is front-dependent (SHADE: M=A field, W=B boundary; UNDER: M=B field, W=A boundary; etc.).
- In Zeus, Mug is natural — M is already an add-on rusher on pass read.
- Do NOT tip blitz vs Mug. The offense should not be able to tell the difference pre-snap.

### Game-Plan Specials (Not Weekly)
Dawg, MaD, Shave, Freebird, Cobra, staB — available in the playbook but only installed for specific game plans.

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
- Poach destination: 10-12 yds deep, splitting #2/#3 trips side. Do not drift past far hash.
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
- **Empty (3x2):** Field = MOD (FC/#1, FS/#2, B/#3). Boundary = CLAMP (BC/#1, D/#2). M/W = hook zone.
- **Empty (2x3):** FS becomes poach on bnd #3. Field = MOD with 2. D top-down on #2 bnd.
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

### Cover 1 vs Trips (3x1)
B always takes #3 trips side. Assignments vary by variant:
- Oregon (trips field): FC=#1, D=#2, B=#3. (Trips bnd): BC=#1, D=#2, B=#3.
- Oklahoma (trips field): FC=#1, FS=#2, B=#3. (Trips bnd): BC=#1, FS=#2, B=#3.
- Ohio (trips field): FC=#1, FS=#2, D=#3. (Trips bnd): BC=#1, D=#2, FS=#3.

### Cover 1 Bunch/Stack Rules
**Bunch (3-man, Cover 1):** Corner = first OUT (6 yds outside leverage). B = first IN / 3rd OUT. Cover safety = 8-9 yds, second IN/OUT/middle.
**Stack (2-man, Cover 1):** Corner + whoever has #2 per CAMP sort IN/OUT.
**Bunch (3-man, Cover 0):** Corner = first OUT / 3rd IN. FS = 8-9 yds second IN/OUT/middle. D = first IN / 3rd OUT.
**Stack (2-man, Cover 0):** First IN / first OUT with corner and safety.
EXCHANGE on contact (rub/pick).

### ZORRO — EXCEPTION
B aligns at ~8 yds deep in the middle of the formation to key the RB (not at apex). Changes pre-snap look.

---

## COVERAGE: COVER 0 / Z-FAMILY

All Z-calls = Cover 0. No deep safety help.

### CAMP DB Rules (0-Family)
- FC: man #1 field. BC: man #1 boundary.
- FS: man #2 field (or #3 away). D: man #2 boundary (or #3 away).

### Z-Family Trips Rules (3x1)
Safeties handle #2/#3 to trips side: nearest safety takes #2, far safety rotates to #3. B's role does not change (per Z-call). Backside safety takes #1 backside if not rotating to trips.

### Universal Tags
- **TAMPA:** 2nd-level players become droppers/RAT.
- **SPY:** Tagged player spies QB.

### ZEUS (Run-First / Pass-Read Delayed Pressure)
**All second-level players (M, B, W) are RUN-FIRST.** They play their run fit until they read pass, then execute their pass assignment.
- A & E: Cage/contain. T & N: Vertical push / collapse pocket.
- M: Read key = guard. Run = fit gap. Pass = add-on rusher.
- B: Read key = EMOL. Run = fit gap. Pass = RB funnel (RB to you → take; away → rush).
- W: Read key = guard. Run = fit gap. Pass = RB funnel (RB to you → take; away → rush; middle → W takes).
- PA rule: max 2 steps downhill before reading pass.

**Call-off:** After showing Zeus 1-3 times, bail to NINJA or VIKING.

### ZORRO
- B has RB. M/W no pass responsibility unless tagged (TAMPA = droppers, SPY = spy QB).

### ZUNNEL
- M and W funnel RB. RB to your side → take. Away → rush. TAMPA: away = RAT.
- **B: Green-light rusher.** No pass responsibility. M/W handle the RB, freeing B to rush on any pass read.

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

**Tags:**
- VIKING SEAM: Curl/flat player carries #2 vertical to deep-third defender, passes off, settles in curl zone.
- VIKING PUSH (trips): B/D widens to #3 flat. M/W slides to replace vacated curl zone. Deep 3 unchanged.
- VIKING CROSS: Curl/flat player carries crosser to 12 yds, hands off to hook player (M/W).
- VIKING SCREEN: DL yells "SCREEN!" and redirects. Curl/flat player attacks screen — primary tackler. LBs rally.

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

### UNDER (On-Field Alert — Z-Family Only)
- Trigger: receiver runs UNDER to pick RB-responsible defender AND RB releases fast out.
- Rule: RB player takes UNDER (replaces pick). UNDER defender takes RB (swap).
- Call: "UNDER! UNDER!" (no numbers). Fixer safety calls it.
- Cover 1 uses EXCHANGE instead (man coverage).
- RB player by Z-call: Zeus = B or W. Zorro = B. Zunnel = M or W. Zill = W. Zike = M.

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
- General: Gap responsibility is based on the package. Play-away = slow-play, hunt cutback.
- MINT: M/W = A gap (away from RB). In zone coverage, M has contain awareness.
- ACE: React to DL 2-gap (tabled: define DL play first).
- JET: M = B gap field, W = B gap boundary.
- SLIP: M = B gap field, W = A gap boundary.

---

## CALL GRAMMAR & SIGNALS

**Order:** Front + Stunt + Blitz + Coverage/Tags

**Examples:**
- UNDER + SLANT + BoW + ZIKE
- GRIZZLY + sWarM + ZORRO
- GRIZZLY + SPLIT + Mike + ZEUS
- BOSS + SPLIT + Cobra + ZEUS
- ZEUS (show) → call-off to NINJA/VIKING

### Signals
- MINT: "M" on thigh. ACE: 1 finger up. JET: whoosh forward.
- Anchor Raven: point field → flap flap. Edge Raven: point boundary → flap flap.
- Grammar: front sign, then stunt sign.

### Communication
Front/stunt/blitz calls are signaled — coverage is verbal. Signals taught during install. Safeties echo and relay.

### Tempo Default
When the offense's tempo is faster than we can signal our plays in, the defense defaults to the **tempo call** — set before each possession. Default: SHADE + NINJA. We can change the tempo call at any point during the game. Safeties must know the current tempo call at all times.

---

## DEFERRED / PENDING ITEMS
- ~~Viking fire zone~~ — dropped (pressure packages cover this)
- ~~Install plan~~ — completed (Section 24, 10 camp days + Friday sessions)
- DL technique appendix — hand placement, pass-rush moves, stunt timing (deferred to position coaches)
- DB technique appendix — press technique, bail footwork, off-man reads (deferred to position coaches)
- Blitz/pressure drill progressions
- Viking Tags detail — come back with diagrams
- Dawg/MaD/Shave philosophy — tabled
- Unbalanced/Quads detail — refine with diagrams
- ACE DL 2-gap play — tabled (define before LB fits)
- Split Zone depth — tabled

## COMPLETED SECTIONS (in MD playbook)
- Section 18: Formation Recognition & Adjustment Rules
- Section 19: Personnel Grouping ID
- Section 20: Pressure Cards (Rush/Drop Assignments) — all pressures × all coverages
- Section 21: Front-Stunt Legality Matrix
- Section 22: Run Scheme Specifics (IZ, OZ, Power, Counter, Draw, QB Run, Jet Sweep, Split Zone)
- Section 23: Situational Defense (3rd down, red zone, goal line, 2-min, backed up, 4-min)
- Section 24: Camp Install Plan (10 Days)
- Section 25: Game-Day Call Sheet Template
- Section 26: Quick-Reference Cards (M/W Gap Fit, NINJA Teaching, Coverage Family, Bandit Assignment)
- Section 27: Option Defense Appendix
