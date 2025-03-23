import numpy as np

# SECTION - copying array

# this doesn't work

a = np.array([1, 2, 4])
# b = a
# b[0] = 34
# print(b)
# print(a)  # this is also modified, what???
# b = a only copies the reference and both of them implies to the same memory location


#Actual copy
b = np.copy(a) # or b = a.copy()
b[0] = 34
print(b)
print(a)