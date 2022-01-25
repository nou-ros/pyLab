def arrayMultiply(arr, value):
    mul = 1
    for i in arr: 
        res = i % value
        mul *= res
    return mul % value
a = [100, 10, 5, 25, 35, 14]
val = 11
print(arrayMultiply(a, val))
