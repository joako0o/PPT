"""Gráficos del deck — paleta institucional UTFSM."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
import numpy as np, glob, os

for f in glob.glob("/home/user/work/fonts/ssp/font_source_sans_pro/files/*.ttf"):
    fm.fontManager.addfont(f)
FONT = "Source Sans Pro"

ROJO, AMAR, AZUL = "#D10120", "#F7B006", "#005F91"
INK, GRAY, LINE = "#15181D", "#6E6E6E", "#DFE3E8"
MUTED = "#C2CBD2"

plt.rcParams.update({
    "font.family": FONT, "font.size": 15,
    "axes.edgecolor": LINE, "axes.labelcolor": INK, "text.color": INK,
    "xtick.color": GRAY, "ytick.color": GRAY,
    "axes.spines.top": False, "axes.spines.right": False,
    "figure.facecolor": "white", "axes.facecolor": "white",
    "savefig.facecolor": "white",
})

OUT = "/home/user/work/charts"
os.makedirs(OUT, exist_ok=True)


def benchmark_sku():
    data = [
        ("ES-GBM  ·  arquitectura propuesta", 16.10, "hero"),
        ("ES-GBM  ·  shares dinámicos", 24.35, "alt"),
        ("LSTM  ·  con precio ex-ante", 45.75, "n"),
        ("Chronos-Bolt  ·  desagregado", 48.44, "n"),
        ("LSTM  ·  sin precio ex-ante", 53.76, "n"),
        ("Seasonal Naïve", 69.89, "n"),
        ("SARIMAX", 73.24, "n"),
        ("SARIMA", 76.74, "n"),
        ("SBA (Syntetos-Boylan)", 83.42, "n"),
        ("Croston clásico", 84.87, "n"),
    ]
    labels = [d[0] for d in data][::-1]
    vals = [d[1] for d in data][::-1]
    kinds = [d[2] for d in data][::-1]
    colors = {"hero": AZUL, "alt": "#7FA8BE", "n": MUTED}
    fig, ax = plt.subplots(figsize=(10.2, 6.0), dpi=210)
    y = np.arange(len(vals))
    bars = ax.barh(y, vals, height=0.62, color=[colors[k] for k in kinds], zorder=3)
    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=15)
    for t, k in zip(ax.get_yticklabels(), kinds):
        if k == "hero":
            t.set_color(AZUL); t.set_fontweight("bold"); t.set_fontsize(16)
        else:
            t.set_color("#4A5158")
    for b, v, k in zip(bars, vals, kinds):
        ax.text(v + 1.4, b.get_y() + b.get_height() / 2, f"{v:,.2f}".replace(".", ",") + " %",
                va="center", ha="left", fontsize=15,
                fontweight="bold" if k == "hero" else "normal",
                color=AZUL if k == "hero" else "#4A5158")
    ax.set_xlim(0, 100)
    ax.set_xlabel("WAPE fuera de muestra, nivel SKU  ·  menor es mejor", fontsize=14, color=GRAY, labelpad=10)
    ax.xaxis.set_major_formatter(lambda v, p: f"{int(v)} %")
    ax.grid(axis="x", color="#EEF1F4", zorder=0)
    ax.set_axisbelow(True)
    ax.spines["left"].set_color(LINE)
    ax.spines["bottom"].set_visible(False)
    ax.tick_params(axis="y", length=0, pad=8)
    ax.tick_params(axis="x", labelsize=13)
    # banda de mejora
    ax.annotate("", xy=(16.1, 9.55), xytext=(69.89, 9.55),
                arrowprops=dict(arrowstyle="<->", color=ROJO, lw=1.6))
    ax.text(43, 9.85, "−53,8 pp vs. la mejor referencia clásica", ha="center", va="bottom",
            fontsize=14.5, color=ROJO, fontweight="bold")
    ax.set_ylim(-0.7, 10.6)
    fig.tight_layout(pad=0.4)
    fig.savefig(f"{OUT}/benchmark_sku.png", bbox_inches="tight", pad_inches=0.06)
    plt.close(fig)


def benchmark_familia():
    data = [("ES-GBM", 12.89), ("Chronos-Bolt", 36.35), ("LSTM", 40.51),
            ("SARIMAX", 59.64), ("Seasonal Naïve", 59.78), ("SARIMA", 64.84)][::-1]
    fig, ax = plt.subplots(figsize=(6.4, 3.5), dpi=210)
    y = np.arange(len(data))
    cols = [AZUL if d[0] == "ES-GBM" else MUTED for d in data]
    ax.barh(y, [d[1] for d in data], height=0.6, color=cols, zorder=3)
    ax.set_yticks(y); ax.set_yticklabels([d[0] for d in data], fontsize=14)
    for t, d in zip(ax.get_yticklabels(), data):
        if d[0] == "ES-GBM": t.set_color(AZUL); t.set_fontweight("bold")
        else: t.set_color("#4A5158")
    for i, d in enumerate(data):
        ax.text(d[1] + 1.2, i, f"{d[1]:.2f}".replace(".", ",") + " %", va="center", fontsize=13.5,
                color=AZUL if d[0] == "ES-GBM" else "#4A5158",
                fontweight="bold" if d[0] == "ES-GBM" else "normal")
    ax.set_xlim(0, 80); ax.grid(axis="x", color="#EEF1F4", zorder=0); ax.set_axisbelow(True)
    ax.spines["bottom"].set_visible(False); ax.spines["left"].set_color(LINE)
    ax.tick_params(axis="y", length=0, pad=6); ax.set_xticks([])
    ax.set_title("WAPE nivel Familia", fontsize=14.5, color=GRAY, loc="left", pad=8)
    fig.tight_layout(pad=0.3)
    fig.savefig(f"{OUT}/benchmark_familia.png", bbox_inches="tight", pad_inches=0.06)
    plt.close(fig)


def ablation():
    labels = ["Sin información\nde precios", "Precio rezagado\nt−1 (histórico)", "Plan comercial\nex-ante t"]
    vals = [38.25, 26.42, 16.10]
    cols = [MUTED, "#7FA8BE", AZUL]
    fig, ax = plt.subplots(figsize=(7.6, 5.0), dpi=210)
    x = np.arange(3)
    ax.bar(x, vals, width=0.55, color=cols, zorder=3)
    for i, v in enumerate(vals):
        ax.text(i, v + 1.1, f"{v:.2f}".replace(".", ",") + " %", ha="center", fontsize=19,
                fontweight="bold", color=AZUL if i == 2 else "#4A5158")
    ax.set_xticks(x); ax.set_xticklabels(labels, fontsize=15, color="#3A3F47")
    ax.set_ylim(0, 50); ax.set_yticks([])
    ax.grid(axis="y", color="#F0F2F5", zorder=0); ax.set_axisbelow(True)
    ax.spines["left"].set_visible(False); ax.spines["bottom"].set_color(LINE)
    ax.tick_params(axis="x", length=0, pad=8)
    # deltas
    def delta(i, j, txt):
        ymax = max(vals[i], vals[j]) + 6.2
        ax.annotate("", xy=(i, ymax), xytext=(j, ymax), arrowprops=dict(arrowstyle="<->", color=ROJO, lw=1.5))
        ax.text((i + j) / 2, ymax + 0.8, txt, ha="center", fontsize=14.5, color=ROJO, fontweight="bold")
    delta(0, 1, "−11,8 pp")
    delta(1, 2, "−10,3 pp")
    fig.tight_layout(pad=0.4)
    fig.savefig(f"{OUT}/ablation.png", bbox_inches="tight", pad_inches=0.06)
    plt.close(fig)


def inventario():
    """Stock de seguridad requerido por modelo (unidades)."""
    data = [("SARIMA\nMAE 54,2", 8916, MUTED), ("LSTM\nMAE 32,3", 5313, "#7FA8BE"),
            ("ES-GBM\nMAE 11,4", 1875, AZUL)]
    fig, ax = plt.subplots(figsize=(7.2, 4.6), dpi=210)
    x = np.arange(3)
    ax.bar(x, [d[1] for d in data], width=0.5, color=[d[2] for d in data], zorder=3)
    for i, d in enumerate(data):
        ax.text(i, d[1] + 220, f"{d[1]:,}".replace(",", ".") + " un.", ha="center", fontsize=17,
                fontweight="bold", color=AZUL if i == 2 else "#4A5158")
    ax.set_xticks(x); ax.set_xticklabels([d[0] for d in data], fontsize=14.5, color="#3A3F47")
    ax.set_ylim(0, 10800); ax.set_yticks([])
    ax.grid(axis="y", color="#F0F2F5", zorder=0); ax.set_axisbelow(True)
    ax.spines["left"].set_visible(False); ax.spines["bottom"].set_color(LINE)
    ax.tick_params(axis="x", length=0, pad=8)
    ax.annotate("", xy=(2, 9700), xytext=(0, 9700), arrowprops=dict(arrowstyle="<->", color=ROJO, lw=1.6))
    ax.text(1, 9950, "−7.041 unidades de buffer  ·  $105,6M CLP", ha="center", fontsize=15,
            color=ROJO, fontweight="bold")
    ax.set_title("Stock de seguridad requerido (CSL 95 %, L = 1 mes)", fontsize=14.5,
                 color=GRAY, loc="left", pad=10)
    fig.tight_layout(pad=0.4)
    fig.savefig(f"{OUT}/inventario.png", bbox_inches="tight", pad_inches=0.06)
    plt.close(fig)


if __name__ == "__main__":
    benchmark_sku(); benchmark_familia(); ablation(); inventario()
    for f in sorted(glob.glob(f"{OUT}/*.png")):
        from PIL import Image
        im = Image.open(f); print(os.path.basename(f), im.size, round(im.size[0] / im.size[1], 2))
