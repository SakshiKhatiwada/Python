# SECTION Implicit Type Conversion
# a = 10
# b = 12.5
# print("sum ", a+b )
 
# d=True
# print(d+b) # 1 + 12.5 = 13.5
# print(b+d)

# print(4 + False)
# print(4 + True) # + 1

# print("sunshine"+"sakshi")
# print(5+"sakshi") error: can't add int and str

#SECTION - Explicit Type Conversion
# s = 12.4
# print (12 + int(s))
# print (12 + s)
# print ( float(12) + s)

# print(float(12))
# OUTPUTS: 
# 24
# 24.4
# 24.4
# 12.0


s = "sakshi"
# print ( list(s) )
# print ( tuple(s) )
# print ( set(s) )
# print ( dict(s) ) -> error: ValueError: dictionary update sequence element #0 has length 1; 2 is required

#OUTPUTS
# ['s', 'a', 'k', 's', 'h', 'i']
# ('s', 'a', 'k', 's', 'h', 'i')
# {'a', 'i', 'h', 's', 'k'}


#SECTION - Number Conversion under ETC
a = 43
print(hex(a))
print(bin(a))
print(oct(a))

''' wow this is also comment 🤣 interesting 😋
#hi 
# dfdf
# dfdf
# '''