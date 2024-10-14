def celsius_to_fahrenheit(temp):
    return temp * (9 / 5) + 32


def fahrenheit_to_celsius(temp):
    return (temp - 32) * (5 / 9)


def print_celsius_to_fahrenheit_conversion_table(min, max):
    print("Celsius Fahrenheit")
    print("------------------")
    for x in range(min, max + 1):
        print('{}\t\t{}'.format(x, round(celsius_to_fahrenheit(x))))


def print_fahrenheit_to_celsius_conversion_table(min, max):
    print("Fahrenheit Celsius")
    print("-----------------------")
    for x in range(min, max + 1):
        print('{}\t\t\t{}'.format(x, round(fahrenheit_to_celsius(x))))


min_celsius = int(input('Minimum Celsius Temperature: '))
max_celsius = int(input('Maximum Celsius Temperature: '))
print()
print_celsius_to_fahrenheit_conversion_table(min_celsius, max_celsius)
print()
min_fahrenheit = int(input("Minimum Fahrenheit temperature: "))
max_fahrenheit = int(input("Maximum Fahrenheit temperature: "))
print()
print_fahrenheit_to_celsius_conversion_table(min_fahrenheit, max_fahrenheit)
