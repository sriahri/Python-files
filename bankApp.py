low_readings = []
high_readings = []


def add(low_reading, high_reading):
    low_readings.append(low_reading)
    high_readings.append(high_reading)


def delete(id):
    if id > 0:
        low_readings.pop(id - 1)
        high_readings.pop(id - 1)
    else:
        print('Could not delete')


def print_readings():
    print('ID\tLow Reading\t\tHigh Reading')
    for i in range(len(low_readings)):
        print(i + 1, low_readings[i], high_readings[i], sep="\t\t")

    print('n = {} Mean low = {} Mean high = {}'.format(len(low_readings),
                                                       sum(low_readings) / len(low_readings),
                                                       sum(high_readings) / len(high_readings)))


if __name__ == '__main__':
    while True:
        print('''MENU
        a - add an experimental reading
        d - delete an experimental reading
        p - print the experimental readings
        q - quit the program''')

        choice = input("Enter the command from the menu: ")
        while choice not in ['a', 'd', 'p', 'q']:
            continue

        if choice == 'a':
            low = float(input("Enter the low temperature: "))
            high = float(input("Enter the high temperature: "))
            add(low, high)

        elif choice == 'd':
            id = int(input('Which reading number do you wish to delete?: '))
            delete(id)

        elif choice == 'p':
            print_readings()

        elif choice == 'q':
            import sys

            sys.exit(0)
