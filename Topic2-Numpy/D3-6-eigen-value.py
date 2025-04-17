# SECTION - eigen values

import numpy as np

a = np.array([[1, 2], [3, 4]])
print("eigen: ", np.linalg.eig(a))
eigenvalues, eigenvectors = np.linalg.eig(a)
# print("eigenvalues ", eigenvalues, "\neigenvectors: \n", eigenvectors)
# NOTE - eigenvectors is a colm vector

# NOTE - e_vec * e_val = A * e_vec

# print(eigenvectors[:,0]) ? => eigenvector is a column vector
b = eigenvectors[:, 0] * eigenvalues[0]
print(b)
c = a @ eigenvectors[:, 0]
print(c)

# print(b == c) #[ True False] => get numeric error => not the correct way to compare
print(
    np.allclose(b, c) 
)  # Returns True if two arrays are element-wise equal within a tolerance.
