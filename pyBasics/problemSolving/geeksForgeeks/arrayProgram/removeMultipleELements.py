def removeMultiple(arr, unwantedList):
    return [ele for ele in arr if ele not in unwantedList]

arr = [11, 5, 17, 18, 23, 50]
unwantedList = [11, 5]
print(removeMultiple(arr, unwantedList))

