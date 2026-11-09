# Shows menu and reacts to their choice.
from game_data import view_stats, play_round


def show_menu():
    # The loop keeps repeating while 'is_running' is True
    is_running = True
    while is_running:
        print("\nMenu:")
        print("1. Play Round")
        print("2. View Stats")
        print("3. Exit")

        choice = input("Choose an option (Enter 1-3): ").strip()

        if choice == "1":
            play_round()
        elif choice == "2":
            view_stats()
        elif choice == "3":
            # Show final stats and ends loop.
            view_stats()
            is_running = False
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
