import math

def recFact(n):
    return 1 if(n == 1 or n == 0) else n * recFact(n - 1);

def iterFact(n):
    if n < 0:
        return 0;
    elif n == 0 or n == 1:
        return 1;
    else:
        fact = 1
        while(n > 1):
            fact *= n;
            n -= 1;
        return fact

def builtFact(n):
    return(math.factorial(n))

num = 5;
print("(Recursion)Factorial of: ", num, " is ", recFact(num));
print("(Iterative)Factorial of: ", num, " is ", iterFact(num));
print("(Built in function)Factorial of: ", num, " is ", builtFact(num));


