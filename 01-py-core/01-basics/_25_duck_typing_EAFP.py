# Duck typing and Easier to ask forgiveness than permission(EAFP)
# LBYL(look before you leap) is when you first check whether something will succeed and only proceed if you know it will work.

class Duck:
    def quack(self):
        print('Quack, quack')
    
    def fly(self):
        print('Flap flap!')

class Person:
    def quack(self):
        print("I'm Quacking Like a Duck!")
    
    def fly(self):
        print("I'm flapping my arms!")

'''
def quack_and_fly(thing):
    # Not Duck-Typed(non-pythonic)
    if isinstance(thing, Duck):
        thing.quack()
        thing.fly()
    else:
        print('This has to be a Duck!')
    
    print()

d = Duck()
quack_and_fly(d)

p = Person()
quack_and_fly(p)
'''
'''
def quack_and_fly_1(thing):
    thing.quack()
    thing.fly()

    print()

d = Duck()
quack_and_fly_1(d)

p = Person()
quack_and_fly_1(p)
'''

'''
# making the quack_and_fly_1 more secure
def quack_and_fly_2(thing):
    # LBYL(Non-pythonic)
    if hasattr(thing, 'quack'):
        if callable(thing.quack):
            thing.quack()

    if hasattr(thing, 'fly'):
        if callable(thing.fly):
            thing.fly()

# pythonic approach for above function
def quack_and_fly_3(thing):
    # EAFP(pythonic)
    try:
        thing.quack()
        thing.fly()
        thing.bark()
    except AttributeError as e:
        print(e)
    print()


d = Duck()
quack_and_fly_3(d)

p = Person()
quack_and_fly_3(p)
'''

'''
person = {'name': 'Jess', 'age': 23, 'job':'Programmer'}
person = {'name': 'Jess', 'age': 23}

# LBYL (Non-Pythonic)
if 'name' in person and 'age' in person and 'job' in person:
    print("I'm {name}. I'm {age} years old and I am a {job}".format(**person))
else:
    print('Missing some keys')

# EAFP(Pythonic)
try:
    print("I'm {name}. I'm {age} years old and I am a {job}".format(**person))
except KeyError as e:
    print('Missing {} keys'.format(e))
'''

'''
# non-pythonic
my_list = [1,2,3,4,5,6]
if len(my_list) >= 6:
    print(my_list[5])
else:
    print('That index does not exist')

# pythonic
try:
    print(my_list[5])
except IndexError:
    print('That index does not exist')
'''
