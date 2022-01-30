def transposeMatrix(matrix):
    res = [[0, 0, 0], [0, 0, 0]] 
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            res[i][j] = matrix[j][i]

    return res

mat = [[1, 2], [3, 4], [5, 6]]
print(transposeMatrix(mat))
