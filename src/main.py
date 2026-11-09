# This file starts the whole app.
from menu import show_menu


def start_app():  # Greets the player, runs the menu, and says goodbye when it ends.
    print("Welcome to Rock, Paper, Scissors!")
    show_menu()
    print("\nThanks for playing! Goodbye!")


# Only start the app if this file is ran directly, not if imported.
if __name__ == "__main__":
    start_app()
