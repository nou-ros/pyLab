from abc import ABCMeta, abstractmethod

# A base class which contains abstract methods that are to be overridden in its derived class is called an abstract base class

class Shape(metaclass=ABCMeta):
    @abstractmethod
    def area(self):
        return 0

class Square(Shape):
    side = 4
    def area(self):
        print("Area of a square: ",self.side * self.side) 

class Rectangle(Shape):
    width = 5
    length = 10
    def area(self):
        return (self.width * self.length)

square = Square()
square.area()
rectangle = Rectangle()
print("Area of a rectangle: ", rectangle.area())
