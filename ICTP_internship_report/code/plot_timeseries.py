"""Generate a publication-ready plot from processed ICTP measurements."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

DATA_PATH = Path("data") / "example_measurements.csv"
OUTPUT_PATH = Path("figs") / "timeseries.pdf"


def prepare_dataframe(path: Path) -> pd.DataFrame:
    """Return a DataFrame indexed by hours with smoothed values."""
    raw = pd.read_csv(path, parse_dates=["timestamp"])
    raw = raw.set_index("timestamp").sort_index()
    hourly = raw.resample("1H").mean().interpolate()
    hourly.index = (hourly.index - hourly.index[0]).total_seconds() / 3600
    hourly.index.name = "hours"
    return hourly


def save_plot(df: pd.DataFrame, output: Path) -> None:
    """Export a Matplotlib figure with ICTP house style."""
    plt.style.use("seaborn-v0_8-talk")
    fig, ax = plt.subplots(figsize=(7, 3.5))
    ax.plot(df.index, df["signal"], marker="o", color="#008080")
    ax.set_xlabel("Time (h)")
    ax.set_ylabel("Signal (a.u.)")
    ax.grid(True, which="both", alpha=0.3)
    fig.tight_layout()
    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output)
    plt.close(fig)


if __name__ == "__main__":
    dataframe = prepare_dataframe(DATA_PATH)
    save_plot(dataframe, OUTPUT_PATH)
    print(f"Saved plot to {OUTPUT_PATH}")
