word1 = input("type one word\n>")   #pr0blem 1
word2 = input("type in your second word\n>")    #second input
word3 = input("type in your third word\n>")    #third input
print(word1 + " " + word2 + " " + word3)    #concatnation
# end of problem 1



def add_three(x, y, z):     #problem two
    add_three()    
x = input("type your first number\n>")
x = int(x)
y = input("type in your second number\n>")
y = int(y)
z = input("type in your third number\n>")
z = int(z)
print(x + y + z)


def data_three():
    item = input("type in the name of an item\n>")
    item = str(item)
    number = input("type in a number\n>")
    number = int(number)
    decimal = input("type in a decimal\n>")
    decimal = float(decimal)
    print(str(item) + " = " + str(number) + str(decimal))

data_three()