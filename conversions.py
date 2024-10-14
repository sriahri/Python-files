# Variable conversions defined
def MilesToKilometers(Miles):
    Kilometers = Miles * 1.6

    print(f"Miles:{format(Miles, '.2f')},Kilometers:{format(Kilometers, '.2f')}")


def FahrenheitToCelsius(Fahrenheit):
    Celsius = (Fahrenheit - 32) * 5 / 9

    print(f"Fahrenheit:{format(Fahrenheit, '.2f')}], Celsius:{format(Celsius, '.2f')}")


def GallonToLiters(Gallons):
    Liters = Gallons * 3.9

    print(f"gallons:{format(Gallons, '.2f')}], Liters: {format(Liters, '.2f')})")


def PoundsToKilograms(Pounds):
    Kilograms = Pounds * 3.45

    print(f"Pounds:{format(Pounds, '.2f')}], Kilograms:{format(Kilograms, '.2f')}")


def InchesToCentimeters(Inches):
    Centimeters = Inches * 2.54

    print(f"Inches:{format(Inches, '.2f')}], Centimeters: {format(Centimeters, '.2f')}")


# Creating a main function for conversions

def main():
    string = '''
    1. Convert Miles to Kilometers
    2. Convert Fahrenheit to Celsius
    3. Convert Gallons to Liters
    4. Convert Pounds to Kilograms
    5. Convert Inches to Centimeters'''

    metric_measurements = ('Miles', 'Fahrenheit', 'Gallons', 'Pounds', 'Inches')
    conversion_measurements = ('Kilometers', 'Celsius', 'Liters', 'Kilograms', 'Centimeters')
    print(string)
    choice = int(input('Please enter your chosen decision: '))
    count = 3
    flag = True
    while flag:
        input_value = float(input(
            "Please enter the amount {0} you would like to convert to {1} ".format(metric_measurements[choice - 1],
                                                                                   conversion_measurements[
                                                                                       choice - 1])))

        if choice == 2:
            if input_value >= 1000:
                count -= 1
                print('This is not a valid input you have', count, 'chances to enter a valid input')

            else:
                FahrenheitToCelsius(input_value)
                flag = False
        else:
            if input_value == 0:
                count -= 1
                print('This is not a valid input you have', count, 'chances to enter a valid input')
            else:
                if choice == 1:
                    MilesToKilometers(input_value)
                    flag = False
                if choice == 2:
                    FahrenheitToCelsius(input_value)
                    flag = False
                if choice == 3:
                    GallonToLiters(input_value)
                    flag = False
                if choice == 4:
                    PoundsToKilograms(input_value)
                    flag = False
                if choice == 5:
                    InchesToCentimeters(input_value)
                    flag = False
                if count == 0:
                    flag = False


main()
