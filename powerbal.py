from random import randint
# The function returns the number of vowels in the given name.
def countVowels(name):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for i in name:
        if i in vowels:
            count += 1
    return count
# The function returns the range for the main numbers to be generated in the range 1-69.
def find_range_from_name(name):
    if countVowels(name) % 2 == 0:
        return [1, 34]
    else:
        return [35, 69]
# The function returns the range for the powerball number to be generated in the range 1-26.
def find_range_from_month(month):
    if month <= 6:
        return [1, 13]
    else:
        return [14, 26]
# The function returns the range for the powerball number to be generated in the range 1-26.
def find_range_from_year(year, month):
    start, end = find_range_from_month(month)
    if year < 2000:
        return [start, end//2]
    else:
        return [start, end]
        

name = input("Enter your name: ")
month_of_birth = int(input("Enter the month of your birth: "))
year_of_birth = int(input("Enter the year of birth: "))
limit = find_range_from_name(name)
start, end = limit[0], limit[1]
# Generate random number in the range
number1 = randint(start, end)
number2 = randint(start, end)
number3 = randint(start, end)
number4 = randint(start, end)
number5 = randint(start, end)
limit = find_range_from_year(year_of_birth, month_of_birth)
start, end = limit[0], limit[1]
powerball_number = randint(start, end)
print("The main numbers are {}, {}, {}, {}, {}".format(number1, number2, number3, number4, number5))
print("The powerball number is {}".format(powerball_number))