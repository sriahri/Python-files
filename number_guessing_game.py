import random
import math

smaller_number = int(input("Enter the smaller number: "))
larger_number = int(input("Enter the larger number: "))
count = 1
computer_number = random.randint(smaller_number, larger_number)
while True:
    print("{} {}".format(smaller_number, larger_number))
    computer_number = (smaller_number + larger_number)//2
    print('Your number is {}\n'.format(computer_number))
    choice = input("Enter =, <, or >: ")
    if choice == '=':
        print("Hooray, I've got it in {} tries".format(count))
        break
    if smaller_number == larger_number:
        print('I am out of guesses, and you cheated')
        break
    if choice == '<':
        larger_number = computer_number - 1
    elif choice == '>':
        smaller_number = computer_number + 1

    count += 1

