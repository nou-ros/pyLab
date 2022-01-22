def order(x):
    n = 0
    while(x != 0):
        n = n + 1
        x = x // 10
    return n

def power(x, y):
    if y == 0:
        return 1
    return x**y


def isArmstrong(x):
    n = order(x);
    temp = x;
    add = 0;

    while(temp != 0):
        r = temp % 10
        add = add + power(r, n)
        temp = temp // 10

    return (add == x)

x = 153
print(isArmstrong(x))
x = 1253
print(isArmstrong(x))


