def get_data(filename, car_type):
    file = open(filename)
    lines = file.readlines()
    car_prices = []
    for line in lines:
        type_of_car = line[0].lower()
        price = float(line.split()[1].strip())
        if type_of_car == car_type.lower()[0]:
            car_prices.append(price)
    return car_prices


def count_range(sale_prices, minimum, maximum):
    count = 0
    for price in sale_prices:
        if minimum <= price <= maximum:
            count += 1
    return count


def main():
    print('Welcome to the Automobile Sales Analyzer!')
    filename = input('Enter the name of the data file: ')
    used_cars = get_data(filename, 'u')
    new_cars = get_data(filename, 'n')
    used_cars_less_than_12k = count_range(used_cars, 0, 12000)
    used_cars_less_than_25k = count_range(used_cars, 12000, 25000)
    used_cars_greater_than_25k = count_range(used_cars, 25000, 500000)
    new_cars_less_than_35k = count_range(new_cars, 0, 35000)
    new_cars_less_than_50k = count_range(new_cars, 35000, 50000)
    new_cars_greater_than_50k = count_range(new_cars, 50000, 500000)

    print('New Automobiles')
    print('Total number sold:', new_cars_less_than_35k + new_cars_less_than_50k + new_cars_greater_than_50k)
    print('  Under 35K:', new_cars_less_than_35k)
    print('  35K to 50K:', new_cars_less_than_50k)
    print('  Over 50K:', new_cars_greater_than_50k)
    print('Total sales:', sum(new_cars))
    print('  Average:', sum(new_cars)/len(new_cars))
    print('Used Automobiles')
    print('Total number sold:', used_cars_less_than_12k + used_cars_greater_than_25k + used_cars_less_than_25k)
    print('  Under 12K:', used_cars_less_than_12k)
    print('  12K - 25K:', used_cars_less_than_25k)
    print('  Over 25K:', used_cars_greater_than_25k)
    print('Total sales:', sum(used_cars))
    print('  Average:', sum(used_cars)/len(used_cars))
    print('Thanks for using the Automobile Sales Analyzer!')


if __name__ == '__main__':
    main()
