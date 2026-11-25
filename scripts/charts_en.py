import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm

for f in fm.findSystemFonts():
    if "Inter" in f and "Display" not in f:
        fm.fontManager.addfont(f)
plt.rcParams["font.family"] = "Inter"

V, M, O, G = "#7C3AED", "#E11D74", "#F59E0B", "#64748B"
INK, SUB, AX = "#0F172A", "#64748B", "#475569"
SIG = "Fusion in 5 Minutes · November 15, 2026"
OUT = "/home/claude/fusion-site/assets/img/"


def frame(title, subtitle, source):
    fig = plt.figure(figsize=(18, 10.12), dpi=100)
    fig.patch.set_facecolor("white")
    fig.text(0.04, 0.92, title, fontsize=38, fontweight="bold", color=INK)
    fig.text(0.04, 0.855, subtitle, fontsize=22, color=SUB)
    fig.text(0.04, 0.035, source, fontsize=16, color=SUB)
    fig.text(0.96, 0.035, SIG, fontsize=16, color=V, fontweight="bold", ha="right")
    return fig


def style(ax, grid_axis="y"):
    for s in ["top", "right"]:
        ax.spines[s].set_visible(False)
    for s in ["left", "bottom"]:
        ax.spines[s].set_color("#CBD5E1")
    ax.tick_params(colors=AX, labelsize=20)
    ax.grid(axis=grid_axis, color="#E2E8F0")
    ax.set_axisbelow(True)


# 1. JET
fig = frame("JET: 26 years to triple its record",
            "Fusion energy released in a single pulse (megajoules)",
            "Source: EUROfusion / UKAEA (2024)")
ax = fig.add_axes([0.08, 0.16, 0.88, 0.6])
yrs, vals, cols = ["1997", "2021", "2023"], [22, 59, 69], [V, M, O]
ax.bar(yrs, vals, color=cols, width=0.55)
for i, v in enumerate(vals):
    ax.text(i, v + 1.5, f"{v} MJ", ha="center", fontsize=28, fontweight="bold", color=INK)
ax.text(2, 32, "0.2 mg\nof fuel", ha="center", va="center", fontsize=20, fontweight="bold", color="white")
ax.set_ylim(0, 80)
style(ax)
ax.tick_params(axis="x", labelsize=24)
fig.savefig(OUT + "en-01-jet.png")

# 2. NIF
fig = frame("NIF: winning at the table, losing at the casino",
            "Record experiment, April 2025 (megajoules)",
            "Source: LLNL (2025). *LLNL estimate for the 2022 shot.")
ax = fig.add_axes([0.3, 0.16, 0.64, 0.6])
labels = ["Electricity to power\nthe lasers*", "Laser energy\nreaching the target", "Fusion energy\nproduced"]
vals, cols = [300, 2.08, 8.6], [G, V, M]
ax.barh(labels, vals, color=cols, height=0.55)
ax.text(304, 0, "≈300 MJ", va="center", fontsize=24, fontweight="bold", color=INK)
ax.text(2.08 + 4, 1, "2.08 MJ", va="center", fontsize=24, fontweight="bold", color=INK)
ax.text(8.6 + 4, 2, "8.6 MJ", va="center", fontsize=24, fontweight="bold", color=INK)
ax.text(70, 2, "← target gain: ×4.1", va="center", fontsize=22, fontweight="bold", color=M)
ax.set_xlim(0, 350)
style(ax, "x")
fig.savefig(OUT + "en-02-nif.png")

# 3. Investment
fig = frame("Private money arrived in fusion",
            "Cumulative investment in fusion companies (billions of USD)",
            "Source: Fusion Industry Association, annual reports 2021–2026")
ax = fig.add_axes([0.08, 0.16, 0.88, 0.6])
yrs = ["2021", "2022", "2023", "2024", "2025", "2026"]
vals = [1.9, 4.8, 6.2, 7.1, 9.8, 14.2]
ax.bar(yrs, vals, color=[V] * 5 + [M], width=0.6)
for i, v in enumerate(vals):
    ax.text(i, v + 0.3, f"${v}B", ha="center", fontsize=24, fontweight="bold", color=INK)
ax.annotate("×7.5 in\nfive years", xy=(4.65, 12.4), xytext=(3.2, 12.3), fontsize=22,
            fontweight="bold", color=M, va="center",
            arrowprops=dict(arrowstyle="->", color=M, lw=2.5))
ax.set_ylim(0, 16.5)
style(ax)
fig.savefig(OUT + "en-03-investment.png")
print("ok")
