# Car Guessing Game

Welcome to the **Car Guessing Game**, a fun Python-based game where you have 12 chances to guess the name of a randomly chosen car. The car name will be hidden, and you have to guess it letter by letter.

## How to Play

- The game will randomly select a car name from a predefined list.
- You will have 12 chances to guess the correct car name.
- For each turn, guess a letter. If it is in the car's name, the letter will be revealed in its correct position.
- If your guess is incorrect, you will lose a turn.
- If you guess all the letters correctly, you win!
- If you use all your guesses, you lose and the correct car name will be revealed.

## Requirements

- Python 3.x installed on your machine.

## How to Run

1. Clone or download the repository.
2. Open the terminal or command prompt in the project folder.
3. Run the following command:

    ```bash
    python car_guessing_game.py
    ```

4. Enter your name and start guessing the car name.

## Example

Let's say the game chooses the car "toyota". Here's how the game could unfold:

```plaintext
Enter your name: Sanju
Hello Sanju, Welcome to the Car Guessing Game!
You have 12 chances to guess the car name.
The car name have 6 characters
_ _ _ _ _ _ 
Guess any alphabet: 
_
_
_
_
_
_

guess a character:j
Wrong
You have 11 more guesses
_
_
_
_
_
_

guess a character:t
t _
_
_
t _

guess a character:o
t o _
o t _

guess a character:y
t o y o t _

guess a character:a
t o y o t a
You Win
The word is:  toyota
