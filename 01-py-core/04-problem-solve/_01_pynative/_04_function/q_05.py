'''
Create an inner function to calculate the addition in the following way

- Create an outer function that will accept two parameters a and b

- Create an inner function inside an outer function that will calculate the addition of a and b

- At last, an outer function will add 5 into addition and return it
'''

def outer(a, b):
    a+=2 
    b+=2
    def inner():
        add = a + b
        return add

    s=inner() + 5
    return s

print(outer(5, 10))

