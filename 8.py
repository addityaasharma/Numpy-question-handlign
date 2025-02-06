import numpy as np

arr = np.array([15, 8, 25, 10])
# ✅ Add 5 to each element.
# ✅ Subtract 3 from each element.
# ✅ Multiply each element by 2.
# ✅ Divide each element by 5.
# ✅ Find the remainder when each element is divided by 4.

print(arr+5)
print(arr-3)
print(arr*2)
print(arr/5)
remainder = arr/4
print(np.mod(arr,4))
