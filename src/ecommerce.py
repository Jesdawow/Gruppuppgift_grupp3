# Class to make writing in notebook easier. Collects every function & loads all the data from io_utils, metrics & viz

from src.io_utils import load_data, coerce_data_types # Loads everything from io_utils
from src.metrics import( # Loads everything from metrics
    total_revenue,
    average_order_value,
    total_units,
    revenue_by_category,
    revenue_by_city
)

class Ecommerce_Analysis:
    def __init__(self):
        df = load_data() # Loads the data from io_utils into the class
        self.data = coerce_data_types(df) # Makes sure all the datatypes are correct (from io_utils)

    def summary(self):
        print(f"Total revenue: {total_revenue(self.data):,.0f} kr")
        print(f"Average Order Value: {average_order_value}")
        print(f"Total units sold: {total_units(self.data):,.2f} kr")
    def top_categories(self, n=3):
        return revenue_by_category(self.data).head(n)
    