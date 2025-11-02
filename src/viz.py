# File to create all graphs & charts.

import matplotlib.pyplot as plt
from src.metrics import revenue_over_time, revenue_by_category, revenue_by_city
import pandas as pd


def _cat_for_plot(s, missing_label="Okänd"):
    if not hasattr(s, "where"):
        s = pd.Series(s, dtype="object")
    else:
        s = s.astype("object")
    s = s.where(~pd.isna(s), other=missing_label)
    return s


def _num_for_plot(s):
    try:
        return pd.to_numeric(s, errors="coerce").fillna(0)
    except Exception:
        return s


def plt_revenue_by_category(df):
    """
    Bar chart: revenue per category (shows values in kSEK).
    Keeps local styling (bold title, grid) and saves image to images/fig_revenue_by_category.png.
    """
    revenue_cat = revenue_by_category(df)
    fig, ax = plt.subplots(figsize=(9, 4))

    x = _cat_for_plot(revenue_cat.index)
    y = _num_for_plot(revenue_cat.values / 1000)
    ax.bar(x, y, color="#2b7fbf", edgecolor="black")
    ax.set_title("Revenue per category", fontsize=14, fontweight="bold")
    ax.set_xlabel("Category")
    ax.set_ylabel("Revenue (kSEK)")
    ax.grid(True, axis="y")

    # Annotate values (kSEK) above bars
    for i, v in enumerate(y):
        ax.text(i, v, f"{v:,.1f}", ha="center", va="bottom", fontsize=9)

    plt.tight_layout()
    plt.savefig("images/fig_revenue_by_category.png", dpi=200)
    plt.show()


def plot_revenue_over_time(df):
    """
    Line chart: revenue over time. Uses monthly frequency and saves an image.
    """
    monthly_revenue = revenue_over_time(df, freq='ME')
    # keep readable labels
    monthly_revenue.index = monthly_revenue.index.strftime("%b %Y")

    plt.figure(figsize=(10, 6))
    plt.plot(monthly_revenue.index.astype(str), monthly_revenue.values, marker='o', linestyle='-')
    plt.title("Intäkt över tid (per månad)", fontsize=14, fontweight="bold")
    plt.xlabel("Månad")
    plt.ylabel("Intäkt (kr)")
    plt.xticks(rotation=45)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.savefig("images/fig_revenue_over_time.png", dpi=200)
    plt.show()


def plot_revenue_by_city(df):
    """
    Ritar ett stapeldiagram som visar intäkt per stad.
    This comes from origin/main; kept as-is and integrated with local style.
    """
    rev_by_city = df.groupby("city", observed=True)["revenue"].sum().sort_values(ascending=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(rev_by_city.index, rev_by_city.values, color="#1f547a", edgecolor="black")
    ax.set_title("Intäkt per stad")
    ax.set_xlabel("Stad")
    ax.set_ylabel("Intäkt (SEK)")
    ax.tick_params(axis="x", rotation=45)
    ax.ticklabel_format(style="plain", axis="y")

    for i, v in enumerate(rev_by_city.values):
        ax.text(i, v, f"{v:,.0f}".replace(",", " "), ha="center", va="bottom", fontsize=9)

    plt.tight_layout()
    plt.show()


def plot_avg_price_by_category(df):
    """
    Ritar ett stapeldiagram som visar genomsnittligt pris per kategori.
    Sourced from origin/main and kept here to preserve added visualization.
    """
    avg_price = df.groupby("category", observed=True)["price"].mean().sort_values(ascending=False)
    avg_price = avg_price.fillna(0)

    plt.figure(figsize=(10, 5))
    plt.bar(avg_price.index, avg_price.values, color="#24a124", edgecolor="black")
    plt.title("Genomsnittligt pris per kategori")
    plt.xlabel("Kategori")
    plt.ylabel("Genomsnittligt pris (SEK)")
    plt.xticks(rotation=45)

    for i, v in enumerate(avg_price.values):
        plt.text(i, v, f"{v:,.2f}".replace(",", " "), ha="center", va="bottom", fontsize=9)

    plt.tight_layout()
    plt.show()
