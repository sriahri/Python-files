def calculate_perimeter(width, height):
    return 2 * (height + width)


if __name__ == '__main__':
    while True:
        width = float(input('Enter the width: '))
        height = float(input('Enter the height: '))
        if width == 0 and height == 0:
            break
        else:
            print('The perimeter is {}'.format(calculate_perimeter(width, height)))
