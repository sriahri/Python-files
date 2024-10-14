def pretty_print_dollars(currency):
    amount = str(currency)
    if '.' in amount:
        dollars = amount.split('.')[0]
        cents = amount.split('.')[1]
    else:
        dollars = amount
        cents = '00'

    dollars = dollars[::-1]
    res = ''
    dollars = dollars.replace('-', '')
    for i in range(0, len(dollars), 3):
        res += dollars[i:i+3] + ','
    res = res[::-1]

    if len(cents) < 2:
        cents += '0'
    if currency < 0:
        return '-$' + res[1:] + '.' + cents
    else:
        return '$' + res[1:] + '.' + cents


if __name__ == '__main__':
    print(pretty_print_dollars(1000.0))
    print(pretty_print_dollars(5.99))
    print(pretty_print_dollars(547475874))
    print(pretty_print_dollars(-84989))
    print(pretty_print_dollars(999.58))
