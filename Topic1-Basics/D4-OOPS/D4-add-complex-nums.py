class AddComplexNumber:
    def __init__ (self, value):
        temp = value.split('+') #form: ['3', '4j']
        self.real = temp[0]
        self.imaginary = int(temp[1][:-1]) # int(str.[:-1])
        print(self.real, self.imaginary)
        
    def addComplexNumber (self, object):
        return f"{self.real + object.real} + {self.imaginary + object.imaginary}j"
    
    def __add__ (self, object):
        return f"{self.real + object.real} + {self.imaginary + object.imaginary}j"
        
    
    

x = AddComplexNumber("3+4j")
y = AddComplexNumber("4+8j")

print( x+ y)
print(x.addComplexNumber(y))

print ("sakshi"[::-1])
    