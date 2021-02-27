'''
Given a string, return the sum and average of the digits that appear in the string, ignoring all other characters
'''
import re

str1 = "English = 78 Science = 83 Math = 68 History = 65"

x = re.findall('[0-9]+', str1)
s = 0
l = (len(x))
for i in x:
    s+=int(i)

avg = s/l
print("Total Marks: ", s)
print("Average: ", avg)


