'''
Write a function calculation() such that it can accept two variables and calculate the addition and subtraction of it. And also it must return both addition and subtraction in a single return call
'''

# way 1
def calculate(num1, num2):
    add = num1 + num2
    sub = num1 - num2
    return f"addition: {add} and subtraction: {sub}"

res = calculate(40, 10)
print(res)

# way 2 
def calculation(a, b):
    return a+b, a-b

res = calculation(40, 10)
print(res)

# way 3
def calculation(a, b):
    return a+b, a-b

add, sub = calculation(40, 10)
print(add)
print(sub)