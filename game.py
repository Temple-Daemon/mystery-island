def new_game(name):
    player = {
        "name": name,
        "location": "Beach",
        "energy": 5,
        "inventory": [],
        "game_over": False,
        "won": False
    }
    return player

def available_actions(player):
    location = player["location"]
    actions = ["inventory", "quit"]

    if location == "Beach":
        actions.append("examine map")
        actions.append("go jungle")
    elif location == "Jungle":
        actions.append("go beach")
        actions.append("go cave")
        actions.append("take rope")
    elif location == "Cave":
        actions.append("go jungle")
        actions.append("go old bridge")
        actions.append("take lantern")
    elif location == "Old Bridge":
        actions.append("go cave")
        actions.append("go lighthouse")
    elif location == "Lighthouse":
        actions.append("go old bridge")
        actions.append("light beacon")

    return actions

def apply_action(player, action):
    action = action.strip().lower()

    if player["game_over"]:
        return "The game has already ended."

    if action == "quit":
        player["game_over"] = True
        return "You have chosen to leave the island. Goodbye!"

    if action == "inventory":
        if len(player["inventory"]) == 0:
            return "Your inventory is empty."
        return "Your inventory: " + ", ".join(player["inventory"])

    if action == "examine map":
        if player["location"] == "Beach":
            return "The old map shows a route through the Jungle, Cave and Old Bridge to the Lighthouse."
        return "There is no map here to examine."

    if action == "take rope":
        if player["location"] != "Jungle":
            return "There is no rope here."
        if "rope" in player["inventory"]:
            return "You have already collected the rope."
        player["inventory"].append("rope")
        return "You collected the rope! You may need it to cross the bridge."

    if action == "take lantern":
        if player["location"] != "Cave":
            return "There is no lantern here."
        if "lantern" in player["inventory"]:
            return "You have already collected the lantern."
        player["inventory"].append("lantern")
        return "You collected the lantern! You will need it to light the lighthouse."

    if action == "light beacon":
        if player["location"] != "Lighthouse":
            return "You must reach the Lighthouse first."
        if "lantern" not in player["inventory"]:
            return "You cannot light the beacon without a lantern."
        player["won"] = True
        player["game_over"] = True
        return "You restored the lighthouse beacon! The rescue boat has spotted the light. YOU ESCAPED THE ISLAND!"

    if action.startswith("go "):
        destination = action[3:].title()
        current_location = player["location"]

        routes = {
            "Beach": ["Jungle"],
            "Jungle": ["Beach", "Cave"],
            "Cave": ["Jungle", "Old Bridge"],
            "Old Bridge": ["Cave", "Lighthouse"],
            "Lighthouse": ["Old Bridge"]
        }

        if destination not in routes[current_location]:
            return "You cannot travel there from your current location."

        if current_location == "Old Bridge" and destination == "Lighthouse":
            if "rope" not in player["inventory"]:
                return "The bridge is unsafe! You need a rope before crossing."

        player["location"] = destination
        player["energy"] -= 1

        if player["energy"] == 0:
            player["game_over"] = True
            return "You reached " + destination + ", but you have run out of energy. GAME OVER!"

        return "You travelled to " + destination + "."

    return "Invalid action! Please choose one of the available actions."

def is_win(player):
    return player["won"]

def is_game_over(player):
    return player["game_over"]