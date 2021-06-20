'''
Given a number count the total number of digits in a number
'''
num = int(input("Enter a number: "))
c=0
while(num>0):
    num=num//10
    c+=1

print(c)
