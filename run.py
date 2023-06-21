def riddleme():
    """
    The main game function, that runs the riddleme game!
    """
    print("Welcome to the riddle game!\n First you need to tell me your name.\n Then after you have to tell me which ability you wish to learn. \n")
    name = input("Enter your name: ")
    ability = input("Enter your ability: ")
    print(f"Hi there {name} i see you wish to have the ability to {ability}.")


riddleme()
