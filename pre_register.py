def discount():
    print('You are preregistered and qualify for a 5% discount')


def noDiscount():
    print('Sorry, you did not preregister and do not qualify for a 5% discount')


if __name__ == '__main__':
    registerString = input('Did you preregister? Enter Y or N: ')
    if registerString == 'Y':
        discount()
    else:
        noDiscount()
