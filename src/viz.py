# File to create all graphs & charts.

import matplotlib.pyplot as plt
from src.metrics import revenue_over_time, revenue_by_category
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
    revenue_cat = revenue_by_category(df)
    fig, ax = plt.subplots(figsize=(9, 4))

    x = _cat_for_plot(revenue_cat.index)
    y = _num_for_plot(revenue_cat.values / 1000)
    ax.bar(x, y)
    ax.set_title("Revenue per category", fontsize=14, fontweight="bold")
    ax.set_xlabel("Category")
    ax.set_ylabel("Revenue (kSEK)")
    ax.grid(True, axis="y")
    plt.savefig("images/fig_revenue_by_category.png", dpi=200)
    plt.show()
    


def plot_revenue_over_time(df):
    monthly_revenue = revenue_over_time(df, freq='ME')
    monthly_revenue.index = monthly_revenue.index.strftime("%b %Y")

    plt.figure(figsize=(9, 4))
    plt.plot(monthly_revenue.index, monthly_revenue.values, marker='o', linestyle='-')
    plt.title("Income over time (per month)",fontsize=14, fontweight="bold")
    plt.xlabel("Month")
    plt.ylabel("Revenue (kr)")
    plt.xticks(rotation=45)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.savefig("images/fig_revenue_over_time.png", dpi=200)
    plt.show()
