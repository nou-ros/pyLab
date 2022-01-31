def verticalConcat(matrix):
    res = []
    n = 0
    while n != len(matrix):
        temp = ''
        for idx in matrix:
            try: temp = temp + idx[n]
            except IndexError: pass 
        res.append(temp)
        n += 1
    
    ans = [ele for ele in res if ele]
    print(ans)



matrix = [["Hello ", "I "], ["world, ", "am "], ["Initiated!", "Nouros"]]
verticalConcat(matrix)


