''' 
Given a string, display only those characters which are present at an even index number.
'''

str = "python"
print("Original string is: ", str)
print("Printing only even index chars")

# as python's for loop is a for each loop
index = 0
for i in str:
    if (index%2==0):
        print(i)
    index+=1