'''
Given 2 strings, s1 and s2, create a new string by appending s2 in the middle of s1
'''

s1 = "Ault"
s2 = "Kelly"

def adding(str1, str2):
    mid = len(str1)//2
    print("Original string: ", str1)
    newStr = str1[:mid:]+str2+str1[mid:]
    print("New string: ", newStr)

adding(s1, s2)