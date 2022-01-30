def addMatrix(matrix1, matrix2):
    result = [[0]*3]*3
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result[i][j] = matrix1[i][j] + matrix2[i][j]

    return result

def addMatrixTwo(matrix1, matrix2):
    result = [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

    for r in result:
        print(r)

x = [[1,2,3], [4, 5, 6], [7, 8, 9]]
y = [[9,8,7], [6,5,4], [3, 2, 1]]

print(addMatrix(x,y))
print(addMatrixTwo(x, y))
