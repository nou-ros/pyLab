''' From given string replace each punctuation with #'''
from string import punctuation

str1 = '/*Jon is @developer & musician!!'
print("The original string is : ", str1)

# Replace punctuations with #
replace_char = '#'

# Using string.punctuation to get the list of all punctuations
# use string function replace() to replace each punctuation with #

for char in punctuation:
    str1 = str1.replace(char, replace_char)

print("The strings after replacement : ", str1)