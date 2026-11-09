# Holds the game's data and rules.
import random

# Constants: never change.
MOVES = ["rock", "paper", "scissors"]
BEATS = {"rock": "scissors", "scissors": "paper", "paper": "rock"}


game_stats = {
    "wins": 0,
    "losses": 0,
    "ties": 0,
}


def view_stats():
    # Prints the score. Total and win rate are calculated.
    wins = game_stats["wins"]
    losses = game_stats["losses"]
    ties = game_stats["ties"]
    total = wins + losses + ties

    # Avoids dividing by zero when no games are played.
    if total == 0:
        win_rate = 0
    else:
        win_rate = round(wins / total * 100)

    print("\nCurrent Statistics:")
    print(f"Games Won: {game_stats['wins']}")
    print(f"Games Lost: {game_stats['losses']}")
    print(f"Games Tied: {game_stats['ties']}")
    print(f"Total Games: {total}")
    print(f"Win Rate: {win_rate}%")


def get_computer_move():
    # Computer picks random move from MOVES
    return random.choice(MOVES)


def determine_winner(player, computer):
    # Compare two moves and return "tie", "win", or "loss"
    if player == computer:
        return "tie"
    if BEATS[player] == computer:
        return "win"
    return "loss"


def play_round():
    player = input("Choose a move (rock, paper or scissors): ").strip().lower()

    if player not in MOVES:
        print("Invalid move. Please type rock, paper, or scissors")
        return

    computer = get_computer_move()
    result = determine_winner(player, computer)

    print(f"\nYou chose: {player}")
    print(f"Computer chose: {computer}")

    # Update the stats and show who won.
    if result == "win":
        game_stats["wins"] += 1
        print(f"{player.capitalize()} beats {computer}! You win!")
    elif result == "loss":
        game_stats["losses"] += 1
        print(f"{computer.capitalize()} beats {player}! You lose!")
    else:
        game_stats["ties"] += 1
        print("It's a tie!")
