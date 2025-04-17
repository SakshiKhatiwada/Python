import re

# re module for regex

# re.search, re.sub, re.split, re.findall

text = "HI, I am Sakshi Khatiwada. **"

x = re.search("^HI .* ada .*", text)
y = re.findall(r"\w", text) #strings having words character -> alphabets, numbers, _ -> ['H', 'I', 'I', 'a', 'm', 'S', 'a', 'k', 's', 'h', 'i', 'K', 'h', 'a', 't', 'i', 'w', 'a', 'd', 'a']
# z = re.findall(r"\W", text) #strings not having words character
print("sub", re.sub("Sak", "shi", text))  # replaces "Sak" by "shi" in the string text
# print(x,y,z)

txt = "The rain in Spain"
x = re.split(r"\s", txt) # always pass raw string r"" for regex
# y = re.split(r"\s", txt, 1)  # only after one occurence
y = re.split(r"\s", txt, maxsplit=1)  # new updata
print(x, y)
