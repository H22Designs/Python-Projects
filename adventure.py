import os

def clear():
    os.system('cls')

yes_no = ["yes", "no"]
direction = ["left", "right", "forward", "back"]

print("Welcome to the Dark Knight Hotel. Your adventure will begin momentarily.")
print("\nAll answers will be: left, right, forward, yes, no.")
print("\nYou can enter 'back' at any time to go to the previous room.")
name = input("\nBut first, we must know the name of the guest staying at the hotel tonight. ")
clear()
print("Welcome " + name + ". We hope you enjoy your stay.")
print("\nYour adventure begins in a dark castle-type hotel.")
print("Storms have knocked out all electricity.")
print("The only light is that of lightning, that flashes ever so often.")
print("You attempt to find your way to your bed chambers, to sleep through the rest of the night, but you are unfamiliar with this castle.")

def begin():
    beginning = ""
    while beginning not in yes_no:
        beginning = input("\nAre you ready to begin " + name + "?").lower()
        if beginning == "yes": 
            clear()  
            print("We are so glad you will be staying with us. So sorry for the power being out!")       
            great_hall()
        elif beginning =="no":
            clear()
            print("Sorry to hear you will not be staying with us this evening")
            input("\n\nPress the enter key to exit.")
        else:
            clear()
            print("I don't understand.")

def great_hall():
    clear()
    print("You are in the Great Hall, lined with dozens of tables and chairs.")
    print("You try to find your way through, but you continuously trip over everything.")
    print("With the next flash of lightning, you see there are 2 doorways.")
    print("One straight ahead, and one to the left.")
    proceed = ""
    while proceed not in direction:
        proceed = input("\nHow do you wish to proceed, " + name + "?").lower()
        if proceed == "forward":
            kitchen()
        elif proceed == "left":
            hallway()
        elif proceed == "right":
            great_hall()
        else:
            clear()
            print("\nI don't understand that. Please type 'forward' or 'left'.")

def kitchen():
    clear()
    print("You are now in the kitchen.")
    print("You bump into something and hear the rustling of many pots and pans.")
    print("There is even less ambient light in here, but with the next ")
    print("flash of lightning, you're able to make out the room.")
    print("There is a doorway to the right and one to the left.")
    proceed2 = ""
    while proceed2 not in direction:
        proceed2 = input("\nHow do you wish to proceed, " + name + "?").lower()
        if proceed2 == "right":
            pantry()
        elif proceed2 == "left":
            freezer()
        elif proceed2 == "back":
            great_hall()
        elif proceed2 == "forward":
            kitchen()
        else:
            clear()
            print("\nI don't understand that. Please type 'right', 'left', or 'back.")

def pantry():
    clear()
    print("You have found the pantry.")
    print("The shelves are lined with unopened boxes and cans of food.")
    print("You feel around finding a snack cake, to satisfy your hunger.")
    print("With your sweet tooth satisified, you grow slightly more tired.")
    print("There is nowhere to go but back.")
    proceed3 = ""
    while proceed3 not in direction:
        proceed3 = input("\nHow do you wish to proceed, " + name + "?").lower()
        if proceed3 == "back":
            kitchen()
        else:
            clear()
            print("\nI don't understand that. Please type 'back.")

def freezer():
    clear()
    print("You managed to make your way into the freezer.")
    print("Unfortunately, the freezer has latched behind you.")
    print("You are unable to open the door to make your way back out.")
    print("The hotel staff finds your frozen corpse the next morning.")
    print("Better luck next time, " + name + ".")
    input("\n\nPress the enter key to exit.")
    quit()

def hallway():
    clear()
    print("You find yourself in a long empty hallway.")
    print("With your arms stretched out, you're able to locate a few doorways in the darkness.")
    print("There is a door on the left, a door on the right, and a door straight ahead.")
    proceed4 = ""
    while proceed4 not in direction:
        proceed4 = input("\nHow do you wish to proceed, " + name + "?").lower()
        if proceed4 == "left":
            toilet()
        elif proceed4 =="right":
            stairwell()
        elif proceed4 =="forward":
            corridor()
        elif proceed4 == "back":
            great_hall()
        else:
            clear()
            print("\nI don't understand that. Please type 'right', 'left', 'forward', or 'back.")

def toilet():
    clear()
    print("You find the toilet. You have been holding it for a while.")
    print("You take the opportunity to relieve yourself.")
    print("The only way to go is back")
    proceed5 = ""
    while proceed5 not in direction:
        proceed5 = input("\nHow do you wish to proceed, " + name + "?").lower()
        if proceed5 == "back":
            hallway()
        elif proceed5 == "left":
            toilet()
        elif proceed5 == "forward":
            toilet()
        elif proceed5 == "right":
            toilet()
        else:
            clear()
            print("\nI don't understand that. Please type 'back.")

def stairwell():
    clear()
    print("Behind this door is a stairwell leading down. It is very cold in this stairwell.")
    print("You smell a strange odor?")
    answer = ""
    while answer not in yes_no:
        answer = input("\nDo you wish to descend the stairwell, " + name + "?").lower()
        if answer == "yes":
            print("\n\nYou begin your descent down the stairwell.")
            print("As you reach the bottom, you slowly walk forward attempting to find out where you are.")
            print("After a couple steps, you fall into a well.")
            print("You put in a good effort to climb out, but as time goes on, your arms become weak.")
            print("Unfortunately, you eventually drown. Better luck next time, " + name + ".")
            input("\n\nPress the enter key to exit.")
            quit()
        elif answer == "no":
            hallway()
        else:
            clear()
            print("\nI don't understand that. Please type 'yes' or 'no'.\n")

def corridor():
    clear()
    print("You walk forward through the doorway and into a corridor with 2 stairwells.")
    print("One stairwell leads to the left, and the other leads to the right.")
    proceed6 = ""
    while proceed6 not in direction:
        proceed6 = input("\nWhich set of stairs would you like to take, " + name + "?").lower()
    if proceed6 == "left":
        study()
    elif proceed6 == "right":
        bed_chambers()
    elif proceed6 == "back":
        hallway()
    else:
        clear()
        print("\nI don't understand that. Please type 'left', 'right', or 'back.\n")

def study():
    clear()
    print("You walk up the left set of stairs. You find the study")
    print("The walls are lined with enough books to last 50 lifetimes.")
    print("As an avid reader, you would love to take a look at their selection, ")
    print("but this would be very difficult in the dark.")
    print("Your only way out is back.")
    proceed7 = ""
    while proceed7 not in direction:
        proceed7 = input("\nHow would you like to proceed, " + name + "?").lower()
    if proceed7 == "back":
        corridor()
    else:
        clear()
        print("\nI don't understand that. Please type 'back'.")

def bed_chambers():
    clear()
    print("You walk up the stairs to the right.")
    print("After quite some time, you have finally found your chambers.")
    print("You make your way over to the bed, and fall fast asleep.")
    print("You awaken, in the morning, to clear skies and a beautiful day.")
    print("Congratulations " + name + ". You have survived the night.")
    print(
            """
            TTTTT  H   H  EEEEE
              T    H   H  E
              T    H   H  E
              T    HHHHH  EEE
              T    H   H  E
              T    H   H  E
              T    H   H  EEEEE

            EEEEE  N   N  DDDD
            E      NN  N  D   D
            E      N N N  D   D
            EEE    N N N  D   D
            E      N N N  D   D
            E      N  NN  D   D
            EEEEE  N   N  DDDD
            """
         )
    input("\n\nPress the enter key to exit.")

begin()
