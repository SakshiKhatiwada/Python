# SECTION - @classmethod VS @staticmethod

# Python program to demonstrate
# use of class method and static method.
from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # a class method to create a Person object by birth year.
    @classmethod  # Class methods (@classmethod) are used when you need to manipulate class attributes or create an instance in a different way.
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year) #returns an obj of the same class

    # a static method to check if a Person is adult or not.
    @staticmethod  # Static methods (@staticmethod) are used when the function is independent of the class but still logically belongs to it.
    def isAdult(age):
        return age > 18


person1 = Person("mayank", 21)
person2 = Person.fromBirthYear("mayank", 1996)

print(person1.age)
print(person2.age)

# print the result
print(Person.isAdult(22))

#NOTE - Class Methods: Can access and modify class state and are bound to the class, which makes them suitable for operations that involve the class itself.
# Static Methods: Do not access or modify class or instance state and are used for utility functions that do not require access to the class or instance



class Order:
    def __init__(self, orderName):
        self.orderName = orderName
        
    @classmethod
    def orderedFullNameCaps(cls, order): #do some operation and calls the class and get the obj and returns that
        return cls(order.upper())
    
    @staticmethod
    def checkOrder(order):
        if order == 'coke':
            return "coke"
        else:
            return "not coke"
        
product = Order("fanta")
product2 = Order.orderedFullNameCaps("coke")

print(product.orderName)
print(product2.orderName)
print(Order.checkOrder("fanta"))