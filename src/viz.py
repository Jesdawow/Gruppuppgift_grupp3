# File to create all graphs & charts.

from cProfile import label
import matplotlib.pyplot as plt
# from src.metrics import revenue_by_category,revenue_over_time 
# Imports functions from metrics to plot the data in viz

import pandas as pd

from src.metrics import revenue_by_category


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

    plt.show()


# def bar(ax, x, y, title, xlabel, ylabel, grid: bool = True, label=None):
#     x = _cat_for_plot(x)
#     y = _num_for_plot(y)
#     ax.bar(x, y)
#     if label:
#         ax.legend()
#     ax.set_title(title)
#     ax.set_xlabel(xlabel)
#     ax.set_ylabel(ylabel)
#     ax.grid(grid, axis="y")
#     return ax

# # Revenue by category bar plot
# def plt_revenue_by_category(df):
#     revenue_cat = revenue_by_category(df)
#     fig, ax = plt.subplots(figsize=(9, 4))
#     bar(ax, revenue_cat["category"], revenue_cat["revenue"]/1000, "Revenue per category", "Category", "Revenue (kSEK)")
#     plt.show()

