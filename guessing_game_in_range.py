import random


def guessing_game():
    # Your Code Here
    print('Okay I have a number from 1 to 100.')
    number_of_guesses = 1
    random_number = random.randint(1, 100)
    guess = 0
    while True:
        try:
            while guess != random_number:
                guess = int(input("What's your guess? "))
                while guess < 1 or guess > 100:
                    print('Invalid guess! Please guess between 1 and 100')
                    guess = int(input("What's your guess? "))
                if guess > random_number:
                    print('lower')
                elif guess < random_number:
                    print('higher')
                else:
                    return number_of_guesses
                number_of_guesses += 1
        except Exception:
            print('Invalid guess! Please guess between 1 and 100')


# Test cases - do not edit.

# To run the test cases successfully you will need to type the numbers given in the print statement!

random.seed(10)
print("Try these numbers:  0  101  huge   100 1  50  75  66  71  73  74")
print("The first 3 should show invalid input.")
print("  At the end you should see Got it! It took you 8 tries! ")
x = guessing_game()
print(f"Got it! It took you {x} tries!")
if x > 8:
    print("Should have said 8 tries.")
else:
    print("Pass if you got 3 invalid inputs!")
