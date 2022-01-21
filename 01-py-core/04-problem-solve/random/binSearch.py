def binarySearch(arr, target):
    left = 0
    right = len(arr)-1

    while(left<=right):
        mid = (left+right)//2

        if(arr[mid]==target):
            return mid
        elif(arr[mid]<target):
            left = mid+1
        else:
            right = mid-1
    
    return -1
    
arr = [1,2,3,4,5,6]
target = 6
res = binarySearch(arr, target)

if res != -1:
    print("Element is found at index %d", res)
else:
    print("Element not found.")