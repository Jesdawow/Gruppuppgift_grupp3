import pandas as pd

REQUIRED = ["order_id", "date", "city", "category", "price", "units", "revenue"]

def load_data(file_path: str) -> pd.DataFrame:  
    """
    Reads data from a CSV file and creates a DataFrame.
    """
    df = pd.read_csv(file_path, encoding="utf-8", parse_dates=["date"]) #Ensures date column is parsed as datetime
    missing = [col for col in REQUIRED if col not in df.columns]
    if missing:
        raise ValueError(f"Missing columns in dataframe: {missing}") #Check for required columns
    return df

def coerce_data_types(df: pd.DataFrame) -> pd.DataFrame:
    """
    Coerces DataFrame columns to appropriate data types.
    """
    out = df.copy() # Avoid modifying original dataframe

    # Convert categorical columns to type category
    out["city"] = out["city"].astype("category")
    out["category"] = out["category"].astype("category")

    # to_numeric with errors="coerce" converts invalid parsing to NaN and returns a float64 by default
    # Int64:
    out["order_id"] = pd.to_numeric(out["order_id"], errors="coerce").astype("Int64")
    out["units"] = pd.to_numeric(out["units"], errors="coerce").astype("Int64")  
    # DateTime:
    out["date"] = pd.to_datetime(out["date"], errors="coerce")
    # Float64:
    out["price"] = pd.to_numeric(out["price"], errors="coerce") #.astype("Float64")  
    out["revenue"] = pd.to_numeric(out["revenue"], errors="coerce") #.astype("Float64") 
    return out

def top_cities(df, n =int):
    return ((df.groupby("city")["revenue"].agg("sum").sort_values(ascending=False).head(n))/1000).round(1)