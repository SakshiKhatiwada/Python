# Theoretical Part to avoid trivial mistakes later

1. Indentation matters!
2. Dynamically typed: no need to specify type before (disadv: chances of run time error -> high)
3. w = z

- Here, w and z initially point to the same memory location, but after modifying w, it points to a new memory location (immutable types like integers, strings and tuples)
- For mutable types, when you do w = z, both variables point to the same object in memory, and changes made to one will affect the other.

4. A Python docstring is a string used to document a Python module, class, function or method. Enclosed in triple quotes

5. str[:-1] removes the last character
6. str[::-1] inverses the string characters

7. for i in d:
        print("%s : %d" % (i, d[i]))  #printing a format
