us_dollars = 0
exchange_rate = 0

while True:
    us_dollars = input('How many US Dollars do you want to exchange: ')
    if not us_dollars.isnumeric():
        continue
    else:
        break

currency = input('Enter the name of the currency you are converting dollars to: ')
while True:
    exchange_rate = input('What is the exchange rate?  ')
    if not exchange_rate.isnumeric():
        continue
    else:
        break

result = int(us_dollars) * int(exchange_rate)
print()
print('You can exchange {} U.S. dollars for {} {} '.format(us_dollars, result, currency))
