'''
Count all lower case, upper case, digits, and special symbols from a given string
'''
str1 = "P@#yn26at^&i5ve"

def count(str1):
    char = 0
    digit = 0
    symbol = 0

    for i in str1:
        if i.islower() or i.isupper():
            char+=1
        elif i.isnumeric():
            digit+=1
        else:
            symbol+=1
    
    print("Characters: ", char, "Digits: ", digit, "Symbol: ", symbol)

count(str1)
