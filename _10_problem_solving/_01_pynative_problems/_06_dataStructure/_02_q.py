'''
Given an input list removes the element at index 4 and add it to the 2nd position and also, at the end of the list.
'''
original = [34, 54, 67, 89, 11, 43, 94]

print("List After removing element at index 4")
original.pop(4)
print(original)
original.insert(2, 11)
print(original)
original.append(11)
print(original)