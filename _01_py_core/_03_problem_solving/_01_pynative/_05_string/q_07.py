'''
String characters balance Test. We’ll say that a String s1 and s2 is balanced if all the chars in the s1 are there in s2. characters position doesn’t matter.
'''
str1 = "Yn"
str2 = "PYnative"

str3 = "hey"
str4 = "hello"

def balance(s1, s2):
    c = True
    for i in s1:
        if i in s2:
            continue
        else:
            c=False
    
    return c
    
print(balance(str3, str4))
