########################################################################
#Stuti Sapru
#CS 30
#March 14, 2023
#A simple version of a "Choose your adventure" game
########################################################################


def game_over():
    """
    The user chooses to quit the game
    """
    print("\nYou exist no more. Perhaps you have never existed. Goodbye.")


def other():
    """
    The user types an invalid input
    """
    print("\nI didn't understand that. Please restart the game and try again.")


def run():
    """
    The user chooses to run
    """
    print("\nYou have chosen to run. 20 minutes into your run, you smell "
        "burning and look back to see your house on fire. You think you have "
        "been saved. But you are never safe. \n\n5 minutes later, you are "
        "attacked by zombies. As they are about to bite you, you are "
        "transported back in time. You are given the option to start your "
        "day again. Perhaps this time you will be luckier.")


def start():
    """
    prints out the main menu and provides the user with choices to procees the 
    game 
    """
    print("\nIt's a new day! What would you like to do today?")
    path = input("laze around in bed, make some breakfast or go for a run?")

    if path == "laze around in bed":
        #if the user chooses to stay in bed
        print("\nYou decide to stay in bed for a little bit longer. You pick "
            "up your phone to check the news but your phone is detected on the"
            " server. You have to run now. There goes your lazy morning!")
        path2 = input("Do you want to stay or run?")

        if path2 == "stay":
            #if the user chooses to stay in the house
            print("\nYou decide to stay and fight but it is too late for "
                " you now. Perhaps it has been too late for you for a "
                "while now. You have already sealed your fate. Would you "
                "like to change your fate?")
            path3 = input("yes or no?")

            if path3 == "yes":
                #if the user chooses to change their fate and run
                run()
                start()

            elif path3 == "no":
                #if the user chooses not to change their fate and stay in the
                #house
                print("\nToo bad. You have never had a chance to chose "
                    "your fate and you never will. You are forced to run.")
                run()
                start()

            elif path3 == "quit":
                #if the user chooses to quit the game
                game_over()

            else:
                #invalid user entry
                other()
                start()

        elif path2 == "run":
            #if the user chooses to run ionstead of stay in the house
            run()
            start()

        elif path2 == "quit":
            #if the user chooses to quit the game
            game_over()

        else:
            #invalid user entry
            other()
            start()

    elif path == "go for a run":
        #if the user chooses to run initially
        run()
        start()

    elif path == "make some breakfast":
        #if the user chooses to make some breakfast initially
        print("\nYou're hungry so you head to make breakfast. It's eerily "
            "quiet for this time of the morning but you don't notice. A "
            "fatal mistake.\n\nEventually, you feel the eyes on you. But by "
            "the time you reach for the knife, it's too late. As you feel "
            "them bite into you, you're transported back in time. You're "
            " given the option to choose your day again. Perhaps this time "
            "you'll be luckier.")
        start()

    elif path == "quit":
        #if the user chooses to quit the game
        game_over()

    else:
        #invalid user entry
        other()
        start()

#these are the user instructions in order for the program to work
print("Please type all answers in lower case and exactly as given in the "
    "question.\nFor example, when asked if you want to check your texts or "
    "go for a run, you would answer 'check your texts' or 'go for a run' "
    "only. \n\nHope you enjoy the game! To stop, type 'quit' at any time.")
#starts the game
start()