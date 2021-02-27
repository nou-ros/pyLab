'''
Given an input string, count occurrences of all characters within a string
str1 = "Apple"
{'A': 1, 'p': 2, 'l': 1, 'e': 1}
'''
import re

str1 = "Apple"
dic = {}
for char in str1:
    count = str1.count(char)
    dic[char] = count

print(dic)