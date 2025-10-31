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
    ax.set_title("Revenue per category")
    ax.set_xlabel("Category")
    ax.set_ylabel("Revenue (kSEK)")
    ax.grid(True, axis="y")
    plt.savefig("images/fig_revenue_by_category.png", dpi=200)
    plt.show()
    


def plot_revenue_over_time(df):
    monthly_revenue = revenue_over_time(df, freq='ME')

    plt.figure(figsize=(10, 6))
    plt.plot(monthly_revenue.index.astype(str), monthly_revenue.values, marker='o', linestyle='-')
    plt.title("Intäkt över tid (per månad)")
    plt.xlabel("Månad")
    plt.ylabel("Intäkt (kr)")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
