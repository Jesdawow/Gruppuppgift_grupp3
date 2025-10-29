# All functions go in here.

def total_revenue(df):
    # Calculates total revenue.
    return df["revenue"].sum()
def average_order_value (df):
    # Calculates Average Order Value (AoV)
    return df["revenue"].sum() / df["order_id"].nunique()
def total_units(df):
    return df["units"].sum()
def revenue_by_category(df):
    return df.groupby("category")["revenue"].sum().sort_values(ascending=False)
def revenue_by_city(df):
    return df.groupby("City")["revenue"].sum().sort_values(ascending=False)