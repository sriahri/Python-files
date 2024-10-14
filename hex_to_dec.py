def hexadecimal_to_decimal_converter(hexadecimal_string):
    n = len(hexadecimal_string)
    rev_string = hexadecimal_string[::-1]
    var = 0
    for i in range(0, n):
        if rev_string[i].upper() == 'A':
            x = 10
        elif rev_string[i].upper() == 'B':
            x = 11
        elif rev_string[i].upper() == 'C':
            x = 12
        elif rev_string[i].upper() == 'D':
            x = 13
        elif rev_string[i].upper() == 'E':
            x = 14
        elif rev_string[i].upper() == 'F':
            x = 15
        else:
            x = int(rev_string[i])
        var += x * 16 ** i

    return var


if __name__ == '__main__':
    hexadecimal_string = '7'
    decimal_value = hexadecimal_to_decimal_converter(hexadecimal_string)
    print('{} in hexadecimal is {} in decimal'.format(hexadecimal_string, decimal_value))

    hexadecimal_string = 'D'
    decimal_value = hexadecimal_to_decimal_converter(hexadecimal_string)
    print('{} in hexadecimal is {} in decimal'.format(hexadecimal_string, decimal_value))

    hexadecimal_string = 'FF'
    decimal_value = hexadecimal_to_decimal_converter(hexadecimal_string)
    print('{} in hexadecimal is {} in decimal'.format(hexadecimal_string, decimal_value))

    hexadecimal_string = '2A'
    decimal_value = hexadecimal_to_decimal_converter(hexadecimal_string)
    print('{} in hexadecimal is {} in decimal'.format(hexadecimal_string, decimal_value))