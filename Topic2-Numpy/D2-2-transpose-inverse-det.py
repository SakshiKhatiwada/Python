import numpy as np

a = np.array([[1, 2, 3], [3, 4, 5], [7, 8, 0]])
print(a)
print(a.shape)  # (2, 3) -> 2 rows, 3 columns

print(a[0][0])
print(a[0, 0])  # another syntax

print(a[:, 0])  #: -> all, here all rows, colm 0
# print(a[15, :]) #row 0, all colm #ERROR - IndexError: index 5 is out of bounds for axis 0 with size 4
print(a[0, :])

print("Transpose: ", a.T)  # Transpose the array
# print("Inverse: ", np.linalg.inv(a))  # Inverse the array #numpy.linalg.LinAlgError: Last 2 dimensions of the array must be square
print("Inverse: \n", np.linalg.inv(a))
print("determinant:", np.linalg.det(a))

print(np.diag(a)) #gives a vector of diagonal element
c = np.diag(a)
print(np.diag(c)) # gives diagonal matrix #OVERLOADED func





