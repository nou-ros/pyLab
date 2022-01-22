def primeNumbers(x, y):
    primeList = []
    for i in range(x, y):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i/2) + 1):
                if i % j == 0:
                    break
            else:
                primeList.append(i)
    return primeList          

start = 2
end = 7
lst = primeNumbers(start, end)
if len(lst) == 0:
    print("There are no prime numbers in this range")
else:
    print("The prime numbers in this range are: ", lst)
