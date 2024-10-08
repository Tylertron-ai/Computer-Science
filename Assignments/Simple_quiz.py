print("take this are you smarter then a 1st grader quiz")
x = 0

question1 = input("At what frame does Snake's grenade come out in Super smash bros.\n>")
answer1 = "1"
if question1 == answer1:
    print("correct")
    x = x + 1
else:
    print("WORNG")

question2 = input("how many rats are in the rat vangaurd boss fight in ds2\n>")
answer2 = "all of them"
if question2 == answer2:
    print("correct")
    x = x + 1
else:
    print("WRONG")

question3 = input("In the game cuphead which character has the best boss music\n>")
answer3 = "King Dice"
if question3 == answer3:
    print("correct")
    x = x + 1

else:
    print("WRONG")

question4 = input("In the game a way out who is the final boss\n>")
answer4 = "Vince or Leo"
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