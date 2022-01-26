def swapElement(arr):
    size = len(arr)
    temp = arr[0]
    arr[0] = arr[size - 1]
    arr[size - 1] = temp;
    return arr

def swapElementTwo(arr):
    arr[0], arr[-1] = arr[-1], arr[0]
    return arr

def swapElementThree(arr):
    get = arr[-1], arr[0]
    arr[0], arr[-1] = get
    return arr

def swapElementFour(arr):
    start, *middle, end = arr
    arr = [end,*middle,start]
    return arr

def swapElementFive(arr):
    first = arr.pop(0)
    last = arr.pop(-1)
    arr.insert(0, last)
    arr.append(first)
    return arr

array = [12, 35, 9, 56, 24]
print(swapElement(array))
#print(swapElementTwo(array))
#print(swapElementThree(array))
#print(swapElementFour(array))
#print(swapElementFive(array))
