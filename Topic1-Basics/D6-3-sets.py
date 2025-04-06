# sets- unordered collection data type that is iterable, mutable and has no duplicate elements

# unordered -> can't access using indexes

# NOTE - Frozen set-> immutable objects that only support methods and operators that doesn't change the original set

# Set Methods: add(), union(), intersection(), difference(), clear()

setvar = {1, 2, 3, 4, 5}

setvar.add(9)
print(setvar)

setvar2={6,7,4}

print(setvar.union(setvar2))
print(setvar.intersection(setvar2))
print(setvar.difference(setvar2))

setvar.clear()
print(setvar) #set()