def nLargestElement(arr, n):
    newArr = []
    for i in range(0, n):
        max1 = 0
        for j in range(len(arr)):
            if(arr[j] > max1):
                max1 = arr[j]
        arr.remove(max1)
        newArr.append(max1)
    print(newArr)

def nLargestElementTwo(arr, n):
    arr.sort()
    return arr[-n:]


    
arr = [4, 5, 1, 2, 9]
n = 2
nLargestElement(arr, n)
arr2 = [1000, 298, 2512, 100, 200, -45, 900]
print(nLargestElementTwo(arr2, n))
