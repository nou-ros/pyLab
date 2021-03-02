'''
Given a two integer numbers return their product and if the product is greater than 1000, then return their sum
'''

print("Enter two numbers")
num_1 = int(input())
num_2 = int(input())
prod = num_1*num_2

if(prod<1000):
    print("Product of the numbers: ",prod)
else:
    add = num_1+num_2
    print("Addition of the numbers: ", add) 
