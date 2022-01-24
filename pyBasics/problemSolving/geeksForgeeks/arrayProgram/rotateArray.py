def rotateArray(arr, length, rotateElement):
    temp = []
    i = 0
    while(i < rotateElement):
        temp.append(arr[i])
        i = i + 1
    i = 0
    while(rotateElement < length):
        arr[i] = arr[rotateElement]
        i = i + 1
        rotateElement = rotateElement + 1
    arr[:] = arr[:i] + temp
    return arr

arr = [1, 2, 3, 4, 5, 6, 7]
print(rotateArray(arr, len(arr), 2))
