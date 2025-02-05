import numpy as np

# Sample fitness tracker data: [User ID, Steps Taken, Calories Burned]
fitness_data = np.array([
    [1, 8500, 300],   # User 1
    [2, 12000, 600],  # User 2
    [3, 9500, 400],   # User 3
    [4, 15000, 750],  # User 4
    [5, 11000, 550],  # User 5
    [6, 5000, 200],   # User 6
    [7, 18000, 900],  # User 7
    [8, 7500, 350],   # User 8
    [9, 13000, 650],  # User 9
    [10, 10500, 520]  # User 10
])

#days more then 10,000 steps and burns more then 500 calories.

steps = (fitness_data[:,1]>10000) & (fitness_data[:,2]>500)
print(fitness_data[steps])
