# extract email from a string using regex

import re

text = "HI, I am Sakshi Khatiwada. To contact me, kindly mail me at sakshikhatiwada37@gmail.com"
pattern = r"(\w+)@(\w+)\.(\w+)"  # for email verification using GROUP ()
# print("pattern: ", pattern)
# NOTE \w = word character = a-Z, 0-9, _

match = re.search(pattern, text)

if match:
    # group(0) = entire matched text
    # print(match)
    username = match.group(1)
    domain = match.group(2)
    tld = match.group(3)  # Top-Level Domain

    print("username: ", username, " domain: ", domain, " tld: ", tld)


# learnt
# findall -> Whole string -> List of matches
# match	 -> Beginning only -> Match object or None
# search ->	Whole string -> First match object or None
