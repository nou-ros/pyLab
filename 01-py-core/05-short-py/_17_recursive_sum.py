numb = [2,4,6]
s, i = 0, 0
# print(numb[-1])
def recursive_sum(numb):
    if len(numb)==1:
        return numb[0]
    else:
        return numb[0]+recursive_sum(numb[1:])

print(recursive_sum(numb))