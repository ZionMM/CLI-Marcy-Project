from game_data import game_stats

print(game_stats)


def show_menu():
    is_running = True
    while is_running:
        print("\nMenu:")
        print("1. [First Option]")
        print("2. [Second Option]")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            print("You chose option 1")
        elif choice == "2":
            print("You chose option 2")
        elif choice == "3":
            is_running = False
        else:
            print("Invalid choice. Please try again.")
