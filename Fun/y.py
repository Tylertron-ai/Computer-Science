money = 20
fries = False               # not reccommended for kids or anyone but can be used to convince others
ba_da_blaser = False        # comes in handy for tight situations\
ron_anger = False
family_love = False
def begaining():
    print("Your name is Johnny Salami and your a faceless grunt in the mafia, and you only have $20 to your name but things change and your gonna change em' for better or for worse, but above all you'll become a made man")     
#Endings    Made man(rich),  Made man(family), Maid man, Made(game over), Made rat, Made man(Leader), made turncoat, unmade man

    print("\nYour making your way down the street when you suddenly spot that weasel Ron Mcdon peddling his signiture fries on your turf what do you do?\n")
    print("1. Confront Ron Mcdon")                 # Rich / Leader / turncoat / Game Over
    print("2. go to the police and tattle")         # Rat / family / Game Over
    print("3. buy some of his Fries(-$10)")          # Maid / Leader / turncoat / unmaid man
    print("4. Leave, it's none of your business")   # Family / Rich
    

def ron():
    ron_choice = input(">")
    if ron_choice == "1":
        print("\nyou walk up to Ron Mcdon and question him on why he's selling on your turf. Ron Mcdon says that your family doesn't need to know about his little side hussle and offers you a little incentive")
        print("1. Take the money and stay silent (+$15)")                           # Turncoat / Rich
        print("2. 'Whack' Ron and take his stuff (+$25 and Ron Mcdon 'Fries')")     # Leader / Rich
        print("3. Do what is responsible and call the local authorities")           # Game Over
        print("4. Break his legs")                                                  # Leader / Family
        
    bribe_choice = input(">")   
    if bribe_choice == "1": # input 1 path
        print("you take the bribe and walk away")
        global money; money + 15
        print("$" + money)
                
    elif bribe_choice == "2":
        print("\nYou 'whack' Ron Mcdon in the middle of the street and take his loot you get $25, his 'fries' and his ba-da-blaser")
        global ba_da_blaser; True
        global fries; True
        money = money + 25
        print("$" + money)

begaining()
ron()
