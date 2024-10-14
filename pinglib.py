from ping3 import ping


def pingthis(IP):
    response = ping(IP)
    if response:
        return [IP, str(response)]
    else:
        return [IP, 'Not found']


def main():
    import sys
    IP = sys.argv[1]
    response = pingthis(IP)
    print(' '.join(response))


if __name__ == '__main__':
    main()