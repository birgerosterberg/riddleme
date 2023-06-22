"""
This is a riddle game that will take you through a test,
to be able to gain a special ability of your own choice!
"""


def give_riddle(riddle, choices, correct_answer):
    """
    The function that controls and gives the riddles!
    """
    print(riddle)
    # prints all choices row for row!
    for choice in choices:
        print(choice)
    # making sure the letter entered is a valid option!!
    while True:
        answer = input("Enter your answer (a, b, c, d) or 'x' to exit: ").lower()

        if answer == "x":
            return None
        elif answer in ["a", "b", "c", "d"]:
            break
        else:
            print("Invalid input! Please chose a valid option!\n a, b, c, d")

    if answer == correct_answer:
        print("Correct answer!\n")
        return True
    else:
        print("Wrong answer!\n")
        return False


def riddleme():
    """
    The main game function, that runs the riddleme game!
    """
    print("Welcome to the cave of mysteries, i have an amazing gift!\n")
    print("I can grant you an ability of your own choice, but to get it you will have to prove worthy!\n")
    print("You have to answer a few riddles that will test you.\n")
    name = ""
    ability = ""
    # This while loop make sure that you insert a name and ability that is legit to what i have told the program to do. need to add x to exit!
    while not name or not ability:
        if not name:
            print("First you need to tell me your name. It cannot be empty or only contain numbers!")
            name = input("Enter your name: ")
            if not name:
                print("Name cannot be empty. Please try again.\n")
                continue
            if name.isdigit():
                print("Name cannot be purely numeric. Please try again.\n")
                name = ""
                continue

        if not ability:
            print("Then you also need to tell me which ability you want to learn. Cannot be empty or only contain numbers!")
            ability = input("Enter your ability: ")
            if not ability:
                print("Ability cannot be empty. Please try again.\n")
                continue
            if ability.isdigit():
                print("Ability cannot be purely numeric. Please try again.\n")
                ability = ""
                continue
    print(f"Hi there {name.capitalize()} i see you wish to have the ability to {ability.capitalize()}.\n")
    print("Great Choice!")
    print("But to be able to keep this ability you need to pass a few riddles, to be worthy!\n")

    # Where i store the riddles
    riddles = [
        {
            "riddle": "first What goes and goes but never gets where its ment to go?",
            "choices": ["a. the clock", "b. restless person", "c. tomato", "d. life"],
            "correct_answer": "a"
        },
        {
            "riddle": "second What goes and goes but never gets where its ment to go?",
            "choices": ["a. tomato", "b. the clock", "c. restless person", "d. life"],
            "correct_answer": "b"
        },
        {
            "riddle": "third What goes and goes but never gets where its ment to go?",
            "choices": ["a. tomato", "b. restless person", "c. the clock", "d. life"],
            "correct_answer": "c"
        },
        {
            "riddle": f"Wow {name.capitalize()} you made it through the test, the ability to {ability.capitalize()} is now yours, use it with good intention! Press the button 'e' to exit!",
            "choices": [],
            "correct_answer": "e"
        }
    ]

    def ask_riddle():
        """
        Asks the riddle and get the results through the give_riddle function, where
        the verification logic hides!
        need to end the loop with a victory screen!!!
        """

        for riddle in riddles:
            while True:
                result = give_riddle(riddle["riddle"], riddle["choices"], riddle["correct_answer"])
                if result is True:
                    print("True")
                    break
                elif result is False:
                    # right now continues until i get the right answer, will have to give a choice of exit or try again that sends user back to the start!
                    gameover = input(f"{name} would you like to restart if so 'y' for yes else 'n' to exit (y/n): ").lower()
                    if gameover == "n":
                        return
                    else:
                        ask_riddle()
                elif result is None:
                    print(f"Exit! Bye bye {name.capitalize()}, now you wont get the ability to {ability.capitalize()}.")
                    return None
    ask_riddle()


riddleme()
