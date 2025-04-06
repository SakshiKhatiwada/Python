# To find if a number is prime or not
import math     #NOTE - import the module

print("To check if a number is prime: ")
number = int (input("Enter the number you want to check: "))
flag = 0 #to keep track whether it's prime or not

for i in range (2, math.ceil(number/2)):
    if (number % i == 0):
       flag = flag + 1
       if (flag ==1):
           break # break the loop if not prime

if (flag == 0):
    print (number, " is a prime number")
else:
    print(number, " is NOT a prime number")
        


