def add(*args):
    print(args)
    print(sum(args)) # tuple unpacking concept
    
add(5,4,3,4,6)


#li = [i for i in range(3,100,3)]

#print(chr(97))

#li = [chr(i) for i in range(97,122) if (chr(i) in )]

# vowels=['a', 'e', 'i', 'o', 'u']
# str = "my name is bibek"

# li = [letter for letter in str if (letter in vowels) ]
# print("".join(li))

# li2 = str.split(" ")
# print(li2)

#scoping
def func():
    student = ""
    def func2():
        # global student 
        nonlocal student # information sharing in nested/closure func
        student = "sakshi"
        print(id(student))
        
    func2()
    print(id(student))
    
    
func()
# print(id(student))



