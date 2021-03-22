'''
1  
2 2  
3 3 3  
4 4 4 4  
5 5 5 5 5

for i in range(1, 6):
    for j in range(i):
        print(i, end='')
    print()
'''
'''
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5

for i in range(1, 6):
    for j in range(i):
        print(j+1, end=' ')
    print()
'''

'''
1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5

b = 0
for i in range(5, 0, -1):
    b+=1
    for j in range(1, i+1):
        print(b, end='')
    print()
'''
'''
5 5 5 5 5 
5 5 5 5 
5 5 5 
5 5 
5

b=5
for i in range(5, 0, -1):
    for j in range(1, i+1):
        print(b, end='')
    print()
'''

'''
0 1 2 3 4 5 
0 1 2 3 4 
0 1 2 3 
0 1 2 
0 1

for i in range(6, 1, -1):
    b=0
    for j in range(1, i+1):
        print(b, end=' ')
        b+=1
    print()
'''
'''
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1

for i in range(5, 0, -1):
    for j in range(i):
        print(i, end=' ')
    print()
'''

'''
1 
2 1 
3 2 1 
4 3 2 1 
5 4 3 2 1

for i in range(5):
    for j in range(i+1, 0, -1):
        print(j, end=' ')
    print()

'''
'''
1 
3 3 
5 5 5 
7 7 7 7 
9 9 9 9 9

b=1
for i in range(1, 6):
    for j in range(i):
        print((i*2-1), end=" ")
    print()
'''

'''
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1

for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print()
'''



'''
1
3 2
6 5 4
10 9 8 7
'''
start = 1
stop = 2
current_num = stop
for row in range(2, 6):
    for col in range(start, stop):
        current_num -= 1
        print(current_num, end=' ')
    print("")
    start = stop
    stop += row
    current_num = stop
 
'''
*
**
* *
*  *
*****
n = int(input("Enter the number of rows: "))
for row in range(n):
    for col in range(n):
        if col == 0 or row==(n-1) or row==col:
            print("*", end='')
        else:
            print(end=" ")
    print()

'''
