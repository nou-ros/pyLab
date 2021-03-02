'''
Display Fibonacci series up to 10 terms
'''
def fibonacci(num):
    fir = 0
    sec = 1
    print(fir, end=" ")
    print(sec, end=" ")
    for i in range(1, num-1):
        s = fir + sec
        fir = sec
        sec = s
        print(s, end=" ")

print("Fibonacci series: ")
fibonacci(10)