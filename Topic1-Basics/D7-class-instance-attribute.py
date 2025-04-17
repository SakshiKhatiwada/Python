class sample:
    count = 0

    def increase(self):
        sample.count += 1


obj1 = sample()
obj2 = sample()
obj1.increase()
# print ("count by obj1: ", obj1.count)
obj2.increase()
# print ("count by obj2: ", obj2.count)
# print ("count", sample.count)

# NOTE - this count is class attribute, so it is not different for every other objects and changing it through any object directly affecs that variable


# SECTION - 2 funcs to list the attributes of an instance (vars()) and class (dir()) in the form of dict

print("vars", vars(sample))  # attributes of instance of sample
print("dir", dir(sample))  # attributes of the class, including of the ancestor class

# SECTION - Class Member Access
# Built-in functions:

# getattr(object, attribute, default)
print(
    getattr(obj1, "count")
)  # <built-in method count of str object at 0x000002945D30AC40>
print('getattr',
    getattr(obj1, "random", "msg: attribute not found")
)  # without this, default is AttributeError

# hasattr(object, attribute)
print(hasattr(obj1, "count"))  # obj1 has attribute count ? True

# setattr(obj, attribute, value)
setattr(obj1, "count", 40)
print(obj1.count)

# delattr(obj2, attribute)
delattr(sample, "count")
# print(sample.count) #ERR AttributeError: type object 'sample' has no attribute 'count'
