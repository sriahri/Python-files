import random
import sys

DAYS_PER_YEAR = 365

number_of_trials = 0
if len(sys.argv) > 1:
    number_of_trials = int(sys.argv[1])

number_of_samples = 1
birthdays = [False] * DAYS_PER_YEAR

for _ in range(number_of_trials):
    number = random.randrange(0, 365)
    if birthdays[number]:
        print(number_of_samples)
        break
    else:
        birthdays[number] = True
        number_of_samples += 1
