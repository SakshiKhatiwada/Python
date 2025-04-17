# lists = dynamically typed Array
# sequence data type used to store collection of data types

var = ["s", "a", "k", "s", "h", "i", 57]  # -> list may not be homogenous
var[6] = 82  # -> list is mutable
# print(var)

# SECTION - Adding elements to a list
li = []
# print(len(li))
li = [1, 2, 3]
# print(len(li))
# print(li.__len__())

# SECTION - Adding elements using append(), extend()

li.append((3, 7))  # adds the tuple as it is
# print(li)

li.extend((3, 7))  # adds tuple element as normal elements, extend the li
# print(li)

# SECTION - insert()
print(li)
li.insert(1000, 93)  # insert(index, number), doesn't return any value
# li = li + [123]
print(li)
# NOTE if given index doesn't lie in the range, it just inserts in the last index. We can't specify without index
# print(li)

# SECTION - count ()

list_name = ["s", "a", "k", "s", "h", "i"]
# print(list_name.count('s'))
# raises TypeError is more than one string is passed

# SECTION - del keyword, pop(), remove() built-in methods
# NOTE difference -> remove() takes value-to-remove, del and pop() takes index

del list_name[2]
# print(list_name)

list_name.remove("s")  # first matched value is removed
# print(list_name)

# list_name.pop(2)
# print(list_name.pop(2)) # NOTE -> pop() also returns deleted value
# print(list_name)


# SECTION - max(), min(), sort(), reverse()

# print("max:", max(3, 4, 4, 6))
# print("min:", min(3, 4, 4, 6))

li = [3, 5, 8, 2, 1]
# li.sort(reverse=False)
# print("sorted: ", li)

# ------------ custom sorting function
# def myFunc(e):
#   return e['year']

# cars = [
#   {'car': 'Ford', 'year': 2005},
#   {'car': 'Mitsubishi', 'year': 2000},
#   {'car': 'BMW', 'year': 2019},
#   {'car': 'VW', 'year': 2011}
# ]

# cars.sort(key=myFunc)
# print(cars)

li.reverse()
print(li) #reverse of the string
