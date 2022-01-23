import math

def isPerfectSquare(x):
    value = int(math.sqrt(x))
    return value * value == x

def isFibonacci(n):
    first = 5 * n**2 + 4
    second = 5 * n**2 - 4

    return isPerfectSquare(first) or isPerfectSquare(second)

# utility function 
for i in range(1, 11):
    if(isFibonacci(i) == True):
        print(i, " is a fibonacci number.")
    else:
        print(i, " is not a fibonacci number.")

    
