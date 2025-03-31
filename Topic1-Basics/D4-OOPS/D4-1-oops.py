# OOP helps you organize code into modular and reusable sections, which simplifies the development, maintenance, and scaling of software applications.

#four pillars of OOP - Inheritance, Encapsulation, Polymorphism and Abstraction

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age #__ represents private age attribute
        
    # to get private attribute, we do 
    def get_age (self):
        return self.__age 