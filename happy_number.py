def digits_square(n):
    result = 0
    while n:
        result += (n % 10) * (n % 10)
        n = int(n / 10)
    return result


def heavy(number, base):
    number = int(number, base)
    st = set()
    while 1:
        number = digits_square(number)
        if number == 1:
            return True
        if number not in st:
            return False
        st.add(number)


if __name__ == '__main__':
    print(heavy('4', 10))
