# Riddle Me!
This is a small game/quiz that allows you to gain an ability in a magical cave. However, in order to obtain the ability, you must correctly answer a series of riddles.

## How To Play?
- Firstly, you will be prompted to enter your name.
- Secondly, you will be asked to enter the ability you wish to acquire.
- Third, you will be presented with a riddle along with four answer choices: A, B, C, and D. You can also choose to exit the game by entering "X."
- Keep in mind that you have only one attempt to answer each riddle. If you fail to answer correctly, the game will exit. Remember, this gift is not easily obtained!
- To gain the ability, you need to answer five riddles correctly.

Flowchart! \
![Flowchart](assets/readme/flowchart.png)

Overall inspiration and ideas from:
 - https://realpython.com/python-quiz-application/
 - https://medium.com/@rahulmallah785671/creating-an-engaging-quiz-game-with-python-a-step-by-step-guide-ea11bd76f159
 - https://www.geeksforgeeks.org/print-colors-python-terminal/
 - https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/
 - https://www.geeksforgeeks.org/clear-screen-python/
 - https://play.howstuffworks.com/quiz/test-your-mental-mettle-with-these-ridiculous-riddles

 Buggs
  - when i insert a capitalized letter it goes false!
    - Solution: add .lower() to make sure the input is lowercased
  - Its possible to bypass my checks by inserting blankspaces...
    - Add .strip() behind the input to remove the blankspaces and it will be empty
  - Answering question with the right answer but followed by a blankstep = error...
    - solved with .strip()

