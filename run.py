"""
This is a riddle game that will take you through a test,
to be able to gain a special ability of your own choice!
"""

def give_riddle(riddle, choices, correct_answer):
    """
    The function that controls and gives the riddles!
    need to add verification for choices.
    needs to add None to exit, which will be x?!
    needs to add validation for which letter is entered... a b c or d should be possible and x for exit!
    """
    print(riddle)
    # prints all choices row for row!
    for choice in choices:
        print(choice)
    answer = input("Enter your answer (a, b, c, d): ")

    if answer == correct_answer:
        print("Correct answer!")
        return True
    else:
        print("Wrong answer!")
        return False


def riddleme():
    """
    The main game function, that runs the riddleme game!
    """
    print("Welcome to the cave of mysteries, i have an amazing gift!")
    print("I can grant you an ability of your own choice, but to get it you will have to prove worthy!")
    print("You have to answer a few riddles that will test you.")
    name = ""
    ability = ""
    # This while loop make sure that you insert a name and ability that is legit to what i have told the program to do. need to add x to exit!
    while not name or not ability:
        if not name:
            print('First you need to tell me your name. It cannot be empty or only contain numbers! press "x" to exit')
            name = input("Enter your name: ")
            if not name:
                print("Name cannot be empty. Please try again.")
                continue
            if name.isdigit():
                print("Name cannot be purely numeric. Please try again.")
                name = ""
                continue

        if not ability:
            print('Then you also need to tell me which ability you want to learn. Cannot be empty or only contain numbers! press "x" to exit')
            ability = input("Enter your ability: ")
            if not ability:
                print("Ability cannot be empty. Please try again.")
                continue
            if ability.isdigit():
                print("Ability cannot be purely numeric. Please try again.")
                ability = ""
                continue
    print(f"Hi there {name} i see you wish to have the ability to {ability}.") 
    print("Great Choice!")
    print("But to be able to keep this ability you need to pass a few riddles, to be worthy!")

    # Where i store the riddles
    riddles = [
        {
            "riddle": "first What goes and goes but never gets where its ment to go?",
            "choices":["a. the clock", "b. restless person", "c. tomato", "d. life"],
            "correct_answer": "a"
        },
        {
            "riddle": "second What goes and goes but never gets where its ment to go?",
            "choices":["a. tomato", "b. the clock", "c. restless person", "d. life"],
            "correct_answer": "b"
        },
        {
            "riddle": "third What goes and goes but never gets where its ment to go?",
            "choices":["a. tomato", "b. restless person", "c. the clock", "d. life"],
            "correct_answer": "c"
        }
    ]

    for riddle in riddles:
        while True:
        # Asks the riddle and get the results through the give_riddle function, where the verification logic hides!
        # need to end the loop with a victory screen!!!
            result = give_riddle(riddle['riddle'],riddle['choices'],riddle['correct_answer'])
            if result is True:
                print("True")
                break
            elif result is False:
                # right now continues until i get the right answer, will have to give a choice of exit or try again that sends user back to the start!
                print("False")
                continue
            elif result is None:
                print('nothing! made for exit! break here else endlessssssssssloooooop')
                break

riddleme()
