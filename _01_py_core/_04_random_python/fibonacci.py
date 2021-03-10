
def fibonacci(num):
    first = 0
    second = 1
    # print(first)
    # print(second)
    for i in range(1, num):
        s= first+second
        first=second
        second=s
        print(s)

    # print(s)


fibonacci(10)