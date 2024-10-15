# String functions1
# A group of like-functions that manipulate strings 
# They modify strings
# SUPER easy and convenient to use
# Pyton would really not be fun without them

#  .Lower()
# converts a string to all lowercase
# no matter what the input casing is, it is coverted to lowercase
# and the answer is lowercase
input_answer = "Lord of The Rings".lower() # makes line 12 irrelevent
input_answer = input_answer.lower() # Converts to "lord of the rings"
real_answer = "lord of the rings"
print(input_answer == real_answer)

#.upper()
# Converts a string to uppercase!
x = "hello word".upper()
print(x)    # prints HELLO WORLD

# .capitalize()
# converts to lowercase, then capitalizes the first letter
y=" HeLlo wOrlD".capitalize
print(y)    # print "Hello world"

# .title()
# converts a string to titlecase
#capital first letters of words
z = "hellO WoRld".title()
print(z)    # print "Hello World"

# .swapcase()
# it inverts the caseing of each character
q = "hello world!"