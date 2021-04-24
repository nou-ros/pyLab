import requests

user_input = input("Enter a phrase: ").split()
print(user_input)
a = ""
for i in user_input:
    a = a + str(i[0].upper())
print(a)
