if __name__ == '__main__':
    original_price = float(input('Original Price: '))
    discount_rate = float(input('Discount Rate: '))
    number_ordered = int(input('Number Ordered: '))

    new_sales_price = original_price * (1 - discount_rate)
    print('The new sales price for one T-shirt is {}'.format(new_sales_price))
    subtotal = new_sales_price * number_ordered
    print('The number of T-shirts ordered is {}'.format(number_ordered))
    print('The subtotal is {}'.format(subtotal))
    sales_tax = subtotal * 0.07
    print('The sales tax is {}'.format(sales_tax))
    shipping_and_handling_fee = 3.99
    print('The shipping and handling fee is {}'.format(shipping_and_handling_fee))
    print('The total payment of the order is {}'.format(subtotal + sales_tax + shipping_and_handling_fee))
