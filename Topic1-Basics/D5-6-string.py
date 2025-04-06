# str = "sakshi"
# print(str[-1])  #last char
# print(str[::-1]) #reverse string

# SECTION slicing

# print(str[1:5]) #1st and 5th included, 5-1 = 4th index -> aksh
# print(str[0:5]) #same thing, leaves last character
# print(str[:-1]) #leaves last character
# print(str[:-2]) #leaves last 2 character

# print(chr(97))

# SECTION - using "" inside quotation
# print("Escape sequencing with python \" hi I am Sakshi \" ")
# print('''or I can simply do 'this' ''')
# print("hi 'i'm' sakshi")

# SECTION - index() method -> index(substring, begp, endp)

str = "sakshishshsh is sakshi"
# print(str.__len__())
# print(str.index('sh')) # returns the index of first index of substring, by default begp - 0, endp - length of string

# try except block
try:
    print(str.index("sh", 0, 3))  # doesn't check the last point
# NOTE - raise ValueError if substring is not found
except ValueError:
    print("substring not found")

# print(str.index('sh')) # first index -> 3
# print(str.rindex('sh')) # last index or highest index -> 10
# print(
#     str.find("p")
# )  # NOTE first index, returns -1 if substring not found, The Only difference between find() and index()

# SECTION - case changing of Strings

# print(str.lower()) #lower case
# print(str.upper()) #upper case
# print(str.title()) #title case

# SECTION - string built-in methods
# print(str.strip())  # removes leading and trailing spaces
# string1 = "sakshi is sakshi, she is sweet"

# print(string1.startswith("sh"))  # false
# print(string1.endswith("et"))  # true
