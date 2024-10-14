first_name, last_name = input('Enter the first and last name of the customer: ').split()
item_id = input('Enter the item id: ')
cost = float(input('Enter the cost: '))
cash_given = float(input('Enter the cash given: '))

company_id = item_id[:5]
product_id = item_id[len(item_id) - 4:]
total_cost = round(cost + cost * 0.15, 2)
change = round(cash_given - total_cost, 2)

print('Customer (Last, First): {} {}'.format(last_name, first_name))
print('Item Number (Product, Company): {} {}'.format(product_id, company_id))
print('Item Cost (+ Sales Tax): {}'.format(total_cost))
print('Change: {}'.format(change))
