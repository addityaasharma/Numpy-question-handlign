import numpy as np

# Sample temperature data for 30 days: [Day, Temperature (°C)]
data = np.array([
    [1, -5],  # Day 1, Temperature -5°C
    [2, -2],  # Day 2, Temperature -2°C
    [3, 3],   # Day 3, Temperature 3°C
    [4, 7],   # Day 4, Temperature 7°C
    [5, 12],  # Day 5, Temperature 12°C
    [6, 15],  # Day 6, Temperature 15°C
    [7, 18],  # Day 7, Temperature 18°C
    [8, 20],  # Day 8, Temperature 20°C
    [9, 22],  # Day 9, Temperature 22°C
    [10, 25], # Day 10, Temperature 25°C
    [11, 30], # Day 11, Temperature 30°C
    [12, 33], # Day 12, Temperature 33°C
    [13, 35], # Day 13, Temperature 35°C
    [14, 38], # Day 14, Temperature 38°C
    [15, 40], # Day 15, Temperature 40°C
    [16, 42], # Day 16, Temperature 42°C
    [17, 45], # Day 17, Temperature 45°C
    [18, -3], # Day 18, Temperature -3°C
    [19, 1],  # Day 19, Temperature 1°C
    [20, 5],  # Day 20, Temperature 5°C
    [21, 8],  # Day 21, Temperature 8°C
    [22, -1], # Day 22, Temperature -1°C
    [23, -6], # Day 23, Temperature -6°C
    [24, 4],  # Day 24, Temperature 4°C
    [25, 7],  # Day 25, Temperature 7°C
    [26, 9],  # Day 26, Temperature 9°C
    [27, 11], # Day 27, Temperature 11°C
    [28, -4], # Day 28, Temperature -4°C
    [29, 6],  # Day 29, Temperature 6°C
    [30, 10]  # Day 30, Temperature 10°C
])

# Use this data to answer the question:
# Identify the days when the temperature was below 0°C (freezing) and convert those temperatures to Fahrenheit.
above = data[:,1]<0
farenheit = (data[above,1] * 9/5) + 32
print(farenheit)
