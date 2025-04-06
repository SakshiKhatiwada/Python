# Loops: while, do while, for


# Range(start, end, steps) steps: no. of increments done in a step -> difference between 2 steps


# for i in range (2,5,1):
#     print(i)

# d = dict();
# print(d)
# d['xyz'] = 123
# d['abc'] = 456

# for i in d:
#     print("%s : %d" % (i, d[i])) #NOTE - printing a format

# SECTION - break and continue
# program to print from 1 to 10 except 6

for i in range(1, 11):
    if i == 6:
        continue
    else:
        print(i, end=" ")
