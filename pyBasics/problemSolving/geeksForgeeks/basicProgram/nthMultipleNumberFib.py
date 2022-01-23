#nth multiple of a number in fibonacci series. nth multiple of k, input: k = 2 and n = 3 output: 9 -> 34
def findPosition(k, n):
    f1 = 0
    f2 = 1
    i = 2;
    while i != 0:
        f3 = f1 + f2
        f1 = f2
        f2 = f3
        if f2 % k == 0:
            return n*i
        i += 1
    return 

n = 4
k = 2
print("Position of n'th multiple of k in Fibonacci series: ", findPosition(k, n))
