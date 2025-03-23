import numpy as np

a = np.zeros((2, 3))  # 2X3 matrix
# print(a)

a = np.ones((2, 3))  # 2X3 matrix
# print(a)

a = np.ones((2, 3), dtype=np.int64)  # 2X3 matrix
# print(a)

a = np.full((3, 3), 8)  # entire matrix is filled with the given number
# print(a)

a = np.eye(3)  # identity matrix of 3x3
# print(a)

a = np.arange(20)  # 1D array from 0 upto 19

a = np.linspace(
    0, 10, 3
)  # start, stop, steps #NOTE - handy for making equally spaced array

a = np.random.random((3, 2))  # from the Uniform Dist., btwn 0-1
# print(a)

a = np.random.randn(
    3, 2
)  # NOTE - doesn't take tuple, directly value, --> normal/ Gaussian dist. where mean = 0, var = 1
# print(a)

a = np.random.randn(1000)
# print(
#     "mean: ", a.mean(), "variance: ", a.var()
# )  # mean:  0.028983226509377957 variance:  1.0446766588782335

a = np.random.randint(
    3, 10, size=(3, 3)
)  # start, end, size #NOTE - matrix elements range from 3 to 9, 10 is excluded, in 3x3 matrix
print(a)  # use .flatten() to obtain 1D array, .choice() functionality S

a = np.random.choice(
    5, size=10
)  # generates an array of size 10, number chosen from 0 upto 5
# print(a)

a = np.random.choice(
    [-8, -6, 2], size=10
)  # generates an array of size 10, number chosen from the list
print(a)

# a = np.random.choice(5,6, size=10) #TypeError: choice() got multiple values for keyword argument 'size'
# print(a)
