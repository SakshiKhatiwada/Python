import numpy as np

# SECTION - Broadcasting: helps to work with arrays of any shape

x = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6], [4, 5, 6]])
a = np.array([1, 0, 1])
# notice x has 4 rows, a has 3 rows but numpy is smarter in this case
# a = np.array([[1, 0, 1],[1, 0, 1],[1, 0, 1],[1, 0, 1]]) => no need for all the dimensions like this
y = x + a
print(y)