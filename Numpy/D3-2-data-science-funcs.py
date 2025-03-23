import numpy as np

#NOTE - sum(), axis(), var() for variance, std() for standard deviation, min(), max()

# SECTION - sum() in array, using optional parameter 'axis', mean()
a = np.array([[7, 8, 9, 10, 11, 12, 13], [17, 18, 19, 20, 21, 22, 23]])
print(a)
print(a.sum())  # 210
# print(a.sum(axis = None)) #default
print(a.sum(axis=0))  # [24 26 28 30 32 34 36] -> calculated along rows, vertically to the down, elements of colm 1 summed, and so on
print(a.sum(axis=1))  # [ 70 140] -> calculated along columns, horizontally to the right, elements of row 1 summed, and so on

print(a.mean(axis=None))
print(a.mean(axis=0))
print(a.mean(axis=1))
#15.0
# [12. 13. 14. 15. 16. 17. 18.]
# [10. 20.]

