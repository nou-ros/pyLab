def printDuplicate(arr):
    newArr = []
    for i in range(0, len(arr) - 1):
        count = 0
        for j in range(i, len(arr)-1):
            if arr[j] == arr[i]:
                count += 1
        if(count > 1):
            if arr[i] not in newArr:
                newArr.append(arr[i])
    return newArr


arr = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
print(printDuplicate(arr))

