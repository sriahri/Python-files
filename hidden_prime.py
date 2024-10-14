def is_prime(n):
    from math import sqrt
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def main():
    number = int(input("Enter the number: "))
    string = str(number)
    substrings = [string[i:j] for i in range(len(string)) for j in range(i + 1, len(string) + 1)]
    for i in substrings:
        if len(i) == len(string):
            if is_prime(int(i)):
                return False
        else:
            if is_prime(int(i)):
                return True
    return False


if __name__ == '__main__':
    if main():
        print('True')
    else:
        print('False')
