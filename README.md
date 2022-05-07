# Week 03: Dice

---

## Getting Started

---

Make sure you have Python 3.8.10 or newer installed and running on your machine. Open terminal or PowerShell and
browse to the project's root folder. Start the program by running the following command.

```
python3 Hilo
```

You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the
project folder. Select the main module inside the Hilo folder and click the "run" button.

There are some rules to this game and are listed as follows:

- The player will start with 300 points.
- Individual cards are represented as a number from 1 to 13.
- The current card is displayed.
- The player guesses if the next one will be higher or lower.
- The next card is displayed.
- The player earns 100 points if they guessed correctly.
- The player loses 75 points if they guessed incorrectly.
- If a player reaches 0 points the game is over.
- If a player has more than 0 points they decide if they want to keep playing.
- If a player decides not to play again the game is over.

The goal of the game is to score as many points as possible without reducing your points to 0. You can type n or no to stop playing the game. If you wish to continue playing, you'll type y or yes when prompted.

Your score will be displayed after each next card. Good luck and have fun!

## Project Structure

---

The project files and folders are organized as follows

```
root                    (project root folder)
+-- hilo                (source code for game)
  +-- game              (specific classes)
    +-- card.py         (Card class)
    +-- deck.py         (Deck class)
    +-- director.py     (Director class)
  +-- __main__.py       (program entry point)
+-- README.md           (general info)
```

## Authors

---

CSE210 Spring 2022 session
Section 07, Group G

- Austin Donovan
- Dylan Ruppell
- Ellen Reyes-Sotelo
- Matt Pellet
- Nathan Roper
