import numpy as np

# Sample student performance data: [Student ID, Math Score, Science Score, English Score]
student_data = np.array([
    [1, 85, 92, 88],  # Student 1
    [2, 78, 80, 70],  # Student 2
    [3, 90, 94, 85],  # Student 3
    [4, 65, 70, 60],  # Student 4
    [5, 95, 98, 92],  # Student 5
    [6, 70, 72, 75],  # Student 6
    [7, 88, 85, 80],  # Student 7
    [8, 84, 89, 90],  # Student 8
    [9, 77, 75, 78],  # Student 9
    [10, 91, 92, 93]  # Student 10
])

# Use this data to answer the question:
# Find out which students have scored above 80 in all subjects.

marks = (student_data[:, 1:] > 80).all(axis=1)  # .all(axis=1) ensures all subjects for a student

print(student_data[marks])
