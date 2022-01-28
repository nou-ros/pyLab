def cloneList(arr):
    newArr = arr[:]
    return newArr

def cloneListTwo(arr):
    newArr = []
    newArr.extend(arr)
    return newArr
arr = [4, 8, 2, 10, 15, 18]
print(cloneList(arr))
print(cloneListTwo(arr))

