numb = int(input("Enter a number: "))

def fact(numb):
    if numb==1:
        return 1
    else:
        return numb * fact(numb-1)

print(f'Factorial of {numb} is: {fact(numb)}')