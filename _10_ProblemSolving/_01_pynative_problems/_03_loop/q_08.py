'''
Reverse the following list using for loop
list1 = [10, 20, 30, 40, 50]
'''

list1 = [
        10,
        20,
        30,
        40,
        50
        ]

print(list1[::-1])

print()

length= len(list1)-1
for i in range(length, 0, -1):
    print(list1[i])