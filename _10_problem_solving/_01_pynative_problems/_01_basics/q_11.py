'''
Write a code to extract each digit from an integer, in the reverse order
'''
num=7536
print("Given number: ", num)
def extract(num):
    while(num>0):
        r=num%10
        num=num//10
        print(r, end=' ')
print("Output: ", end=' ')
extract(num)