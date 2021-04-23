# Following Simple Python Project | Text-Based Adventure Game: Time Unraveled
# Comp Sci Central
# https://www.youtube.com/watch?v=ypNFNr72Xe8
# Game created by Zachary Meisner for learning purposes
#
def intro():
    print()
    print("EVERYTHING IS DARK")
    print("You feel around, using your hands to see.")
    print("The ground is cold, damp, and covered in thick vines.")
    print("You feel a round rock that sinks into the floor when you press it.")
    print("The ground starts rumbling.")
    print("Light begins flooding in.")
    print()
    print('"I\'m in a cave..?"')
    print()
    print("The rock released a boulder that was blocking the cave entrance.")
    print("Three paths are revealed:")
    print()
    print("Path #1: Exit forward through the cave entrance, into the light.")
    print("Path #2: Explore the depths of the rear of the cave, into the darkness.")
    print("Path #3: Climb down the vines into a botomless hole in the ground.")
    print()
    firstPath = input("Which path will you choose? (1/2/3): ")
    if firstPath == '1':
        print()
        path1()
    elif firstPath == '2':
        print()
        path2()
    elif firstPath == '3':
        print()
        path3()

def path1():
    print()

def path1_1():
    print()

def path1_2():
    print()

def path2():
    print()

def path2_1():
    print()

def path2_2():
    print()

def path3():
    print("You climb down the vines into a bottomless hole in the ground.")
    print("It's dark, damp, and hard to climb down the vines, but your vision and muscles eventually adjust.")
    print("A huge boulder slides into place above you, blocking your escape.")
    print("You continue climbing down the vines until you hear something whirring up at you.")
    print("Someone calls out to you.")
    print()
    print('"Hey, hey there!..."')
    print("...My name is HERMES... I'll be your guide to freedom..." )
    print("...Yes, I know all about you! You're looking for CHRONOS...")
    print("...He's the one who trapped you in the time loop...")
    print("...I'm on my way to deliver a message, so I can't escort you personally...")
    print("...However, I can transport you there, or anywhere else on Mount OLYMPUS...")
    print("...CHRONOS is jsut below and he'll certainly TEST YOU when you meet him...")
    print()
    print("HERMES will transport you anywhere on Mount OLYMPUS")
    print("Path #1: Continue below to face CHRONOS.")
    print("Path #2: Read: THE SECRETS OF TIME.")
    print("Path #3: Speak with ARES.")
    print("Path #4: Speak with ARTEMIS.")
    print("Path #5: Speak with APOLLO.")
    print()
    secondPath = input("Which path will you choose? (1/2/3/4/5): ")
    if secondPath == '2':
        path2_2()
    elif secondPath == '3':
        path1_1()
    elif secondPath == '4':
        path1()
    elif secondPath == '5':
        path2()
    else:
        print()
    print("You continue down the vines until you reach the bottom.")
    print("You see a small old woman next to the largest red and black iron-wrought double doors you've ever seen.")
    print("The old woman calls out to you.")
    print()
    print('"Hello there, young traveler..."')
    print('...My name is MOIRAE, I\'m in great need of help...')
    print('...I know who you seek... CHRONOS is just beyond this door...')
    print('...If you enter, you may speak with him and restore your freedom.')
    print('But before you do so, would you take me HOME?...')
    print('...I\'m unable to escape this cold, dark cave on my own...')
    print('...The choice is yours."')
    print()
    print('Path #1: Forget the old woman. Enter the doors and speak with CHRONOS.')
    print("Path #2: Honor the woman's request. Help MOIRAE return home safely.")
    thirdPath = input("Which path would you like to take? (1/2): ")
    if thirdPath == '1':
        path3_1()
    elif thirdPath == '2':
        path3_2()

        
def path3_1():
    print()
    print("You begin walking toward the doors, ignoring MOIRAE's request")
    print('"I would help you out but I\'m in a bit of a hurry, you understand."')
    print("You pull open the massive doors with all of your might and enter.")
    print("Standing now in the largest room, in front of the largest man you've ever seen.")
    print("The room is dark, but you can see the source of the thunderous voice which calls out to you...")
    print()
    print('"Ah... I\'ve been expecting you. But you\'re somewhat early..."')
    print("...It appears you've taken a fairly hard route...")
    print("...Your vision is keen. You see through the darkness and the light...")
    print("...And your strength has grown from your travels...")
    print("...However, there is still just one...")
    print("...One more thing you need to learn")
    print("...And learn you will...")
    print("...In time,\"")
    intro()

def path3_2():
    print("You begin walking toward MOIRAE, honoring her request.")
    print('"I understand, I know what it\'s like to miss home... That\'s why I need to get out of here...')
    print('"But before I walk through those doors, I promise that I\'ll get you home safely."')
    print()
    print('"Ah... I\'ve been expecting you. And you\'re right on time!...')
    print('...It appears you\'ve taken a very difficult route...')
    print("...Your vision is keen, You see through the darkness and the light...")
    print("...And your strength has grown from your travels...")
    print("...You've even put others needs before your own...")
    print("...You have learned everything I have to teach you...")
    print("...So you may finally be free...")
    print("...It's time to return.")
    print()
    print("Thanks for playing!!!")

print()
print()
print(" ###################################")
print(" #                                 #")
print(" #         Time Unraveled          #")
print(" #                                 #")
print(" ###################################")
print()
print()
print("Wha... What happened where am I?")
print("It's too dark to see anything...")
print()
startGame = input("Would you like to start the game? (Y/N): ")
if startGame == 'n' or startGame == 'N':
    print("Maybe next time")
elif startGame == 'y' or startGame == 'Y':
    intro()
