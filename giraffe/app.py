print("Hello World")

print(len("Hello World"))
print(50-2.74683)
char_name = "Nishant"
print(char_name.upper().isupper())
print(char_name[3])
print(char_name.index("t"))
print(char_name.replace("h", "s"))
print(char_name.replace("Nishant", "Kanungo"))
print(10 % 3)

my_num = 5
print(my_num)
#str as string
print(str(my_num) + " is my fav number")
#absolute number : we use abs
my_number = -5
print(abs(my_number))
#pow is used as power ex: 4^6
print(pow(4, 6))
#max is used for greater number
print(max(4, 7, 54, 67, -7))
#min is used for lower number
print(min(4, 7, 54, 67, -7))
#round is used as round figure of decimal number
print(round((6.4)))
print(round(6.8))
print(round(6.5))

from math import *
#floor is used for lowest round number of decimal
print(floor(5.8))
#ceil is used for greater round number of decimal
print(ceil(5.3))
#sqrt for square root
print(sqrt(36))
#There are many math functions in math module, need to search

#for input
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hi " + name + "! You are " + age)

#mad libs
color = input("Enter a color: ")
plural_noun = input("Enter a plural noun: ")
celebrity = input("Enter a celebrity: ")

print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)