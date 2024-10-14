def canParkCar(carLen, streetLen, carsLocation, carsLength):
    # Place all '-' in empty places
    space = ['-' for i in range(streetLen)]
    for i in range(len(carsLocation)):
        loc = carsLocation[i]
        space_occupied = carsLength[i]
        # If a place is occupied, replace '-' with 'x'
        for j in range(space_occupied):
            space[loc + j] = 'x'

    # Check whether there is empty space sufficient for the car or not.
    x = ''.join(space)
    res = '-' * carLen
    return True if res in x else False


if __name__ == '__main__':
    carLen = 2
    streetLen = 10
    carLocations = [1, 4, 8]
    carLengths = [1, 2, 2]
    print(canParkCar(carLen, streetLen, carLocations, carLengths))

    carLen = 3
    streetLen = 11
    carLocations = [1, 5, 8]
    carLengths = [2, 3, 3]
    print(canParkCar(carLen, streetLen, carLocations, carLengths))
