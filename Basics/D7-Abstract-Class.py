from abc import ABC, abstractmethod


class Polygon(ABC): #ABC -> Abstract Base Class
    @abstractmethod
    def noOfSides(self):
        pass  # if there is no code for this


class Triangle(Polygon):
    # overriding abstract method
    def noOfSides(self):
        print("I have 3 sides")


class Rectangle(Polygon):
    def noOfSides(self):
        print("I have four sides")


poly = Polygon()
tri = Triangle()
rect = Rectangle()

poly.noOfSides()  # TypeError: Can't instantiate abstract class Polygon without an implementation for abstract method 'noOfSides' -> strictly error occurs, helps to avoid tiny mistakes like these
tri.noOfSides()
rect.noOfSides()
