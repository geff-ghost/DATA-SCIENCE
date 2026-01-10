
weights = [0.3, 0.2, 0.5]

kanto = [73, 67, 43]
johto = [91, 88, 64]
hoenn = [87, 134, 58]
sinnoh = [102, 43, 37]
unova = [69, 96, 70]

def crop_yield(region, weights):
    result = 0
    for r, w in zip(region, weights):
        result += r * w
    return result

print(f'Crop yield for Kanto: {crop_yield(kanto, weights)}')
print(f'Crop yield for Johto: {crop_yield(johto, weights)}')
print(f'Crop yield for Unova: {crop_yield(unova, weights)}')
