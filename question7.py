import numpy as np

# Sample customer purchase data: [Purchase Amount ($), Items Bought, Customer Age, Repeat Customer (1 = Yes, 0 = No)]
customer_data = np.array([
    [150, 3, 25, 1],  # Customer 1: $150, 3 items, age 25, repeat customer
    [220, 6, 30, 0],  # Customer 2: $220, 6 items, age 30, new customer
    [180, 4, 28, 1],  # Customer 3: $180, 4 items, age 28, repeat customer
    [350, 8, 40, 0],  # Customer 4: $350, 8 items, age 40, new customer
    [210, 7, 35, 1],  # Customer 5: $210, 7 items, age 35, repeat customer
    [190, 5, 27, 0],  # Customer 6: $190, 5 items, age 27, new customer
    [300, 10, 50, 1], # Customer 7: $300, 10 items,age 50, repeat customer
    [150, 2, 22, 0],  # Customer 8: $150, 2 items, age 22, new customer
    [400, 12, 45, 1], # Customer 9: $400, 12 items,age 45, repeat customer
    [250, 9, 38, 0]   # Customer 10: $250, 9 items,age 38, new customer
])

# Find customers who spent more than $300 and bought at least 10 items.- Done
# What is the average purchase amount of repeat customers?
# Identify the oldest customer who bought less than 3 items.

customer1 = (customer_data[:,0]>300) & (customer_data[:,1]>9)
print(customer_data[customer1])

total_customer = 0
total_item = 0
for i in customer_data:
    item = i[0]
    rep_customer = i[3]
    if rep_customer == 1:
        total_customer = total_customer + rep_customer
        total_item = total_item + item
    else:
        continue
    final_answer = total_item/total_customer

print("Average purchase amount is",final_answer)
