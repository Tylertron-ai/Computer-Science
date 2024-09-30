def add():  #Adding function
    print("Add two numbers")
    x = input("Input first number\n>")
    x = int(x)  #x conversion
    y = input("Input second number\n>")
    y = int(y)  #y conversion
    print(str(x) + " + " + str(y) + " = " + str(x + y))

add()
