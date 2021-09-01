from name import boy_names, girl_names, both_names
import random


name_list_1 = []
name_list_2 = []
new_name_list = []


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
        quit()
    elif intro_answer != 'y' or 'n':
        print("That is not a valid input, please try again...")
        introduction()


"""
Obtains required inputs from users to start the game
"""


def start():

    global user1
    global user2
    user1 = input("What is the name of user 1?: \n")
    user2 = input("Thanks, can I now have the name of user 2 please?: \n")

    print(f"Hello {user1} and {user2}, are you ready to see which")
    print("baby names you both like?\n")
    print(f"{user1}, you will go first, {user2}, you will go second...")
    print("When the baby names appear, please type 'y' or 'n'\n")
    print("Would you like to 1select boy names, girl names or both?")

    gender_selection = input("1.Boy, 2.Girl, 3.Both: ")
    if gender_selection == str(1) or gender_selection == 'boy':
        name_generation('boy')
    elif gender_selection == str(2) or gender_selection == 'girl':
        name_generation('girl')
    elif gender_selection == str(3) or gender_selection == 'both':
        name_generation('both')
    else:
        print("You entered and ivalid input, try again...\n")
        start()


"""
- Iterates through boy_names list generating 20 random names,
removes that name from the list (to prevent repeat names) and
creates new list so user 2 can receive same names.
- Asks user for input, if they like the name and if so, is
appended to a new list to compare with user 2.
"""


def name_generation(a):
    print(f"{user1}, are you ready, your names are coming...")
    if a == 'boy':
        names = boy_names
    if a == 'girl':
        names = girl_names
    if a == 'both':
        names = both_names
    for name in range(20):
        name = (random.choice(names))
        if a == 'boy':
            boy_names.remove(name)
        if a == 'girl':
            girl_names.remove(name)
        if a == 'both':
            both_names.remove(name)

        new_name_list.append(name)

    result = new_name_list
    user_choice(result)
    return result


def user_choice(names):
    global user_answer
    for name in names:
        print(name)
        while True:
            user_answer = input("y/n: ")
            if user_answer == 'y':
                name_list_1.append(name)
                break
            elif user_answer == 'n':
                break
            else:
                print("Sorry, invalid input, please enter 'y' or 'n'\n")
                print(name)

    user2_start()
    return name_list_1,


"""
- Prints out the same randomly generatd boy list that user 1 received
- User 2 selects if they like the name and if so, name is appended
to another lise to compare to user 1's selections
"""


def user2_start():
    print(f"{user2} it's now your turn... get ready..." + "\n")
    for name in new_name_list:
        print(name)
        while True:
            user2_answer = input("y/n:\n ")
            if user2_answer == 'y':
                name_list_2.append(name)
                break
            elif user2_answer == 'n':
                break
            else:
                print("Sorry, invalid input, please enter 'y' or 'n'\n")
                print(name)

    check_matches()
    return name_list_2,


"""
Compares both boy name lists from both users and checks for matches,
calling required function dependent on reulsts of data.
"""


def check_matches():
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

    return matches


"""
Prints statement to users if no matches
"""


def game_over():
    print("Sorry, no matches. You'll have to play again")


"""
Prints statement to users advising them of their matches
"""


def results(list):
    print("The names you both like are: ")
    print(', '.join(matches))


list1 = name_list_1
list2 = name_list_2
introduction()
