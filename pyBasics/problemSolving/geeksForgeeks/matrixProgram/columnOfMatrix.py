def nthColumn(matrix, col):
    res = [sub[col] for sub in matrix]
    return res;

def nthColumnTwo(matrix, col):
    res = []
    for sub in matrix:
        res.append(sub[col])
    return res

            
matrix = [[4, 5, 6], [8, 1, 10], [7, 12, 5]]
col = 2
print(nthColumn(matrix, col))
print(nthColumnTwo(matrix, col))
