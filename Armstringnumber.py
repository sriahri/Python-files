def is_armstrong(my_int):
    s = str(my_int)
    count = 0
    length = len(s)
    for i in s:
        count += int(i)**length

    if count == my_int:
        return True
    return False


if __name__ == '__main__':
    print(is_armstrong(123))
    print(is_armstrong(153))
    print(is_armstrong(234))
    print(is_armstrong(371))