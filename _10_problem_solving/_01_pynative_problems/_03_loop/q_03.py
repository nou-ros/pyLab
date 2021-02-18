'''
Accept number from user and calculate the sum of all number between 1 and given number
'''
print("Enter a number: ")
num = int(input())
s = 0
for i in range(1, num+1):
    s+=i

print("Sum of ", num , " numbers: ", s)