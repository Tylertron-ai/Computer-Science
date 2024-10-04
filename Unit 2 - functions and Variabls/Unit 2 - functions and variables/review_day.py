#2 functions
print("Goodbye ")
input("enter your mothers name\n>") #\n is called an escape character
# \n starts a new line (linebreak)
#input is never required

#varibales
#syntax
#   <name> = <value>
x = 5

#snake naming convention = all lowercdase, underscore for spaces
# CONCISE: Short and descriptive
username = "Tyler"              #Define
george = "favorite icecream"    #Define
stupid = 75              #Define
percent_complete = 23.45        #Define float (decimal number)
is_cool = True                  #Define Boolean (True/False)
first_letter = 'c'              #Define Chatacter (single symbol)

stupid = 6               #Reassign


#Arithmetic Operators
# +, -, *, /, **, %, //

print(4 + 4)        #> 8
print("4" + "4")    #> 44
print("cat" * 3)    #> catcatcat
print("cat" + 3)    #ERROR: Cannot use + for string and int

#make some working programs
#1. add two numbers using input
x = input("what is x>\n>")      #input() always returns a string
x = int(x)      # Convert from string to int
y = input("what is y>\n>")      # even if you type in a number
y = int(y)      # convert from string to int
print(x + y)

x = int(input("what is x?\n"))  #alt conversion

# 2. Converts celcius to farenheight
temp_celcius = input("What is the temperature in Celcius>\n>")
temp_celcius = int(temp_celcius)
temp_farenheight = (temp_celcius * 1.8) + 32
print(temp_celcius + " degrees C equals " + temp_farenheight + " degrees F")

#Some conversion functions
str()
int()
float()
bin()
bool()

#the stuff that goes between the parenthesis is called PARAMETERS
#Parameters are the values that the function needs to run


#Functions
# Functions are a lot like varibales
# They have names
# They can be recalled from memory by calling their name
# Store information
# Varibales store values, function store code
def potato():       #def keyword + name + () + :
    print("totato") #lines indented underneath are "inside" he function

# functions are not ran when they are defined
# they must be called by their name to run
potato()        # Every function call needs open and closed parenthesis
                # Even if it has no parameters

def jump(how_high):
    print("You jumped " + str(how_high) + " inches!")

jump(578)

def make_a_word(a, b, c, d, e, f, g, h, i):
    print( a + b + c + d + e + f + g + h + i)

    #functions can have many lines
    def top_ten_games():
        print("1. Elden ring")
        print("2. super smash bros")
        print("3. fallout New Vegas")
        print("4. Skyrim")
        print("5. Sekiro")
        print("6. Ashuras wrath")
        print("7. KOTOR II")
        print("8. ultimate chicken horse")
        print("9. Battlefront II")
        print("10 COD II")

#Scope: Global and local Varibales!
#Scope refers to the context in which the varibale was defined
#GOBAL- defined at no indentation level
#LOCAL  defined inside of a function

#Global varibales can be used anywhere
todd = "cool guy"       #Global varibale- no indentation level

#local varibales only exist in the scope they were defined
def my_function():
    smith = "not cool guy"  #Local caribale- define in a function
    todd = "strange guy"    #Locla caribale even though it has the same name
    print(todd)     #prints "strange guy" - local caribale
    #When you call a varibale in a function
    # It searches local varibales first, then global varibales

#If you want to reassign a global varibale inside of a function
todd = "cool guy"
def my_function2():
    global todd             # in this function whenever I call todd
                            #I mean the global todd, not the local
    todd = "strange guy"    # Reassign todd - global
    print(todd)             #print todd - global

    #Return functions
    # Functions can also return values
    # the value that is returened is sent back to where the function was called
    # This is very similar to how a varibale works
    # The function does its work and returns an answer back
def add2(x, y):
    return x + y    #rreturns the sum of x and y to where the function was called

answer = add2(2, 10)
print(answer)
