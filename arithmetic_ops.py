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

# # Adding a scalar
# print(arr2 + 3)
# print()
# # Element-wise subtraction
# print(arr3 - arr2)
# print()
# # Division by scalar
# print(arr2 / 2)
# print()
# # Element-wise multiplication
# print(arr2 * arr3)
# print()
# # Modulus with scalar
# print(arr2 % 4)

# arr5 = np.array([2, 3])
# print(arr5.shape)

print('---Logical Operations---')
arr1 = np.array([[1, 2, 3], [3, 4, 5]])
arr2 = np.array([[2, 2, 3], [1, 2, 3]])

print(f"arr1:\n{arr1}")
print()
print(f"arr2:\n{arr2}")

print(f'\n arr1 == arr2 \n{arr1 == arr2}')
print(f'\n arr1 != arr2 \n{arr1 != arr2}')
print(f'\n arr1 >= arr2 \n{arr1 >= arr2}')
print(f'\n arr1 < arr2 \n{arr1 < arr2}')
print(f'\n(arr1 == arr2).sum(): {(arr1 == arr2).sum()}')


print('\n\n---Array indexing and slicing---\n')
arr3 = np.array([
    [[11, 12, 13, 14],
    [13, 14, 15, 19]],

    [[15, 16, 17, 21],
    [63, 92, 36, 18]],

    [[98, 32, 81, 23],
    [17, 18, 19.5, 43]]
])
print(f"arr3:\n{arr3}")
print(arr3.shape)
print()

# Single Element
print(arr3[1, 1, 2])
print()

# Subarray using ranges
print(arr3[1:, :1, :2])
print(arr3[1:, :1, :2].shape)
print()

# Mixing indices and ranges
print(arr3[1:, 1, 3])
print(arr3[1:, 1, 3].shape)
print()

print(arr3[:, 1, :3])
print(arr3[:, 1, :3].shape)
print()

# Using fewer indices
print(arr3[:2, 1])
print(arr3[:2, 1].shape)
print()

# Using too many indices
# print(arr3[1, 3, 2, 1]) -> IndexOutOfRange
