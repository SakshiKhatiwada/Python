# NOTE - keys are case sensitive

dictionary = {
    "key": 2,
    2: 23,
}

# we can't use mutable objects as key since key is immutable, can't use array like this [2, 4]: "value"

dictionary[2] = 46
print(dictionary)  # {'key': 2, 2: 46}

dictionary.update({"a": "bye"})
print(dictionary)  # {'key': 2, 2: 46, 'a': 'bye'}

print(dictionary.get("key"))

dict2 = dictionary.copy()
print(dict2)

print(dict2.items())  # tuple of (key,value) pair

print(dict2.pop(2))  # NOTE pops value of specified key
print("dict2 pop", dict2)

print(dict2.popitem())  # pops last key-value

print(
    dict2.update({"key2": "value2"})
)  # None -> because it just updates and returns nothing

print(dict2.values())
print(dict2.keys())
