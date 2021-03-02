'''
Given a two list. Create a third list by picking an odd-index element from the 
first list and even index elements from the second.
'''
listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]

listThree = []
listFour = []
for i in range(len(listOne)):
    if i%2!=0:
        listThree.append(listOne[i])
    if i%2==0:
        listFour.append(listTwo[i])

print("Element at odd-index positions from list one")
print(listThree)
print("Element at even-index positions from list two")
print(listFour)
print("Printing Final third list")
listFive = listThree + listFour
print(listFive)

# 2nd way
oddElements = listOne[1::2]
print("Element at odd-index positions from list one")
print(oddElements)

EvenElement = listTwo[0::2]
print("Element at even-index positions from list two")
print(EvenElement)

print("Printing Final third list")
listThree.extend(oddElements)
listThree.extend(EvenElement)
print(listThree)