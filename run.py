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

    intro_answer = input("Please type 'y' for yes or 'n' for no: \n")

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
    global user1
    global user2
    global updated_boy_list1
    user1 = input("What is the name of user 1?: \n")
    user2 = input("Thanks, can I now have the name of user 2 please?: \n")

    print(f"Hello {user1} and {user2}, are you ready to see which")
    print("baby names you both like?\n")
    print(f"{user1}, you will go first, {user2}, you will go second...")
    print("When the baby names appear, please type 'y' or 'n'\n")
    print("Would you like to 1select boy names, girl names or both?")

    gender_selection = input("1.Boy, 2.Girl, 3.Both: ")
    print(f"{user1}, are you ready, your names are coming...")

    # print(gender_selection)
    # print("BOY")

    if gender_selection == str(1) or gender_selection == 'boy':
        updated_boy_list1 = boys()
        # list 1
        # print(updated_boy_list1[0])
        #list 2
        # print(updated_boy_list1[1])

    elif gender_selection == str(2) or gender_selection == 'girl':
        updated_girl_list2 = girls()
    elif gender_selection == str(3) or gender_selection == 'both':
        updated_both_list3 = both()


boy_list_1 = []
boy_list_2 = []
girl_list_2 = []
both_list_3 = []
new_boy_list = []


def boys():
    global boys_answer
    # for names in boy_names:
    for name in range(20):
        name = (random.choice(boy_names))
        boy_names.remove(name)
        print(name)
        new_boy_list.append(name)
        boys_answer = input("y/n: ")
        if boys_answer == 'y':
            boy_list_1.append(name)

    # print(new_boy_list)
    return new_boy_list, boy_list_1


def girls():
    for gname in range(20):
        gname = (random.choice(girl_names))
        girl_names.remove(gname)
        print(gname)
        girls_answer = input("y/n: ")
        if girls_answer == 'y':
            girl_list_2.append(gname)

    return girl_list_2


def both():
    for bname in range(20):
        bname = (random.choice(both_names))
        both_names.remove(bname)
        print(bname)
        both_answer = input("y/n: ")
        if both_answer == 'y':
            both_list_3.append(bname)

    return both_list_3


"""
Prints out the same randomly generatd list that user 1 had, for user 2
"""


def user2_start():
    print(f"{user2} it's now your turn... get ready..." + "\n")
    # my_list = len(new_boy_list)
    for name in range(20):
        print(name)
        user2_answer = input("y/n: ")

#     name2 = (random.choice(updated_boy_list1))
#     updated_boy_list1.remove(name2)
#     print(name2)
#     boys_answer2 = input("y/n: ")
#     if boys_answer2 == 'y':
#         boy_list_2.append(name2)

#     return boy_list_2


list1 = boy_list_1
list2 = girl_list_2
list3 = both_list_3
# list4 = boy_list_2
introduction()
print(list1)
print(list2)
print(list3)
# print(list4)
user2_start()
