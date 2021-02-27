'''
Cleaning text steps
1. Create a text file and take text from it
2. Convert the letter into lowercase (Ant -> ant)
3. Remove punctuations like .,!? etc.
'''
# with open('_01_test.txt') as f:
#     text = f.readlines()
#     print(text)
import string 
text = open('_01_test.txt', encoding='utf-8').read()
lower_text = text.lower()
# print(string.punctuation)


cleaned_text = lower_text.translate(str.maketrans("","",string.punctuation))
print(cleaned_text)

'''
The translate() method returns a string where some specified characters are replaced with the character described in a dictionary, or in a mapping table.

Use the maketrans() method to create a mapping table.
'''