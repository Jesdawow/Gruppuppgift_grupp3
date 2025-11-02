# Class to make writing in notebook easier. Collects every function & loads all the data from io_utils, metrics & viz files

from src.io_utils import load_data, coerce_data_types # Loads everything from io_utils
from src.metrics import( # Loads everything from metrics
    total_revenue,
    average_order_value,
    total_units,
    revenue_by_category,
    revenue_by_city,
    order_value_std,
    check_revenue_integrity,
    average_price_by_category,
)
from src.viz import ( # Loads everything from viz
    plot_revenue_over_time,
    plt_revenue_by_category,
)
from src.paths import ECOMMERCE_FILE # Loads the file path from paths

class Ecommerce_Analysis:
    def __init__(self):
        df = load_data(ECOMMERCE_FILE) # Loads the data from io_utils
        self.data = coerce_data_types(df) # Makes sure all the datatypes are correct (from io_utils)

    def show_summary(self):
        # Can print out a summary of key metrics (If needed)
        print(f"Total revenue: {total_revenue(self.data):,.0f} kr")
        print(f"Average Order Value: {average_order_value(self.data):,.2f} kr")
        print(f"Total units sold: {total_units(self.data):,.0f} units.")
        print(f"Standard deviation (order variation): {order_value_std(self.data):,.0f} kr")
        print("Top-3 categories by revenue(kr):")
        print(revenue_by_category(self.data).head(3).to_string(index=True, header=False))
        print("Revenue by city(kr)")
        print(revenue_by_city(self.data).to_string(index=True, header=False))
        print()
        if check_revenue_integrity(self.data):
            print("Data integrity check passed: revenue = price x units")
        else:
            print("Warning: revenue column does not match price x units")
        
    def top_categories(self, n: int = 3):
        # Returns the most profitable categories (n)
        return revenue_by_category(self.data).head(n)
    
    def top_cities(self, n: int =3):
        # Returns the most cities with the most profit (n)
        return revenue_by_city(self.data).head(n)
    
    def plot_revenue_over_time(self) -> None:
        # Plots revenue_over_time directly from viz
        plot_revenue_over_time(self.data)

    def plot_revenue_by_category(self) -> None:
        # Plots revenue_by_category directly from viz
        plt_revenue_by_category(self.data)
    
    def order_stats(self):
        # Returns average order value & STD
        aov = average_order_value(self.data)
        std = order_value_std(self.data)
        return aov, std