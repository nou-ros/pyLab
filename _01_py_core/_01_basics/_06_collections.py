'''Collections
The collections module in Python implements specialized container datatypes providing alternatives to Python’s general purpose built-in containers, dict, list, set, and tuple.
The following tools exist:

namedtuple : factory function for creating tuple subclasses with named fields
OrderedDict : dict subclass that remembers the order entries were added
Counter : dict subclass for counting hashable objects
defaultdict : dict subclass that calls a factory function to supply missing values
deque : list-like container with fast appends and pops on either end
In Python 3 some more modules exist (ChainMap, UserDict, UserList, UserString). See https://docs.python.org/3/library/collections.html for further references.'''

'''Counter
A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.'''

from collections import Counter
a = "aaaaabbbbcccdde"
my_counter = Counter(a)
print(my_counter)

print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())

my_list = [0, 1, 0, 1, 2, 1, 1, 3, 2, 3, 2, 4]
my_counter = Counter(my_list)
print(my_counter)

# most common items
print(my_counter.most_common(1))

# Return an iterator over elements repeating each as many times as its count. 
# Elements are returned in arbitrary order.
print(list(my_counter.elements()))

'''
namedtuple
namedtuples are easy to create, lightweight object types. They assign meaning to each position in a tuple and allow for more readable, self-documenting code. They can be used wherever regular tuples are used, and they add the ability to access fields by name instead of position index.'''

from collections import namedtuple
# create a namedtuple with its class name as string and its fields as string
# fields have to be separated by comma or space in the given string
Point = namedtuple('Point','x, y')
pt = Point(1, -4)
print(pt)
print(pt._fields)
print(type(pt))
print(pt.x, pt.y)

Person = namedtuple('Person','name, age')
friend = Person(name='Tom', age=25)
print(friend.name, friend.age)

'''OrderedDict
OrderedDicts are just like regular dictionaries but they remember the order that items were inserted. When iterating over an ordered dictionary, the items are returned in the order their keys were first added. If a new entry overwrites an existing entry, the original insertion position is left unchanged. They have become less important now that the built-in dict class gained the ability to remember insertion order (guaranteed since Python 3.7). But some differences still remain, e.g. the OrderedDict is designed to be good at reordering operations.'''

from collections import OrderedDict
ordinary_dict = {}
ordinary_dict['a'] = 1
ordinary_dict['b'] = 2
ordinary_dict['c'] = 3
ordinary_dict['d'] = 4
ordinary_dict['e'] = 5
# this may be in orbitrary order prior to Python 3.7
print(ordinary_dict)

ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
ordered_dict['e'] = 5
print(ordered_dict)
# same functionality as with ordinary dict, but always ordered
for k, v in ordinary_dict.items():
    print(k, v)

'''defaultdict
The defaultdict is a container that's similar to the usual dict container, but the only difference is that a defaultdict will have a default value if that key has not been set yet. If you didn't use a defaultdict you'd have to check to see if that key exists, and if it doesn't, set it to what you want.'''

from collections import defaultdict

# initialize with a default integer value, i.e 0
d = defaultdict(int)
d['yellow'] = 1
d['blue'] = 2
print(d.items())
print(d['green'])

# initialize with a default list value, i.e an empty list
d = defaultdict(list)
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 5)]
for k, v in s:
    d[k].append(v)

print(d.items())
print(d['green'])

'''deque
A deque is a double-ended queue. It can be used to add or remove elements from both ends. Deques support thread safe, memory efficient appends and pops from either side of the deque with approximately the same O(1) performance in either direction. The more commonly used stacks and queues are degenerate forms of deques, where the inputs and outputs are restricted to a single end.'''

from collections import deque
d = deque()

# append() : add elements to the right end 
d.append('a')
d.append('b')
print(d)

# appendleft() : add elements to the left end 
d.appendleft('c')
print(d)

# pop() : return and remove elements from the right
print(d.pop())
print(d)

# popleft() : return and remove elements from the left
print(d.popleft())
print(d)

# clear() : remove all elements
d.clear()
print(d)

d = deque(['a', 'b', 'c', 'd'])

# extend at right or left side
d.extend(['e', 'f', 'g'])
d.extendleft(['h', 'i', 'j']) # note that 'j' is now at the left most position
print(d)

# count(x) : returns the number of found elements
print(d.count('h'))

# rotate 1 positions to the right
d.rotate(1)
print(d)

# rotate 2 positions to the left
d.rotate(-2)
print(d)