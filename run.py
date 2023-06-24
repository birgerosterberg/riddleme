"""
This is a riddle game that will take you through a test,
to be able to gain a special ability of your own choice!
"""
import os
import pyfiglet
# Coloroma to color the text in the console
from colorama import Fore, Style

# clear screen from the os import!
os.system('cls' if os.name == 'nt' else 'clear')

# Ascii art from the pyfiglet import!
ascii_art = pyfiglet.figlet_format("Riddle Me!", font = "banner3-D")
print(ascii_art)


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
                    "Invalid input, chose a valid option: a, b, c, or d\n"
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

    print(
        Fore.BLUE +
        "Welcome to the cave of mysteries, i have an amazing gift!\n")
    print(
        "I can grant you an ability of your own choice\n"
        "but you will have to prove worthy!\n"
        )
    print("Answer correct on these riddles and you will prove yourself!\n"
          + Style.RESET_ALL)
    input("Press enter to continue...")
    name = ""
    ability = ""
    # This while loop make sure that you insert a name and ability that is
    # legit to what i have told the program to do. need to add x to exit!
    while not name or not ability:
        if not name:
            print(
                Fore.CYAN +
                "First i need to know your name.\n"
                "It cannot be empty or only contain numbers!"
                + Style.RESET_ALL
            )
            name = input("Enter your name: ").strip()
            if not name:
                print(
                    Fore.RED +
                    "Name cannot be empty. Please try again.\n"
                    + Style.RESET_ALL)
                continue
            if name.isdigit():
                print(
                    Fore.RED +
                    "Name cannot be purely numeric. Please try again.\n"
                    + Style.RESET_ALL
                    )
                name = ""
                continue

        if not ability:
            print(
                Fore.CYAN +
                "Then you also need to tell me which ability you want."
            )
            print(
                Style.DIM +
                "Cannot be empty or only contain numbers!"
                + Style.RESET_ALL
                )
            ability = input("Enter your ability: ").strip()
            if not ability:
                print(
                    Fore.RED +
                    "Ability cannot be empty. Please try again.\n"
                    + Style.RESET_ALL
                    )
                continue
            if ability.isdigit():
                print(
                    Fore.RED +
                    "Ability cannot be purely numeric. Please try again.\n"
                    + Style.RESET_ALL
                    )
                ability = ""
                continue
    os.system('cls' if os.name == 'nt' else 'clear')
    print(
        Fore.BLUE +
        f"Hi there {name.capitalize()}, "
        f"i see you wish to have the ability to {ability.capitalize()}.\n"
        )
    print("Great Choice!")
    print(
        "But to be able to keep this ability you need to pass a few riddles, "
        "to be worthy!\n"
        + Style.RESET_ALL
        )

    # Where i store the riddles
    riddles = [
        {
            "riddle":
            "What goes and goes but never gets there?",

            "choices":
                ["a. A Watch",
                 "b. Restless person",
                 "c. Tomato",
                 "d. Life"],

            "correct_answer": "a"
        },
        {
            "riddle":
            "What type of lion never roars?",

            "choices":
                ["a. A Mountain Lion",
                 "b. A Lion Cub",
                 "c. A Captured Lion",
                 "d. A Dandelion"],

            "correct_answer": "d"
        },
        {
            "riddle":
            "What can you catch but cannot throw?",

            "choices":
                ["a. A Boomerang",
                 "b. A Tennis ball",
                 "c. Your toys",
                 "d. A Cold"],

            "correct_answer": "d"
        },
        {
            "riddle":
            "Pick me up and scratch my head."
            "I'll turn red and then black. What am I?",

            "choices":
                ["a. A Match",
                 "b. Candle",
                 "c. A Match",
                 "d. None of the above"],

            "correct_answer": "a"
        },
        {
            "riddle":
            "I have a neck, but I dont have a head,"
            " and I wear a cap. What am I?",

            "choices":
                ["a. A Ghost",
                 "b. A Bottle",
                 "c. A Clam",
                 "d. A Snake"],

            "correct_answer": "b"
        }
    ]

    def ability_granted():
        os.system('cls' if os.name == 'nt' else 'clear')
        print(
            Fore.BLUE +
            f"{name} this is a truly remarkable day, you have"
            "proven to be worthy,\n its with great responsibility "
            "i grant you the ability to"
            )
        ability_art = pyfiglet.figlet_format(ability.capitalize())
        print(ability_art + Style.RESET_ALL)

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
                        print(
                            Fore.GREEN + "Correct answer!\n"
                            + Style.RESET_ALL
                              )
                        if how_many_riddles == 5:
                            ability_granted()
                            return
                        break

                    elif result is False:
                        how_many_riddles = 0
                        input(
                            f"{name} you answered wrong, you are not worthy "
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
