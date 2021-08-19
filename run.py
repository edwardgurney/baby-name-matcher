import name

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
       
def start():
    user1 = input("What is the name of user 1?: ")
    user2 = input("Thanks, can I now have the name of user 2 please?: ")

    print(f"Hello {user1} and {user2}, are you ready to see which")
    print("baby names you both like?")
    print(f"{user1}, you will go first, {user2}, you will go second.")
    print("When the baby names appear, please type 'y' for yes and 'n' fo no\n")
    print(f"{user1}, are you ready, your names are coming...")


introduction()
