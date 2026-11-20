"""
Program Name: Lab15_joewidd-1.py
Author: Joe Widdifield
Purpose: Generate x and y data for the butterfly curve (discovered by
    Temple H. Fay) using the math library, then plot the curve with
    matplotlib and save the plot to an image file.

    Butterfly curve (parametric form):
        r(t) = e^cos(t) - 2cos(4t) - sin^5(t / 12)
        x(t) = sin(t) * r(t)
        y(t) = cos(t) * r(t)
    for t from 0 to 12*pi.
Starter Code: None. Formula reference:
    https://en.wikipedia.org/wiki/Butterfly_curve_(transcendental)
Date: 2026-11-20
"""

import math
from pathlib import Path

import matplotlib.pyplot as plt

# Number of sample points; more points gives a smoother curve.
NUM_POINTS = 5000
# The butterfly curve repeats after t reaches 12 * pi.
T_MAX = 12 * math.pi
# Image file the finished plot is saved to. It is placed in the same folder
# as this script so it works no matter which folder the script is run from.
OUTPUT_FILE = Path(__file__).parent / "butterfly_curve.png"


def butterfly_radius(t):
    """Return the butterfly curve's radius r(t) for the angle t (radians)."""
    return math.exp(math.cos(t)) - 2 * math.cos(4 * t) - math.sin(t / 12) ** 5


def generate_butterfly_data(num_points, t_max):
    """Build and return the x and y lists for the butterfly curve."""
    x_values = []
    y_values = []
    for i in range(num_points + 1):
        t = t_max * i / num_points
        r = butterfly_radius(t)
        x_values.append(math.sin(t) * r)
        y_values.append(math.cos(t) * r)
    return x_values, y_values


def plot_curve(x_values, y_values, file_name):
    """Plot the x and y lists, label the plot, and save it to file_name."""
    fig, ax = plt.subplots(figsize=(8, 8))
    # Challenge: custom line color, dashed line style, and line thickness.
    ax.plot(x_values, y_values, color="mediumvioletred", linestyle="--",
            linewidth=1.2)

    ax.set_title("Butterfly Curve", fontsize=18)
    ax.set_xlabel("x = sin(t) * r(t)", fontsize=12)
    ax.set_ylabel("y = cos(t) * r(t)", fontsize=12)

    # Challenge: add a grid and keep the x and y scales equal so the
    # butterfly is not stretched.
    ax.grid(True, linestyle=":", alpha=0.6)
    ax.set_aspect("equal")

    fig.savefig(file_name, dpi=150, bbox_inches="tight")
    plt.close(fig)


def main():
    """Generate the butterfly curve data, then plot and save it."""
    x_values, y_values = generate_butterfly_data(NUM_POINTS, T_MAX)
    plot_curve(x_values, y_values, OUTPUT_FILE)


if __name__ == "__main__":
    main()
