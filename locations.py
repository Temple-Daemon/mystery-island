def show_island_locations():
    print("1. Beach🏖️")
    print("2. Light house🔦")
    print("3. Cave🦇")
    print("4. Old bridge🌉")
    print("5. Jungle🌳")
    user_location_choice = input("Explorer, chose your destination! ")
    if user_location_choice == "1":
        beach_adventure()
    elif user_location_choice == "2":
        lighthouse_adventure()
    elif user_location_choice == "3":
        cave_adventure()
    elif user_location_choice == "4":
        old_bridge_adventure()
    elif user_location_choice == "5":
        jungle_adventure()
    else:
        print("Invalid destination! Please choose between 1 and 5.")
def beach_adventure():
    print("Explorer, you are welcome to the beach! ")
    print("You have discovered an old map")  
def lighthouse_adventure():
    print("Explorer, you are welcome to the lighthouse! ")
    print("You discovered that the entrance is locked! ")
def cave_adventure():
    print("welcome to the wonders of the cave! ")
    print("You discovered a mysterious crystal hidden inside the cave! 💎")
def old_bridge_adventure():
    print("Welcome to the forgotten old bridge")
    print("The bridge is broken! you will need to find another way across")  
def jungle_adventure():
    print("Seems like you made it the jungle! ")
    print("You discovered a hidden pathway leading deeper into the island! 🌿 ")    
