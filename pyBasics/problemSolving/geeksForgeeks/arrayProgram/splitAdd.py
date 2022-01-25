def splitAdd(a, k):
    b = a[:k]
    return (a[k:] + b[:])

arr = [12, 10, 5, 6, 52, 36]
position = 2
newArr = splitAdd(arr, position)
for i in newArr:
    print(i, end = ' ')

