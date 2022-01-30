def multiplyMatrix(matrix1, matrix2):
    result = [[0, 0, 0, 0], [0, 0 , 0, 0], [0, 0, 0, 0]]

    # iterate by row of 1
    for i in range(len(matrix1)):
       # iterate by column 2
        for j in range(len(matrix2[0])):
            # iterate by rows of 2
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    for r in result:
        print(r)

matrix1 = [
            [12, 7, 3],
            [4, 5, 6],
            [7, 8, 9]
          ]

matrix2 = [
        [5, 8, 1, 2],
        [6, 7, 3, 0],
        [4, 5, 9, 1]
        ]

multiplyMatrix(matrix1, matrix2)

