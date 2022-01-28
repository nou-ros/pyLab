def sumOfDigits(arr):
    newArr = []
    for value in arr:
        add = 0
        while(value > 0):
            temp = value % 10
            add += temp
            value = value//10
        newArr.append(add)
    return newArr

values = [12, 67, 98, 34]
print(sumOfDigits(values))

