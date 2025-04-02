# Find the majority element from the given list of size n. The majority element in a list is the element that appears more than n/2 times.

# Assumption: We will assume the list is non-empty and the majority element is always present in the list.

# Sakshi's Brain cell did this 🤣
# numbers = [1, 7, 8, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 3, 3, 8, 9]

# set_el = set(numbers)
# for num in set_el:
#     if numbers.count(num) > numbers.__len__() // 2:  # // -> integer division
#         print(num, " is majority element")


# Efficient Algorithm: Boyer-Moore Voting Algorithm:
