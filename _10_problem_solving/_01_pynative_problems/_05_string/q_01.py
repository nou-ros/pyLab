'''
Given a string of odd length greater than 7, return a string made of the middle three chars of a given String
'''
str1 = "JhonDipPeta"
str2 = "JaSonAy"

def getMiddleThree(str1):
    middleIndex = int(len(str1)/2)
    print("Original String is: ", str1)
    middleThree = str1[middleIndex-1:middleIndex+2]
    print("Middle three chars are: ", middleThree)

getMiddleThree(str2)