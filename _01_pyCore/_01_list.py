"""Lists
List is a collection data type which is ordered and mutable. Unlike Sets, Lists allow duplicate elements. They are useful for preserving a sequence of data and further iterating over it. Lists are created with square brackets."""

# create a list
list_1 = ["banana", "cherry", "apple"]
print(list_1)

# Or create an empty list with the list function
list_2 = list()
print(list_2)

# Lists allow different data types
list_3 = [5, True, "apple"]
print(list_3)

# Lists allow duplicates
list_4 = [0, 0, 1, 1]
print(list_4)


""" Access elements """
item = list_1[0]
print(item)

# You can also use negative indexing, e.g -1 refers to the last item,
# -2 to the second last item, and so on
item = list_1[-1]
print(item)

# Change items
# Lists can be altered after their creation
list_1[2] = "lemon"
print(list_1)

""" Useful methods """

# len() : get the number of elements in a list
print("Length:", len(list_1))

# append() : adds an element to the end of the list
list_1.append("orange")

# insert() : adds an element at the specified position
list_1.insert(1, "blueberry")
print(list_1)

# pop() : removes and returns the item at the given position, default is the last item
item = list_1.pop()
print("Popped item: ", item)

# remove() : removes an item from the list
list_1.remove("cherry") # Value error if not in the list
print(list_1)

# clear() : removes all items from the list
list_1.clear()
print(list_1)

# reverse() : reverse the items
list_1 = ["banana", "cherry", "apple"]
list_1.reverse()
print('Reversed: ', list_1)

# sort() : sort items in ascending order
list_1.sort()
print('Sorted: ', list_1)

# use sorted() to get a new list, and leave the original unaffected.
# sorted() works on any iterable type, not just lists
list_1 = ["banana", "cherry", "apple"]
new_list = sorted(list_1)

# create list with repeated elements
list_with_zeros = [0] * 5
print(list_with_zeros)

# concatenation
list_concat = list_with_zeros + list_1
print(list_concat)

# convert string to list
string_to_list = list('Hello')
print(string_to_list)



""" Copy a list """
list_org = ["banana", "cherry", "apple"]

# this just copies the reference to the list, so be careful
list_copy = list_org

# now modifying the copy also affects the original
list_copy.append(True)
print(list_copy)
print(list_org)

# use copy(), or list(x) to actually copy the list
# slicing also works: list_copy = list_org[:]
list_org = ["banana", "cherry", "apple"]

list_copy = list_org.copy()
# list_copy = list(list_org)
# list_copy = list_org[:]

# now modifying the copy does not affect the original
list_copy.append(True)
print(list_copy)
print(list_org)

"""Iterating"""
# Iterating over a list by using a for in loop
for i in list_1:
    print(i)

# Check if an item exists
if "banana" in list_1:
    print("yes")
else:
    print("no")

"""
Slicing
Access sub parts of the list wih the use of colon (:), just as with strings.
"""
# a[start:stop:step], default step is 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = a[1:3] # Note that the last index is not included
print(b)
b = a[2:] # until the end
print(b)
b = a[:3] # from beginning
print(b)
a[0:3] = [0] # replace sub-parts, you need an iterable here
print(a)
b = a[::2] # start to end with every second item
print(b)
a = a[::-1] # reverse the list with a negative step:
print(a)
b = a[:] # copy a list with slicing
print(b)

"""
List comprehension
A elegant and fast way to create a new list from an existing list.
List comprehension consists of an expression followed by a for statement inside square brackets.
"""
a = [1, 2, 3, 4, 5, 6, 7, 8]
b = [i * i for i in a] # squares each element
print(b)

# Nested lists
# Lists can contain other lists (or other container types)
a = [[1, 2], [3, 4]]
print(a)
print(a[0])