'''
Removal all the characters other than integers from string
'''
# first way
import re
str1 = 'I am 25 years and 10 months old'
x = re.findall("[0-9]", str1)
print(x)
[print(int(num),end="")for num in x ]

print()
# second 

res = "".join([item for item in str1 if item.isdigit()])

print(res)