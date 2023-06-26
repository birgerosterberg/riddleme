"""
This is a riddle game that will take you through a test,
to be able to gain a special ability of your own choice!
"""


# to be able to clear the terminal
import os
# To make the nice ascii art!
import pyfiglet
# Colorama to color the text in the console
from colorama import Fore, Style

# clear screen from the os import!
os.system('cls' if os.name == 'nt' else 'clear')

# Ascii art from the pyfiglet import!
ascii_art = pyfiglet.figlet_format("Riddle Me!", font="banner3-D")
print(ascii_art)
input("Press enter to continue...\n")
os.system('cls' if os.name == 'nt' else 'clear')


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
                "Enter your answer (a, b, c, d) or 'x' to give up: \n"
                + Style.RESET_ALL).lower().strip()

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


def display_welcome():
    """
    Displays the first welcome screen!
    """

    print(
        Fore.BLUE +
        "Welcome to the Cave of Mysteries! I have an amazing gift for you.\n")
    print(
        "I can grant you an ability of your choice, "
        "but first,\nyou must prove yourself worthy.\n"
    )
    print(
        "Answer these riddles correctly, and you will prove yourself!\n"
    )
    print("The rules are very simple...")
    print("You have only one try to get it right.")
    print(
        "You will get 4 choices to choose from.\n"
        + Style.RESET_ALL
    )
    input("Press enter to continue...\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    get_name_ability()


def get_name_ability():
    """
    Gets your name and ability!
    """
    name = ""
    ability = ""

    # This while loop make sure that you insert a name and ability that is
    # legit to what i have told the program to do. and 'x' to exit!
    while not name or not ability:
        if not name:
            print(
                Fore.CYAN +
                "First i need to know your name.\n"
            )
            print(
                "It cannot be empty or only contain numbers!\n"
                + Style.RESET_ALL
            )
            name = input("Enter your name: \n").strip()
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
                f"{name.capitalize()} in order to proceed, "
                "please let me know which ability \n"
                "you would like to receive.\n"
            )
            print(
                "It cannot be empty or only contain numbers!\n"
                + Style.RESET_ALL
            )
            ability = input("Enter your ability: \n").strip()
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
        f"Okey, {name.capitalize()}, "
        f"i see you wish to have the ability to {ability.capitalize()}.\n"
    )
    print("Great Choice!")
    print(
        "But to be able to keep this ability you need to pass a few riddles,\n"
        " to be worthy!\n"
        + Style.RESET_ALL
    )
    return riddleme(name, ability)


def riddleme(name, ability):
    """
    The main game function, that runs the riddleme game!
    """
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
            Fore.CYAN +
            f"{name.capitalize()} this is a truly remarkable day, you have "
            "proven to be worthy,\nits with great responsibility "
            "i grant you the ability to"
        )
        ability_art = pyfiglet.figlet_format(ability.capitalize())
        print(ability_art + Style.RESET_ALL)
        exit()

    def ask_riddle():
        """
        Asks the riddle and get the results through the give_riddle function,
        where the verification logic hides!
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
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(f"Game Over {name.capitalize()}!")
                        while True:
                            gameover = input(
                                "Please enter 'y' to try again or 'n' to exit!: \n"
                            ).lower()
                            if gameover == 'y':
                                ask_riddle()
                                break
                            elif gameover == 'n':
                                exit()
                            else:
                                os.system('cls' if os.name ==
                                          'nt' else 'clear')
                                print(
                                    Fore.RED +
                                    "Not valid input.\n"
                                    + Style.RESET_ALL
                                )

                    elif result is None:
                        print(
                            f"Leaving! Bye bye {name.capitalize()}.\n"
                            "now you wont get the ability to "
                            f"{ability.capitalize()}."
                        )
                        exit()
                    else:
                        raise ValueError(
                            "Something went very wrong?!"
                        )
                except ValueError as error:
                    print(error)
    ask_riddle()


def main():
    """
    The function runs the game!
    Firstly displays the welcome message!
    """
    display_welcome()


main()
