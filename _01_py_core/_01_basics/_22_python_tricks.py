# Value swapping
a, b = 5, 10
print(a, b)
a, b = b, a
print(a, b)
# also possible in a list
myList = [1, 2, 3, 4, 5]
print("Initial list :", myList)
myList[0], myList[1] = myList[1], myList[0]
print("Modified list:", myList)

'''Create a single string from list'''

my_list = ["I", "am", "awesome"]

# bad
a = ""
for i in my_list:
    a += i + " "
print(a)

# good
a = " ".join(my_list)
print(a)

# join method is much faster
from timeit import default_timer as timer
my_list = ["a"] * 1000000

# bad
start = timer()
a = ""
for i in my_list:
    a += i
end = timer()
print(end - start)
#print(a)

# good
start = timer()
a = " ".join(my_list)
end = timer()
print(end - start)
#print(a)

# multiple inputs 
a, b = input("Enter 2 integers: ").split()
print(a, b)
# multiple int input
x, y, z = [int(i) for i in input("enter 3 numbers").split()]
print(y)

# and/or for multiple conditions
subs = 2450
likes = 200
comment = 60

conditions = [
    subs > 150,
    likes > 150,
    comment > 50
    ]
# all returns true, if all list items are true - and
if all(conditions):
    print("Awesome upload!")

# to fullfill atleast one condition - or 
checks = [ 
    subs > 2500, 
    likes > 500, 
    comment > 50
    ] 

if any(checks):
    print('Awesome video!')

    
# most repeated within a list
most_repeated = max(a, key=a.count)
print(most_repeated)

# reverse on spot
name = 'Ichigo Kurosaki'[::-1]
print(name)

#palindrome
name = "madam"
isPalin = name.find(name[::-1]) == 0
print(isPalin)
