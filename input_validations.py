def check_names(name):
    names = name.split()
    if len(names) != 2:
        print('Please enter valid first and last name by a space.')
        return False
    return True


def check_hours(hours):
    try:
        hours = float(hours)
        if 0 < hours <= 80:
            return True
        else:
            print('This value must be greater than 0 and less than 80')
    except Exception:
        print('This value must be a number')
    return False


def check_hourly_pay_rate(hourly_pay_rate):
    try:
        hourly_pay_rate = float(hourly_pay_rate)
        if hourly_pay_rate > 0:
            return True
        else:
            print('This value must be greater than 0')
    except Exception:
        print('This value must be a number')
    return False


def check_federal_tax(federal_tax):
    federal_tax = federal_tax.lower()
    if federal_tax == 's' or federal_tax == 'm':
        return True

    return False


def check_state_tax(state_tax):
    try:
        state_tax = float(state_tax)
        if 0 < state_tax < 100:
            return True
        else:
            print('This value must be greater than 0')
    except Exception:
        print('This value must be a number')
    return False


if __name__ == '__main__':
    names = input("What is employee's first and last name: ")
    while not check_names(names):
        names = input("What is employee's first and last name: ")
    first_name, last_name = names.split()
    first_name = first_name.title()
    last_name = last_name.title()

    inf = 'How many hours did {} {} work this week? '.format(first_name, last_name)
    hours = input(inf)
    while not check_hours(hours):
        inf = 'How many hours did {} {} work this week? '.format(first_name, last_name)
        hours = input(inf)

    hours = float(hours)
    hourly_rate = input('What is hourly pay rate? ')
    while not check_hourly_pay_rate(hourly_rate):
        hourly_rate = input('What is hourly pay rate? ')

    hourly_rate = float(hourly_rate)

    federal_tax = input('Enter federal tax (S for single M for married) ')
    while not check_federal_tax(federal_tax):
        federal_tax = input('Enter federal tax (S for single M for married) ')

    state_tax = input('Enter state tax: ')
    while not check_state_tax(state_tax):
        state_tax = input('Enter state tax: ')
    state_tax = float(state_tax)
    if state_tax > 1:
        state_tax = state_tax / 100

    print('Name is {} {}'.format(first_name, last_name))
    print('Hours is {}'.format(hours))
    print('Hourly pay rate: {}'.format(hourly_rate))
    print('Federal tax is {}'.format(federal_tax))
    print('State tax is {}'.format(state_tax))
