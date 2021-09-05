'''
#string concatenation
#suppose we want to create a string that says "subscribe to__"
youtuber = ""
#few ways to do this
print("subscribe to " + youtuber)
print("subscribe to {}".format(youtuber))
print(f"subscribe to {youtuber}")
'''

adj = input("Enter an adjective: ")
verb1 = input("Enter a verb: ")
verb2 = input("Enter the other verb: ")
famous_person = input("Enter name of famous person: ")

madlibs = f"Computer programming is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you're {famous_person}!"

print(madlibs)
