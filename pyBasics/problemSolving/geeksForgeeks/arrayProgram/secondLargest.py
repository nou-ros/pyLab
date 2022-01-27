def secondLarge(arr):
    second = arr[0]
    first = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > first:  
            second = first
            first = arr[i]
        elif arr[i] < first and arr[i] != second:
            second = arr[i]
    return second

def secondLargeTwo(arr):
    arr.sort()
    return arr[-2]
 

arr = [2, 0, 9, 7, 8, 3, 6]
print(secondLarge(arr))
print(secondLargeTwo(arr))
