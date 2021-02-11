'''
Tuple
A tuple is a collection of objects which is ordered and immutable. Tuples are similar to lists, the main difference ist the immutability. In Python tuples are written with round brackets and comma separated values.
'''

'''
Create a tuple
Tuples are created with round brackets and comma separated values. Or use the built-in tuple function.
'''
tuple_1 = ("Max", 28, "New York")
tuple_2 = "Linda", 25, "Miami" # Parentheses are optional

# Special case: a tuple with only one element needs to have a comma at the end, 
# otherwise it is not recognized as tuple
tuple_3 = (25,)
print(tuple_1)
print(tuple_2)
print(tuple_3)

# Or convert an iterable (list, dict, string) with the built-in tuple function
tuple_4 = tuple([1,2,3])
print(tuple_4)

'''
Access elements
You access the tuple items by referring to the index number. Note that the indices start at 0.
'''
item = tuple_1[0]
print(item)
# You can also use negative indexing, e.g -1 refers to the last item,
# -2 to the second last item, and so on
item = tuple_1[-1]
print(item)

# _____ Add or change items
# Not possible and will raise a TypeError.
tuple_1[2] = "Boston"

# _____ Delete a tuple
del tuple_2

# _____ Iterating over a tuple by using a for in loop
for i in tuple_1:
    print(i)
    
# _____ Check if an item exists
if "New York" in tuple_1:
    print("yes")
else:
    print("no")

'''Usefule methods''''
my_tuple = ('a','p','p','l','e',)

# len() : get the number of elements in a tuple
print(len(my_tuple))

# count(x) : Return the number of items that is equal to x
print(my_tuple.count('p'))

# index(x) : Return index of first item that is equal to x
print(my_tuple.index('l'))

# repetition
my_tuple = ('a', 'b') * 5
print(my_tuple)

# concatenation
my_tuple = (1,2,3) + (4,5,6)
print(my_tuple)

# convert list to a tuple and vice versa
my_list = ['a', 'b', 'c', 'd']
list_to_tuple = tuple(my_list)
print(list_to_tuple)

tuple_to_list = list(list_to_tuple)
print(tuple_to_list)

# convert string to tuple
string_to_tuple = tuple('Hello')
print(string_to_tuple)

'''Slicing'''
# Access sub parts of the tuple wih the use of colon (:), just as with strings.

# a[start:stop:step], default step is 1
a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
b = a[1:3] # Note that the last index is not included
print(b)
b = a[2:] # until the end
print(b)
b = a[:3] # from beginning
print(b)
b = a[::2] # start to end with every second item
print(b)
b = a[::-1] # reverse tuple
print(b)

'''Unpack tuple'''
# number of variables have to match number of tuple elements
tuple_1 = ("Max", 28, "New York")
name, age, city = tuple_1
print(name)
print(age)
print(city)

# tip: unpack multiple elements to a list with *
my_tuple = (0, 1, 2, 3, 4, 5)
item_first, *items_between, item_last = my_tuple
print(item_first)
print(items_between)
print(item_last)


# Nested tuples
# Tuples can contain other tuples (or other container types).
a = ((0, 1), ('age', 'height'))
print(a)
print(a[0])


'''Compare tuple and list
The immutability of tuples enables Python to make internal optimizations. Thus, tuples can be more efficient when working with large data.
'''
# compare the size
import sys
my_list = [0, 1, 2, "hello", True]
my_tuple = (0, 1, 2, "hello", True)
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")

# compare the execution time of a list vs. tuple creation statement
import timeit
print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))