'''
Find all occurrences of “USA” in given string ignoring the case
'''
str1 = "Welcome to USA. usa awesome, isn't it?"

str2 = str1.lower()
sub = 'usa'
c = str2.count(sub)

print(c)