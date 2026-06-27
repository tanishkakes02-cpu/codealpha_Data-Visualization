"""
Data Visualization Portfolio - Task 3
Author: Tanishka
Tools: Matplotlib, Seaborn, Pandas, NumPy
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns
import pandas as pd
import numpy as np
from matplotlib.patches import FancyBboxPatch
import warnings
warnings.filterwarnings('ignore')

# ──────────────────────────────────────────────
# GLOBAL STYLE
# ──────────────────────────────────────────────
DARK_BG   = "#0F1117"
CARD_BG   = "#1A1D2E"
ACCENT    = "#7C5CBF"
ACCENT2   = "#C45BAA"
ACCENT3   = "#F59E0B"
TEXT      = "#E2E8F0"
MUTED     = "#64748B"
GRID      = "#1E2235"
PALETTE   = ["#7C5CBF", "#C45BAA", "#F59E0B", "#10B981", "#3B82F6", "#EF4444"]

plt.rcParams.update({
    "figure.facecolor": DARK_BG,
    "axes.facecolor":   CARD_BG,
    "axes.edgecolor":   GRID,
    "axes.labelcolor":  TEXT,
    "axes.grid":        True,
    "grid.color":       GRID,
    "grid.linewidth":   0.6,
    "text.color":       TEXT,
    "xtick.color":      MUTED,
    "ytick.color":      MUTED,
    "xtick.labelsize":  9,
    "ytick.labelsize":  9,
    "font.family":      "DejaVu Sans",
    "legend.facecolor": CARD_BG,
    "legend.edgecolor": GRID,
    "legend.labelcolor":TEXT,
})

# ──────────────────────────────────────────────
# 1. GLOBAL SALES DASHBOARD (main poster)
# ──────────────────────────────────────────────
def chart1_sales_dashboard():
    np.random.seed(42)
    months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    revenue = [42,55,48,70,63,88,95,82,110,97,120,135]
    profit  = [12,18,14,25,20,34,38,30,45,40,52,60]
    expenses= [r-p for r,p in zip(revenue,profit)]
    units   = [820,1020,930,1300,1150,1600,1750,1520,2010,1800,2200,2450]

    fig = plt.figure(figsize=(18, 10), facecolor=DARK_BG)
    fig.text(0.5, 0.97, "📊  Global Sales Dashboard — 2024", ha="center", va="top",
             fontsize=22, fontweight="bold", color=TEXT)
    fig.text(0.5, 0.935, "Revenue · Profit · Units Sold · Regional Split",
             ha="center", va="top", fontsize=11, color=MUTED)

    gs = gridspec.GridSpec(2, 3, figure=fig,
                           hspace=0.45, wspace=0.35,
                           left=0.07, right=0.97, top=0.90, bottom=0.07)

    # ── KPI cards row ──
    kpi_ax = fig.add_axes([0.07, 0.82, 0.90, 0.07])
    kpi_ax.axis("off")
    kpis = [("Total Revenue", "$1.005M", ACCENT),
            ("Total Profit",  "$388K",  ACCENT2),
            ("Units Sold",    "18,550", ACCENT3),
            ("Growth YoY",    "+42%",   "#10B981")]
    for i,(label,val,col) in enumerate(kpis):
        x = 0.08 + i*0.24
        kpi_ax.add_patch(FancyBboxPatch((x,0.05),0.20,0.90,
                          boxstyle="round,pad=0.02",
                          facecolor=CARD_BG, edgecolor=col, linewidth=1.5,
                          transform=kpi_ax.transAxes))
        kpi_ax.text(x+0.10, 0.72, label, ha="center", va="center",
                    fontsize=9, color=MUTED, transform=kpi_ax.transAxes)
        kpi_ax.text(x+0.10, 0.32, val,   ha="center", va="center",
                    fontsize=15, fontweight="bold", color=col,
                    transform=kpi_ax.transAxes)

    # ── Line chart – Revenue vs Profit ──
    ax1 = fig.add_subplot(gs[0, :2])
    x = np.arange(len(months))
    ax1.fill_between(x, revenue, alpha=0.15, color=ACCENT)
    ax1.plot(x, revenue, "-o", color=ACCENT,  lw=2.2, ms=5, label="Revenue ($K)")
    ax1.fill_between(x, profit,  alpha=0.15, color=ACCENT2)
    ax1.plot(x, profit,  "-s", color=ACCENT2, lw=2.2, ms=5, label="Profit ($K)")
    ax1.set_xticks(x); ax1.set_xticklabels(months)
    ax1.set_title("Monthly Revenue vs Profit", fontsize=12, fontweight="bold", color=TEXT, pad=8)
    ax1.legend(loc="upper left", fontsize=9)
    ax1.set_ylabel("Amount ($K)")

    # ── Donut – Regional ──
    ax2 = fig.add_subplot(gs[0, 2])
    regions = ["North America","Europe","Asia-Pacific","LatAm","MEA"]
    shares  = [38, 27, 20, 9, 6]
    wedges, texts, autotexts = ax2.pie(
        shares, labels=regions, colors=PALETTE,
        autopct="%1.0f%%", startangle=140,
        wedgeprops=dict(width=0.55, edgecolor=DARK_BG, linewidth=2),
        pctdistance=0.78, labeldistance=1.12)
    for t in texts: t.set_fontsize(7.5); t.set_color(TEXT)
    for a in autotexts: a.set_fontsize(8); a.set_color(DARK_BG); a.set_fontweight("bold")
    ax2.set_title("Revenue by Region", fontsize=12, fontweight="bold", color=TEXT, pad=8)

    # ── Stacked Bar – Revenue vs Expenses ──
    ax3 = fig.add_subplot(gs[1, :2])
    ax3.bar(x, profit,   color=ACCENT2, label="Profit",   width=0.6)
    ax3.bar(x, expenses, bottom=profit, color=ACCENT, alpha=0.7, label="Expenses", width=0.6)
    ax3.set_xticks(x); ax3.set_xticklabels(months)
    ax3.set_title("Revenue Composition (Profit + Expenses)", fontsize=12, fontweight="bold", color=TEXT, pad=8)
    ax3.legend(fontsize=9)
    ax3.set_ylabel("Amount ($K)")

    # ── Units sparkline ──
    ax4 = fig.add_subplot(gs[1, 2])
    ax4.fill_between(x, units, alpha=0.2, color=ACCENT3)
    ax4.plot(x, units, "-o", color=ACCENT3, lw=2, ms=4)
    ax4.set_xticks(x[::2]); ax4.set_xticklabels(months[::2])
    ax4.set_title("Units Sold per Month", fontsize=12, fontweight="bold", color=TEXT, pad=8)
    ax4.set_ylabel("Units")

    fig.savefig("/home/claude/data_viz_project/assets/01_sales_dashboard.png",
                dpi=160, bbox_inches="tight", facecolor=DARK_BG)
    plt.close(fig)
    print("✅ Chart 1 – Sales Dashboard saved")


# ──────────────────────────────────────────────
# 2. HEATMAP – CORRELATION MATRIX
# ──────────────────────────────────────────────
def chart2_heatmap():
    np.random.seed(7)
    cols = ["Revenue","Profit","Units","Marketing","Satisfaction","Returns"]
    data = pd.DataFrame(np.random.randn(120, 6)*10, columns=cols)
    data["Revenue"] = data["Profit"]*3 + np.random.randn(120)*5
    data["Returns"] = -data["Satisfaction"]*0.4 + np.random.randn(120)*2
    corr = data.corr()

    fig, ax = plt.subplots(figsize=(9, 7), facecolor=DARK_BG)
    ax.set_facecolor(CARD_BG)
    mask = np.triu(np.ones_like(corr, dtype=bool))
    cmap = sns.diverging_palette(260, 330, s=80, l=50, as_cmap=True)
    sns.heatmap(corr, mask=mask, cmap=cmap, annot=True, fmt=".2f",
                linewidths=0.8, linecolor=DARK_BG, ax=ax,
                annot_kws={"size": 11, "weight": "bold"},
                cbar_kws={"shrink": 0.75})
    ax.set_title("Correlation Matrix — Business KPIs", fontsize=15,
                 fontweight="bold", color=TEXT, pad=14)
    plt.setp(ax.get_xticklabels(), rotation=30, ha="right", color=TEXT)
    plt.setp(ax.get_yticklabels(), rotation=0, color=TEXT)
    fig.tight_layout(pad=1.5)
    fig.savefig("/home/claude/data_viz_project/assets/02_heatmap_correlation.png",
                dpi=160, bbox_inches="tight", facecolor=DARK_BG)
    plt.close(fig)
    print("✅ Chart 2 – Heatmap saved")


# ──────────────────────────────────────────────
# 3. SCATTER — MARKETING SPEND vs REVENUE
# ──────────────────────────────────────────────
def chart3_scatter():
    np.random.seed(11)
    n = 200
    marketing = np.random.uniform(5, 100, n)
    revenue   = 2.5*marketing + np.random.normal(0, 15, n) + 20
    category  = np.random.choice(["Product A","Product B","Product C","Product D"], n)
    df = pd.DataFrame({"Marketing":marketing,"Revenue":revenue,"Category":category})

    fig, ax = plt.subplots(figsize=(10, 6), facecolor=DARK_BG)
    ax.set_facecolor(CARD_BG)
    for i, cat in enumerate(df["Category"].unique()):
        sub = df[df["Category"]==cat]
        ax.scatter(sub["Marketing"], sub["Revenue"],
                   color=PALETTE[i], alpha=0.75, s=55, label=cat, edgecolors="none")
    # regression line
    z = np.polyfit(df["Marketing"], df["Revenue"], 1)
    xr = np.linspace(5,100,200)
    ax.plot(xr, np.poly1d(z)(xr), "--", color=ACCENT3, lw=2, label="Trend line")
    ax.set_xlabel("Marketing Spend ($K)", fontsize=11)
    ax.set_ylabel("Revenue ($K)", fontsize=11)
    ax.set_title("Marketing Spend vs Revenue  ·  Product Breakdown",
                 fontsize=14, fontweight="bold", color=TEXT, pad=10)
    ax.legend(fontsize=9, markerscale=1.3)
    fig.tight_layout(pad=1.5)
    fig.savefig("/home/claude/data_viz_project/assets/03_scatter_marketing.png",
                dpi=160, bbox_inches="tight", facecolor=DARK_BG)
    plt.close(fig)
    print("✅ Chart 3 – Scatter plot saved")


# ──────────────────────────────────────────────
# 4. VIOLIN + BOX — CUSTOMER SATISFACTION
# ──────────────────────────────────────────────
def chart4_violin():
    np.random.seed(3)
    depts = ["Sales","Support","Billing","Tech","Logistics"]
    records = []
    params = [(7.2,1.1),(6.4,1.5),(5.8,2.0),(8.1,0.9),(6.9,1.3)]
    for dept,(mu,sd) in zip(depts,params):
        scores = np.clip(np.random.normal(mu,sd,120), 1, 10)
        for s in scores:
            records.append({"Department":dept,"Score":s})
    df = pd.DataFrame(records)

    fig, ax = plt.subplots(figsize=(11, 6), facecolor=DARK_BG)
    ax.set_facecolor(CARD_BG)
    sns.violinplot(data=df, x="Department", y="Score",
                   palette=PALETTE[:5], inner="box",
                   linewidth=1.4, ax=ax, cut=0.5)
    ax.set_title("Customer Satisfaction Scores by Department",
                 fontsize=14, fontweight="bold", color=TEXT, pad=10)
    ax.set_xlabel("Department", fontsize=11)
    ax.set_ylabel("Satisfaction Score (1–10)", fontsize=11)
    ax.axhline(7, color=ACCENT3, ls="--", lw=1.5, label="Target = 7.0")
    ax.legend(fontsize=10)
    fig.tight_layout(pad=1.5)
    fig.savefig("/home/claude/data_viz_project/assets/04_violin_satisfaction.png",
                dpi=160, bbox_inches="tight", facecolor=DARK_BG)
    plt.close(fig)
    print("✅ Chart 4 – Violin plot saved")


# ──────────────────────────────────────────────
# 5. HORIZONTAL BAR — TOP 10 PRODUCTS
# ──────────────────────────────────────────────
def chart5_hbar():
    products = [f"Product {chr(65+i)}" for i in range(10)]
    sales    = sorted(np.random.randint(80, 500, 10))
    colors   = [ACCENT if s < 250 else ACCENT2 if s < 380 else ACCENT3 for s in sales]

    fig, ax = plt.subplots(figsize=(10, 6), facecolor=DARK_BG)
    ax.set_facecolor(CARD_BG)
    bars = ax.barh(products, sales, color=colors, edgecolor="none", height=0.6)
    for bar, val in zip(bars, sales):
        ax.text(bar.get_width()+6, bar.get_y()+bar.get_height()/2,
                f"{val}K", va="center", fontsize=9, color=TEXT)
    ax.set_xlabel("Units Sold (K)", fontsize=11)
    ax.set_title("Top 10 Products by Units Sold",
                 fontsize=14, fontweight="bold", color=TEXT, pad=10)
    ax.set_xlim(0, max(sales)*1.18)
    ax.invert_yaxis()
    # legend manually
    from matplotlib.patches import Patch
    legend_elements = [Patch(facecolor=ACCENT,  label="Standard"),
                       Patch(facecolor=ACCENT2, label="High"),
                       Patch(facecolor=ACCENT3, label="Top")]
    ax.legend(handles=legend_elements, loc="lower right", fontsize=9)
    fig.tight_layout(pad=1.5)
    fig.savefig("/home/claude/data_viz_project/assets/05_hbar_products.png",
                dpi=160, bbox_inches="tight", facecolor=DARK_BG)
    plt.close(fig)
    print("✅ Chart 5 – Horizontal bar saved")


# ──────────────────────────────────────────────
# 6. PAIRPLOT — MULTI-VARIABLE INSIGHT
# ──────────────────────────────────────────────
def chart6_pairplot():
    np.random.seed(21)
    n = 150
    categories = np.random.choice(["Segment A","Segment B","Segment C"], n)
    df = pd.DataFrame({
        "Revenue":      np.where(categories=="Segment A", np.random.normal(80,12,n),
                         np.where(categories=="Segment B", np.random.normal(55,10,n),
                                                            np.random.normal(35,8,n))),
        "Units Sold":   np.where(categories=="Segment A", np.random.normal(200,30,n),
                         np.where(categories=="Segment B", np.random.normal(140,25,n),
                                                            np.random.normal(90,20,n))),
        "Marketing":    np.random.normal(40,15,n),
        "Segment":      categories
    })
    pal = {"Segment A": ACCENT, "Segment B": ACCENT2, "Segment C": ACCENT3}

    with plt.rc_context({"figure.facecolor": DARK_BG,
                         "axes.facecolor":   CARD_BG,
                         "axes.edgecolor":   GRID,
                         "axes.labelcolor":  TEXT,
                         "text.color":       TEXT,
                         "xtick.color":      MUTED,
                         "ytick.color":      MUTED}):
        g = sns.pairplot(df, hue="Segment", palette=pal, plot_kws={"alpha":0.6,"s":35},
                         diag_kind="kde", corner=True)
    g.figure.suptitle("Multi-Variable Pairplot — Segment Analysis",
                       y=1.01, fontsize=14, fontweight="bold", color=TEXT)
    g.figure.set_facecolor(DARK_BG)
    g.savefig("/home/claude/data_viz_project/assets/06_pairplot_segments.png",
              dpi=140, bbox_inches="tight", facecolor=DARK_BG)
    plt.close("all")
    print("✅ Chart 6 – Pairplot saved")


# ──────────────────────────────────────────────
# RUN ALL
# ──────────────────────────────────────────────
if __name__ == "__main__":
    print("\n🎨  Generating all visualizations …\n")
    chart1_sales_dashboard()
    chart2_heatmap()
    chart3_scatter()
    chart4_violin()
    chart5_hbar()
    chart6_pairplot()
    print("\n✨  All 6 charts saved to assets/\n")
