def cumulativeSum(arr):
    newArr = []
    for i in range(0, len(arr)):
        if i != 0:
            add = arr[i] + newArr[i - 1]
            newArr.append(add)
        else:
            newArr.append(arr[i])
    return newArr

def cumulativeSumTwo(arr):
    newArr = []
    val = 0
    for i in range(0, len(arr)):
        val += arr[i]
        newArr.append(val)
    return newArr
arr = [10, 20, 30, 40, 50]
print(cumulativeSum(arr))
print(cumulativeSumTwo(arr))



