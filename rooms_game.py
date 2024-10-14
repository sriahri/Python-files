name = input("What is your name: ")
print("\nInstructions >>")
print("  * In this game you have to collect all the six items to win the game.")
print("  * If you face Evil Spirit before collecting all these six items game is over.")
print("\nLet's start " + name + "!\n\n")

# A dictionary for a simplified moving between rooms game
# The dictionary links a room to other rooms.
rooms = {'Mud Room': [None, ['North', 'East', 'South', 'West']],
         'Study': ['Book on shotgun shells', ['South', 'East']],
         'Basement': ['Flashlight', ['West']],
         'Kitchen': ['Salt Container', ['East']],
         'Living Room': ['Shotgun', ['North', 'East']],
         'Storage Room': ['Shotgun Shells', ['West']],
         'Bedroom': ['Beef Jerky', ['North', 'West']]
         }

inventory = []
current_room = 'Mud Room'

while True:  # loop

    # function
    if current_room == "Vampire's Room":  # if
        print("Game over!!!, Vampire killed Vampire Hunter :(")
        break

    print("Vampire Hunter currently in", current_room)
    current_item = rooms[current_room][0]
    print("The current room has", current_item)

    if current_item is not None:  # if
        opinion = input("Do you want to pick " + current_item + "? (Y/N): ").upper()
        if opinion in ['Y', 'YES']:  # if
            inventory.append(current_item)
            rooms[current_room][0] = None

    print("Collected items:", inventory)

    if len(inventory) == 6:  # if
        print("\nCongrats!!!, Collected all items, won the game :)")
        break

    direction = input("What direction you want to move? (East,West,North,South): ").title()  # asking user

    while direction not in rooms[current_room][1]:  # loop
        print("Invalid direction from " + current_room + ". Try again")
        direction = input("What direction you want to move? (East,West,North,South): ").title()

    next_room = current_room
    if current_room == 'Great Hall':  # if
        if direction == 'East':  # if
            next_room = 'Cellar'
        elif direction == 'West':  # if
            next_room = 'Bedroom'
        elif direction == 'North':  # if
            next_room = 'Livingroom'
        else:
            next_room = 'Kitchen'

    elif current_room == 'Livingroom':  # if
        if direction == 'East':  # if
            next_room = 'Attic'
        else:
            next_room = 'Great Hall'

    elif current_room == 'Attic':  # if
        next_room = 'Livingroom'

    elif current_room == 'Bedroom':  # if
        next_room = 'Great Hall'

    elif current_room == 'Kitchen':  # if
        if direction == 'East':  # if
            next_room = 'Basement'
        else:
            next_room = 'Great Hall'

    elif current_room == 'Basement':  # if
        next_room = 'Kitchen'

    elif current_room == 'Cellar':  # if
        if direction == 'North':  # if
            next_room = "Vampire's Room"
        else:
            next_room = 'Great Hall'

    current_room = next_room
    print("Vampire Hunter moved to", current_room, "\n")  # print

print("\nThanks for playing this game.")  # print
