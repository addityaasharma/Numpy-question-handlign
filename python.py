import numpy as np
# 1. Sales Data Filtering
# You have a dataset representing sales data of a retail store for the past year, where each row contains data for a specific month (e.g., month, sales_amount, items_sold). You want to extract information based on specific conditions.

# Question: From the sales dataset, extract the months where the sales amount was above $100,000, and the number of items sold was more than 500.
# Hint: Use Boolean indexing to filter out the rows that meet both conditions.


# Sample sales data: [Month, Sales Amount, Items Sold]
sales_data = np.array([
    [1, 120000, 600],   # January
    [2, 95000, 450],    # February
    [3, 135000, 700],   # March
    [4, 80000, 400],    # April
    [5, 150000, 750],   # May
    [6, 110000, 500],   # June
    [7, 125000, 650],   # July
    [8, 145000, 720],   # August
    [9, 90000, 480],    # September
    [10, 160000, 800],  # October
    [11, 170000, 850],  # November
    [12, 95000, 430]    # December
])


sales_amount = (sales_data[:,1]>100000) & (sales_data[:,2]>500)
print(sales_data[sales_amount])
