import os

def clear():
    os.system('cls')

yes_no = ["yes", "no"]
direction = ["left", "right", "forward", "back"]

print("Welcome to the Dark Knight Hotel. Your adventure will begin momentarily.")
print("All answers will be: left, right, forward, yes, no.")
print("You can enter 'back' at any time to go to the previous room.")
name = input("But first, we must know the name of the guest staying at the hotel tonight. ")
clear()
print("Welcome " + name + ". We hope you enjoy your stay.")
print("\n\nYour adventure begins in a dark castle-type hotel.")
print("Storms have knocked out all electricity.")
print("The only light is that of lightning, that flashes ever so often.")
print("You attempt to find your way to your bed chambers, to sleep through the rest of the night, but you are unfamiliar with this castle.")

def begin():
    beginning = ""
    while beginning not in yes_no:
        beginning = input("\nAre you ready to begin " + name + "?")
        if beginning == "yes": 
            clear()  
            print("We are so glad you will be staying with us. So sorry for the power being out!")       
            great_hall()
        elif beginning =="no":
            clear()
            print("\n\nSorry to hear you will not be staying with us this evening")
            input("\n\nPress the enter key to exit.")
        else:
            print("I don't understand.")

def great_hall():
    print("\n\nYou are in the Great Hall, lined with dozens of tables and chairs.")

    print("With the next flash of lightning, you see there are 2 doorways.")
    print("One straight ahead, and one to the left.")
    proceed = ""
    while proceed not in direction:
        proceed = input("\nHow do you wish to proceed, " + name + "?").lower()
        if proceed == "forward":
            clear()
            print("You chose to go through the door straight ahead of you. Now you are in the kitchen\n")
            kitchen()
        elif proceed == "left":
            clear()
            print("The door to the left of you has brought you to the hallway.\n")
            hallway()
        elif proceed == "right":
            clear()
            print("You cannot go right. You must go forward or left")
            great_hall()
        
    else:
        print("\nI don't understand that. Please type 'forward' or 'left'.")

def kitchen():
    print("\n\nYou are now in the kitchen.")
    print("You bump into something and hear the rustling of many pots and pans.")
    print("There is a doorway to the right and one to the left.")
    proceed2 = ""
    while proceed2 not in direction:
        proceed2 = input("\nHow do you wish to proceed, " + name + "?").lower()
        if proceed2 == "right":
            clear()            
            pantry()
        elif proceed2 == "left":
            clear()
            freezer()
        elif proceed2 == "back":
            clear()
            great_hall()
        elif proceed2 == "forward":
            clear()
            print("You cannot go forward. You must go right or left")
            kitchen()
        else:
            print("\nI don't understand that. Please type 'right', 'left', or 'back.")
            kitchen()

def pantry():
    print("\n\nYou have found the pantry.")
    print("The shelves are lined with unopened boxes and cans of food.")
    print("You feel around finding a snack cake, to satisfy your hunger.")
    print("There is nowhere to go but back.")
    proceed3 = ""
    while proceed3 not in direction:
        proceed3 = input("\nHow do you wish to proceed, " + name + "?").lower()
        if proceed3 == "back":
            clear()
            kitchen()
        else:
            clear()
            print("\nI don't understand that. Please type 'back.")

def freezer():
    print("\n\nYou managed to make your way into the freezer.")
    print("Unfortunately, the freezer has latched behind you.")
    print("You are unable to open the door to make your way back out.")
    print("The hotel staff finds your frozen corpse the next morning.")
    print("Better luck next time, " + name + ".")
    input("\n\nPress the enter key to exit.")

def hallway():
    print("\n\nYou find yourself in a long empty hallway.")
    print("There is a door on the left, a door on the right, and a door straight ahead.")
    proceed4 = ""
    while proceed4 not in direction:
        proceed4 = input("\nHow do you wish to proceed, " + name + "?").lower()
        if proceed4 == "left":
            clear()
            toilet()
        elif proceed4 =="right":
            clear()
            stairwell()
        elif proceed4 =="forward":
            clear()
            corridor()
        elif proceed4 == "back":
            clear()
            great_hall()
        else:
            clear()
            print("\nI don't understand that. Please type 'right', 'left', 'forward', or 'back.")

def toilet():
    print("\n\nYou find the toilet. You have been holding it for a while.")
    print("You take the opportunity to relieve yourself.")
    print("The only way to go is back")
    proceed5 = ""
    while proceed5 not in direction:
        proceed5 = input("\nHow do you wish to proceed, " + name + "?").lower()
        if proceed5 == "back":
            clear()
            hallway()
        elif proceed5 == "left":
            clear()
            print("\nYou cannot go left. You can only go back")
            toilet()
        elif proceed5 == "forward":
            clear()
            print("\nYou cannot go forward. You can only go back")
            toilet()
        elif proceed5 == "right":
            clear()
            print("\nYou cannot go right. You can only go back")
            toilet()
        else:
            clear()
            print("\nI don't understand that. Please type 'back.")

def stairwell():
    print("\n\nBehind this door is a stairwell leading down. It is very cold in this stairwell.")
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
        elif answer == "no":
            clear()
            hallway()
        else:
            clear()
            print("\nI don't understand that. Please type 'yes' or 'no'.\n")

def corridor():
    print("\n\nYou walk forward through the doorway and into a corridor with 2 stairwells.")
    print("One stairwell leads to the left, and the other leads to the right.")
    proceed6 = ""
    while proceed6 not in direction:
        proceed6 = input("\nWhich set of stairs would you like to take, " + name + "?").lower()
    if proceed6 == "left":
        clear()
        study()
    elif proceed6 == "right":
        clear()
        bed_chambers()
    elif proceed6 == "back":
        clear()
        hallway()
    else:
        clear()
        print("\nI don't understand that. Please type 'left', 'right', or 'back.\n")

def study():
    print("\n\nYou walk up the left set of stairs. You find the study")
    print("The walls are lined with enough books to last 50 lifetimes.")
    print("Your only way out is back. You back out and return to the corridor.")
    proceed7 = ""
    while proceed7 not in direction:
        proceed7 = input("\nWhich set of stairs would you like to take, " + name + "?").lower()
    if proceed7 == "back":
        clear()
        corridor()
    else:
        clear()
        print("\nI don't understand that. Please type 'back'.\n")

def bed_chambers():
    print("\n\nYou walk up the stairs to the right.")
    print("After quite some time, you have finally found your chambers.")
    print("You make your way over to the bed, and fall fast asleep.")
    print("You awaken, in the morning, to clear skies and a beautiful day.")
    print("Congratulations " + name + ". You have survived the night. The end.")
    input("\n\nPress the enter key to exit.")

begin()