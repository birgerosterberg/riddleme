"""
This is a riddle game that will take you through a test,
to be able to gain a special ability of your own choice!
"""
from colorama import Fore, Style


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
        try:
            answer = input(
                Fore.GREEN +
                "Enter your answer (a, b, c, d) or 'x' to exit: "
                + Style.RESET_ALL).lower()

            if answer == "x":
                return None
            elif answer in ["a", "b", "c", "d"]:
                break
            else:
                raise ValueError(
                    Fore.RED +
                    "\nInvalid input, please chose a valid option: a, b, c, or d\n"
                    + Style.RESET_ALL
                    )
        except ValueError as error:
            print(error)

    if answer == correct_answer:
        return True
    else:
        return False


def riddleme():
    """
    The main game function, that runs the riddleme game!
    """
    print("Welcome to the cave of mysteries, i have an amazing gift!\n")
    print(
        "I can grant you an ability of your own choice "
        "but you will have to prove worthy!\n"
        )
    print("You have to answer a few riddles that will test you.\n")
    name = ""
    ability = ""
    # This while loop make sure that you insert a name and ability that is
    # legit to what i have told the program to do. need to add x to exit!
    while not name or not ability:
        if not name:
            print(
                "First you need to tell me your name."
                "It cannot be empty or only contain numbers!"
            )
            name = input("Enter your name: ").strip()
            if not name:
                print("Name cannot be empty. Please try again.\n")
                continue
            if name.isdigit():
                print(
                    "Name cannot be purely numeric. Please try again.\n"
                    )
                name = ""
                continue

        if not ability:
            print(
                "Then you also need to tell me which ability you want."
                "Cannot be empty or only contain numbers!"
                )
            ability = input("Enter your ability: ").strip()
            if not ability:
                print("Ability cannot be empty. Please try again.\n")
                continue
            if ability.isdigit():
                print("Ability cannot be purely numeric. Please try again.\n")
                ability = ""
                continue
    print(
        f"Hi there {name.capitalize()},"
        f"i see you wish to have the ability to {ability.capitalize()}.\n"
        )
    print("Great Choice!")
    print(
        "But to be able to keep this ability you need to pass a few riddles,"
        "to be worthy!\n"
        )

    # Where i store the riddles
    riddles = [
        {
            "riddle":
            "first What goes and goes but never gets where its ment to go?",

            "choices":
                ["a. the clock",
                 "b. restless person",
                 "c. tomato",
                 "d. life"],

            "correct_answer": "a"
        },
        {
            "riddle":
            "second What goes and goes but never gets where its ment to go?",

            "choices":
                ["a. tomato",
                 "b. the clock",
                 "c. restless person",
                 "d. life"],

            "correct_answer": "b"
        },
        {
            "riddle":
            "third What goes and goes but never gets where its ment to go?",

            "choices":
                ["a. tomato",
                 "b. restless person",
                 "c. the clock",
                 "d. life"],

            "correct_answer": "c"
        },
    ]

    def ability_granted():
        print(
            "This day is the day you gained the ability to "
            f"{ability.capitalize()}!"
            )

    def ask_riddle():
        """
        Asks the riddle and get the results through the give_riddle function,
        where the verification logic hides!
        need to end the loop with a victory screen!!!
        """

        # Make sure 5 questions been asked and answered correctly!
        how_many_riddles = 0

        for riddle in riddles:

            while True:
                try:
                    result = give_riddle(
                        riddle["riddle"],
                        riddle["choices"],
                        riddle["correct_answer"]
                        )

                    if result is True:
                        how_many_riddles += 1
                        print("Correct answer!\n")
                        if how_many_riddles == 3:
                            ability_granted()
                            return
                        break

                    elif result is False:
                        how_many_riddles = 0
                        input(
                            f"{name} Sorry you answered wrong "
                            "please press enter to exit!: "
                        ).lower()
                        return
                    elif result is None:
                        print(
                            f"Exit! Bye bye {name.capitalize()}.\n"
                            "now you wont get the ability to "
                            f"{ability.capitalize()}."
                            )
                        return
                    else:
                        raise ValueError(
                            "Something went very wrong?!"
                            )
                except ValueError as error:
                    print(error)
    ask_riddle()


riddleme()
