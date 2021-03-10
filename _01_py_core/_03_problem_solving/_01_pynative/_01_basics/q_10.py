'''
Given a two list of numbers create a new list such that new list should contain only odd numbers from the first list and even numbers from the second list
First List  [10, 20, 23, 11, 17]
Second List  [13, 43, 24, 36, 12]

result List is [23, 11, 17, 24, 36, 12]
'''
first = [10, 20, 23, 11, 17]
second = [13, 43, 24, 36, 12]
new = []

for i in first:
    if i%2!=0:
        new.append(i)

for j in second:
    if j%2==0:
        new.append(j)

print(new)