
'''JSON
JSON (JavaScript Object Notation) is a leightweight data format for data exchange. In Python you have the built-in json module for encoding and decoding JSON data. Simply import it and you are ready to work with JSON data.

Some advantages of JSON:

JSON exists as a "sequence of bytes" which is very useful in the case we need to transmit (stream) data over a network.
Compared to XML, JSON is much smaller, translating into faster data transfers, and better experiences.
JSON is extremely human-friendly since it is textual, and simultaneously machine-friendly.'''

# JSON format
'''{
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "swimming", "singing"],
    "age": 28,
    "children": [
        {
            "firstName": "Alex",
            "age": 5
        },
        {
            "firstName": "Bob",
            "age": 7
        }
    ]
}


JSON supports primitive types (strings, numbers, boolean), as well as nested arrays and objects. Simple Python objects are translated to JSON according to the following conversion:

Python	JSON
dict -	object
list, tuple - array
str	- string
int, long, float - number
True - true
False -	false
None -	null

'''
'''
From Python to JSON (Serialization, Encode)
Convert Python objects into a JSON string with the json.dumps() method.'''

import json

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

# convert into JSON:
person_json = json.dumps(person)
# use different formatting style
person_json2 = json.dumps(person, indent=4, separators=("; ", "= "), sort_keys=True)

# the result is a JSON string:
print(person_json) 
print(person_json2)
{"name": "John", "age": 30, "city": "New York", "hasChildren": false, "titles": ["engineer", "programmer"]}
{
    "age"= 30; 
    "city"= "New York"; 
    "hasChildren"= false; 
    "name"= "John"; 
    "titles"= [
        "engineer"; 
        "programmer"
    ]
}
# Or convert Python objects into JSON objects and save them into a file with the json.dump() method.
person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

with open('person.json', 'w') as f:
    json.dump(person, f) # you can also specify indent etc...


'''
FROM JSON to Python (Deserialization, Decode)
Convert a JSON string into a Python object with the json.loads() method. The result will be a Python dictionary.'''

person_json = """
{
    "age": 30, 
    "city": "New York",
    "hasChildren": false, 
    "name": "John",
    "titles": [
        "engineer",
        "programmer"
    ]
}
"""
person = json.loads(person_json)
print(person)

# Or load data from a file and convert it to a Python object with the json.load() method.

with open('person.json', 'r') as f:
    person = json.load(f)
    print(person)

'''Working with Custom Objects
Encoding
Encoding a custom object with the default JSONEncoder will raise a TypeError. We can specify a custom encoding function that will store the class name and all object variables in a dictionary. Use this function for the default argument in the json.dump() method.'''

def encode_complex(z):
    if isinstance(z, complex):
        # just the key of the class name is important, the value can be arbitrary.
        return {z.__class__.__name__: True, "real":z.real, "imag":z.imag}
    else:
        raise TypeError(f"Object of type '{z.__class__.__name__}' is not JSON serializable")

z = 5 + 9j
zJSON = json.dumps(z, default=encode_complex)
print(zJSON)

# You can also create a custom Encoder class, and overwrite the default() method. Use this for the cls argument in the json.dump() method, or use the encoder directly.
from json import JSONEncoder
class ComplexEncoder(JSONEncoder):
    
    def default(self, o):
        if isinstance(z, complex):
            return {z.__class__.__name__: True, "real":z.real, "imag":z.imag}
        # Let the base class default method handle other objects or raise a TypeError
        return JSONEncoder.default(self, o)
    
z = 5 + 9j
zJSON = json.dumps(z, cls=ComplexEncoder)
print(zJSON)
# or use encoder directly:
zJson = ComplexEncoder().encode(z)
print(zJSON)


'''Decoding
Decoding a custom object with the defaut JSONDecoder is possible, but it will be decoded into a dictionary. Write a custom decode function that will take a dictionary as input, and creates your custom object if it can find the object class name in the dictionary. Use this function for the object_hook argument in the json.load() method.'''
# Possible but decoded as a dictionary
z = json.loads(zJSON)
print(type(z))
print(z)

def decode_complex(dct):
    if complex.__name__ in dct:
        return complex(dct["real"], dct["imag"])
    return dct

# Now the object is of type complex after decoding
z = json.loads(zJSON, object_hook=decode_complex)
print(type(z))
print(z)

'''
Template encode and decode functions
This works for all custom classes if all instance variables are given in the __init__ method.'''

class User:
    # Custom class with all instance variables given in the __init__()
    def __init__(self, name, age, active, balance, friends):
        self.name = name
        self.age = age
        self.active = active
        self.balance = balance
        self.friends = friends
        
class Player:
    # Other custom class
    def __init__(self, name, nickname, level):
        self.name = name
        self.nickname = nickname
        self.level = level

            
def encode_obj(obj):
    """
    Takes in a custom object and returns a dictionary representation of the object.
    This dict representation also includes the object's module and class names.
    """
  
    #  Populate the dictionary with object meta data 
    obj_dict = {
      "__class__": obj.__class__.__name__,
      "__module__": obj.__module__
    }
  
    #  Populate the dictionary with object properties
    obj_dict.update(obj.__dict__)
  
    return obj_dict


def decode_dct(dct):
    """
    Takes in a dict and returns a custom object associated with the dict.
    It makes use of the "__module__" and "__class__" metadata in the dictionary
    to know which object type to create.
    """
    if "__class__" in dct:
        # Pop ensures we remove metadata from the dict to leave only the instance arguments
        class_name = dct.pop("__class__")
        
        # Get the module name from the dict and import it
        module_name = dct.pop("__module__")
        
        # We use the built in __import__ function since the module name is not yet known at runtime
        module = __import__(module_name)
        
        # Get the class from the module
        class_ = getattr(module,class_name)

        # Use dictionary unpacking to initialize the object
        # Note: This only works if all __init__() arguments of the class are exactly the dict keys
        obj = class_(**dct)
    else:
        obj = dct
    return obj

# User class works with our encoding and decoding methods
user = User(name = "John",age = 28, friends = ["Jane", "Tom"], balance = 20.70, active = True)

userJSON = json.dumps(user,default=encode_obj,indent=4, sort_keys=True)
print(userJSON)

user_decoded = json.loads(userJSON, object_hook=decode_dct)
print(type(user_decoded))

# Player class also works with our custom encoding and decoding
player = Player('Max', 'max1234', 5)
playerJSON = json.dumps(player,default=encode_obj,indent=4, sort_keys=True)
print(playerJSON)

player_decoded = json.loads(playerJSON, object_hook=decode_dct)
print(type(player_decoded))