import numpy as np

a = np.array([[1, 2], [3, 5]])
# print(a)

# NOTE - concatenate

b = np.array([[4, 7]])
# c = np.concatenate((a, b))  # sent as a tuple
# c = np.concatenate((a,b), axis=0) # axis = 0 is default
# c = np.concatenate((a,b), axis=None) # flattens the array
# c = np.concatenate((a,b), axis=1) # valueError: dimension is not matched
# c = np.concatenate(([[1, 2]], [[5, 6]]), axis=1)  
# c = np.concatenate((a, b.T), axis=1) 
# print("c: \n", c)

# SECTION - hstack and vstack

d = np.array([1, 2, 3, 4])
e = np.array([5, 6, 7, 8])

# hstack
f = np.hstack((d, e))
print(f)
f = np.vstack((d, e))
print(f)
