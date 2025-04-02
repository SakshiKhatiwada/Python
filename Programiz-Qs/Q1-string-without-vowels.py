# Write a code that removes vowels from the input string

# tip Remember that strings are immutable, so we can not change the original string. So initialize a new string that stores the resulting string (string without vowels).


def remove_vowels(str1):
    print(str1)
    new_str = ""  # to save the string without vowels
    vowels = ["a", "e", "i", "o", "u"]

    for char in str1:
        if char.lower() not in vowels: # NOTE .lower()
            new_str += char

    print("string without vowels: ", new_str)


str1 = "There is blueeeee ocean"
print(type(str1))
remove_vowels(str1)
