'''
Remove empty strings from a list of strings
'''
# 1
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
newstr = []

for i in str_list:
    if i is not None and i != '':
        newstr.append(i)

print(newstr)

# 2
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
print("Original list of sting")
print(str_list)

# use built-in function filter to filter empty value
new_str_list = list(filter(None, str_list))

print("After removing empty strings")
print(new_str_list)