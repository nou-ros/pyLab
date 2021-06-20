'''
Reverse a given string
str1 = "PYnative"
evitanYP
'''
# 1
str1 = "PYnative"
rev = str1[::-1]
print(rev)

# 2
str1 = "PYnative"
print("Original String is:", str1)

str1 = ''.join(reversed(str1))
print("Reversed String is:", str1)