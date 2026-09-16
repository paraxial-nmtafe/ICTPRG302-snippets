"""
This is a small sample game to demonstrate a dungeon crawler in basic Python.
"""

possible_rooms = {
    "hall": {
        "description":"A drafty old hall",
        "loot": 0
    },
    "library": {
        "description": "A room packed with ancient books",
        "loot": 60
    },
    "dining": {
        "description": "A banquet hall set for 1",
        "loot": 10
    },
    "mushroom_garden": {
        "description": "A strange room filled with mushrooms growing out of the walls",
        "loot": 3
    }
}
current_room = "hall"
current_coins = 0

def show_instructions():
    print()
    print("look: See what you can see")
    print("rooms: List the rooms of the dungeon")
    print("move: Go to a different room")
    print("take: Take any treasure we find")

def show_room(room):
    print(f"You are in the {room}")
    print(possible_rooms.get(room)["description"])

def present_rooms_nicely():
    output = ""
    for room in possible_rooms.keys():
        if room == current_room:
            continue
        output += f"{room},"

    return output

def handle_movement():
    selection = ""
    while selection not in possible_rooms.keys():
        print(f"The rooms are: {present_rooms_nicely()}")
        selection = input("Where do you want to go? ")
    return selection

def take_loot():
    loot = possible_rooms.get(current_room)["loot"]
    possible_rooms[current_room]["loot"] = 0

    return loot

print("Welcome to the dungeon. Type help if you're stuck.")
while True:
    print("What do you do? (help)")
    user_input = input("> ").strip().lower()

    if user_input not in ['look', 'move', 'rooms', 'take', 'quit', 'help']:
        print("Command not recognised")
        continue

    if user_input == 'look':
        show_room(current_room)
    elif user_input == "help":
        show_instructions()
    elif user_input == 'rooms':
        print(present_rooms_nicely())
    elif user_input == 'move':
        current_room = handle_movement()
    elif user_input == 'take':
        current_coins += take_loot()
        print(f"You now have {current_coins} coins")
    elif user_input == 'quit':
        break

    print("==================================")


print(f"You finished the game, congrats 🎉.  You had {current_coins} coins.")
