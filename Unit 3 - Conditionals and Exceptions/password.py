password = input("type in the password\n>")    #variable
if password == "skibidi68":
    print("ACCESS GRANTED, YOU HAVE WON A NEW CAR!")

else:
    print("ACCESS DENIED") 




print("take this are you smarter then a 1st grader quiz")
x = 0

question1 = input("What is:\nX-5 = 5^7\n>")
answer1 = 78130
if question1 == answer1:
    print("correct")
    x = x + 1
else:
    print("WORNG")

question2 = input("what is the second layer of the earth called\n>")
answer2 = "The Mantle"
if question2 == answer2:
    print("correct")
    x = x + 1
else:
    print("WRONG")

question3 = input("What is the 8th planet from the sun\n>")
answer3 = "Neptune"
if question3 == answer3:
    print("correct")
    x = x + 1

else:
    print("WRONG")

question4 = input("Which founding father wrote a letter about the benefits of being with an older woman\n>")
answer4 = "Benjamin Franklin"
if question4 == answer4:
    print("correct")
    x = x + 1

else:
    print("WORNG")

question5 = input("Who is the best boss in Elden Ring\n>")
answer5 = "Bayle the Dread"
if question5 == answer5:
    print("correct")
    x = x + 1

else:
    print("WORNG")

print("you got " + str(x) + "/5 questions right")
