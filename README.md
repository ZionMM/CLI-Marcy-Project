# Rock, Paper, Scissors CLI 

A command-line Rock, Paper, Scissors game where you play against the computer.
The game keeps score across rounds until you choose to quit, then shows your
final statistics.

## Features 
- Type your move in any case ("rock", "ROCK", and "Rock" all work)
- View your wins, losses, ties, and win rate
- Invalid menu choices and moves show a message instead of crashing

## How to Run

You need Python 3 installed. From the project folder, run:

```
python3 src/main.py
```

## Usage Example

```
Welcome to Rock, Paper, Scissors!

Menu:
1. Play Round
2. View Stats
3. Exit
Choose an option (Enter 1-3): 1
Choose a move (rock, paper, or scissors): rock

You chose: rock
Computer chose: scissors
Rock beats scissors! You win!

Menu:
1. Play Round
2. View Stats
3. Exit
Choose an Action (Enter 1-3): 2

Current Statistics:
Games Won: 1
Games Lost: 0
Games Tied: 0
Total Games: 1
Win Rate: 100%
```

## Project Structure

- `src/main.py`: starts the app
- `src/menu.py`: shows the menu and handles the player's choices
- `src/game_data.py`: stores the score and contains the game rules
- `src/test_game_data.py`: tests for the game rules