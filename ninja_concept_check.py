#!/usr/bin/env python3
"""Generate NINJA coverage check diagrams vs comprehensive pass concepts.
Shows MOD (field) / CLAMP (boundary) assignments with updated rules.
"""

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT_DIR = "/tmp/ninja_concept_check"
os.makedirs(OUT_DIR, exist_ok=True)

# Colors
C_NAVY = "#002D62"
C_COLUMBIA = "#6CACE4"
C_GOLD = "#CFA700"
C_GRAY = "#888888"
C_OL = "#AAAAAA"
C_WR = "#666666"
C_WHITE = "#FFFFFF"
C_ROUTE = "#CC3333"
C_DEF_ARROW = "#0066CC"  # Blue arrows for defensive drops/assignments

# Y positions
Y_LOS = 0
Y_DL = 1.2
Y_LB = 3.5
Y_APEX = 3.0
Y_CB = 5.5
Y_S = 8.0

OL_POSITIONS = [(0, 0), (2, 0), (-2, 0), (4, 0), (-4, 0)]


def new_fig(title="", figsize=(12, 9)):
    fig, ax = plt.subplots(1, 1, figsize=figsize)
    ax.set_xlim(-17, 17)
    ax.set_ylim(-5.5, 14)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.axhline(y=0.5, color=C_GRAY, linewidth=1, linestyle="--", alpha=0.3)
    ax.text(15, 13, "FIELD →", fontsize=8, color=C_GRAY, ha="right", va="top", style="italic")
    ax.text(-15, 13, "← BOUNDARY", fontsize=8, color=C_GRAY, ha="left", va="top", style="italic")
    if title:
        ax.set_title(title, fontsize=13, fontweight="bold", color=C_NAVY, pad=10)
    return fig, ax


def draw_ol(ax):
    for x, y in OL_POSITIONS:
        ax.add_patch(plt.Rectangle((x - 0.4, y - 0.4), 0.8, 0.8,
                     fill=True, facecolor=C_OL, edgecolor="#555", linewidth=1.5))


def off_player(ax, x, y, label):
    ax.plot(x, y, "s", color=C_WR, markersize=8, markeredgecolor="#333")
    ax.text(x, y - 0.8, label, fontsize=6, ha="center", color="#555")


def def_player(ax, x, y, label, color=C_NAVY, fontsize=8):
    ax.plot(x, y, "o", color=color, markersize=14, markeredgecolor=C_NAVY, markeredgewidth=1.2)
    ax.text(x, y, label, fontsize=fontsize, ha="center", va="center",
            color=C_WHITE, fontweight="bold")


def route(ax, points):
    """Offensive route: dashed red line with arrowhead."""
    for i in range(len(points) - 1):
        if i < len(points) - 2:
            ax.plot([points[i][0], points[i + 1][0]],
                    [points[i][1], points[i + 1][1]],
                    "--", color=C_ROUTE, lw=1.5, alpha=0.8)
        else:
            ax.annotate("", xy=points[i + 1], xytext=points[i],
                        arrowprops=dict(arrowstyle="-|>", color=C_ROUTE, lw=1.5, linestyle="dashed"))


def def_arrow(ax, x1, y1, x2, y2):
    """Defensive assignment arrow: solid blue."""
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="-|>", color=C_DEF_ARROW, lw=1.5))


def def_curved(ax, x1, y1, x2, y2, rad=0.3):
    """Defensive curved assignment arrow."""
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="-|>", color=C_DEF_ARROW, lw=1.5,
                                connectionstyle=f"arc3,rad={rad}"))


def rlbl(ax, x, y, text):
    ax.text(x, y, text, fontsize=6.5, ha="center", color=C_ROUTE, style="italic")


def dlbl(ax, x, y, text):
    """Defender assignment label."""
    ax.text(x, y, text, fontsize=6.5, ha="center", color=C_DEF_ARROW, style="italic",
            bbox=dict(boxstyle="round,pad=0.15", facecolor="white", edgecolor=C_DEF_ARROW, alpha=0.8, linewidth=0.5))


def note(ax, text):
    """Bottom note."""
    ax.text(0, -5, text, fontsize=8.5, ha="center", color=C_NAVY, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.3", facecolor=C_COLUMBIA, alpha=0.15))


def save(fig, name):
    path = os.path.join(OUT_DIR, f"{name}.png")
    fig.savefig(path, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return path


def base_offense(ax):
    """Draw OL, QB, RB, 2x2 WRs."""
    draw_ol(ax)
    off_player(ax, 0, -1.5, "QB")
    off_player(ax, 0, -3, "RB")
    off_player(ax, 13, 0, "#1 F")
    off_player(ax, 7, 0, "#2 F")
    off_player(ax, -13, 0, "#1 B")
    off_player(ax, -7, 0, "#2 B")


def ninja_def(ax):
    """NINJA pre-snap: MOD field / CLAMP boundary."""
    # DL
    def_player(ax, 4.7, Y_DL, "A")
    def_player(ax, 2.5, Y_DL, "T")
    def_player(ax, -1.5, Y_DL, "N")
    def_player(ax, -4.7, Y_DL, "E")
    # LBs
    def_player(ax, 1.5, Y_LB, "M", color=C_COLUMBIA)
    def_player(ax, -1.5, Y_LB, "W", color=C_COLUMBIA)
    # B at apex
    def_player(ax, 7.5, Y_APEX, "B", color=C_COLUMBIA)
    # DBs
    def_player(ax, 12, Y_CB, "FC", color=C_COLUMBIA)
    def_player(ax, -12, Y_CB, "BC", color=C_COLUMBIA)
    def_player(ax, 5, Y_S, "FS", color=C_GOLD)
    def_player(ax, -5, Y_S, "D", color=C_GOLD)


# ============================================================
# CONCEPT DIAGRAMS
# ============================================================

def gen_four_verts():
    fig, ax = new_fig("NINJA vs FOUR VERTICALS")
    base_offense(ax)
    # Routes: all 4 go vertical
    route(ax, [(13, 0), (13, 12)])
    route(ax, [(7, 0), (7, 12)])
    route(ax, [(-13, 0), (-13, 12)])
    route(ax, [(-7, 0), (-7, 12)])
    route(ax, [(0, -3), (3, -1)])  # RB check
    rlbl(ax, 14, 6, "Go")
    rlbl(ax, 8, 6, "Seam")
    rlbl(ax, -14, 6, "Go")
    rlbl(ax, -8, 6, "Seam")
    rlbl(ax, 4, -1.5, "Check")

    ninja_def(ax)
    # MOD field: FC matches #1, FS reads #2 vert → matches, B pushes #2 vert
    dlbl(ax, 13.5, Y_CB + 1.5, "FC: match #1\nstay on top")
    dlbl(ax, 6, Y_S + 1.5, "FS: #2 vert\n→ match #2")
    dlbl(ax, 9, Y_APEX + 1.5, "B: push #2\ncarry seam")
    # CLAMP bnd: D reads #2 vert → matches, BC stays on #1
    dlbl(ax, -6, Y_S + 1.5, "D: #2 vert\n→ match #2")
    dlbl(ax, -13.5, Y_CB + 1.5, "BC: stay on #1")
    dlbl(ax, -2.5, Y_LB + 1.5, "W: hook/curl\n#3 (RB)")
    dlbl(ax, 2.5, Y_LB + 1.5, "M: hook\nrelate")

    note(ax, "TWO-HIGH CAPS ALL 4 SEAMS — FS matches #2F seam, D matches #2B seam. Best zone look vs 4 verts.")
    return save(fig, "ninja_vs_4verts")


def gen_mesh():
    fig, ax = new_fig("NINJA vs MESH / CROSSERS")
    base_offense(ax)
    # Routes: #1F shallow cross going bnd, #1B shallow cross going field
    route(ax, [(13, 0), (12, 3), (5, 5), (-2, 5)])
    route(ax, [(-13, 0), (-12, 3), (-5, 5), (2, 5)])
    # #2s run vertical/outs
    route(ax, [(7, 0), (7, 8)])
    route(ax, [(-7, 0), (-7, 8)])
    route(ax, [(0, -3), (3, -1)])
    rlbl(ax, 3, 5.8, "Cross")
    rlbl(ax, -3, 5.8, "Cross")
    rlbl(ax, 8, 5, "Seam")
    rlbl(ax, -8, 5, "Seam")

    ninja_def(ax)
    dlbl(ax, 13.5, Y_CB + 1.5, "FC: #1 short\nzone off")
    dlbl(ax, 6, Y_S + 1.5, "FS: #2 vert\n→ match #2")
    dlbl(ax, 9, Y_APEX + 1.5, "B: push #2\ncarry seam")
    dlbl(ax, -6, Y_S + 1.5, "D: #2 vert\n→ match #2")
    dlbl(ax, -13.5, Y_CB + 1.5, "BC: #1 short\nstay on #1")
    dlbl(ax, 2.5, Y_LB + 1.5, "M: CROSS!\ncarry deeper")
    dlbl(ax, -2.5, Y_LB + 1.5, "W: hook/curl\n#3 (RB)")

    note(ax, "M CARRIES THE CROSSER — calls 'CROSS!', W stays on #3. Zone pass-offs handle picks naturally.")
    return save(fig, "ninja_vs_mesh")


def gen_smash():
    fig, ax = new_fig("NINJA vs SMASH (Corner / Hitch)")
    base_offense(ax)
    # Field side smash: #1 hitch, #2 corner
    route(ax, [(13, 0), (13, 5)])  # hitch
    rlbl(ax, 14.5, 4, "Hitch")
    route(ax, [(7, 0), (7, 4), (10, 9)])  # corner
    rlbl(ax, 11.5, 9, "Corner")
    # Boundary side smash: #1 hitch, #2 corner
    route(ax, [(-13, 0), (-13, 5)])
    rlbl(ax, -14.5, 4, "Hitch")
    route(ax, [(-7, 0), (-7, 4), (-10, 9)])
    rlbl(ax, -11.5, 9, "Corner")
    route(ax, [(0, -3), (3, -1)])

    ninja_def(ax)
    # MOD field: FC on #1 hitch, FS reads #2 vert (corner = vertical-ish) → matches
    dlbl(ax, 14.5, Y_CB + 1.5, "FC: match #1\nsit on hitch")
    dlbl(ax, 6, Y_S + 1.5, "FS: #2 vert\n→ match corner")
    dlbl(ax, 9, Y_APEX + 1.5, "B: push #2\nif corner, under")
    # CLAMP bnd: BC reads #2. #2 goes vertical (corner route) → BC stays on #1, D matches #2
    dlbl(ax, -6, Y_S + 1.5, "D: #2 vert\n→ match corner")
    dlbl(ax, -14.5, Y_CB + 1.5, "BC: #2 vert\n→ stay on #1")
    dlbl(ax, 2.5, Y_LB + 1.5, "M: hook\nrelate")
    dlbl(ax, -2.5, Y_LB + 1.5, "W: hook/curl\n#3 (RB)")

    note(ax, "FS/D MATCH CORNER ROUTE — corner route is vertical, so safety matches. CB sits on hitch. No conflict.")
    return save(fig, "ninja_vs_smash")


def gen_flood():
    fig, ax = new_fig("NINJA vs FLOOD / SAIL (3-Level, Field Side)")
    base_offense(ax)
    # Field side flood: #1 go/corner deep, #2 out/dig intermediate, RB flat
    route(ax, [(13, 0), (13, 5), (11, 10)])  # #1 corner/go
    rlbl(ax, 12.5, 10, "Corner")
    route(ax, [(7, 0), (7, 5), (10, 6)])  # #2 out
    rlbl(ax, 11.5, 6, "Out")
    route(ax, [(0, -3), (5, -1), (10, 1)])  # RB flat
    rlbl(ax, 11, 0.5, "Flat")
    # Boundary: #1 and #2 run clears
    route(ax, [(-13, 0), (-13, 8)])
    route(ax, [(-7, 0), (-7, 6)])
    rlbl(ax, -14, 6, "Clear")
    rlbl(ax, -8, 5, "Clear")

    ninja_def(ax)
    dlbl(ax, 14.5, Y_CB + 1.5, "FC: match #1\nstay on top")
    dlbl(ax, 6, Y_S + 1.5, "FS: #2 out\n→ high hole")
    dlbl(ax, 9.5, Y_APEX + 1.5, "B: #2 out\ndrives flat/RB")
    dlbl(ax, -6, Y_S + 1.5, "D: #2 vert\nmatch")
    dlbl(ax, -14, Y_CB + 1.5, "BC: stay #1")
    dlbl(ax, 2.5, Y_LB + 1.5, "M: hook\nrelate out")
    dlbl(ax, -2.5, Y_LB + 1.5, "W: hook/curl\n#3")

    note(ax, "3-LEVEL STRETCH — FS reads #2 out → robs #1 corner. B drives flat. FC stays on top. RB flat = B's job.")
    return save(fig, "ninja_vs_flood")


def gen_levels():
    fig, ax = new_fig("NINJA vs LEVELS (Hi-Lo Crossers)")
    base_offense(ax)
    # #2F runs shallow drag (5 yds)
    route(ax, [(7, 0), (5, 4), (-3, 4)])
    rlbl(ax, -4, 3.3, "Drag (5)")
    # #1F runs dig (12 yds)
    route(ax, [(13, 0), (13, 8), (5, 8)])
    rlbl(ax, 4, 8.7, "Dig (12)")
    # Boundary clears
    route(ax, [(-13, 0), (-13, 8)])
    route(ax, [(-7, 0), (-7, 6)])
    rlbl(ax, -14, 6, "Clear")
    rlbl(ax, -8, 5, "Clear")
    route(ax, [(0, -3), (3, -1)])

    ninja_def(ax)
    dlbl(ax, 14, Y_CB + 1.5, "FC: #1 short\nzone off deep")
    dlbl(ax, 6, Y_S + 1.5, "FS: #2 under\n→ high hole\nrobs dig")
    dlbl(ax, 9, Y_APEX + 1.5, "B: #2 drag\ncarry under")
    dlbl(ax, -6, Y_S + 1.5, "D: #2 vert\nmatch")
    dlbl(ax, -14, Y_CB + 1.5, "BC: stay #1")
    dlbl(ax, 2.5, Y_LB + 1.5, "M: CROSS!\ncarry drag")
    dlbl(ax, -2.5, Y_LB + 1.5, "W: hook/curl\n#3 (RB)")

    note(ax, "HI-LO READ — FS reads #2 under → works to high hole, robs dig. M carries the drag. No conflict.")
    return save(fig, "ninja_vs_levels")


def gen_curl_flat():
    fig, ax = new_fig("NINJA vs CURL / FLAT")
    base_offense(ax)
    # Field: #1 curl, #2 flat
    route(ax, [(13, 0), (13, 8), (12, 7)])  # curl
    rlbl(ax, 13.5, 8.5, "Curl")
    route(ax, [(7, 0), (10, 2)])  # flat
    rlbl(ax, 11, 1.5, "Flat")
    # Boundary: #1 curl, #2 flat
    route(ax, [(-13, 0), (-13, 8), (-12, 7)])
    rlbl(ax, -13.5, 8.5, "Curl")
    route(ax, [(-7, 0), (-10, 2)])
    rlbl(ax, -11, 1.5, "Flat")
    route(ax, [(0, -3), (3, -1)])

    ninja_def(ax)
    # MOD: FC on curl, FS reads #2 out → high hole/rob curl, B drives flat
    dlbl(ax, 14.5, Y_CB + 1.5, "FC: match #1\nsit on curl")
    dlbl(ax, 6, Y_S + 1.5, "FS: #2 out\n→ high hole\nrob curl")
    dlbl(ax, 9, Y_APEX + 1.5, "B: #2 out\ndrives flat")
    # CLAMP: BC reads #2. #2 goes out → BC jumps flat, D takes #1
    dlbl(ax, -6, Y_S + 1.5, "D: #2 out\n→ flip to #1\ncovers curl")
    dlbl(ax, -14, Y_CB + 1.5, "BC: #2 out\n→ JUMP flat")
    dlbl(ax, 2.5, Y_LB + 1.5, "M: hook\nrelate")
    dlbl(ax, -2.5, Y_LB + 1.5, "W: hook/curl\n#3 (RB)")

    note(ax, "NO CURL-FLAT CONFLICT — MOD: B drives flat, FS robs curl. CLAMP: BC jumps #2 flat, D flips to #1 curl.")
    return save(fig, "ninja_vs_curl_flat")


def gen_slant_flat():
    fig, ax = new_fig("NINJA vs SLANT / FLAT")
    base_offense(ax)
    # Field: #1 slant, #2 flat
    route(ax, [(13, 0), (10, 4)])
    rlbl(ax, 9, 4.5, "Slant")
    route(ax, [(7, 0), (10, 2)])
    rlbl(ax, 11, 1.5, "Flat")
    # Boundary: #1 slant, #2 flat
    route(ax, [(-13, 0), (-10, 4)])
    rlbl(ax, -9, 4.5, "Slant")
    route(ax, [(-7, 0), (-10, 2)])
    rlbl(ax, -11, 1.5, "Flat")
    route(ax, [(0, -3), (3, -1)])

    ninja_def(ax)
    dlbl(ax, 14.5, Y_CB + 1.5, "FC: inside lev\nmatch slant")
    dlbl(ax, 6, Y_S + 1.5, "FS: #2 out\n→ high hole")
    dlbl(ax, 9, Y_APEX + 1.5, "B: #2 out\ndrives flat")
    dlbl(ax, -6, Y_S + 1.5, "D: #2 out\n→ flip to #1")
    dlbl(ax, -14, Y_CB + 1.5, "BC: #2 out\n→ JUMP flat")
    dlbl(ax, 2.5, Y_LB + 1.5, "M: hook\nrelate slant")
    dlbl(ax, -2.5, Y_LB + 1.5, "W: hook/curl\n#3 (RB)")

    note(ax, "INSIDE LEVERAGE KILLS SLANT — FC in inside leverage matches slant. B drives flat. CLAMP: BC jumps #2 flat.")
    return save(fig, "ninja_vs_slant_flat")


def gen_stick():
    fig, ax = new_fig("NINJA vs STICK (3-Level Quick)")
    base_offense(ax)
    # Field: #1 stick (6 yds settle), #2 flat, RB vert push
    route(ax, [(13, 0), (11, 5)])  # stick
    rlbl(ax, 10, 5.5, "Stick (6)")
    route(ax, [(7, 0), (10, 2)])  # flat
    rlbl(ax, 11, 1.5, "Flat")
    route(ax, [(0, -3), (2, 0), (3, 5)])  # RB vert push
    rlbl(ax, 4, 5, "RB push")
    # Boundary clears
    route(ax, [(-13, 0), (-13, 8)])
    route(ax, [(-7, 0), (-7, 6)])
    rlbl(ax, -14, 6, "Clear")
    rlbl(ax, -8, 5, "Clear")

    ninja_def(ax)
    dlbl(ax, 14.5, Y_CB + 1.5, "FC: match #1\nrally to stick")
    dlbl(ax, 6, Y_S + 1.5, "FS: #2 out\n→ high hole\nrob stick")
    dlbl(ax, 9, Y_APEX + 1.5, "B: #2 out\ndrives flat")
    dlbl(ax, -6, Y_S + 1.5, "D: #2 vert\nmatch")
    dlbl(ax, -14, Y_CB + 1.5, "BC: stay #1")
    dlbl(ax, 2.5, Y_LB + 1.5, "M: hook\nrelate stick")
    dlbl(ax, -2.5, Y_LB + 1.5, "W: hook/curl\nRB push")

    note(ax, "3-LEVEL COVERED — FC on stick, B drives flat, W takes RB push (#3). FS robs from high hole.")
    return save(fig, "ninja_vs_stick")


def gen_rpo():
    fig, ax = new_fig("NINJA vs RPO (Bubble / Now Screen)")
    base_offense(ax)
    # Field: #2 runs bubble/now screen, #1 blocks or go
    route(ax, [(13, 0), (13, 8)])  # #1 go
    rlbl(ax, 14, 5, "Go/Block")
    route(ax, [(7, 0), (9, 1)])  # bubble
    rlbl(ax, 10.5, 1.5, "Bubble")
    # Boundary: normal
    route(ax, [(-13, 0), (-13, 6)])
    route(ax, [(-7, 0), (-7, 6)])
    # RB run fake
    ax.annotate("", xy=(2, -2), xytext=(0, -3),
                arrowprops=dict(arrowstyle="-|>", color=C_ROUTE, lw=1.5, linestyle="dashed"))
    rlbl(ax, 3.5, -2.5, "Run fake")

    ninja_def(ax)
    dlbl(ax, 14, Y_CB + 1.5, "FC: match #1\nif go, on top")
    dlbl(ax, 6, Y_S + 1.5, "FS: #2 out\n→ high hole")
    dlbl(ax, 9, Y_APEX + 1.5, "B: #2 bubble\nDRIVE ON IT")
    dlbl(ax, -6, Y_S + 1.5, "D: #2 vert\nmatch")
    dlbl(ax, -14, Y_CB + 1.5, "BC: stay #1")
    dlbl(ax, 2.5, Y_LB + 1.5, "M: read\ndon't bite run")
    dlbl(ax, -2.5, Y_LB + 1.5, "W: hook/curl\n#3")

    note(ax, "B IS THE KEY — B covers down on #2. If #2 runs bubble, B drives on it immediately. M must NOT bite on run fake.")
    return save(fig, "ninja_vs_rpo")


def gen_double_post():
    fig, ax = new_fig("NINJA vs DOUBLE POST")
    base_offense(ax)
    # Both #1s run post routes
    route(ax, [(13, 0), (13, 5), (8, 10)])
    rlbl(ax, 7, 10.5, "Post")
    route(ax, [(-13, 0), (-13, 5), (-8, 10)])
    rlbl(ax, -7, 10.5, "Post")
    # #2s run under/out
    route(ax, [(7, 0), (7, 5)])
    rlbl(ax, 8, 4, "Seam/In")
    route(ax, [(-7, 0), (-7, 5)])
    rlbl(ax, -8, 4, "Seam/In")
    route(ax, [(0, -3), (3, -1)])

    ninja_def(ax)
    dlbl(ax, 14, Y_CB + 1.5, "FC: match #1\nstay on post")
    dlbl(ax, 6, Y_S + 1.5, "FS: #2 vert\n→ match #2\nOR high hole\ncaps post")
    dlbl(ax, 9, Y_APEX + 1.5, "B: push #2\nmatch")
    dlbl(ax, -6, Y_S + 1.5, "D: #2 vert\n→ match #2\ncaps post")
    dlbl(ax, -14, Y_CB + 1.5, "BC: match #1\nstay on post")
    dlbl(ax, 2.5, Y_LB + 1.5, "M: hook\nrelate")
    dlbl(ax, -2.5, Y_LB + 1.5, "W: hook/curl\n#3 (RB)")

    note(ax, "TWO-HIGH SPLITS POSTS — each safety caps a post in their half. Best coverage vs double post.")
    return save(fig, "ninja_vs_double_post")


def gen_dagger():
    """Dagger: #1 runs post/seam, #2 runs dig behind it."""
    fig, ax = new_fig("NINJA vs DAGGER (Post + Dig)")
    base_offense(ax)
    # Field: #1 post, #2 dig
    route(ax, [(13, 0), (13, 6), (9, 10)])
    rlbl(ax, 8, 10.5, "Post")
    route(ax, [(7, 0), (7, 7), (2, 7)])
    rlbl(ax, 1, 7.5, "Dig")
    # Boundary clears
    route(ax, [(-13, 0), (-13, 8)])
    route(ax, [(-7, 0), (-7, 6)])
    rlbl(ax, -14, 6, "Clear")
    rlbl(ax, -8, 5, "Clear")
    route(ax, [(0, -3), (3, -1)])

    ninja_def(ax)
    dlbl(ax, 14, Y_CB + 1.5, "FC: match #1\nstay on post")
    dlbl(ax, 6, Y_S + 1.5, "FS: #2 vert/in\n→ match dig\nOR high hole")
    dlbl(ax, 9, Y_APEX + 1.5, "B: push #2\ncarry dig")
    dlbl(ax, -6, Y_S + 1.5, "D: #2 vert\nmatch")
    dlbl(ax, -14, Y_CB + 1.5, "BC: stay #1")
    dlbl(ax, 2.5, Y_LB + 1.5, "M: hook\nrally to dig")
    dlbl(ax, -2.5, Y_LB + 1.5, "W: hook/curl\n#3 (RB)")

    note(ax, "POST-DIG READ — FC stays on post. FS reads #2 inside → high hole, helps on dig. B carries #2 underneath.")
    return save(fig, "ninja_vs_dagger")


def gen_scissors():
    """Scissors / Hi-Lo to one side: #1 post, #2 corner."""
    fig, ax = new_fig("NINJA vs SCISSORS (#1 Post / #2 Corner)")
    base_offense(ax)
    # Field: #1 post, #2 corner (they cross)
    route(ax, [(13, 0), (13, 5), (9, 10)])
    rlbl(ax, 8, 10.5, "Post")
    route(ax, [(7, 0), (7, 5), (12, 10)])
    rlbl(ax, 13, 10, "Corner")
    # Boundary clears
    route(ax, [(-13, 0), (-13, 8)])
    route(ax, [(-7, 0), (-7, 6)])
    rlbl(ax, -14, 6, "Clear")
    rlbl(ax, -8, 5, "Clear")
    route(ax, [(0, -3), (3, -1)])

    ninja_def(ax)
    dlbl(ax, 14, Y_CB + 1.5, "FC: match #1\nstay on post")
    dlbl(ax, 6, Y_S + 1.5, "FS: #2 vert\n→ match corner")
    dlbl(ax, 9, Y_APEX + 1.5, "B: push #2\ncarry vert")
    dlbl(ax, -6, Y_S + 1.5, "D: #2 vert\nmatch")
    dlbl(ax, -14, Y_CB + 1.5, "BC: stay #1")
    dlbl(ax, 2.5, Y_LB + 1.5, "M: hook\nrelate")
    dlbl(ax, -2.5, Y_LB + 1.5, "W: hook/curl\n#3 (RB)")

    note(ax, "SCISSORS — FC stays on post, FS matches #2 corner. Two-high handles the crossing paths cleanly.")
    return save(fig, "ninja_vs_scissors")


def gen_y_cross():
    """Y-Cross / Deep Cross: #2 runs a deep crosser at 15+ yds."""
    fig, ax = new_fig("NINJA vs Y-CROSS (Deep Crosser)")
    base_offense(ax)
    # Field: #1 go, #2 deep cross to boundary
    route(ax, [(13, 0), (13, 10)])
    rlbl(ax, 14, 7, "Go")
    route(ax, [(7, 0), (7, 6), (0, 8), (-6, 8)])
    rlbl(ax, -7, 8.5, "Deep Cross")
    # Boundary: #1 curl, #2 out
    route(ax, [(-13, 0), (-13, 6), (-12, 5)])
    rlbl(ax, -14, 6.5, "Curl")
    route(ax, [(-7, 0), (-10, 2)])
    rlbl(ax, -11, 1.5, "Flat")
    route(ax, [(0, -3), (3, -1)])

    ninja_def(ax)
    dlbl(ax, 14, Y_CB + 1.5, "FC: match #1\nstay on go")
    dlbl(ax, 6, Y_S + 1.5, "FS: #2 inside\n→ carry cross\nOR high hole")
    dlbl(ax, 9, Y_APEX + 1.5, "B: #2 inside\nrelate/push")
    dlbl(ax, -6, Y_S + 1.5, "D: #2 out\n→ flip to #1\ncurl")
    dlbl(ax, -14, Y_CB + 1.5, "BC: #2 out\n→ JUMP flat")
    dlbl(ax, 2.5, Y_LB + 1.5, "M: CROSS!\ncarry deep X")
    dlbl(ax, -2.5, Y_LB + 1.5, "W: hook/curl\n#3 (RB)")

    note(ax, "DEEP CROSS — FS reads #2 inside, can carry or work high hole. M calls CROSS and carries. D flips to #1 on CLAMP trigger.")
    return save(fig, "ninja_vs_y_cross")


def gen_out_routes():
    """Both #2s run out routes — tests CLAMP trigger on boundary."""
    fig, ax = new_fig("NINJA vs OUT ROUTES (Both #2s Out)")
    base_offense(ax)
    # Field: #1 go, #2 out
    route(ax, [(13, 0), (13, 8)])
    rlbl(ax, 14, 5, "Go")
    route(ax, [(7, 0), (7, 4), (10, 4)])
    rlbl(ax, 11.5, 4, "Out")
    # Boundary: #1 go, #2 out
    route(ax, [(-13, 0), (-13, 8)])
    rlbl(ax, -14, 5, "Go")
    route(ax, [(-7, 0), (-7, 4), (-10, 4)])
    rlbl(ax, -11.5, 4, "Out")
    route(ax, [(0, -3), (3, -1)])

    ninja_def(ax)
    # MOD field: B drives to flat on #2 out. FS → high hole / rob #1
    dlbl(ax, 14, Y_CB + 1.5, "FC: match #1\nstay on go")
    dlbl(ax, 6, Y_S + 1.5, "FS: #2 out\n→ high hole\nrob #1 go")
    dlbl(ax, 9, Y_APEX + 1.5, "B: #2 out\nDRIVES flat")
    # CLAMP bnd: BC reads #2 out → jumps it. D flips to #1.
    dlbl(ax, -6, Y_S + 1.5, "D: #2 out\n→ FLIP to #1\ncovers go")
    dlbl(ax, -14, Y_CB + 1.5, "BC: #2 out\n→ JUMP #2")
    dlbl(ax, 2.5, Y_LB + 1.5, "M: hook\nrelate")
    dlbl(ax, -2.5, Y_LB + 1.5, "W: hook/curl\n#3 (RB)")

    note(ax, "OUT ROUTES — MOD: B drives flat. CLAMP: BC jumps #2 out, D flips to #1 deep. Both sides covered.")
    return save(fig, "ninja_vs_out_routes")


def gen_whip_wheel():
    """RB wheel route — tests #3 coverage."""
    fig, ax = new_fig("NINJA vs WHEEL (RB Wheel to Boundary)")
    base_offense(ax)
    # Field normal
    route(ax, [(13, 0), (13, 6)])
    route(ax, [(7, 0), (7, 5)])
    rlbl(ax, 14, 4, "Hitch")
    rlbl(ax, 8, 4, "Seam")
    # Boundary: #1 clear, #2 flat
    route(ax, [(-13, 0), (-13, 8)])
    rlbl(ax, -14, 5, "Clear")
    route(ax, [(-7, 0), (-10, 2)])
    rlbl(ax, -11, 1.5, "Flat")
    # RB wheel to boundary
    route(ax, [(0, -3), (-3, -2), (-6, 0), (-8, 4), (-10, 9)])
    rlbl(ax, -11.5, 8, "RB Wheel")

    ninja_def(ax)
    dlbl(ax, 14, Y_CB + 1.5, "FC: match #1\nhitch")
    dlbl(ax, 6, Y_S + 1.5, "FS: #2 vert\nmatch seam")
    dlbl(ax, 9, Y_APEX + 1.5, "B: push #2\ncarry")
    dlbl(ax, -6, Y_S + 1.5, "D: #2 out\n→ flip to #1\nOR RB wheel\ninto his zone")
    dlbl(ax, -14, Y_CB + 1.5, "BC: #2 out\n→ jump flat")
    dlbl(ax, 2.5, Y_LB + 1.5, "M: hook\nrelate")
    dlbl(ax, -2.5, Y_LB + 1.5, "W: #3 = RB\nCARRY wheel")

    note(ax, "RB WHEEL — W has #3 (RB). W must carry the wheel route. BC jumps #2 flat. D helps over top if needed.")
    return save(fig, "ninja_vs_wheel")


def gen_spacing():
    """Spacing: 5 receivers at different levels across the field."""
    fig, ax = new_fig("NINJA vs SPACING (5-Man Quick)")
    base_offense(ax)
    # 5 receivers at different spots: #1F hitch, #2F sit, #1B out, #2B sit, RB flat
    route(ax, [(13, 0), (13, 5)])
    rlbl(ax, 14, 4, "Hitch")
    route(ax, [(7, 0), (5, 4)])
    rlbl(ax, 4, 4.5, "Sit")
    route(ax, [(-13, 0), (-13, 4), (-15, 3)])
    rlbl(ax, -16, 2.5, "Out")
    route(ax, [(-7, 0), (-5, 4)])
    rlbl(ax, -4, 4.5, "Sit")
    route(ax, [(0, -3), (4, 0)])
    rlbl(ax, 5.5, 0, "RB Flat")

    ninja_def(ax)
    dlbl(ax, 14, Y_CB + 1.5, "FC: match #1\nhitch")
    dlbl(ax, 6, Y_S + 1.5, "FS: #2 under\n→ high hole")
    dlbl(ax, 9, Y_APEX + 1.5, "B: #2 under\ndrives flat\n+ RB")
    dlbl(ax, -6, Y_S + 1.5, "D: #2 under\n→ sit/bracket")
    dlbl(ax, -14, Y_CB + 1.5, "BC: match #1\nout")
    dlbl(ax, 2.5, Y_LB + 1.5, "M: hook\nrelate sits")
    dlbl(ax, -2.5, Y_LB + 1.5, "W: hook/curl\nrelate sit")

    note(ax, "SPACING — Zone defenders sit in windows. M/W relate to sit routes. B handles flat + RB. Safeties in high holes.")
    return save(fig, "ninja_vs_spacing")


# ============================================================
# MAIN
# ============================================================

def main():
    concepts = [
        ("Four Verticals", gen_four_verts),
        ("Mesh / Crossers", gen_mesh),
        ("Smash", gen_smash),
        ("Flood / Sail", gen_flood),
        ("Levels", gen_levels),
        ("Curl / Flat", gen_curl_flat),
        ("Slant / Flat", gen_slant_flat),
        ("Stick", gen_stick),
        ("RPO / Bubble", gen_rpo),
        ("Double Post", gen_double_post),
        ("Dagger", gen_dagger),
        ("Scissors", gen_scissors),
        ("Y-Cross", gen_y_cross),
        ("Out Routes", gen_out_routes),
        ("RB Wheel", gen_whip_wheel),
        ("Spacing", gen_spacing),
    ]

    print(f"Generating {len(concepts)} NINJA concept check diagrams...")
    paths = []
    for name, func in concepts:
        path = func()
        paths.append(path)
        print(f"  ✓ {name}: {path}")

    print(f"\nDone! {len(paths)} diagrams saved to {OUT_DIR}/")
    print("Files:")
    for p in sorted(paths):
        print(f"  {p}")


if __name__ == "__main__":
    main()
