class OperatorFunc ():
    def __init__(self,value): #NOTE it's an constructor, yup name should be exactly same and it's double underscore not single 😭
        # print('printing self: ', self) #printing self:  <__main__.OperatorFunc object at 0x000001816A5E6A50>
        self.value = value
        
    def __and__ (self, obj): #NOTE _and_ is recognized by python and object a&b works by default, if another identifier is used, we have to manually call it like a.my_and(b)---by the way, remember OOPS from before! Object a is calling the function and passing Object b as an argument
        print("and operator")
        if isinstance(obj, OperatorFunc):
            return self.value & obj.value
        else:
            raise ValueError("Passed obj is not an instance of OperatorFunc.")
        
    def __or__ (self, obj):
        print("and operator")
        if isinstance(obj, OperatorFunc):
            return self.value | obj.value
        else:
            raise ValueError("Passed obj is not an instance of OperatorFunc.")
        
# and so on.
    
# calling the instance, Driver's code:
if __name__ == "__main__":
    a= OperatorFunc(3)
    b= OperatorFunc(4)
    print (a&b)