def read_automobiles_number():
    while True:
        try:
            n = int(input("Enter the number of automobiles: "))
            if n <= 0:
                raise Exception
            else:
                return n
        except Exception:
            print("You must enter an integer > 0:")


def read_VIN():
    while True:
        try:
            VIN = input("Please enter the automobile VIN: ")
            if len(VIN) != 17:
                raise Exception
            else:
                return VIN
        except Exception:
            print("You must enter a VIN that has 17 characters:")


def read_model():
    model = input("Please enter the Model: ")
    return model


def print_list(l):
    print("Auto VINs\t\tModel")
    for i in range(len(l)):
        print(l[i][0], l[i][1])


def write_file(file, l):
    for i in range(len(l)):
        file.write(l[i][0] + '\t' + l[i][1] + '\n')


def main():
    automobiles = []
    try:
        number = read_automobiles_number()
        for i in range(number):
            automobiles.append([read_VIN(), read_model()])

        print(automobiles)
        print_list(automobiles)
        file = open("autos_file.txt", 'w')
        write_file(file, automobiles)
        file.close()
    except Exception:
        pass


if __name__ == '__main__':
    main()
