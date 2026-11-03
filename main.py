def start_game():
    print("🏝️ MYSTERY ISLAND: THE LOST LIGHTHOUSE 🔦")
    print("your adventure begins! ")
def show_island_locations():
    print("1. Beach🏖️")
    print("2. Light house🔦")
    print("3. Cave🦇")
    print("4. Old bridge🌉")
    print("5. Jungle🌳")
def beach_adventure():
    print("You have discovered an old map")    
    user_location_choice = input("Explorer, chose your destination! ")
    if user_location_choice == "1":
        print("Welcome to the beach! ")
    elif user_location_choice == "2":
        print("Welcome to the light house! ")
    elif user_location_choice == "3":
        print("Welcome to the cave!")
    elif user_location_choice == "4":
        print("Welcome to the Old bridge! ")
    else:
        print("Welcome to the jungle")                
user_choice = input("Do you want to PLAY or EXIT ? ")
if user_choice == "play":
    start_game()
    show_island_locations()
else:
    print("Good bye, explore! ")

