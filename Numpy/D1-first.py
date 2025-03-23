import numpy as np

# print (np.__version__)

# a = np.array([1, 2, 3, 3, 5])
# print(a)
# print(a.shape)
# print(a.dtype) #int64
# print(a.ndim)
# print(a.size)
# print(a.itemsize, 'bytes')
# print(a[0])

# b = a * np.array([2, 3, 5, 3, 8])
# print(b)


#SECTION - python lists VS numpy arrays
# l = [1,2,3]
# x = np.array([1,2,3])

# l.append(4)
# l = l+[5]

# x.append(4)#AttributeError
# x = x + np.array([4]) #4 is added to each element -> #NOTE - Broadcasting
# x = x + np.array([4,4,4]) # actual way, numpy does this to above

# print(l,x)


#MULTIPLY

# l = l*2 # repeats the list elements twice
# print(l)

# x = x * 2 # gives element operation 
# print (x)

#NOTE - findings: In Numpy Arrays, operations are performed elementwise

# x = np.sqrt(x)
# print (x)

# x = np.log(x)
# print (x)


l1 = [1,2,3]
l2 = [4,5,6]
a1 = np.array(l1)
a2 = np.array(l2)

#dot product

#in list
dot = 0
for i in range(len(l1)):
    dot += l1[i] * l2[i]
# print (dot)
 
#dot product in -> numpy array
dot = np.dot(a1,a2)
# print(dot)

sum1 = a1 * a2
# print(sum1)
dot = sum(sum1)
# print('dot ', dot)

#in newer version
dot = a1 @ a2
# print(dot)