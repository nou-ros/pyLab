'''
LEGB
Local, Enclosing, Global, Built-in
'''
# global and Local
'''
x = 'global x'

a = 'global a'

print(a)

def test():
    y = 'local y'
    x = 'local x'
    print(y)
    print(x)

    global a 
    a = 'global a value changed'
    print(a)

    global g 
    g = 'global g'
    print(g)

test()
print(x)
print(a)
print(g)

def test2(z):
    print(z)

test2('local z')
'''

# builtin 
'''
# min, max, 
m = min([5, 1, 3, 4])
print(m)

import builtins
# print(dir(builtins))
'''

# enclosing - related to nested function
'''
r = 'global r'

def outer():
    r = 'outer r'
    def inner():
        print(r)
    
    inner()
    print(r)

outer()
print(r)

def outer():
    x = 'outer x'
    y = 'outer y'
    v = 'outer v'
    def inner():
        x = 'inner x'
        # will be affecting the outer v
        nonlocal v
        v = 'inner v'
        print(x)
        print(y)

    inner()
    print(x)
    print(v)

outer()
'''

r = 'global r'

def outer():
    r = 'outer r'
    def inner():
        r = 'inner r'
        print(r)
    
    inner()
    print(r)

outer()
print(r)