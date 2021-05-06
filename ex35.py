# to exit without error
from sys import exit

# def the gold room, where you have to give in an amount
def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input(">")
    # test to see the input is a number
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

# nice input, you win or you die
    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")

# def the bear room, where you have to face the bear
def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False
    
    # go through the options, to deal with the bear
    while True:
        choice = input(">")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")

# def for the cthulhu room
def cthulhu_room():
    print("Here you seen the great Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

# go through the options for this room, or reset
    choice = input(">")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

# def to print out while you're daed and exit without error
def dead(why):
    print(why, "Good job!")
    exit(0)

# def to start the game, choose out of the options
def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Wich one do you take?")

    choice = input(">")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room untill you starve.")

start()