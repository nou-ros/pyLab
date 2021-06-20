'''
Generators
Generators are functions that can be paused and resumed on the fly, returning an object that can be iterated over. Unlike lists, they are lazy and thus produce items one at a time and only when asked. So they are much more memory efficient when dealing with large datasets.
A generator is defined like a normal function but with the yield statement instead of return.

def my_generator():
    yield 1
    yield 2
    yield 3

Execution of a generator function
Calling the function does not execute it. Instead, the function returns a generator object which is used to control execution. Generator objects execute when next() is called. When calling next() the first time, execution begins at the start of the function and continues until the first yield statement where the value to the right of the statement is returned. Subsequent calls to next() continue from the yield statement (and loop around) until another yield is reached. If yield is not called because of a condition or the end is reached, a StopIteration exception is raised:
'''

def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1

# this will not print 'Starting'
cd = countdown(3)

# this will print 'Starting' and the first value
print(next(cd))

# will print the next values
print(next(cd))
print(next(cd))

# this will raise a StopIteration
print(next(cd))

# you can iterate over a generator object with a for in loop
cd = countdown(3)
for x in cd:
    print(x)

# you can use it for functions that take iterables as input
cd = countdown(3)
sum_cd = sum(cd)
print(sum_cd)

cd = countdown(3)
sorted_cd = sorted(cd)
print(sorted_cd)

'''Big advantage: Generators save memory!
Since the values are generated lazily, i.e. only when needed, it saves a lot of memory, especially when working with large data. Furthermore, we do not need to wait until all the elements have been generated before we start to use them.'''

# without a generator, the complete sequence has to be stored here in a list
def firstn(n):
    num, nums = 0, []
    while num < n:
        nums.append(num)
        num += 1
    return nums

sum_of_first_n = sum(firstn(1000000))
print(sum_of_first_n)
import sys
print(sys.getsizeof(firstn(1000000)), "bytes")

# with a generator, no additional sequence is needed to store the numbers
def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1

sum_of_first_n = sum(firstn(1000000))
print(sum_of_first_n)
import sys
print(sys.getsizeof(firstn(1000000)), "bytes")

# Another example: Fibonacci numbers

def fibonacci(limit):
    a, b = 0, 1 # first two fibonacci numbers
    while a < limit:
        yield a
        a, b = b, a + b

fib = fibonacci(30)
# generator objects can be converted to a list (only used for printing here)
print(list(fib))

'''
Generator expressions
Just like list comprehensions, generators can be written in the same syntax except with parenthesis instead of square brackets. Be careful not to mix them up, since generator expressions are often slower than list comprehensions because of the overhead of function calls (https://stackoverflow.com/questions/11964130/list-comprehension-vs-generator-expressions-weird-timeit-results/11964478#11964478)'''

# generator expression
mygenerator = (i for i in range(1000) if i % 2 == 0)
print(sys.getsizeof(mygenerator))

# list comprehension
mylist = [i for i in range(1000) if i % 2 == 0]
print(sys.getsizeof(mylist))

'''Concept behind a generator
This class implements our generator as an iterable object. It has to implement __iter__ and __next__ to make it iterable, keep track of the current state (the current number in this case), and take care of a StopIteration. It can be used to understand the concept behind generators. However, there is a lot of boilerplate code, and the logic is not as clear as with a simple function using the yield keyword.'''

class firstn:
    def __init__(self, n):
        self.n = n
        self.num = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num < self.n:
            cur = self.num
            self.num += 1
            return cur
        else:
            raise StopIteration()
             
firstn_object = firstn(1000000)
print(sum(firstn_object))