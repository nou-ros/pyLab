def removeEmptyList(arr):
    res = [ele for ele in arr if ele != []]
    return res

def removeEmptyListTwo(arr):
    res = list(filter(None, arr))
    return res

arr = [5, 6, [], 3, [], [], 9]
print(removeEmptyList(arr))
print(removeEmptyListTwo(arr))
