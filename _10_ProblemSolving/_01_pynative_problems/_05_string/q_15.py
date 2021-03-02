'''
Remove special symbols/Punctuation from a given string
'''
import string

str1 = "/*Jon is @developer. & musician?"
str2 = str1.translate(str.maketrans("","",string.punctuation))
print(str2)

# 2nd way
import re

str3 = re.sub(r'[^\w\s]', '', str1)