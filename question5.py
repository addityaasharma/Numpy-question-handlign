import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Sample sales data: [Month, Sales Amount ($), Items Sold, Discount Given (%)]
sales_data = np.array([
    [1, 120000, 600, 10],  # January
    [2, 95000, 450, 8],    # February
    [3, 135000, 700, 12],  # March
    [4, 80000, 400, 7],    # April
    [5, 150000, 750, 15],  # May
    [6, 110000, 500, 9],   # June
    [7, 125000, 650, 11],  # July
    [8, 145000, 720, 13],  # August
    [9, 90000, 480, 8],    # September
    [10, 160000, 800, 16], # October
    [11, 170000, 850, 18], # November
    [12, 95000, 430, 9]    # December
])

# Columns Explanation:
# Month (1-12): Represents January to December.
# Sales Amount ($): Total revenue generated in that month.
# Items Sold: Number of items sold in that month.
# Discount Given (%): Discount percentage applied on sales.

#  Find total revenue after discount for months where sales > $100,000 and items sold > 500.
#  Identify the month with the highest discount among these selected months.

sales = np.where(sales_data[:,1]>100000)
total_rev = sales_data[sales]
print(total_rev[:,1])
print(total_rev[:,3])

# print(np.column_stack((total_rev[:,1], total_rev[:,3])))
z=0
for row in total_rev:
    i = row[1]
    j = row[3]
    k = (i/100)*j
    print(k)
    z= k + z

# print('Value are',k)
sns.histplot(total_rev)
plt.show()
