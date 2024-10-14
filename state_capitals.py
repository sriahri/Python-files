states_and_capitals = {}

def find(state):
    if state in states_and_capitals:
        return states_and_capitals[state]
    return "No state with {} name is found".format(state)


def add(state, capital):
    global states_and_capitals
    states_and_capitals[state] = capital
    print('Added successfully')

def remove(state):
    if state in states_and_capitals:
        states_and_capitals.pop(state)
        print("Removed successfully")

    else:
        print("Key {} not found".format(state))


def modify(state, capital):
    if state in states_and_capitals:
        states_and_capitals[state] = capital
    else:
        print('{} not found'.format(state))


def print_all():
    for state, capital in states_and_capitals.items():
        print("{}: {}".format(state, capital))

def main():
    print('1. Find\n2.Add\n3.Remove\n4.Modify\n5.Print\n6.End')
    choice = int(input('Enter your choice: '))
    if choice == 1:
        state = input('Enter the state name to find: ')
        print(find(state))
    elif choice == 2:
        state = input('Enter the state to add: ')
        capital = input('Enter the corresponding capital: ')
        add(state, capital)
    elif choice == 3:
        state = input('Enter the state name to remove: ')
        remove(state)
    elif choice == 4:
        state = input('Enter the state to modify: ')
        capital = input('Enter the corresponding capital: ')
        modify(state, capital)
    elif choice == 5:
        print_all()
    elif choice == 6:
        import sys
        sys.exit(0)

if __name__ == '__main__':
    while True:
        main()