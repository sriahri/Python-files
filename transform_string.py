def transform(transformation_spec):
    res = ""
    for i in range(0, len(transformation_spec), 2):
        letter = transformation_spec[i]
        digit = transformation_spec[i + 1]
        res += letter * int(digit)

    return res


if __name__ == '__main__':
    print(transform('w4a2k1'))
