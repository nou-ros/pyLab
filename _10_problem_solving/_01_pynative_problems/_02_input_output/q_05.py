'''
Accept list of 5 float numbers as a input from user
'''
num = []
n = int(input("Enter the list size: "))

for i in range(n):
    print("Enter number at location ",(i+1), ":")
    item=float(input())
    num.append(item)
print()
print("Float number list is: ", num)