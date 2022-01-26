def reverseFirst(arr):
    return [ele for ele in reversed(arr)]

def reverseSecond(arr):
    arr.reverse()
    return arr

def reverseThird(arr):
    return arr[::-1]

arr = [10, 11, 12, 13, 14, 15]
print(reverseFirst(arr))
print(reverseThird(arr))
print(reverseSecond(arr))

