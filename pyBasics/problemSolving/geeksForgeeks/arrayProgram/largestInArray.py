def largestElement(arr):
    maximum = arr[0]
    for i in arr:
        if maximum < i:
            maximum = i
    return maximum

print("Largest value in array: ", largestElement([12, 18, 5, 21, 9, 4]))
