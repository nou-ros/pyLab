'''
Python program to display all the prime numbers within a range
'''
start = 25
end = 50
print(f"Prime numbers between {start} and {end}: ")

for i in range(start, end+1):
    for j in range(2, i):
        if (i%j)==0:
            break
    else:
        print(i)
