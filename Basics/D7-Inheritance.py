class Person:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def display(self):
        print("HI I am", self.firstName, " ", self.lastName)


class Student(Person):
    def __init__(
        self, firstName, lastName, sem
    ):  # overrides the constructor of parent class
        super().__init__(
            firstName, lastName
        )  # super() function that will make the child class inherit all the methods and properties from its parent, or we can also use Person.__init__(self, firstName,lastName)
        self.sem = sem

    # def display(self): #METHOD OVERRIDING
    #     super().display()
    #     print("I am currently studying in ", self.sem, "sem\n")


x = Student("sakshi", "khatiwada", 5)
x.display()
