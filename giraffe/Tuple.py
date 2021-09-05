
'''
coordinates = (4, 5)
#coordinates[1] = 10 will throw an error as TUPLE is immutable, cannot be changed or modified
print(coordinates[1])

#Functions
def sayhi(name, age):
    print("Hello " + name + " You are " + age)#indented (space in starting) executes under functions else not
sayhi("Anita", "26")
sayhi("Pendu", "26")#calling the function

#Return Statement
def cube(num):
    return num*num*num
print(cube(3))# or result = cube(3)  print(result)

#if statements
is_male = True
is_tall = True
if is_male or is_tall:#either condition has to be true
    print("You are a male or tall or both")
else:
    print("You are neither male or tall")

is_male = True
is_tall = False
if is_male and is_tall:#both conditions has to be true
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but tall")
else:
    print("You are not a male and not tall")

#if statements and comparisons
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(32, 45, -26))

#Dictionaries
#Make sure of duplicate values
monthConversion = {"Jan": "January", "Feb": "February", "Mar": "March", "Apr": "April", "May": "May", "Jun": "June", "Jul": "July", "Aug": "August", "Sep": "September", "Oct": "October", "Nov": "November", "Dec": "December"}
print(monthConversion.get("Dec", "Not a valid key"))#if not a valid key,it will throw not a valid key

#While Loop
i = 1
while i <= 10:#condition, it will loop till the value
    print(i)
    i += 1#it will add 1 and will continue till the loop value

print("Loop is done")

#Building a guessing game
secret_word = "Giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False
while guess != "Giraffe" and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter secret word: ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("You're out of guesses, You Lose!")
else:
    print("You Win!")

#For Loop
for letter in "Nishant":#iteration of each letter in string
    print(letter)

friends = ["Nshant", "Anita" , "Pendu"]
for friend in friends:
    print(friend)

for index in range(len(friends)):
    print(friends[index])


#Exponent Function
print(2**3)#2^3

#power of number
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result
print(raise_to_power(2, 8))

#2D Lists and Nested Loops
num = [[1, 2, 3], [4, 5, 6], [7, 8, 9],[0]]
#       0  1  2    0  1  2    0  1  2   0
#          0          1          2      3
print(num[0][2])#2D List
for row in num:
    for column in row:
        print(column)

#Build a Translator
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation
print(translate(input("Enter a phrase: ")))


#Except
try:
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Invalid Input")

#Reading Files from external files(not python files)
n_i = open("newtch.txt", "r")#r for read the file and w for write on a file and a for append to add new information to file
#and r+ for read and write
print(n_i.read())#read to read, if readable then o/p will be in boolean(whether True/False)
# readline to read only first line of the file
n_i.close()#to cloase a file

#OR in for loop
n_i = open("newtch.txt", "r")
for n in n_i.readlines():
    print(n)
n_i.close()

#Writing to Files
n_i = open("newtch.txt", "a")#w may overwrite on file so a/append is used
n_i.write("xyz -abc")#to add new information into the file
n_i.close()

#Writing a new file
employee_file = open("employees.html", "w")
employee_file.write("<p>This is HTML</p>")
employee_file.close()

#Modules and PIP (importing a python file to existing python file
import Calculator#imported from other python file name Calculator.py
print(Calculator.num1)
#Pip is a package manager,through this we can install external modules which are not present in the version
#used in Command Prompt(cmd)

import docx
docx.
'''


#Inheritance



#Classes and Objects
#Building a multiple choice quiz
from Question import Question

question_pattern =["What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Oranage\n\n",
                   "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
                   "What color are Strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"]

questions = [Question(question_pattern[0], "a"),
             Question(question_pattern[1], "c"),
             Question(question_pattern[2], "b")]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)#prompt used for one by one pattern of question(class)
        if answer == question.answer:
            score += 1
    print("You Scored " + str(score) + "/" + str(len(questions)) + " correct")
run_test(questions)

#Object Functions
#In 2 classes, class chef and class chinese_chef, if class chinese_chef(chef) it copies or inherits the class of chef

#Python Interpreter
# Python can also be written in Command Prompt
