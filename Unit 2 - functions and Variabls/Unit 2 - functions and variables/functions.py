def top_five_movies(movie_1, movie_2, movie_3, movie_4, movie_5):       #Define a new function
    print("Tyler's top five movies")            #favorite
    print("1. " + movie_1)
    print("2. " + movie_2)
    print("3. " + movie_3)
    print("4. " + movie_4)
    print("5. " + movie_5)

movie_1 = input("What is your favorite movie?") #glaboal variable

x = 4
def my_function():
   global x    #From now on, when I call x, I'm talking about the global version! Not the Local version...
   x = 5
   print(x)    #prints 5

print(x)    #prints 4
my_function()

def add (x, y):
    print(x + y)
    #THIS IS A FUNCTION WITHOUT A RETURN
    #IT IS TOTALLY OKAY FOR THE FUNCTION TO NOT RETURN
sum = add (10, 9)
print(sum)

x = 4   #GLOBAL VARIABLE X as 4
def function():
    x = 5   #define LOCAL VARIABLE x
    print(x)    #print LOCAL VARIABLE