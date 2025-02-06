import numpy as np

A = np.array([[2, 3], [5, 7]])
B = np.array([[1, 4], [6, 8]])

# ✅ Compute the dot product of A and B.
# ✅ Compute the matrix multiplication of A and B.
# ✅ Find the inverse of A.
# ✅ Compute the determinant of A.

print(np.dot(A,B))
print(np.matmul(A,B))
print(np.linalg.inv(A))
print(np.linalg.det(A))
