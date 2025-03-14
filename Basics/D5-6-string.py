# str = "sakshi"
# print(str[-1])  #last char
# print(str[::-1]) #reverse string

# slicing

# print(str[1:5]) #1st and 5th included -> aksh
# print(str[0:5]) #same thing, leaves last character
# print(str[:-1]) #leaves last character
# print(str[:-2]) #leaves last 2 character

# print(chr(97))

# SECTION - using "" inside quotation
# print("Escape sequencing with python \" hi I am Sakshi \" ")
# print('''or I can simply do 'this' ''')

# SECTION - index() method -> index(substring, begp, endp)

# str = 'sakshishshsh is sakshi'
# print(str.index('sh')) # returns the index of first index of substring, by default begp - 0, endp - length of string
# print(str.index('sh',0,3)) #doesn't check the last point
# NOTE - raise ValueError if substring is not found

# print(str.index('sh')) #first index -> 3
# print(str.rindex('sh')) #highest index -> 10

# SECTION - case changing of Strings

# print(str.lower()) #lower case
# print(str.upper()) #upper case
# print(str.title()) #title case

# SECTION - string built-in methods
string1 = "sakshi is sakshi, she is sweet"

print(string1.startswith("sh"))  # false
print(string1.endswith("et"))  # true
