from name import boy_names, girl_names, both_names
# from name import girl_names
# from name import both_names
import random
import string
# import os

"""
Introduction to the game that seeks user input asking if they want to play
"""


def introduction():
    print("Welcome to the Baby Name Matching Robot. I'm here")
    print("to help you pick a name for your new baby.\n")
    print("Would you like to start a matching session?\n")

    intro_answer = input("Please type 'y' for yes or 'n' for no: ")

    if intro_answer == 'y':
        start()
    elif intro_answer == 'n':
        print("Oh that's too bad... maybe next time.")
    elif intro_answer != 'y' or 'n':
        print("That is not a valid input, system will now close...")


"""
Obtains required inputs from users to start the game
"""


def start():
    user1 = input("What is the name of user 1?: ")
    user2 = input("Thanks, can I now have the name of user 2 please?: ")

    print(f"Hello {user1} and {user2}, would you like to select boy names")
    print("girl names or both?")
    gender_selection = input("1.Boy, 2.Girl, 3.Both: ")

    print(f"Hello {user1} and {user2}, are you ready to see which")
    print("baby names you both like?")
    print(f"{user1}, you will go first, {user2}, you will go second.")
    print("When the baby names appear, please type 'y' or 'n'\n")
    print(f"{user1}, are you ready, your names are coming...")
    if gender_selection == 1 or 'boy':
        updated_boy_list1 = boys()
    # if gender_selection == 2 or 'girl':
    #     girls()
    # elif gender_selection == 3 or 'both':
    #     both()


boy_list_1 = []
# girl_list_2 = []
# both_list_3 = []


def boys(length=20):
    # for names in boy_names:
    for name in range(20):
        name = (random.choice(boy_names))
        print(name)
        boys_answer = input("y/n: ")
        if boys_answer == 'y':
            boy_list_1.append(name)
            # print(boy_list_1)
    return boy_list_1


list1 = boy_list_1
introduction()
print(list1)
