def convert_base(number, base_x, base_y):
    # Convert the number from ase x to decimal
    decimal_number = int(number, base_x)
    result = ''
    while decimal_number > 0:
        digit = int(decimal_number % base_y)
        if digit < 10:
            result += str(digit)
        else:
            result += chr(ord('A') + digit - 10)
        decimal_number //= base_y
    result = result[::-1]
    return result


if __name__ == '__main__':
    original_number = '10110'
    present_base = 2
    future_base = 7
    print('The number in base {} is {}'.format(future_base, convert_base('10110', 2, 7)))
