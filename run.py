"""
This is a riddle game that will take you through a test,
to be able to gain a special ability of your own choice!
"""
def riddleme():
    """
    The main game function, that runs the riddleme game!
    """
    print("Welcome to the riddle game!")
    name = ""
    ability = ""

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
    return print(f"Hi there {name} i see you wish to have the ability to {ability}."), print("Great Choice!"), print("But to be able to keep this ability you need to pass a few riddles, to be worthy!")


riddleme()
