'''
Arrange string characters such that lowercase letters should come first
'''
str1 = 'PyNaTive'
low = []
upp = []

for char in str1:
    if char.islower():
        low.append(char)
    else:
        upp.append(char)
    
newstr = ''.join(low+upp)
print('Arranging characters from lowercase to uppercase letter')
print(newstr)