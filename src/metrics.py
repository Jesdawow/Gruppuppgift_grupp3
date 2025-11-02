# All functions go in here.
import pandas as pd
import numpy as np

def total_revenue(df: pd.DataFrame) -> float:
    # Calculates total revenue.
    return np.sum(df["revenue"].to_numpy())

def average_order_value (df: pd.DataFrame) -> float:
    # Calculates Average Order Value (AoV)
    orders = df.groupby("order_id", observed=True)["revenue"].sum().to_numpy()
    return np.mean(orders)

def total_units(df: pd.DataFrame) -> int:
    # Returns total number of units sold
    return np.sum(df["units"].to_numpy())

def revenue_by_category(df: pd.DataFrame) -> pd.DataFrame:
    # Returns revenue by category
    return df.groupby("category", observed=True)["revenue"].sum().sort_values(ascending=False)


def revenue_by_city(df):
    # Returns revenue by city
    return df.groupby("city", observed=True)["revenue"].sum().sort_values(ascending=False)

def revenue_over_time(df: pd.DataFrame, freq: str = "ME") -> pd.DataFrame:
    if freq == "M":
        freq = "ME"
    # Returns revenue over time per month
    return df.set_index("date").resample(freq)["revenue"].sum()

def order_value_std(df: pd.DataFrame) -> float:
    # Returns standard deviation (STD) of order value (If needed)
    orders = df.groupby("order_id", observed=True)["revenue"].sum().to_numpy()
    return np.std(orders)

def check_revenue_integrity(df: pd.DataFrame) -> bool:
    # Controls that revenue = price * units in all rows (Not meant to be used, just to check)
    calculated = df["price"].to_numpy() * df["units"].to_numpy()
    return np.allclose(df["revenue"].to_numpy(), calculated)

def revenue_mismatch(df: pd.DataFrame) -> pd.DataFrame:
    # Finds rows where revenue is not equal to price * units
    return df[df["revenue"] != df["price"] * df["units"]]

def low_revenue_categories(df: pd.DataFrame, quantile: float = 0.2) -> pd.DataFrame:
    # Returns categories in the lowest 20% revenue
    cat_rev = df.groupby("category", observed=True)["revenue"].sum().reset_index()
    threshold = cat_rev["revenue"].quantile(quantile)
    return cat_rev[cat_rev["revenue"] <= threshold].sort_values("revenue")

def high_revenue_categories(df: pd.DataFrame, quantile: float = 0.8) -> pd.DataFrame:
    # Returns categories in the highest 20% revenue
    cat_rev = df.groupby("category", observed=True)["revenue"].sum().reset_index()
    threshold = cat_rev["revenue"].quantile(quantile)
    return cat_rev[cat_rev["revenue"] >= threshold].sort_values("revenue", ascending=False)

def high_revenue_days(df: pd.DataFrame, quantile: float = 0.99) -> pd.DataFrame:
    # Returns dates with the daily revenue top 1%
    daily_rev = df.groupby("date", observed=True)["revenue"].sum().reset_index()
    threshold = daily_rev["revenue"].quantile(quantile)
    return daily_rev[daily_rev["revenue"] > threshold].sort_values("revenue", ascending=False)