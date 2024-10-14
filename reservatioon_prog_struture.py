import string
import random

print("BOOKING SERVICES")
chars = string.ascii_letters
choice = input("\nWould you like to book the entire restaurant? yes/no: ")
if choice.lower() == "yes":
    date = input("Enter the date of reservation: ")
    code = ''.join(random.choice(chars) for _ in range(14))
    code = code.upper()
    code = ' '.join(reversed(code))
    code = code.replace(" ", "")
    print("\nReservation Code: ", code)

elif choice.lower() == "no":
    date = input("Enter the date of reservation: ")
    guest = input("Enter the number of people: ")
    code = ''.join(random.choice(chars) for _ in range(14))
    code = code.upper()
    code = ''.join(reversed(code))
    code = code.replace(" ", "")
    print("\nReservation Code: ", code)
