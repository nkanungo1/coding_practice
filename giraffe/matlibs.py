##
#mad libs
'''
color = input("Enter a color: ")
plural_noun = input("Enter a plural noun: ")
celebrity = input("Enter a celebrity: ")

print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)

#lists
friends = ["Sabyasachi", "Anita", "Rachana", "Jatin", "Goldy"]
#               0            1         2        3        4
#               -5           -4        -3        -2        -1
#lists can take even numbers and booleans other than strings like ["Anita", 26, True]
print(friends[1])
print(friends[-2])
print(friends[1:])#prints all after index 1
print(friends[1:3])#prints from index 1 to index 2 not including 3
friends[3] = "Lalit"
print(friends)

#List Functions
lucky_numbers = [2, 45, 87, 90, 25, 64]
friends = ["Sabyasachi", "Anita", "Goldy", "Goldy", "Rachana", "Jatin", "Goldy"]
friends.extend(lucky_numbers)
#extend function helps to append the lists
print(friends)
friends.append("Don")
#append function helps append an element in the list
print(friends)
friends.insert(2, "Jordan")
#insert function inserts the new element in the index you want to insert
print(friends)
friends.remove("Goldy")
#remove function removes the element you want to remove from the string
print(friends)
friends.clear()
#clear function removes all elements from the list
print(friends)
friends.pop()
#pop function removes the last element of the list
print(friends)
print(friends.index("Anita"))#used for whether the element is present in the list

print(friends.count("Goldy"))#count function counts how many exact elements are there in the list

friends.sort()#sort fuction helps in arrangint the list in alphabatical orders
print(friends)
lucky_numbers.sort()#sort in ascending order
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)#reverse the list

freinds2 = friends.copy()#copy function copies the other list
print(friends2)
##

#Tuples
#Tuples is a Data Structure which cannot be changed, modified, add like list
coordinates = (4, 5)
print(coordinates[1])

employee_file = open("employees.txt", "w")
employee_file.write("Nishant: CEO")
employee_file.close()
'''
#Class

from Student import Student

student1 = Student("Nishant", "Mechanical", 7.9, True)
student2 = Student("Anita", "ETC", 8.0, False)

print(student2.on_honor_roll())
'''


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
        answer = input(question_pattern)
        if answer == question.answer:
            score += 1
    print("You Scored " + str(score) + "/" + str(len(questions)) + " correct")
run_test(questions)
'''

#Intermediate
#Lists
my_list = [0] * 5
print(my_list)
my_list1 = [1, 2, 3, 5, 6]
new_list = my_list + my_list1
print(new_list)

my_list2 = [1, 2, 3, 4, 5]
b = [i*i for i in my_list2]
print(my_list2)
print(b)

#Tuple
my_tuple1 = ("Max", 28, "Boston")
my_tuple2 = "Max", 28, "Boston"
my_tuple3 = ("Max",) #if single element is there it will be string type, so need to put a comma after it
print(type(my_tuple1))

my_tuple4 = tuple(["Max", 28, "Boston"])
print(my_tuple4)

print(my_tuple1[-3])

for i in my_tuple1:
    print(i)

if "Max" in my_tuple1:
    print("Yes")
else:
    print("No")

a = (1, 2, 3, 4, 5, 6, 7, 8, 9)
b = a[::2] # removes every second number
print(b)

tuple = ("Nishant", 27, "Damanjodi")
name, age, area = tuple # number of elements in tuple should be equal to these ex: "name age area" elements
print(name)
print(age)
print(area)

tuple1 = (0, 1, 2, 3, 4, 5)
i1, *i2, i3 = tuple1 # in case of numbers i1 will be 1st, i3 will be last, and rest in between will be i2
print(i1)
print(i3)
print(i2)

#Size
import sys
n_list = [0, 1, 2, "Nishant", True]
n_tuple = (0, 1, 2, "Nishant", True)
print(sys.getsizeof(n_list), "bytes") #size in bytes will be larger than tuple
print(sys.getsizeof(n_tuple), "bytes") #size will be lesser than list

#timeit
import timeit
print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number = 1000000)) # it takes much more time than a tuple
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number = 1000000)) # lesser than list
# Hence tuple is more efficient than list

#Dictionaries: Key-value pairs, Unordered, Mutable
my_dict = {"name": "Anita", "age": 26, "area": "cuttack"}
my_dict1 = {"name": "Nishant", "age": 27, "area": "damanjodi"}
print(my_dict)

my_dict["email"] = "anniesinghdgr8@gamil.com"
print(my_dict)
my_dict["email"] = "nkanungo6@gmail.com"
print(my_dict)

#del my_dict["name"] # del used to delete the element or my_dict.pop("name")
#print(my_dict)
'''
if "name" in my_dict:
    print(my_dict["name"])
OR
'''
try:
    print(my_dict["name"])
except:
    print("Error")

for key in my_dict:
    print(key)
for value in my_dict.values():
    print(value)
for key, value in my_dict.items():
    print(key, value)

my_dict.update(my_dict1)
print(my_dict)

my_dict2 = {3: 9, 6: 36, 9: 81}
print(my_dict2)

value = my_dict2[3]
print(value)

mytuple = (8, 7) # but it will be error in list
mydict = {mytuple : 15}
print(mydict)

#Sets: Unordered, Mutable, No duplicates
myset = {1, 2, 3, 1, 2}
print(myset)# no duplicates

myset1 = set("Hello")
print(myset1)# Unordered

myset2 = set()
myset2.add(1)
myset2.add(2)
myset2.add(3) # add the element

myset2.remove(3) # remove the element
#myset.discard(3) remove the element
#myset.clear() clears the set
#print(myset.pop()) removes the last element
print(myset2)

for x in myset2: # iterate
    print(x)
#union and intersection
odd = {1, 3, 5, 7, 9}
even = {0, 2, 4, 6, 8}
prime = {2, 3, 5, 7}

union = odd.union(even) # combines all the elements
print(union)

intersection = odd.intersection(even) # even and odd don't have the same elements: set()
print(intersection)
intersection1 = odd.intersection(prime) # 3, 5, 7 are common in odd and prime
print(intersection1)

setA = {1,2,3,4,5,6}
setB = {1,2,3}
setC = {7, 8}
diff = setA.difference(setB) # uncommon in setA from B
print(diff)
diff1 = setB.difference(setA) # uncommon in setB from A
print(diff1)
diff2 = setA.symmetric_difference(setB) # all uncommons from both setA and B
#       setB                      setB
print(diff2)

setA.update(setB) # executes all the elements
print(setA)
setA.intersection_update(setB) # executes all the common elements
print(setA)
setA.difference_update(setB)
print(setA)
setA.symmetric_difference_update(setB)
print(setA)

print(setA.issubset(setB))
print(setA.issuperset(setB))
print(setA.isdisjoint(setC))

#Frozen Set
f_set = frozenset([1,2,3,4,5])
# a.add(2) will give an error
#a.remove(1) will give an error
print(f_set)

#Strings: Ordered, Immutable, Text Representation
mystring = "Hello World!" # OR 'Hello World!'
print(mystring)
mystring1 = 'I\'m a programmer' # OR "I'm a programmer"
print(mystring1)
# """   """ triple quotes for multi line sentences

mystring2 = "    Hello World   "
#mystring2 = mystring2.strip() # .strip() removes the unnecessary white spaces OR
print(mystring2.strip())
print(mystring2.find('o')) # finds the index of the character, if it won't find the character returns -1
print(mystring2.count('o')) # counts the number of characters in the string
print(mystring2.replace('World', 'Universe')) # replaces the character in the string

mystring3 = 'how,are,you,doing'
my__list = mystring3.split(',') # makes a string into a list with different elements
print(my__list)
new_string = ''.join(my__list) # joins the list into string
print(new_string)

from timeit import default_timer as timer
my_list3 = ['a'] * 10000000

#bad
start = timer()
my_string = ''
for i in my_list3:
    my_string += i
stop = timer()
print(stop-start)
#good
start = timer()
my_string = ''.join(my_list3)
stop = timer()
print(stop-start)

#Formatting Strings
# %, .format(), f-strings
var = "Tom"
my_string1 = "the variable is %s" %var
print(my_string1)

var1 = 4.574
my_string2 = "the variable is %d" %var1
print(my_string2)

var2 = 4.672
my_string3 = "the variable is %f" %var2
print(my_string3) # OR
my_string3 = "the variable is {:.2f} and {}".format(var2,var1) # :.2f signifies the number of digits after decimal, here it's 2
print(my_string3) # OR
my_string3 = f"the variable is {var2} and {var}"
print(my_string3)

# Collections: Counter, namedtuple, OrderedDict, defaultdict, deque

from collections import Counter
a = "aaaabbbbbccccaaaaabbbcc"
my_counter = Counter(a)
print(my_counter)
print(my_counter.items()) # counts the items
print(my_counter.keys()) # only the keys
print(my_counter.values())
print(my_counter.most_common(1)) # most common elements, (1)/(2)second common element
print(list(my_counter.elements())) # ordered list of elements

from collections import namedtuple
Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
print(pt.x, pt.y)

from collections import OrderedDict
ordered_dict = {} # OR OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
print(ordered_dict)

from collections import defaultdict
d = defaultdict(int) # OR float OR list
d['a'] = 1
d['b'] = 2
print(d)

from collections import deque
d_q = deque()

d_q.append(1)
d_q.append(2)
d_q.appendleft(3)
print(d_q)

d_q.pop()
print(d_q) # remove the last element
d_q.popleft()
print(d_q) # remove the left element
'''
 d_q.clear() remove all elements
 d_q.extend([4,5,6]) extends the list of elements
 d_q.extendleft([4,5,6]) extend the list from left side
 d_q.rotate() rotate the elements
'''
# ITERtools: product, permutations, combinations, accumulate, groupby, and infinite iterators
# These are the data types used in a for loop

from itertools import product
a = [1, 2]
b = [3, 4]
prod = product(a,b, repeat=2)
print(list(prod))

from itertools import permutations
a1 = [1, 2, 3]
perm = permutations(a1)
perm1 = permutations(a1, 2) # permutation in length 2
print(list(perm))
print(list(perm1))

from itertools import combinations, combinations_with_replacement
a2 = [1, 2, 3, 4]
comb = combinations(a2, 2)
print(list(comb))
comb_wr = combinations_with_replacement(a2, 2)
print(list(comb_wr))

from itertools import accumulate
import operator
a3 = [1, 2, 3, 4]
acc = accumulate(a3)
acc1= accumulate(a3, func=operator.mul) # it will multiply in place of adding in 'operator'
print(a3)
print(list(acc)) # 1,3(1+2),6(1+2+3),10(1+2+3+4) according to the taken list
print(list(acc1)) # 1,2(1*2),6(1*2*3),24(1*2*3*4)
a4 = [1, 2, 5, 3, 4]
acc2 = accumulate(a4, func=max)
print(list(acc2)) # [1,2,5,5,5]max number will be continued

'''
from itertools import groupby
def smaller_than_3(x):
    return x < 3
y = [1, 2, 3, 4]
group_obj = groupby(x, key = lambda x: x<3) # OR key = smaller_than_3
for key, value in group_obj:
    print(key, list(value))
'''

from itertools import groupby

persons = [{'name': 'Anita', 'age': 26}, {'name': 'Nishant', 'age': 27},
            {'name': 'Pinku', 'age': 23}, {'name': 'Rachna', 'age': 26}]
group_obj1 = groupby(persons, key = lambda x: x['age'])
for key, value in group_obj1:
    print(key, list(value))
# lambda can take any number of arguments, but can have only one expression
from itertools import count, cycle, repeat
for i in count(10):
    print(i)
    if i ==   15:
        break

'''
c = [1, 2, 3]
for i in cycle(c):
    print(i)# repeat infinitly
'''
for i in repeat(1, 4): # repeat 4 times
    print(i)

# Lambda arguments: expression
add10 = lambda x: x+10
print(add10(5))

#def add10_func(x):
#   return x+10   same as above lambda function
mult = lambda x,y: x*y
print(mult(4,7))


points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
def sort_by_y(x):
    return x[1]
points2D_sorted = sorted(points2D, key=sort_by_y) # lambda x: x[1] sort it by 2nd index
points2D_sorted1 = sorted(points2D, key=lambda x:x[0] + x[1])
print(points2D)
print(points2D_sorted)
print(points2D_sorted1)

# Map (func, seq)
n = [1, 2, 3, 4, 5, 6]
m = map(lambda x:x*2, n)
print(list(m))

m1 = [x*2 for x in n] # easier than above 'map'
print(m1)

# Filter (func, seq)
m2 = filter(lambda x:x%2==0, n) # to get only even numbers
print(list(m2))

m_2 = [x for x in n if x%2==0] # easier than above 'filter'
print(m_2)

# Reduce (func, seq)
from functools import reduce
product_n = reduce(lambda x,y: x*y, n) # 1*2*3*4*5*6=720
print(product_n)

# Exceptions
# Errors and exceptions
# typeerror, FileNotFoundError, ValueError, indexerror, KeyError, ZeroDivisionError

q = -5
if q < 0:
    raise Exception('x should be positive') # to forcefully raise an exception error
assert (x>=0), 'x is not positive' # to raise an assertion error

try:
    w = 5 / 0
except:
    print('an error happened')
# OR except Exception as e:
#         print(e)

