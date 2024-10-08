#   If statements evaluate boolean expressions
# Make decisions about which code to run next

temp = input("What's the temprature?\n>")       # Varibale for if statement
temp = int(temp)
if temp >= 80:      # John Boolean
    print(str(temp) + " degrees, wow you better put some lotion on")
if temp < 80:
    print(str(temp) + " degrees, it's a beautiful day ")

else:    # Else takes NO condition and runs when the if above is false
    # Otherwise....
    print("the temperature is " + str(temp) + " degrees.")
    print(str(temp) + " degrees is not hot")