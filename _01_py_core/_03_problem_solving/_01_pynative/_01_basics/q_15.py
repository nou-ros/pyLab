'''
Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
'''

def exponent(base, exp):
    s=1
    print(f"{base} raises to the power of {exp} is: " , end="")
    for i in range(exp):
        s*=base

    print(s)

exponent(2,5)
