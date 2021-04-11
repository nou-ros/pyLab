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

# Assign Multiple Variables on One Line
x,y,z = 5, 10, 15
print(x, y, z)

# Print colored text
print(f'\033[91mError: This is \033[96mcyan. \33[92mContinue?')

# Banker's Rounding - round half towards nearest even number
print(round(10.5))
print(round(11.5))

# Underscores in numbers
my_account_number = 999_999_991_91
print(my_account_number)

# Open a web browser
import webbrowser
# webbrowser.open('https://www.google.com')

# Concatenation without +
message = "Hello world, " "this is, nouros!!"
print(message)

# Split string on multiple lines
print("This is a really long message that I split up over "
"multiple lines for convenience sake. "
"The actual output is the same")

"""
# Multiline string
print('''This is a really long message that I split up over multiple \
    lines for convenience sake. The actual output is the same''')
"""
# Multiline comment
"""
print("Ignore")
print("Ignore again")
"""
# Using id to get identity -- guarenteed to be unique for each object
data = {"Bleach" : 379 }
print(id(data))

# replace list content
def relpace_list(lang):
    lang = ['new']

def replace_list_content(lang):
    lang[:] = ['new']

lang = ['C++','G0', 'Python', 'JS', 'JAVA']
print(lang)
relpace_list(lang)
print(lang)
replace_list_content(lang)
print(lang)

# Copy a list with slicing
languages = ['C++', 'Go', 'Python']
learning = languages[:]
print(id(languages), id(learning))

# check empty list
data = []
# to check empty, None or zero
print(not data)

# unpack list items
def position(x, y, z):
    print(f'after spliting into individual items: {x} {y} {z}')

pos = [5, 10, 15]
position(*pos)

# iterate backwards with reversed
pets = ['dog', 'dog', 'cat', 'bird', 'cat', 'chicked', 'cat', 'dog']
for pet in reversed(pets):
    print(pet, end=" ")


