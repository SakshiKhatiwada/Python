import numpy as np

# SECTION: - practicing solving linear system


# Q. The admission fee at a small fair is $1.50 for children and $4.00 for adults. On a certain day, 2200 people enter the fair and $5050 is collected. How many children and how many adults attended?

# Equations:
# x + y = 2200
# 1.5x + 4.0y = 5050

A = np.array([[1, 1], [1.5, 4]])
b = np.array([2200, 5050])
# b = np.array([[2200], [5050]])

x = np.linalg.inv(A).dot(
    b
)  # NOTE - inv => not the best method to solve it, might encounter numerical issues
# # x = np.linalg.inv(A) @ (b)
# print(x)

x = np.linalg.solve(A, b)
print(x)
