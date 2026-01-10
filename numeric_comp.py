import numpy as np

weights = np.array([0.3, 0.2, 0.5])

kanto = np.array([73, 67, 43])
johto = np.array([91, 88, 64])
hoenn = np.array([87, 134, 58])
sinnoh = np.array([102, 43, 37])
unova = np.array([69, 96, 70])

def crop_yield(region, weights):
    result = 0
    for r, w in zip(region, weights):
        result += r * w
    return result

# print(f'Crop yield for Kanto: {crop_yield(kanto, weights)}')
# print(f'Crop yield for Johto: {crop_yield(johto, weights)}')
# print(f'Crop yield for Unova: {crop_yield(unova, weights)}')

print(type(kanto))
print(type(weights))

# Indexing in Numpy
print(weights[0])
print(unova[2])

# Operating on Numpy arrays
print(f'\nnp.dot function: {np.dot(kanto, weights)}')

print(f'\nUsing *: {(kanto * weights).sum()}')

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print(arr1 * arr2)
print(arr1 + arr2)
