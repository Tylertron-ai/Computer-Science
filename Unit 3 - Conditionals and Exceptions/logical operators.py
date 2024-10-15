# Logical operators
# Comparison operators > < == >= <=
# Arithmetic operators + - / * % ** //

def check_age(age, exp):
    #you must be 18+ yars and have 1 year experience to be eligible
    if age >= 18 and exp >= 1:
        print("You are eligible for the comp!")
    elif age < 18:
        print("get outta here kid!")
    elif exp < 1:
        print("You are not eligible for the comp!")

    a = int(input("How old are you?\n>"))
    e = int(input("How many years of experience do you have?\n>"))

    check_age(a, e) 