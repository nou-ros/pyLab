def sortList(arr1, arr2):
    zippedPairs = zip(arr2, arr1)
    return [x for _, x in sorted(zippedPairs)]


list1 = ["a", "b", "c", "d", "e", "f", "g", "h"]
list2 = [0, 1, 1, 0, 1, 2, 2, 0, 1]
print(sortList(list1, list2))


