'''
Reverse a given number and return true if it is the same as the original number
'''
num = 124
s=0
l_num=num
while(l_num>0):
    r=l_num%10
    s=s*10+r
    l_num=l_num//10

print("Original number: ", num)
print(f"Reverse of {num} is: ", s)

if (s==num):
    print("The original and reverse number is the same.")
else:
    print("The original and the reverse number is not same.")
