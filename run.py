from name import boy_names, girl_names, both_names
import random

"""
Introduction to the game that seeks user input asking if they want to play
"""

boy_list_1 = []
boy_list_2 = []
girl_list_1 = []
girl_list_2 = []
both_list_1 = []
both_list_2 = []
new_boy_list = []
new_girl_list = []
new_both_list = []
# updated_boy_list1 = []
t1 = ()
t2 = ()


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
    # global updated_boy_list1
    user1 = input("What is the name of user 1?: \n")
    user2 = input("Thanks, can I now have the name of user 2 please?: \n")

    print(f"Hello {user1} and {user2}, are you ready to see which")
    print("baby names you both like?\n")
    print(f"{user1}, you will go first, {user2}, you will go second...")
    print("When the baby names appear, please type 'y' or 'n'\n")
    print("Would you like to 1select boy names, girl names or both?")

    gender_selection = input("1.Boy, 2.Girl, 3.Both: ")
    print(f"{user1}, are you ready, your names are coming...")
    if gender_selection == str(1) or gender_selection == 'boy':
        boys()
    elif gender_selection == str(2) or gender_selection == 'girl':
        girls()
    elif gender_selection == str(3) or gender_selection == 'both':
        both()


def boys():
    global boys_answer
    global new_boy_list
    global t1

    for name in range(20):
        name = (random.choice(boy_names))
        boy_names.remove(name)
        print(name)
        new_boy_list.append(name)
        boys_answer = input("y/n: ")
        if boys_answer == 'y':
            boy_list_1.append(name)

    user2_boy_start()
    return new_boy_list, boy_list_1, t1


def girls():
    global girls_answer
    global new_girl_list

    for gname in range(20):
        gname = (random.choice(girl_names))
        girl_names.remove(gname)
        print(gname)
        new_girl_list.append(gname)
        girls_answer = input("y/n: ")
        if girls_answer == 'y':
            girl_list_1.append(gname)

    print(girl_list_1)
    user2_girl_start()
    return girl_list_1, new_girl_list


def both():
    global both_answer
    global new_both_list
    for bname in range(20):
        bname = (random.choice(both_names))
        both_names.remove(bname)
        print(bname)
        new_both_list.append(bname)
        both_answer = input("y/n: ")
        if both_answer == 'y':
            both_list_1.append(bname)

    print(both_list_1)
    user2_both_start()
    return new_both_list, both_list_1


"""
Prints out the same randomly generatd boy list that user 1 had, for user 2
"""


def user2_boy_start():
    global t2
    list.clear(boy_list_2)
    print(f"{user2} it's now your turn... get ready..." + "\n")
    for name in new_boy_list:
        print(name)
        user2_answer = input("y/n: ")
        if user2_answer == 'y':
            boy_list_2.append(name)

    # print(boy_list_2)

    check_matches_boys()
    return boy_list_2, t2


"""
Compares both boy name lists from both users and checks for matches
"""


def check_matches_boys():
    global matches
    a = list1
    b = list2
    matches = []
    for x in a:
        if x in b:
            matches.append(x)

    if len(matches):
        results(matches)
    else:
        game_over()

    print(matches)
    # results(matches)
    return matches


def game_over():
    print("Sorry, no matches. You'll have to play again")


"""
Prints out the same randomly generatd girl list that user 1 had, for user 2
"""


def user2_girl_start():
    print(f"{user2} it's now your turn to play... get ready..." + "\n")
    for name in new_girl_list:
        print(name)
        user2_answer = input("y/n: ")
        if user2_answer == 'y':
            girl_list_2.append(name)

    # print(girl_list_2)
    check_matches_girls()
    return girl_list_2


# def check_matches_girls():
#     global matches
#     a = list3
#     b = list4
#     girl_matches = []
#     for x in a:
#         if x in b:
#             girl_matches.append(x)

#     print(girl_matches)
#     results(girl_matches)
#     return girl_matches


def check_matches_girls():
    global matches
    a = list3
    b = list4
    matches = []
    for x in a:
        if x in b:
            matches.append(x)

    if len(matches):
        results(matches)
    else:
        game_over()

    # print(matches)
    # results(matches)

    # print(matches)
    # results(matches)
    return matches


"""
Prints out the same randomly generatd both names list that user 1 had,
for user 2 to enter responses
"""


def user2_both_start():
    print(f"{user2} it's now your turn... get ready")
    for name in new_both_list:
        print(name)
        user2_answer = input("y/n: ")
        if user2_answer == 'y':
            both_list_2.append(name)

    # print(both_list_2)
    check_matches_both()
    return both_list_2


def check_matches_both():
    global matches

    a = list5
    b = list6
    matches = []
    for x in a:
        if x in b:
            matches.append(x)

    if len(matches):
        results(matches)
    else:
        game_over()

    # print(matches)
    # results(matches)
    # print(matches)
    # results(matches)
    return matches


def results(list):
    print(f"The names you both like are {matches}")


list1 = boy_list_1
list3 = girl_list_1
list4 = girl_list_2
list2 = boy_list_2
list5 = both_list_1
list6 = both_list_2
introduction()
# print(list1)
# print(list2)
# print(list3)
# print(list4)

# user2_boy_start()
# user2_girl_start()
# user2_both_start()
# print(boy_list_1)
# check_matches_boys()
