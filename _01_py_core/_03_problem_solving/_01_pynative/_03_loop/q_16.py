'''
Find the sum of the series 2 +22 + 222 + 2222 + .. n terms
'''
numb_of_terms = 5

start = 2
s = 0

for i in range(numb_of_terms):
    print(start, end=" ")
    s+= start
    start = (start*10)+2
    
print("\nSum of above series is:", s)