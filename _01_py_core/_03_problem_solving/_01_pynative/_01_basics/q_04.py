'''
Given a string and an integer number n, remove characters from a string starting from zero up to n and return a new string
Note: n must be less than the length of the string.
'''

def removeChars(string, n):
    return string[n:]

string = "Programming"
print("Enter a number: ")
n = int(input())

print(removeChars(string, n))