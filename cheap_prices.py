file = open('prices.txt')
prices_list = file.readlines()
prices_list = list(map(float, prices_list))

cheapest_price = prices_list[0]
for price in prices_list:
    if price < cheapest_price:
        cheapest_price = price

total_prices = 0
prices_count_less_than_100 = 0

for price in prices_list:
    if price < 100:
        total_prices += price
        prices_count_less_than_100 += 1

average_price = total_prices/prices_count_less_than_100

print(f'The cheapest price int the file is ${cheapest_price:.2f}')
print(f'The average price in the file less than 100 is ${average_price:.2f}')
