if __name__ == '__main__':
    name = input('Please enter your first name: ')
    try:
        first_number = input(f'Hi {name} please enter the first number: ')
        second_number = input('please enter the first number: ')
        third_number = input('please enter the third number: ')

        first_number = int(first_number)
        second_number = int(second_number)
        third_number = int(third_number)

        if first_number == second_number == third_number:
            print('All the numbers are same')
        elif first_number == second_number or first_number == third_number or second_number == third_number:
            print('Two of the numbers are same')
        else:
            print('All the numbers are different')

    except Exception:
        print('One or more of the numbers are invalid.')
