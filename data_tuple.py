def data_tuple_from_line(line_str):
    result = list(line_str.split(','))
    result[2] = float(result[2])
    result[3] = float(result[3])
    result[4] = float(result[4])
    result[6] = result[6].title()
    return tuple(result)


if __name__ == '__main__':
    input_str = 'SCE-INT-500025441,2011-09-23,4.48,35175,4094,90254,Hermosa beach,CA'
    data_tuple = data_tuple_from_line(input_str)
    print(type(data_tuple))
    for item in data_tuple:
        print(item, type(item))
