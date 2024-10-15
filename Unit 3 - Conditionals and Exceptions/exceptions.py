# Exception Handling
# Write a program that asks for two numbers and adds them

# if     =   try
#elif    =   except specific error type
# else   =   except
def divide_two_numbers():
    try:
        x = int(input("Whats the first number?\n>"))
        y = int(input("Whats the second number?\n>"))
        print(x / y)
        divide_two_numbers()

    except TypeError:
        print("Invalid entry....")
        divide_two_numbers()

    except ZeroDivisionError:
        print("you can't divide by zero...")
        divide_two_numbers()
    finally:
        print()
    
divide_two_numbers()
