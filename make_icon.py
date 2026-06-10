"""One-off: render the Pulse app icons (192 + 512 px) with matplotlib."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

def make(size, out):
    dpi = 100
    fig = plt.figure(figsize=(size / dpi, size / dpi), dpi=dpi)
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 32); ax.set_ylim(0, 32)
    ax.axis("off"); fig.patch.set_alpha(0)
    ax.add_patch(FancyBboxPatch((0.5, 0.5), 31, 31,
                 boxstyle="round,pad=0,rounding_size=7",
                 facecolor="#0A0A0F", edgecolor="none"))
    xs = [5, 10, 13, 17, 20, 22, 27]
    ys = [14, 14, 22, 9, 18, 14, 14]
    ax.plot(xs, ys, color="#4D9FFF", linewidth=size / 38,
            solid_capstyle="round", solid_joinstyle="round")
    ax.plot(xs, ys, color="#7BD3FF", linewidth=size / 110,
            solid_capstyle="round", solid_joinstyle="round", alpha=0.9)
    fig.savefig(out, transparent=True)
    plt.close(fig)
    print("wrote", out)

make(192, "icon-192.png")
make(512, "icon-512.png")
