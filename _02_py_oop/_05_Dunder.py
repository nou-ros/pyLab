class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last +'@email.com'
    
    def fullName(self):
        return '{} {}'.format(self.first, self.last)

    # repr is an unambiguous representation of an object
    # should be used for debugging and logging
    # meant to be seen by other developers
    # display something that can be copied and paste to the python interpreter
    # try to return a string that can be used to recreate an object
    def __repr__(self):
        return "Employee ({}, {}, {})".format(self.first, self.last, self.pay)

    # str is more readable representation of an object
    # meant to used as display to the end user
    def __str__(self):
        return "{} - {}".format(self.fullName(), self.email)

    # operator overloading
    def __add__(self, other):
        return self.pay + other.pay

    # method to get the length of an employee's fullname
    def __len__(self):
        return len(self.fullName())



emp_1 = Employee('Nouros', 'Yousuf', 25000)
emp_2 = Employee('Yohan', 'Zazak', 55000)

print(emp_1)

print(emp_1+emp_2)
print(len(emp_1))