
# Number Guessing Game

This Python app implements a fun and interactive number guessing game where the player tries to guess a randomly generated number between 1 and 100. The program includes difficulty levels, feedback, and a replay option.

# Features:

- Random Number Generation: A number is randomly chosen between 1 and 100.
- Difficulty Levels:
  - Easy: 10 attempts to guess the correct number.
  - Hard: 5 attempts to guess the correct number.
- Interactive Gameplay: Players receive feedback ("Too high!" or "Too low!") after each guess.
- Replay Option: Play as many times as you like.

# How to Use:

1- Run the script using the command:

```bash
python main.py
```

2- The program will display a welcome message and a menu to select difficulty.

3- Choose a difficulty:

- Type `easy` for 10 attempts.
- Type `hard` for 5 attempts.

4- Start guessing:

- Input a number between 1 and 100.
- The program provides feedback to guide your guesses.

5- End the game:

- Win by guessing the correct number within the given attempts.
- If you lose, the program will reveal the correct number.

6- Replay or exit:

- Choose to restart the game or exit based on the prompt.

# Example Output:

```
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Choose a difficulty. Type 'easy' or 'hard': easy
You have 10 attempts remaining to guess the number.
Make a guess: 50
Too high!
You have 9 attempts remaining to guess the number.
Make a guess: 25
Too low!
...
```

# ASCII Art:

- The logo displayed in the terminal when starting the game:

```
  .oooooo.                                                 ooooooooooooo oooo                       
 d8P'  `Y8b                                                8'   888   `8 `888                       
888           oooo  oooo   .ooooo.   .oooo.o  .oooo.o           888       888 .oo.    .ooooo.        
...
```

# Future Enhancements:

- Add more difficulty levels.
- Implement a leaderboard for tracking player scores.
- Provide hints for closer guesses.



