'''
Write a recursive function to calculate the sum of numbers from 0 to 10
'''

def rec(num):
    if num:
        return num + rec(num-1)
    else:
        return 0

res = rec(10)
print(res)