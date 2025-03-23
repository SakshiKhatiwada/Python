import numpy as np

a = np.array([[1, 2, 5, 7], [3, 4, 9, 8]])
# print(a)

# b = a[0, 1]  # indexing
# print(b)

# c = a[0, 1:3] #startingIndex:upto-lastIndex
# c = a[-1, -2] #last row, last colm

# boolean indexing
d = np.array([[1, 2], [3, 4], [5, 6]])
# print(d)

bool_idx = d > 2  # NOTE same array but with True/False elements based on this condn
# print(bool_idx)
# print(d[bool_idx])  # only those elements where there is True


# the same thing in one step
# print(d[d > 2])

# NOTE - np.where()
b = np.where(d > 2, d, -1)
# print(b)

e = np.array([10, 20, 32, 94, 58, 73])
# print(a)
f = [1, 3, 5]
# print(e[f])  # NOTE - fancy indexing

# SECTION - to find even numbers
even = np.argwhere(e % 2 == 0).flatten()
# print('even',e[even])

# SECTION - reshaping array using np.arrange(), <arr_name>.reshape()
g = np.arange(1, 7)  # makes an array having elements from 1 upto 7 i.e 1-6
# print(g)
# print(g.shape)

h = g.reshape(
    [2, 3]
)  # ValueError: cannot reshape array of size 7 into shape (2,3) if shape doesn't match
# print(h)

p = np.array([[1, 2], [3, 4], [5, 6]])
i = p[:, np.newaxis]
print(i)  # list of lists

# arr[np.newaxis, :]	(1, n)	Makes a row vector
# arr[:, np.newaxis]	(n, 1)	Makes a column vector
# p[:, :, np.newaxis]	(n, m, 1)	Expands into 3D
