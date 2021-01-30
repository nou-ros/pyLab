# public => memberName
# private => __memberName
# protected => _memberName
# python follow this naming convention but this is not syntactically forced. So as a developer we will follow such approach while coding. 

class Car:
    wheels = 4
    _color = "Black"
    __yearOfManufacture = 2017

class Bmw(Car):
    def __init__(self):
        print("Protected attribute color: ", self._color)

car = Car()
print("Pulib attribute wheels: ", car.wheels)
# print("Protected attribute color: ", car._color) # will be accessible this way 
bmw = Bmw()
# print("Private attribute year of manufacturer: ", car._Car__yearOfManufacture) # will be accessible this way this is also called name mangling.