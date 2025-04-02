#SECTION - Default Arg

# def func (a = 10):
#     print(a)
    
# func ()
# func(3)


#SECTION - Keyword Arg

# def func (firstName, lastName):
#     print(firstName, lastName)
    
# func("Sakshi", "Khatiwada")
# func(lastName="Khatiwada", firstName= "Sakshi") #no need to remember the order of args

#SECTION - Variable length Arg - *args (Non keyword args) and **kwargs (keyword args)
# def func (*args):
#     for arg in args:
#         print(arg, end=" ")
#     print("")
        
# func ("hi", "I", "am", "Sakshi", "Khatiwada")

# def func2 (**kwargs):
    # for val in kwargs.items(): #('a', 1)
# ('b', 2)
# ('c', 4)
    # print(kwargs) #{'a': 1, 'b': 2, 'c': 4}
    # for key, val in kwargs.items():
    #     print(val)
    #     print(key, val)
        
# func2(a=1, b = 2, c = 4)
# func2(b = 2, c = 4, a=4)