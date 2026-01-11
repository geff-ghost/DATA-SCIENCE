import numpy as np

arr2 = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 1, 2, 3]
])

arr3 = np.array([
    [11, 12, 13, 14],
    [15, 16, 17, 18],
    [19, 11, 12, 13]
])

print(arr2 + arr3)

# Adding a scalar
print(arr2 + 3)
print()
# Element-wise subtraction
print(arr3 - arr2)
print()
# Division by scalar
print(arr2 / 2)
print()
# Element-wise multiplication
print(arr2 * arr3)
print()
# Modulus with scalar
print(arr2 % 4)

arr5 = np.array([2, 3])
print(arr5.shape)


