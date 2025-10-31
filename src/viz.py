# File to create all graphs & charts.

import matplotlib.pyplot as plt
from src.metrics import revenue_over_time

def plot_revenue_over_time(df):
    monthly_revenue = revenue_over_time(df, freq='ME')
    monthly_revenue.index = monthly_revenue.index.strftime("%b %Y")

    plt.figure(figsize=(10, 6))
    plt.plot(monthly_revenue.index.astype(str), monthly_revenue.values, marker='o', linestyle='-')
    plt.title("Intäkt över tid (per månad)")
    plt.xlabel("Månad")
    plt.ylabel("Intäkt (kr)")
    plt.xticks(rotation=45)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.show()