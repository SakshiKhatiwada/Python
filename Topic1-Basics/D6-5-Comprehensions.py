keys = ["k", "e", "y", "s"]
values = ["abc", "def", "uvw", "xyz"]

# NOTE - SYNTAX:  variable = {expression for element in oldList if condition}
Dict = {k: v for (k, v) in zip(keys, values)}
# NOTE - The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.
print(Dict)

# li = [(k,v) for (k,v) in zip(keys,values)]
# print(li)
