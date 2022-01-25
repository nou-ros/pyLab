def isMonotonic(arr):
    return (all(arr[i] <= arr[i+1]  for i in range(len(arr) - 1)) or all(arr[i] >= arr[i+1] for i in range(len(arr) - 1)))

array = [6, 5, 4, 4]
print(isMonotonic(array))
