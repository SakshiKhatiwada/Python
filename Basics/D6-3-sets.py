# sets- unordered collection data type that is iterable, mutable and has no duplicate elements

# unordered -> can't access using indexes

# NOTE - Frozen set-> immutable objects that only support methods and operators that doesn't change the original set

# Set Methods: add(), union(), intersection(), difference(), clear()

set = {1, 2, 3, 4, 5}

set.add(9)
print(set)

set2={6,7,4}

print(set.union(set2))
print(set.intersection(set2))
print(set.difference(set2))

set.clear()
print(set) #set()