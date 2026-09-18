def print_help_text():
    print("You can use the following commands:")
    print("look: to look at the room")
    print("go: to go to another room")
    print("take: to take treasure")
    print("help: to see this help text again")
    print("quit: to quit")


def print_description(location, possible_rooms):
    print(f"You are in the {location}, {possible_rooms[location]["description"]}")


def handle_navigation(location, possible_rooms):
    print(f"There are the following rooms: {possible_rooms.keys()}")
    new_room = ""
    while new_room not in possible_rooms.keys():
        new_room = input("Where do you want to go? ")
        if new_room in ['no', 'oops', 'quit']:
            return location

    return new_room

def take_loot(location, possible_rooms, inventory):
    if possible_rooms[location]['loot'] is not None:
        inventory.append(possible_rooms[location]['loot'])
        possible_rooms[location]['loot'] = None
    return inventory

def main(): 
    running = True
    print_help_text()

    possible_rooms = {
        'hall': {
            "description": "a gloomy stone room",
            "loot": None,
        }, 
        'torture_chamber': {
            "description":"a terrible blood-stained room, many horrors have occurred here",
            "loot": "bones"
        }, 
        'vault': {
            "description":"full of diamonds and gold",
            "loot": "diamonds"
        }, 
        'cave': {
            "description": "a horrible figure that coughs saying 'gollum, gollum' lives here",
            "loot": "one ring and also a lost vegetable"
        },
        'arena': {
            "description": "a literal ongoing fight is occurring, walk carefully",
            "loot": "human teeth"
        }
    }
    current_location = 'hall'
    inventory = []

    while running:
        print("What do you want do do?")
        raw_input = input("> ").strip().lower()

        if raw_input == "quit":
            print("Bye~")
            print(f"You looted {inventory}")
            running = False
        elif raw_input == "help":
            print_help_text()
        elif raw_input == "look":
            print_description(current_location, possible_rooms)
        elif raw_input == "go":
            current_location = handle_navigation(current_location, possible_rooms)
        elif raw_input == "take":
            inventory = take_loot(current_location, possible_rooms, inventory)
            print(f"Your current inventory is {inventory}")
        else:
            print("Please enter a valid command.")



main()