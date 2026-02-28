# Run-Fit Diagram Redesign

## Summary
Generate 12 landscape .docx files (one per front) showing every defender's run-fit responsibility on every diagram. Base fronts shown against all 9 formations. Each legal stunt shown against 2x2.

## Visual Language
- **Solid line + arrow** = DL stunt movement or LB/DB blitz path
- **Dotted line, no arrow** = gap fit (every non-moving player, including secondary)
- Line colors match player circle color (navy=DL, columbia blue=LB, gold=safety)
- Red solid arrows for DL stunt movement

## Document Structure
- 12 documents, one per front
- Landscape orientation, one diagram per page
- Each doc: title page, base alignment section (9 formations), stunts section (legal stunts vs 2x2)

## Formations (9 total)
1. 2x2 Spread (10 pers)
2. 3x1 Trips Field (10 pers)
3. 3x1 Trips Boundary (10 pers)
4. 2x2 + TE Field (11 pers)
5. 2x2 + TE Boundary (11 pers)
6. Empty 3x2 (10 pers)
7. Empty 2x3 (10 pers)
8. 21 Personnel I-Form TE Field
9. 22 Personnel Heavy 2 TE

## TE Handling
- No TE SET logic. Front alignment stays as-is regardless of TE.
- B moves from apex to LB depth on field side when TE present.

## Gap Fit Lines
- Gap letters (A, B, C) labeled between OL at LOS
- Each non-moving defender gets a dotted line to their assigned gap
- Secondary shows run fit: FC/BC = force/alley, FS = alley field, D = force/alley boundary
- Edges (A/E) with contain = dotted line to outside C gap

## 4-Down Stunt Legality (vs 2x2 only)
| Stunt | SHADE | UNDER | EYES | WIDE | DEUCES | GRIZZLY | BOSS | BOSS UNDER |
|-------|-------|-------|------|------|--------|---------|------|------------|
| SLANT | - | BEST | OK | OK | OK | OK | OK | BEST |
| ANGLE | BEST | - | OK | OK | OK | OK | BEST | - |
| PINCH | BEST | BEST | OK | BEST | BEST | OK | OK | OK |
| JACKS | BEST | BEST | BEST | - | OK | OK | OK | OK |
| SPLIT | - | - | - | - | - | BEST | BEST | BEST |
| CRASH | BEST | BEST | OK | BEST | OK | - | OK | OK |
| ANCHOR ATTACK | OK | OK | OK | OK | OK | OK | OK | OK |
| EDGE ATTACK | OK | OK | OK | OK | OK | OK | OK | OK |
| ANCHOR RAVEN | OK | OK | OK | OK | OK | OK | OK | OK |
| EDGE RAVEN | OK | OK | OK | OK | OK | OK | OK | OK |

## 3-Down Stunt Variants
| Stunt | Mechanic | MINT | ACE | JET | SLIP |
|-------|----------|------|-----|-----|------|
| SLANT | A+T+N slant field | Y | Y | Y | - |
| ANGLE | A+T+N slant bnd | Y | Y | Y | Y |
| PINCH | A+N pinch B gaps | Y | Y | Y | - |
| JACKS | A+N expand C gaps | Y | Y | Y | - |
| ANCHOR ATTACK | A washes inside | Y | Y | Y | - |
| ANCHOR RAVEN | A shoots B gap | Y | Y | Y | - |

## Estimated Diagram Counts
| Front | Base (9) | Stunts | Total |
|-------|----------|--------|-------|
| SHADE | 9 | 9 | 18 |
| UNDER | 9 | 9 | 18 |
| EYES | 9 | 10 | 19 |
| WIDE | 9 | 8 | 17 |
| DEUCES | 9 | 9 | 18 |
| GRIZZLY | 9 | 9 | 18 |
| BOSS | 9 | 9 | 18 |
| BOSS UNDER | 9 | 9 | 18 |
| MINT | 9 | 6 | 15 |
| ACE | 9 | 6 | 15 |
| JET | 9 | 6 | 15 |
| SLIP | 9 | 1 | 10 |
| **Total** | **108** | **91** | **~199** |
