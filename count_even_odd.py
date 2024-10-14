numbers = []
while True:
    input_number = input('Enter a positive number. (or press Enter  key to finish: ) ')
    if input_number:
        if input_number.startswith('-'):
            break
        else:
            numbers.append(int(input_number))
    else:
        break

even_count = 0
odd_count = 0
if not numbers:
    print('No positive number was entered.')
else:
    for number in numbers:
        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    print('You entered {} odd and {} even numbers.'.format(odd_count, even_count))
