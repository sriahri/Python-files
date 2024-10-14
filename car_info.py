def print_info(year, price):
    print("Car's information:")
    print("  Model year:", year)
    print("  Purchase price: $", price, sep="")


if __name__ == '__main__':
    year = int(input())
    price = int(input())
    print_info(year, price)
