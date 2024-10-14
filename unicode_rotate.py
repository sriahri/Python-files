def list_rotate(uniquecode_list):
    rotated_list = []
    for unicode in uniquecode_list:
        x_part = unicode.split('-')[0]
        y_part = unicode.split('-')[1]
        result = ''
        alpha_count = 0
        for i in x_part:
            if i.isalpha():
                alpha_count += 1
                result += i
        if alpha_count == 2:
            result += y_part[2:] + y_part[0] + y_part[1]
        elif alpha_count == 1:
            result += y_part[1:] + y_part[0]
        rotated_list.append(result)
    return rotated_list


if __name__ == '__main__':
    uniquecode_list = ["AZ01-1234", "R137-8714"]
    rotated_list = list_rotate(uniquecode_list)
    print(rotated_list)

    uniquecode_list = ['GT21-1011', 'S621-9699']
    rotated_list = list_rotate(uniquecode_list)
    print(rotated_list)

    uniquecode_list = ['GT21-1011', 'SA21-9699']
    rotated_list = list_rotate(uniquecode_list)
    print(rotated_list)
