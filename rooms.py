rooms = {
    'Home': {'South': 'Boat', 'North': 'Bait Shop', 'West': 'Truck', 'East': 'Girl Friend'},
    'Truck': {'East': 'Home', 'Item': 'Fishing Pole'},
    'Wallet': {'West': 'Bait Shop', 'Item': 'Fishing License'},
    'Bait Shop': {'East': 'Wallet', 'South': 'Home', 'Item': 'Stink Bait'},
    'Boat': {'North': 'Home', 'East': 'Tackle Box', 'Item': 'Net'},
    'Tackle Box': {'West': 'Boat', 'Item': 'Bobber'},
    'Girl Friend': {'West': 'Home', 'North': 'Lake', 'Item': 'Permission'},
    'Lake': {'Item': 'Killer Catfish'}
}

current = 'Home'


def get_new_current(current, direction):
    new_current = current
    for i in rooms:
        if i == current:
            if direction in rooms[i]:
                new_current = rooms[i][direction]
    return new_current


def get_item(current):
    return rooms[current]['Item'] if 'Item' in rooms[current] else 'Home'



def show_instructions():
    print('James Goes Fishing')
    print('Collect all 6 items to win the game, or stay home and finish the Honey-Do list.')
    print('Move commands: South, North, East, West')
    print("Add to Inventory: get 'item_name'")


show_instructions()
inventory = []
items = ['Stink Bait', 'Fishing License', 'Fishing Pole', 'Net', 'Bobber', 'Permission']
while True:
    print('You are in ', current)
    print('Inventory:', inventory)
    item = get_item(current)
    print('You see a ', item)
    print('--------------------')
    if item == 'Killer Catfish':
        print('You caught the Killer Catfish! Game Over.')
        exit(0)
    direction = input('Enter direction of travel: ')
    if direction == 'go East' or direction == 'go West' or direction == 'go North' or direction == 'go South':
        direction = direction[3:]
        new_current = get_new_current(current, direction)
        if new_current == current:
            print('No door that way! Pick another direction.')
        else:
            current = new_current
    elif direction == str('get ' + item):
        if item in inventory:
            print('You already have this item. Try another room.')
        else:
            inventory.append(item)
    else:
        print('Invalid input or move or item')
    if len(inventory) == 6:
        print('Congratulations! You have collected all items and caught the Killer Catfish!')
        exit(0)
