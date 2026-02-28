#!/usr/bin/env python3
"""NINJA coverage check diagrams v2 — includes defensive assignment arrows.
Shows MOD (field) / CLAMP (boundary) with movement lines for all defenders.
"""

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT_DIR = "/tmp/ninja_concept_check_v2"
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
C_DEF = "#0066CC"

# Y positions
Y_LOS = 0
Y_DL = 1.2
Y_LB = 3.5
Y_APEX = 3.0
Y_CB = 5.5
Y_S = 8.0

OL_POSITIONS = [(0, 0), (2, 0), (-2, 0), (4, 0), (-4, 0)]

# Defender start positions (NINJA default: MOD field / CLAMP bnd)
FC_X, FC_Y = 12, Y_CB
BC_X, BC_Y = -12, Y_CB
FS_X, FS_Y = 5, Y_S
D_X, D_Y = -5, Y_S
B_X, B_Y = 7.5, Y_APEX
M_X, M_Y = 1.5, Y_LB
W_X, W_Y = -1.5, Y_LB


def new_fig(title="", figsize=(12, 9)):
    fig, ax = plt.subplots(1, 1, figsize=figsize)
    ax.set_xlim(-17, 17)
    ax.set_ylim(-5.5, 14)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.axhline(y=0.5, color=C_GRAY, linewidth=1, linestyle="--", alpha=0.3)
    ax.text(15.5, 13.2, "FIELD →", fontsize=8, color=C_GRAY, ha="right", va="top", style="italic")
    ax.text(-15.5, 13.2, "← BOUNDARY", fontsize=8, color=C_GRAY, ha="left", va="top", style="italic")
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
    """Offensive route: dashed red with arrowhead."""
    for i in range(len(points) - 1):
        if i < len(points) - 2:
            ax.plot([points[i][0], points[i + 1][0]],
                    [points[i][1], points[i + 1][1]],
                    "--", color=C_ROUTE, lw=1.5, alpha=0.8)
        else:
            ax.annotate("", xy=points[i + 1], xytext=points[i],
                        arrowprops=dict(arrowstyle="-|>", color=C_ROUTE, lw=1.5, linestyle="dashed"))


def darrow(ax, x1, y1, x2, y2):
    """Defensive assignment arrow: solid blue."""
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="-|>", color=C_DEF, lw=2.0, alpha=0.7))


def dcurve(ax, x1, y1, x2, y2, rad=0.3):
    """Defensive curved assignment arrow."""
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="-|>", color=C_DEF, lw=2.0, alpha=0.7,
                                connectionstyle=f"arc3,rad={rad}"))


def dpath(ax, points):
    """Defensive multi-segment path with arrow at end."""
    for i in range(len(points) - 1):
        if i < len(points) - 2:
            ax.plot([points[i][0], points[i + 1][0]],
                    [points[i][1], points[i + 1][1]],
                    "-", color=C_DEF, lw=2.0, alpha=0.7)
        else:
            ax.annotate("", xy=points[i + 1], xytext=points[i],
                        arrowprops=dict(arrowstyle="-|>", color=C_DEF, lw=2.0, alpha=0.7))


def rlbl(ax, x, y, text):
    ax.text(x, y, text, fontsize=6.5, ha="center", color=C_ROUTE, style="italic")


def dlbl(ax, x, y, text):
    """Defender assignment label."""
    ax.text(x, y, text, fontsize=6, ha="center", color=C_DEF, style="italic",
            bbox=dict(boxstyle="round,pad=0.12", facecolor="white", edgecolor=C_DEF, alpha=0.85, linewidth=0.5))


def note(ax, text):
    ax.text(0, -5, text, fontsize=8.5, ha="center", color=C_NAVY, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.3", facecolor=C_COLUMBIA, alpha=0.15))


def save(fig, name):
    path = os.path.join(OUT_DIR, f"{name}.png")
    fig.savefig(path, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return path


def base_offense(ax):
    draw_ol(ax)
    off_player(ax, 0, -1.5, "QB")
    off_player(ax, 0, -3, "RB")
    off_player(ax, 13, 0, "#1 F")
    off_player(ax, 7, 0, "#2 F")
    off_player(ax, -13, 0, "#1 B")
    off_player(ax, -7, 0, "#2 B")


def ninja_def(ax):
    # DL
    def_player(ax, 4.7, Y_DL, "A")
    def_player(ax, 2.5, Y_DL, "T")
    def_player(ax, -1.5, Y_DL, "N")
    def_player(ax, -4.7, Y_DL, "E")
    # LBs
    def_player(ax, M_X, M_Y, "M", color=C_COLUMBIA)
    def_player(ax, W_X, W_Y, "W", color=C_COLUMBIA)
    def_player(ax, B_X, B_Y, "B", color=C_COLUMBIA)
    # DBs
    def_player(ax, FC_X, FC_Y, "FC", color=C_COLUMBIA)
    def_player(ax, BC_X, BC_Y, "BC", color=C_COLUMBIA)
    def_player(ax, FS_X, FS_Y, "FS", color=C_GOLD)
    def_player(ax, D_X, D_Y, "D", color=C_GOLD)


# ============================================================
# CONCEPTS
# ============================================================

def gen_four_verts():
    fig, ax = new_fig("NINJA vs FOUR VERTICALS")
    base_offense(ax)
    route(ax, [(13, 0), (13, 12)]); rlbl(ax, 14.2, 6, "Go")
    route(ax, [(7, 0), (7, 12)]); rlbl(ax, 8.2, 6, "Seam")
    route(ax, [(-13, 0), (-13, 12)]); rlbl(ax, -14.2, 6, "Go")
    route(ax, [(-7, 0), (-7, 12)]); rlbl(ax, -8.2, 6, "Seam")
    route(ax, [(0, -3), (3, -1)]); rlbl(ax, 4, -1.5, "Check")
    ninja_def(ax)
    # FC stays on #1 go
    darrow(ax, FC_X, FC_Y, 13, 10)
    dlbl(ax, 14.5, 9, "FC: match\n#1 go")
    # FS reads #2 vert → matches seam
    darrow(ax, FS_X, FS_Y, 7, 10)
    dlbl(ax, 4, 10.5, "FS: #2 vert\n→ match seam")
    # B pushes #2 seam
    darrow(ax, B_X, B_Y, 7, 6)
    dlbl(ax, 9.5, 5, "B: push #2\ncarry seam")
    # D matches #2 bnd seam
    darrow(ax, D_X, D_Y, -7, 10)
    dlbl(ax, -4, 10.5, "D: #2 vert\n→ match seam")
    # BC stays on #1 go
    darrow(ax, BC_X, BC_Y, -13, 10)
    dlbl(ax, -14.5, 9, "BC: stay\non #1")
    # W hook/curl #3
    darrow(ax, W_X, W_Y, -1, 4.5)
    dlbl(ax, -3, 5.5, "W: hook/curl\n#3 (RB)")
    # M hook
    darrow(ax, M_X, M_Y, 1.5, 5)
    dlbl(ax, 3, 6, "M: hook\nrelate")
    note(ax, "TWO-HIGH CAPS ALL 4 SEAMS — FS matches #2F seam, D matches #2B seam. Best zone look vs 4 verts.")
    return save(fig, "ninja_vs_4verts")


def gen_mesh():
    fig, ax = new_fig("NINJA vs MESH / CROSSERS")
    base_offense(ax)
    route(ax, [(13, 0), (12, 3), (5, 5), (-3, 5)]); rlbl(ax, -4, 5.8, "#1F Cross")
    route(ax, [(-13, 0), (-12, 3), (-5, 5), (3, 5)]); rlbl(ax, 4, 5.8, "#1B Cross")
    route(ax, [(7, 0), (7, 9)]); rlbl(ax, 8.2, 6, "Seam")
    route(ax, [(-7, 0), (-7, 9)]); rlbl(ax, -8.2, 6, "Seam")
    route(ax, [(0, -3), (3, -1)]); rlbl(ax, 4, -1.5, "Check")
    ninja_def(ax)
    # FC: #1 goes short → zone off deep
    dcurve(ax, FC_X, FC_Y, 13, 9, rad=-0.2)
    dlbl(ax, 14.5, 9, "FC: #1 short\nzone off deep")
    # FS: #2 vert → match seam
    darrow(ax, FS_X, FS_Y, 7, 10)
    dlbl(ax, 4, 10.5, "FS: #2 vert\n→ match seam")
    # B: push #2 seam
    darrow(ax, B_X, B_Y, 7, 6)
    dlbl(ax, 9.5, 5, "B: push #2\ncarry seam")
    # D: #2 vert → match seam
    darrow(ax, D_X, D_Y, -7, 10)
    dlbl(ax, -4, 10.5, "D: #2 vert\n→ match seam")
    # BC: stays on #1
    darrow(ax, BC_X, BC_Y, -13, 8)
    dlbl(ax, -14.5, 8, "BC: #1 short\nstay on #1")
    # M: CROSS! carries deeper crosser
    dpath(ax, [(M_X, M_Y), (0, 5), (-3, 5.5)])
    dlbl(ax, -1, 7, "M: CROSS!\ncarry deeper")
    # W: stays on #3
    darrow(ax, W_X, W_Y, -1, 4.5)
    dlbl(ax, -3.5, 5, "W: hook/curl\n#3 (RB)")
    note(ax, "M CARRIES THE CROSSER — calls 'CROSS!', W stays on #3. Zone pass-offs handle picks naturally.")
    return save(fig, "ninja_vs_mesh")


def gen_smash():
    fig, ax = new_fig("NINJA vs SMASH (Corner / Hitch)")
    base_offense(ax)
    route(ax, [(13, 0), (13, 5)]); rlbl(ax, 14.5, 4, "Hitch")
    route(ax, [(7, 0), (7, 4), (10, 9)]); rlbl(ax, 11.5, 9, "Corner")
    route(ax, [(-13, 0), (-13, 5)]); rlbl(ax, -14.5, 4, "Hitch")
    route(ax, [(-7, 0), (-7, 4), (-10, 9)]); rlbl(ax, -11.5, 9, "Corner")
    route(ax, [(0, -3), (3, -1)]); rlbl(ax, 4, -1.5, "Check")
    ninja_def(ax)
    # FC sits on hitch
    darrow(ax, FC_X, FC_Y, 13, 6)
    dlbl(ax, 14.5, 7, "FC: match #1\nsit on hitch")
    # FS: #2 vert (corner) → match
    dcurve(ax, FS_X, FS_Y, 9, 9.5, rad=-0.2)
    dlbl(ax, 6.5, 10.5, "FS: #2 vert\n→ match corner")
    # B: push #2, falls under corner
    darrow(ax, B_X, B_Y, 8, 5)
    dlbl(ax, 10, 4.5, "B: push #2\nunder corner")
    # D: #2 vert (corner) → match
    dcurve(ax, D_X, D_Y, -9, 9.5, rad=0.2)
    dlbl(ax, -6.5, 10.5, "D: #2 vert\n→ match corner")
    # BC: #2 vert → stays on #1
    darrow(ax, BC_X, BC_Y, -13, 6)
    dlbl(ax, -14.5, 7, "BC: #2 vert\n→ stay on #1")
    # M hook
    darrow(ax, M_X, M_Y, 1.5, 5)
    dlbl(ax, 3, 6, "M: hook")
    # W hook/curl #3
    darrow(ax, W_X, W_Y, -1, 4.5)
    dlbl(ax, -3.5, 5.5, "W: #3 (RB)")
    note(ax, "FS/D MATCH CORNER ROUTE — corner route is vertical, safety matches. CB sits on hitch. No conflict.")
    return save(fig, "ninja_vs_smash")


def gen_flood():
    fig, ax = new_fig("NINJA vs FLOOD / SAIL (3-Level, Field Side)")
    base_offense(ax)
    route(ax, [(13, 0), (13, 5), (15, 10)]); rlbl(ax, 15.5, 10.5, "Corner")
    route(ax, [(7, 0), (7, 5), (10, 6)]); rlbl(ax, 11.5, 6, "Out")
    route(ax, [(0, -3), (5, -1), (10, 1)]); rlbl(ax, 11, 0.5, "RB Flat")
    route(ax, [(-13, 0), (-13, 8)]); rlbl(ax, -14, 6, "Clear")
    route(ax, [(-7, 0), (-7, 6)]); rlbl(ax, -8, 5, "Clear")
    ninja_def(ax)
    # FC: stays on #1 corner/go
    darrow(ax, FC_X, FC_Y, 12, 9)
    dlbl(ax, 14, 9.5, "FC: match #1\nstay on top")
    # FS: #2 out → drive with control on out route
    dcurve(ax, FS_X, FS_Y, 9, 7, rad=-0.2)
    dlbl(ax, 6, 10.5, "FS: #2 out\n→ drive w/ control\nmatch out")
    # B: #2 out → drives flat, takes RB
    dpath(ax, [(B_X, B_Y), (9, 2), (10, 1.5)])
    dlbl(ax, 9, 4.5, "B: #2 out\ndrives to flat\ntakes RB")
    # D: matches #2 bnd vert
    darrow(ax, D_X, D_Y, -7, 9)
    dlbl(ax, -4, 10, "D: #2 vert\nmatch")
    # BC: stays on #1
    darrow(ax, BC_X, BC_Y, -13, 9)
    dlbl(ax, -14.5, 9, "BC: stay #1")
    # M: hook zone
    darrow(ax, M_X, M_Y, 2, 5)
    dlbl(ax, 4.5, 6, "M: hook")
    # W: hook/curl #3
    darrow(ax, W_X, W_Y, -1, 4.5)
    dlbl(ax, -3, 5.5, "W: #3")
    note(ax, "3-LEVEL STRETCH — FS reads #2 out → drives with control on out. B drives flat/RB. FC stays on top of corner.")
    return save(fig, "ninja_vs_flood")


def gen_levels():
    fig, ax = new_fig("NINJA vs LEVELS (Hi-Lo Crossers)")
    base_offense(ax)
    route(ax, [(7, 0), (5, 4), (-3, 4)]); rlbl(ax, -4, 3.3, "Drag (5)")
    route(ax, [(13, 0), (13, 8), (5, 8)]); rlbl(ax, 3.5, 8.7, "Dig (12)")
    route(ax, [(-13, 0), (-13, 8)]); rlbl(ax, -14, 6, "Clear")
    route(ax, [(-7, 0), (-7, 6)]); rlbl(ax, -8, 5, "Clear")
    route(ax, [(0, -3), (3, -1)]); rlbl(ax, 4, -1.5, "Check")
    ninja_def(ax)
    # FC: #1 short (dig breaks in) → zone off deep
    dcurve(ax, FC_X, FC_Y, 13, 10, rad=-0.15)
    dlbl(ax, 14.5, 10, "FC: #1 short\nzone off deep")
    # FS: #2 under → high hole, robs dig
    dcurve(ax, FS_X, FS_Y, 5, 9, rad=-0.2)
    dlbl(ax, 3, 10.5, "FS: #2 under\n→ high hole\nrobs dig")
    # B: push #2, carries drag under
    dpath(ax, [(B_X, B_Y), (6, 4), (3, 4)])
    dlbl(ax, 9, 5, "B: #2 drag\ncarry under")
    # D: #2 vert match
    darrow(ax, D_X, D_Y, -7, 9)
    dlbl(ax, -4, 10, "D: #2 vert\nmatch")
    # BC: stays on #1
    darrow(ax, BC_X, BC_Y, -13, 9)
    dlbl(ax, -14.5, 9, "BC: stay #1")
    # M: CROSS! carries drag
    dpath(ax, [(M_X, M_Y), (0, 4.5), (-2, 4.5)])
    dlbl(ax, -0.5, 6, "M: CROSS!\ncarry drag")
    # W: hook/curl #3
    darrow(ax, W_X, W_Y, -1, 4.5)
    dlbl(ax, -3.5, 5.5, "W: #3 (RB)")
    note(ax, "HI-LO READ — FS reads #2 under → high hole, robs dig. M carries drag across. No conflict.")
    return save(fig, "ninja_vs_levels")


def gen_curl_flat():
    fig, ax = new_fig("NINJA vs CURL / FLAT")
    base_offense(ax)
    route(ax, [(13, 0), (13, 8), (12, 7)]); rlbl(ax, 14, 8.5, "Curl")
    route(ax, [(7, 0), (10, 2)]); rlbl(ax, 11.5, 1.5, "Flat")
    route(ax, [(-13, 0), (-13, 8), (-12, 7)]); rlbl(ax, -14, 8.5, "Curl")
    route(ax, [(-7, 0), (-10, 2)]); rlbl(ax, -11.5, 1.5, "Flat")
    route(ax, [(0, -3), (3, -1)]); rlbl(ax, 4, -1.5, "Check")
    ninja_def(ax)
    # FC: sits on curl
    darrow(ax, FC_X, FC_Y, 12.5, 7.5)
    dlbl(ax, 14.5, 7, "FC: match #1\nsit on curl")
    # FS: #2 out → high hole, robs curl
    dcurve(ax, FS_X, FS_Y, 8, 9, rad=-0.2)
    dlbl(ax, 6, 10.5, "FS: #2 out\n→ high hole\nrob curl")
    # B: #2 out → drives flat
    dpath(ax, [(B_X, B_Y), (9, 2.5), (10, 2.5)])
    dlbl(ax, 9, 4.5, "B: #2 out\ndrives flat")
    # CLAMP bnd: BC reads #2 out → JUMPS flat
    dpath(ax, [(BC_X, BC_Y), (-11, 4), (-10.5, 2.5)])
    dlbl(ax, -14.5, 6, "BC: #2 out\n→ JUMP flat")
    # D: #2 out → flips to #1 curl
    dcurve(ax, D_X, D_Y, -12, 8, rad=0.3)
    dlbl(ax, -7.5, 10.5, "D: #2 out\n→ flip to #1\ncovers curl")
    # M hook
    darrow(ax, M_X, M_Y, 1.5, 5)
    dlbl(ax, 3.5, 6, "M: hook")
    # W hook/curl #3
    darrow(ax, W_X, W_Y, -2, 5)
    dlbl(ax, -3.5, 6, "W: #3 (RB)")
    note(ax, "NO CURL-FLAT CONFLICT — MOD: B drives flat, FS robs curl. CLAMP: BC jumps #2 flat, D flips to #1 curl.")
    return save(fig, "ninja_vs_curl_flat")


def gen_slant_flat():
    fig, ax = new_fig("NINJA vs SLANT / FLAT")
    base_offense(ax)
    route(ax, [(13, 0), (10, 4)]); rlbl(ax, 9, 4.7, "Slant")
    route(ax, [(7, 0), (10, 2)]); rlbl(ax, 11.5, 1.5, "Flat")
    route(ax, [(-13, 0), (-10, 4)]); rlbl(ax, -9, 4.7, "Slant")
    route(ax, [(-7, 0), (-10, 2)]); rlbl(ax, -11.5, 1.5, "Flat")
    route(ax, [(0, -3), (3, -1)]); rlbl(ax, 4, -1.5, "Check")
    ninja_def(ax)
    # FC: inside leverage → matches slant
    darrow(ax, FC_X, FC_Y, 10.5, 4)
    dlbl(ax, 14.5, 6.5, "FC: inside lev\nmatch slant")
    # FS: #2 out → high hole
    dcurve(ax, FS_X, FS_Y, 7, 9, rad=-0.2)
    dlbl(ax, 5, 10.5, "FS: #2 out\n→ high hole")
    # B: drives flat
    dpath(ax, [(B_X, B_Y), (9, 2.5), (10, 2.5)])
    dlbl(ax, 9, 4.5, "B: #2 out\ndrives flat")
    # CLAMP: BC jumps #2 flat
    dpath(ax, [(BC_X, BC_Y), (-11, 4), (-10.5, 2.5)])
    dlbl(ax, -14.5, 6, "BC: #2 out\n→ JUMP flat")
    # D: flips to #1
    dcurve(ax, D_X, D_Y, -10.5, 5, rad=0.3)
    dlbl(ax, -7, 10, "D: #2 out\n→ flip to #1")
    # M: hook, relates to slant
    darrow(ax, M_X, M_Y, 3, 5)
    dlbl(ax, 4.5, 6, "M: hook\nrelate slant")
    # W: #3
    darrow(ax, W_X, W_Y, -1, 4.5)
    dlbl(ax, -3.5, 5.5, "W: #3 (RB)")
    note(ax, "INSIDE LEVERAGE KILLS SLANT — FC matches slant head on. B drives flat. CLAMP: BC jumps #2 flat.")
    return save(fig, "ninja_vs_slant_flat")


def gen_stick():
    fig, ax = new_fig("NINJA vs STICK (3-Level Quick)")
    base_offense(ax)
    route(ax, [(13, 0), (11, 5)]); rlbl(ax, 10, 5.7, "Stick (6)")
    route(ax, [(7, 0), (10, 2)]); rlbl(ax, 11.5, 1.5, "Flat")
    route(ax, [(0, -3), (2, 0), (3, 5)]); rlbl(ax, 4.2, 5, "RB push")
    route(ax, [(-13, 0), (-13, 8)]); rlbl(ax, -14, 6, "Clear")
    route(ax, [(-7, 0), (-7, 6)]); rlbl(ax, -8, 5, "Clear")
    ninja_def(ax)
    # FC: matches #1 stick
    darrow(ax, FC_X, FC_Y, 11.5, 5.5)
    dlbl(ax, 14, 7.5, "FC: match #1\nrally to stick")
    # FS: #2 out → high hole, robs stick
    dcurve(ax, FS_X, FS_Y, 7, 9, rad=-0.2)
    dlbl(ax, 5, 10.5, "FS: #2 out\n→ high hole\nrob stick")
    # B: drives flat
    dpath(ax, [(B_X, B_Y), (9, 2.5), (10, 2.5)])
    dlbl(ax, 9.5, 4.5, "B: #2 out\ndrives flat")
    # D: matches #2 vert
    darrow(ax, D_X, D_Y, -7, 9)
    dlbl(ax, -4, 10, "D: #2 vert\nmatch")
    # BC: stays on #1
    darrow(ax, BC_X, BC_Y, -13, 9)
    dlbl(ax, -14.5, 9, "BC: stay #1")
    # M: hook, relate stick
    darrow(ax, M_X, M_Y, 3, 5.5)
    dlbl(ax, 2, 7, "M: hook\nrelate stick")
    # W: #3 = RB push
    dpath(ax, [(W_X, W_Y), (0, 4), (2, 5)])
    dlbl(ax, -2, 5.5, "W: #3 = RB\ncarry push")
    note(ax, "3-LEVEL COVERED — FC on stick, B drives flat, W takes RB push (#3). FS robs from high hole.")
    return save(fig, "ninja_vs_stick")


def gen_rpo():
    fig, ax = new_fig("NINJA vs RPO (Bubble / Now Screen)")
    base_offense(ax)
    route(ax, [(13, 0), (13, 8)]); rlbl(ax, 14.2, 5, "Go/Block")
    route(ax, [(7, 0), (9, 1)]); rlbl(ax, 10.5, 1.5, "Bubble")
    route(ax, [(-13, 0), (-13, 6)]); rlbl(ax, -14, 4, "Clear")
    route(ax, [(-7, 0), (-7, 6)]); rlbl(ax, -8, 4, "Clear")
    ax.annotate("", xy=(2, -2), xytext=(0, -3),
                arrowprops=dict(arrowstyle="-|>", color=C_ROUTE, lw=1.5, linestyle="dashed"))
    rlbl(ax, 3.5, -2.5, "Run fake")
    ninja_def(ax)
    # FC: match #1 go
    darrow(ax, FC_X, FC_Y, 13, 8)
    dlbl(ax, 14.5, 8, "FC: match #1\nif go, on top")
    # FS: #2 out → high hole
    dcurve(ax, FS_X, FS_Y, 7, 9, rad=-0.2)
    dlbl(ax, 4.5, 10.5, "FS: #2 out\n→ high hole")
    # B: covers down #2 bubble → DRIVES
    dpath(ax, [(B_X, B_Y), (8, 2), (9, 1.5)])
    dlbl(ax, 9, 4.5, "B: #2 bubble\nDRIVE ON IT")
    # D: #2 vert
    darrow(ax, D_X, D_Y, -7, 9)
    dlbl(ax, -4, 10, "D: #2 vert\nmatch")
    # BC: stay on #1
    darrow(ax, BC_X, BC_Y, -13, 8)
    dlbl(ax, -14.5, 8, "BC: stay #1")
    # M: read, don't bite run
    darrow(ax, M_X, M_Y, 1.5, 5)
    dlbl(ax, 3, 6, "M: read\ndon't bite run")
    # W: #3
    darrow(ax, W_X, W_Y, -1, 4.5)
    dlbl(ax, -3.5, 5.5, "W: #3")
    note(ax, "B IS THE KEY — B covers down on #2. Bubble = B drives on it immediately. M must NOT bite on run fake.")
    return save(fig, "ninja_vs_rpo")


def gen_double_post_seam():
    """Double Post with #2 running a seam (vertical). Safety locked on #2."""
    fig, ax = new_fig("NINJA vs DOUBLE POST (#2 Seam)")
    base_offense(ax)
    route(ax, [(13, 0), (13, 5), (8, 10)]); rlbl(ax, 7, 10.7, "Post")
    route(ax, [(-13, 0), (-13, 5), (-8, 10)]); rlbl(ax, -7, 10.7, "Post")
    route(ax, [(7, 0), (7, 10)]); rlbl(ax, 8.2, 6, "Seam")
    route(ax, [(-7, 0), (-7, 10)]); rlbl(ax, -8.2, 6, "Seam")
    route(ax, [(0, -3), (3, -1)]); rlbl(ax, 4, -1.5, "Check")
    ninja_def(ax)
    # FC: stays on #1 post — must stay on top ALONE
    darrow(ax, FC_X, FC_Y, 9, 9)
    dlbl(ax, 13, 10, "FC: match #1\nstay on post\n(alone)")
    # FS: #2 vertical → LOCKED on seam, cannot help post
    darrow(ax, FS_X, FS_Y, 7, 10)
    dlbl(ax, 4, 11, "FS: #2 vert\n→ match seam\n(locked)")
    # B: push #2 carry seam
    darrow(ax, B_X, B_Y, 7, 6)
    dlbl(ax, 9.5, 5, "B: push #2\ncarry seam")
    # D: #2 vertical → LOCKED on seam, cannot help post
    darrow(ax, D_X, D_Y, -7, 10)
    dlbl(ax, -4, 11, "D: #2 vert\n→ match seam\n(locked)")
    # BC: stays on #1 post — must stay on top ALONE
    darrow(ax, BC_X, BC_Y, -9, 9)
    dlbl(ax, -13, 10, "BC: match #1\nstay on post\n(alone)")
    # M hook
    darrow(ax, M_X, M_Y, 1.5, 5)
    dlbl(ax, 3, 6, "M: hook")
    # W #3
    darrow(ax, W_X, W_Y, -1, 4.5)
    dlbl(ax, -3.5, 5.5, "W: #3 (RB)")
    note(ax, "#2 SEAM LOCKS SAFETY — FS/D must match #2 vertical. CBs are ALONE on post. No safety help available.")
    return save(fig, "ninja_vs_double_post_seam")


def gen_double_post_in():
    """Double Post with #2 running an in/dig (under). Safety reads under → high hole → helps post."""
    fig, ax = new_fig("NINJA vs DOUBLE POST (#2 In/Dig)")
    base_offense(ax)
    route(ax, [(13, 0), (13, 5), (8, 10)]); rlbl(ax, 7, 10.7, "Post")
    route(ax, [(-13, 0), (-13, 5), (-8, 10)]); rlbl(ax, -7, 10.7, "Post")
    route(ax, [(7, 0), (7, 5), (3, 5)]); rlbl(ax, 2, 5.7, "In/Dig")
    route(ax, [(-7, 0), (-7, 5), (-3, 5)]); rlbl(ax, -2, 5.7, "In/Dig")
    route(ax, [(0, -3), (3, -1)]); rlbl(ax, 4, -1.5, "Check")
    ninja_def(ax)
    # FC: stays on #1 post — safety helping from high hole
    darrow(ax, FC_X, FC_Y, 9, 9)
    dlbl(ax, 13, 10, "FC: match #1\nstay on post\n(help coming)")
    # FS: #2 under → high hole → rob/bracket post
    dcurve(ax, FS_X, FS_Y, 7, 10, rad=-0.2)
    dlbl(ax, 4, 11, "FS: #2 under\n→ high hole\nbracket post")
    # B: push #2, carry in/dig under
    dpath(ax, [(B_X, B_Y), (6, 4), (4, 5)])
    dlbl(ax, 9.5, 5, "B: push #2\ncarry in/dig")
    # D: #2 under → high hole → rob/bracket post
    dcurve(ax, D_X, D_Y, -7, 10, rad=0.2)
    dlbl(ax, -4, 11, "D: #2 under\n→ high hole\nbracket post")
    # BC: stays on #1 post — safety helping from high hole
    darrow(ax, BC_X, BC_Y, -9, 9)
    dlbl(ax, -13, 10, "BC: match #1\nstay on post\n(help coming)")
    # M: hook, relate to in/dig
    darrow(ax, M_X, M_Y, 2, 5.5)
    dlbl(ax, 3.5, 6.5, "M: hook\nrelate in/dig")
    # W: hook, relate to in/dig
    darrow(ax, W_X, W_Y, -2, 5.5)
    dlbl(ax, -3.5, 6.5, "W: hook\nrelate in/dig")
    note(ax, "#2 UNDER FREES SAFETY — FS/D read #2 under → high hole → bracket post. CB has help. Much better position.")
    return save(fig, "ninja_vs_double_post_in")


def gen_dagger():
    fig, ax = new_fig("NINJA vs DAGGER (Post + Dig)")
    base_offense(ax)
    route(ax, [(13, 0), (13, 6), (9, 10)]); rlbl(ax, 8, 10.7, "Post")
    route(ax, [(7, 0), (7, 7), (2, 7)]); rlbl(ax, 1, 7.7, "Dig")
    route(ax, [(-13, 0), (-13, 8)]); rlbl(ax, -14, 6, "Clear")
    route(ax, [(-7, 0), (-7, 6)]); rlbl(ax, -8, 5, "Clear")
    route(ax, [(0, -3), (3, -1)]); rlbl(ax, 4, -1.5, "Check")
    ninja_def(ax)
    # FC: match #1 post
    darrow(ax, FC_X, FC_Y, 10, 9)
    dlbl(ax, 13, 10, "FC: match #1\nstay on post")
    # FS: #2 inside → high hole / helps on dig
    dcurve(ax, FS_X, FS_Y, 4, 9, rad=-0.2)
    dlbl(ax, 2.5, 10.5, "FS: #2 in\n→ high hole\nhelps dig")
    # B: push #2, carry dig under
    dpath(ax, [(B_X, B_Y), (6, 5), (4, 7)])
    dlbl(ax, 8.5, 5.5, "B: push #2\ncarry dig")
    # D: #2 vert match
    darrow(ax, D_X, D_Y, -7, 9)
    dlbl(ax, -4, 10, "D: #2 vert\nmatch")
    # BC stays
    darrow(ax, BC_X, BC_Y, -13, 9)
    dlbl(ax, -14.5, 9, "BC: stay #1")
    # M: hook rally to dig
    darrow(ax, M_X, M_Y, 2, 6)
    dlbl(ax, 0, 6.5, "M: hook\nrally to dig")
    # W #3
    darrow(ax, W_X, W_Y, -1, 4.5)
    dlbl(ax, -3.5, 5.5, "W: #3 (RB)")
    note(ax, "POST-DIG READ — FC stays on post. FS reads #2 inside → high hole, helps on dig. B carries #2 underneath.")
    return save(fig, "ninja_vs_dagger")


def gen_scissors():
    fig, ax = new_fig("NINJA vs SCISSORS (#1 Post / #2 Corner)")
    base_offense(ax)
    route(ax, [(13, 0), (13, 5), (9, 10)]); rlbl(ax, 8, 10.7, "Post")
    route(ax, [(7, 0), (7, 5), (12, 10)]); rlbl(ax, 13, 10, "Corner")
    route(ax, [(-13, 0), (-13, 8)]); rlbl(ax, -14, 6, "Clear")
    route(ax, [(-7, 0), (-7, 6)]); rlbl(ax, -8, 5, "Clear")
    route(ax, [(0, -3), (3, -1)]); rlbl(ax, 4, -1.5, "Check")
    ninja_def(ax)
    # FC: match #1 post
    darrow(ax, FC_X, FC_Y, 10, 9)
    dlbl(ax, 13.5, 8, "FC: match #1\nstay on post")
    # FS: #2 vert → match corner
    dcurve(ax, FS_X, FS_Y, 11, 9.5, rad=-0.3)
    dlbl(ax, 5, 11, "FS: #2 vert\n→ match corner")
    # B: push #2 carry vert
    darrow(ax, B_X, B_Y, 8, 6)
    dlbl(ax, 9.5, 5, "B: push #2\ncarry vert")
    # D: #2 vert match
    darrow(ax, D_X, D_Y, -7, 9)
    dlbl(ax, -4, 10, "D: #2 vert\nmatch")
    # BC stays
    darrow(ax, BC_X, BC_Y, -13, 9)
    dlbl(ax, -14.5, 9, "BC: stay #1")
    # M hook
    darrow(ax, M_X, M_Y, 1.5, 5)
    dlbl(ax, 3, 6, "M: hook")
    # W #3
    darrow(ax, W_X, W_Y, -1, 4.5)
    dlbl(ax, -3.5, 5.5, "W: #3 (RB)")
    note(ax, "SCISSORS — FC stays on post, FS matches #2 corner. Two-high handles crossing paths cleanly.")
    return save(fig, "ninja_vs_scissors")


def gen_y_cross():
    fig, ax = new_fig("NINJA vs Y-CROSS (Deep Crosser)")
    base_offense(ax)
    route(ax, [(13, 0), (13, 10)]); rlbl(ax, 14.2, 7, "Go")
    route(ax, [(7, 0), (7, 6), (0, 8), (-6, 8)]); rlbl(ax, -7, 8.7, "Deep Cross")
    route(ax, [(-13, 0), (-13, 6), (-12, 5)]); rlbl(ax, -14, 6.5, "Curl")
    route(ax, [(-7, 0), (-10, 2)]); rlbl(ax, -11.5, 1.5, "Flat")
    route(ax, [(0, -3), (3, -1)]); rlbl(ax, 4, -1.5, "Check")
    ninja_def(ax)
    # FC: match #1 go
    darrow(ax, FC_X, FC_Y, 13, 10)
    dlbl(ax, 14.5, 10, "FC: match #1\nstay on go")
    # FS: #2 inside → carry cross or high hole
    dcurve(ax, FS_X, FS_Y, 3, 9, rad=-0.2)
    dlbl(ax, 2, 10.5, "FS: #2 inside\n→ carry cross\nOR high hole")
    # B: #2 inside, relate/push
    dpath(ax, [(B_X, B_Y), (6, 5), (4, 6)])
    dlbl(ax, 9, 5, "B: #2 inside\nrelate/push")
    # CLAMP: BC jumps #2 flat
    dpath(ax, [(BC_X, BC_Y), (-11, 4), (-10.5, 2.5)])
    dlbl(ax, -14.5, 6, "BC: #2 out\n→ JUMP flat")
    # D: #2 out → flip to #1 curl
    dcurve(ax, D_X, D_Y, -12, 6, rad=0.3)
    dlbl(ax, -7, 10.5, "D: #2 out\n→ flip to #1\ncurl")
    # M: CROSS carries deep cross
    dpath(ax, [(M_X, M_Y), (0, 6), (-3, 7.5)])
    dlbl(ax, -1, 6, "M: CROSS!\ncarry deep X")
    # W: #3
    darrow(ax, W_X, W_Y, -2, 5)
    dlbl(ax, -3.5, 5.5, "W: #3 (RB)")
    note(ax, "DEEP CROSS — FS reads #2 inside. M calls CROSS, carries all the way. CLAMP: BC jumps flat, D flips to #1.")
    return save(fig, "ninja_vs_y_cross")


def gen_out_routes():
    fig, ax = new_fig("NINJA vs OUT ROUTES (Both #2s Out)")
    base_offense(ax)
    route(ax, [(13, 0), (13, 8)]); rlbl(ax, 14.2, 5, "Go")
    route(ax, [(7, 0), (7, 4), (10, 4)]); rlbl(ax, 11.5, 4, "Out")
    route(ax, [(-13, 0), (-13, 8)]); rlbl(ax, -14.2, 5, "Go")
    route(ax, [(-7, 0), (-7, 4), (-10, 4)]); rlbl(ax, -11.5, 4, "Out")
    route(ax, [(0, -3), (3, -1)]); rlbl(ax, 4, -1.5, "Check")
    ninja_def(ax)
    # FC: match #1 go
    darrow(ax, FC_X, FC_Y, 13, 8.5)
    dlbl(ax, 14.5, 9, "FC: match #1\nstay on go")
    # FS: #2 out → high hole, robs go
    dcurve(ax, FS_X, FS_Y, 8, 9.5, rad=-0.2)
    dlbl(ax, 5.5, 10.5, "FS: #2 out\n→ high hole\nrob #1 go")
    # B: drives to flat on out
    dpath(ax, [(B_X, B_Y), (9, 3.5), (10, 4)])
    dlbl(ax, 9, 5.5, "B: #2 out\nDRIVES flat")
    # CLAMP: BC jumps #2 out
    dpath(ax, [(BC_X, BC_Y), (-11, 4.5), (-10.5, 4)])
    dlbl(ax, -14.5, 6, "BC: #2 out\n→ JUMP #2")
    # D: #2 out → flip to #1 go
    dcurve(ax, D_X, D_Y, -13, 9, rad=0.3)
    dlbl(ax, -7, 10.5, "D: #2 out\n→ FLIP to #1\ncovers go")
    # M hook
    darrow(ax, M_X, M_Y, 1.5, 5)
    dlbl(ax, 3, 6, "M: hook")
    # W #3
    darrow(ax, W_X, W_Y, -1, 4.5)
    dlbl(ax, -3.5, 5.5, "W: #3 (RB)")
    note(ax, "OUT ROUTES — MOD: B drives flat. CLAMP: BC jumps #2 out, D flips to #1 deep. Both sides covered.")
    return save(fig, "ninja_vs_out_routes")


def gen_wheel():
    fig, ax = new_fig("NINJA vs WHEEL (RB Wheel to Boundary)")
    base_offense(ax)
    route(ax, [(13, 0), (13, 6)]); rlbl(ax, 14.2, 4, "Hitch")
    route(ax, [(7, 0), (7, 5)]); rlbl(ax, 8, 4, "Seam")
    route(ax, [(-13, 0), (-13, 8)]); rlbl(ax, -14, 5, "Clear")
    route(ax, [(-7, 0), (-10, 2)]); rlbl(ax, -11.5, 1.5, "Flat")
    route(ax, [(0, -3), (-3, -2), (-6, 0), (-8, 4), (-10, 9)]); rlbl(ax, -11.5, 8, "RB Wheel")
    ninja_def(ax)
    # FC: hitch
    darrow(ax, FC_X, FC_Y, 13, 6.5)
    dlbl(ax, 14.5, 7.5, "FC: match #1\nhitch")
    # FS: #2 vert match seam
    darrow(ax, FS_X, FS_Y, 7, 9)
    dlbl(ax, 4.5, 10, "FS: #2 vert\nmatch seam")
    # B: push #2 carry
    darrow(ax, B_X, B_Y, 7, 5.5)
    dlbl(ax, 9.5, 5, "B: push #2\ncarry")
    # CLAMP: BC jumps #2 flat
    dpath(ax, [(BC_X, BC_Y), (-11, 4), (-10.5, 2.5)])
    dlbl(ax, -14.5, 6, "BC: #2 out\n→ jump flat")
    # D: #2 out → flip to #1 OR help wheel
    dcurve(ax, D_X, D_Y, -11, 9, rad=0.3)
    dlbl(ax, -7, 10.5, "D: #2 out\n→ flip to #1\nhelp wheel OT")
    # W: #3 = RB → CARRY WHEEL
    dpath(ax, [(W_X, W_Y), (-4, 3), (-7, 5), (-9, 8)])
    dlbl(ax, -4, 5.5, "W: #3 = RB\nCARRY wheel")
    # M hook
    darrow(ax, M_X, M_Y, 1.5, 5)
    dlbl(ax, 3, 6, "M: hook\nrelate")
    note(ax, "RB WHEEL — W has #3 (RB). W must carry the wheel route all the way up. BC jumps #2 flat. D helps over top.")
    return save(fig, "ninja_vs_wheel")


def gen_spacing():
    fig, ax = new_fig("NINJA vs SPACING (5-Man Quick)")
    base_offense(ax)
    route(ax, [(13, 0), (13, 5)]); rlbl(ax, 14.2, 4, "Hitch")
    route(ax, [(7, 0), (5, 4)]); rlbl(ax, 4, 4.7, "Sit")
    route(ax, [(-13, 0), (-13, 4), (-15, 3)]); rlbl(ax, -16, 2.5, "Out")
    route(ax, [(-7, 0), (-5, 4)]); rlbl(ax, -4, 4.7, "Sit")
    route(ax, [(0, -3), (4, 0)]); rlbl(ax, 5.5, 0, "RB Flat")
    ninja_def(ax)
    # FC: match #1 hitch
    darrow(ax, FC_X, FC_Y, 13, 5.5)
    dlbl(ax, 14.5, 7, "FC: match #1\nhitch")
    # FS: #2 under → high hole
    dcurve(ax, FS_X, FS_Y, 6, 8, rad=-0.15)
    dlbl(ax, 4, 9.5, "FS: #2 under\n→ high hole")
    # B: #2 under → drives flat + RB
    dpath(ax, [(B_X, B_Y), (6, 2), (5, 1)])
    dlbl(ax, 9, 4.5, "B: #2 under\ndrives flat\n+ RB")
    # D: #2 under → sit/bracket
    dcurve(ax, D_X, D_Y, -4, 7, rad=0.15)
    dlbl(ax, -3, 9, "D: #2 under\n→ sit/bracket")
    # BC: match #1 out
    dpath(ax, [(BC_X, BC_Y), (-13.5, 4), (-14.5, 3)])
    dlbl(ax, -14.5, 6.5, "BC: match #1\nout")
    # M: hook relate sits
    darrow(ax, M_X, M_Y, 3, 5)
    dlbl(ax, 4.5, 6, "M: hook\nrelate sits")
    # W: hook/curl relate sit
    darrow(ax, W_X, W_Y, -3, 5)
    dlbl(ax, -4.5, 6, "W: hook/curl\nrelate sit")
    note(ax, "SPACING — Zone defenders sit in windows. M/W relate to sit routes. B handles flat + RB. Safeties high hole.")
    return save(fig, "ninja_vs_spacing")


# ============================================================
# SPLIT ZONE BLUFF CONCEPTS (Y-off)
# ============================================================

def sz_offense(ax):
    """Base 2x2 + Y-off (sniffer field side). Zone fake to field."""
    draw_ol(ax)
    off_player(ax, 0, -1.5, "QB")
    off_player(ax, 0, -3, "RB")
    off_player(ax, 13, 0, "#1 F")
    off_player(ax, 7, 0, "#2 F")
    off_player(ax, -13, 0, "#1 B")
    off_player(ax, -7, 0, "#2 B")
    off_player(ax, 5, -1, "Y")
    # RB zone fake to field
    route(ax, [(0, -3), (4, -2)]); rlbl(ax, 5.5, -2.5, "Run fake")


def gen_sz_flat():
    """Split zone bluff — Y leaks to boundary flat. Boot action."""
    fig, ax = new_fig("NINJA vs SPLIT ZONE BLUFF — Y Flat (Boot)")
    sz_offense(ax)
    # Y: crosses from field, bluffs block on E, leaks to bnd flat
    route(ax, [(5, -1), (0, 0), (-5, 0.5), (-10, 2)])
    rlbl(ax, -11.5, 1.5, "Y Flat")
    # #1 B: Go (clear out deep)
    route(ax, [(-13, 0), (-13, 10)]); rlbl(ax, -14.2, 8, "Go")
    # #2 B: Corner route (intermediate)
    route(ax, [(-7, 0), (-7, 5), (-11, 9)]); rlbl(ax, -12, 9.5, "Corner")
    # #1 F: Post (backside shot)
    route(ax, [(13, 0), (13, 5), (8, 10)]); rlbl(ax, 7, 10.5, "Post")
    # #2 F: Block/stay in
    route(ax, [(7, 0), (7, 2)]); rlbl(ax, 8.5, 1.5, "Block")
    ninja_def(ax)
    # BC: match #1B go — occupied deep
    darrow(ax, BC_X, BC_Y, -13, 9)
    dlbl(ax, -14.5, 9, "BC: match #1\nstay on go")
    # D: reads #2B vert → matches corner route
    dcurve(ax, D_X, D_Y, -10, 9, rad=0.3)
    dlbl(ax, -4, 10.5, "D: #2 vert\n→ match corner")
    # W: KEY — reads Y cross, does NOT bite on run fake, picks up Y flat
    dpath(ax, [(W_X, W_Y), (-4, 3), (-8, 2.5)])
    dlbl(ax, -3.5, 5.5, "W: read Y cross\n→ TAKE Y flat\nDON'T BITE RUN")
    # FC: match #1F post
    dcurve(ax, FC_X, FC_Y, 10, 9, rad=0.15)
    dlbl(ax, 14.5, 9, "FC: match #1\nstay on post")
    # FS: #2F stays in / blocks → high hole field
    dcurve(ax, FS_X, FS_Y, 5, 10, rad=-0.2)
    dlbl(ax, 3, 11, "FS: #2 stays\n→ high hole\nhelp post")
    # B: field side, reads #2F block → relates
    darrow(ax, B_X, B_Y, 7, 3.5)
    dlbl(ax, 9, 4.5, "B: #2 blocks\n→ relate")
    # M: hook, reads run to pass
    darrow(ax, M_X, M_Y, 0, 5)
    dlbl(ax, 3, 6, "M: hook\nread run→pass")
    note(ax, "W IS THE KEY — must not bite on zone fake. Y doesn't block = pass. W takes Y flat. D matches #2B corner.")
    return save(fig, "ninja_vs_sz_bluff_flat")


def gen_sz_wheel():
    """Split zone bluff — Y wheels up boundary sideline."""
    fig, ax = new_fig("NINJA vs SPLIT ZONE BLUFF — Y Wheel")
    sz_offense(ax)
    # Y: crosses from field, bluffs block, wheels up boundary sideline
    route(ax, [(5, -1), (0, 0), (-5, 0.5), (-10, 2), (-12, 7), (-12, 11)])
    rlbl(ax, -13.5, 9, "Y Wheel")
    # #1 B: Post (holds safety inside, clears sideline for wheel)
    route(ax, [(-13, 0), (-13, 5), (-8, 10)]); rlbl(ax, -7, 10.5, "Post")
    # #2 B: Dig/In (underneath option)
    route(ax, [(-7, 0), (-7, 5), (-3, 5)]); rlbl(ax, -2, 4.3, "Dig")
    # #1 F: Go (clear)
    route(ax, [(13, 0), (13, 10)]); rlbl(ax, 14.2, 8, "Go")
    # #2 F: Shallow cross
    route(ax, [(7, 0), (5, 2), (0, 3)]); rlbl(ax, -1.5, 2.3, "Shallow")
    ninja_def(ax)
    # BC: match #1B post — occupied
    dcurve(ax, BC_X, BC_Y, -10, 9, rad=-0.15)
    dlbl(ax, -14.5, 9, "BC: match #1\nstay on post")
    # D: reads #2B in/dig → under → high hole → HELP WHEEL OT
    dcurve(ax, D_X, D_Y, -10, 10, rad=0.3)
    dlbl(ax, -4, 11, "D: #2 under\n→ high hole\nHELP wheel OT")
    # W: KEY — reads Y cross, carries wheel ALL THE WAY
    dpath(ax, [(W_X, W_Y), (-4, 3), (-8, 4), (-11, 7)])
    dlbl(ax, -3, 5.5, "W: read Y cross\n→ CARRY wheel\nall the way up")
    # M: hook, relates to dig/crossers
    dpath(ax, [(M_X, M_Y), (0, 5), (-2, 5)])
    dlbl(ax, 3, 6, "M: hook\nrelate dig")
    # FC: match #1F go
    darrow(ax, FC_X, FC_Y, 13, 9)
    dlbl(ax, 14.5, 9, "FC: match #1\nstay on go")
    # FS: #2F shallow → high hole
    dcurve(ax, FS_X, FS_Y, 5, 10, rad=-0.2)
    dlbl(ax, 3, 11, "FS: #2 under\n→ high hole")
    # B: reads #2F shallow cross → carries under
    dpath(ax, [(B_X, B_Y), (5, 3.5), (2, 3.5)])
    dlbl(ax, 9, 4.5, "B: #2 shallow\n→ carry under")
    note(ax, "W CARRIES WHEEL — must not bite zone fake. Y crosses = read pass. W runs with wheel. D helps over top from high hole.")
    return save(fig, "ninja_vs_sz_bluff_wheel")


def gen_sz_seam():
    """Split zone bluff — Y runs backside seam."""
    fig, ax = new_fig("NINJA vs SPLIT ZONE BLUFF — Y Seam")
    sz_offense(ax)
    # Y: crosses from field, bluffs block, releases vertical up bnd seam
    route(ax, [(5, -1), (0, 0), (-5, 0.5), (-6, 4), (-6, 11)])
    rlbl(ax, -7.5, 9, "Y Seam")
    # #1 B: Go (clear out deep)
    route(ax, [(-13, 0), (-13, 10)]); rlbl(ax, -14.2, 8, "Go")
    # #2 B: Dig/In (underneath, creates vertical stretch with Y seam)
    route(ax, [(-7, 0), (-7, 5), (-3, 5)]); rlbl(ax, -2, 4.3, "Dig")
    # #1 F: Go/Post
    route(ax, [(13, 0), (13, 5), (9, 10)]); rlbl(ax, 8, 10.5, "Post")
    # #2 F: Deep over/crosser
    route(ax, [(7, 0), (7, 4), (0, 6)]); rlbl(ax, -1.5, 6.7, "Over")
    ninja_def(ax)
    # BC: match #1B go — occupied deep
    darrow(ax, BC_X, BC_Y, -13, 9)
    dlbl(ax, -14.5, 9, "BC: match #1\nstay on go")
    # D: reads #2B in/dig → under → HIGH HOLE → sees Y seam → MATCH Y
    dcurve(ax, D_X, D_Y, -6, 10, rad=0.2)
    dlbl(ax, -3.5, 11, "D: #2 under\n→ high hole\n→ MATCH Y seam")
    # W: reads run to pass, picks up #2B dig
    dpath(ax, [(W_X, W_Y), (-4, 4), (-4, 5)])
    dlbl(ax, -3.5, 6.5, "W: read pass\n→ carry #2B dig")
    # M: hook, relates to over/crosser from field
    dpath(ax, [(M_X, M_Y), (1, 5), (-1, 5.5)])
    dlbl(ax, 3, 6, "M: CROSS!\ncarry over")
    # FC: match #1F post
    dcurve(ax, FC_X, FC_Y, 10, 9, rad=0.15)
    dlbl(ax, 14.5, 9, "FC: match #1\nstay on post")
    # FS: #2F inside → carry cross OR high hole
    dcurve(ax, FS_X, FS_Y, 3, 9, rad=-0.2)
    dlbl(ax, 3, 11, "FS: #2 inside\n→ carry cross\nOR high hole")
    # B: reads #2F inside → relates
    dpath(ax, [(B_X, B_Y), (5, 4), (2, 5)])
    dlbl(ax, 9, 4.5, "B: #2 inside\n→ relate/push")
    note(ax, "D IS THE KEY — #2B under frees D to high hole. D MUST see Y climbing seam and match it. W carries dig underneath.")
    return save(fig, "ninja_vs_sz_bluff_seam")


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
        ("Double Post (#2 Seam)", gen_double_post_seam),
        ("Double Post (#2 In/Dig)", gen_double_post_in),
        ("Dagger", gen_dagger),
        ("Scissors", gen_scissors),
        ("Y-Cross", gen_y_cross),
        ("Out Routes", gen_out_routes),
        ("RB Wheel", gen_wheel),
        ("Spacing", gen_spacing),
        ("SZ Bluff — Y Flat", gen_sz_flat),
        ("SZ Bluff — Y Wheel", gen_sz_wheel),
        ("SZ Bluff — Y Seam", gen_sz_seam),
    ]
    print(f"Generating {len(concepts)} NINJA v2 diagrams with defensive arrows...")
    paths = []
    for name, func in concepts:
        path = func()
        paths.append(path)
        print(f"  ✓ {name}: {path}")
    print(f"\nDone! {len(paths)} diagrams → {OUT_DIR}/")


if __name__ == "__main__":
    main()
