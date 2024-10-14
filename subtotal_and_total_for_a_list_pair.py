qtyPrice = [2, 1.5, 4, 0.5, 1, 2.5, 3, 2.0]
total = 0
for i in range(0, len(qtyPrice), 2):
    quantity = qtyPrice[i]
    unitPrice = qtyPrice[i+1]
    subtotal = quantity * unitPrice
    print('{} x {} = {}'.format(quantity, unitPrice, subtotal))
    total += subtotal

print('{} items'.format(len(qtyPrice)//2))
print('Total price ${}'.format(total))
