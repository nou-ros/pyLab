def maximum(a, b):
    if a >= b:
        return a
    else:
        return b

a = 2
b = 4
# first approach
print(maximum(a, b))
# second approach
print(max(a, b))
# third approach
print(a if a >= b else b)
