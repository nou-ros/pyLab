def matrixProduct(matrix):
    mul = 1
    for list in matrix:
        for i in list:
            mul *= i
    return mul

matrix = [[1, 4, 5], [7, 3], [4], [46, 7, 3]]
print(matrixProduct(matrix))

