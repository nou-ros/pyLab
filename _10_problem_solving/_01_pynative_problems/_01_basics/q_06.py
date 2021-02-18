"""
Given a list of numbers, Iterate it and print only those numbers which are divisible of 5
"""

def divisible(num=None):
    for i in num:
        if i%5==0:
            print(i)

num = [10,20,33,46,55]
print("Divisible of 5 in a list: ",num)
divisible(num)