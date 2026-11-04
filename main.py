from game import new_game, available_actions, apply_action, is_win, is_game_over

def start_game():
    print("🏝️ MYSTERY ISLAND: THE LOST LIGHTHOUSE 🔦")
    print("You woke up on Mystery Island after a terrible storm.")
    print("The lighthouse is dark, and a rescue boat is waiting somewhere beyond the island.")
    print("Your mission is to restore the lighthouse beacon before you run out of energy.")
    print("Explore the island, collect useful objects and solve the challenges.")
    print("You have 5 energy points. Every legal move consumes 1 energy point.")
    print()

def play_game():
    player_name = input("Explorer, what is your name? ").strip()

    if player_name == "":
        player_name = "Explorer"

    player = new_game(player_name)

    print()
    print("Welcome to Mystery Island, " + player["name"] + "!")
    print("Your adventure begins at the Beach.")
    print()

    while not is_game_over(player):
        print("-----------------------------------")
        print("📍 Current location:", player["location"])
        print("⚡ Energy:", player["energy"])
        print("🎒 Inventory:", player["inventory"])
        print("-----------------------------------")

        print("What would you like to do?")

        actions = available_actions(player)

        for action in actions:
            print("- " + action)

        user_action = input("\nEnter your action: ")

        result = apply_action(player, user_action)

        print()
        print(result)
        print()

    if is_win(player):
        print("🏆 CONGRATULATIONS, " + player["name"] + "!")
        print("You successfully escaped Mystery Island!")
    elif player["energy"] == 0:
        print("💀 You lost! You ran out of energy before completing your mission.")
    print()

def main():
    start_game()

    while True:
        play_game()

        replay = input("Would you like to play again? (yes/no): ").strip().lower()

        if replay != "yes":
            print("Thank you for playing Mystery Island! Goodbye! 🏝️")
            break

        print()
        print("Starting a new adventure...")
        print()

if __name__ == "__main__":
    main()