def exchange(exchange_rate, nominal_amount, indicator):
    if indicator.lower() == 'euro':
        return 'The amount in dollars is ${}'.format(nominal_amount*exchange_rate)
    elif indicator.lower() == 'dollar':
        return 'The amount in euros is E{}'.format(nominal_amount * exchange_rate)


if __name__ == '__main__':
    print(exchange(0.93, 550, 'Euro'))
