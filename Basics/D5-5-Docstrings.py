def func ():
    """This is Docstring. Docstrings, short for documentation strings, are vital in conveying the purpose and functionality of Python functions, modules, and classes.
    
    The way of writing docstring is: Starts with capital letter and ends fullstop. First line is a short description. If there are more lines in the documentation string, the second line should be blank, visually separating the summary from the rest of the description."""
    return None

# print(func.__doc__) # to access docstring using __doc__
# help(func) # accessing using docstring using help

#SECTION - Google Style Docstring which follows google guideline style

def multiply (a,b):
    """To multiply 2 integers.
    
    Args:
        a (int): The First Number
        b (int): The Second Number
        
        Returns: 
            int: The product of a and b.
    """
    return a*b
print(multiply(2,3))