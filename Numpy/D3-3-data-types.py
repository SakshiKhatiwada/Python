import numpy as np

#SECTION - data types

# x = np.array([1,2])
# x = np.array([1.0,2,'a']) #<U32
# x = np.array(['b','a']) #<U1

#We can also force a data type
x = np.array([1.0,2.3], dtype = np.float16)
print(x)
print(x.dtype)