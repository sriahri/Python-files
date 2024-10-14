import example  # To use the add function


# Calculates the sales using the input from the user.
def calculateSales():
    subTotal = 0  # Variable to store the subtotal
    # To read the prices of 4 items using for loop
    for i in range(4):
        # Prompt the user for item price
        itemSale = float(input('Enter an item price: '))
        subTotal = example.add(subTotal, itemSale)  # Calling the add function

    return subTotal  # Returning the sub total


# It calculates the tax based on the subtotal and the tax rate.
def salesTax(subTotal, TAX_RATE):
    tax = subTotal * TAX_RATE  # Compute the sales tax
    return tax  # Returns the tax


# Computes the total sales price
def totalSalesPrice(totalSales, taxes):
    totalPrice = example.add(totalSales, taxes)  # Calling the add function
    return totalPrice  # Returns the total price


# Main function
if __name__ == '__main__':
    TAX_RATE = 0.07  # TaxRate for computing the sales tax
    # Numbers to add.
    num1 = 2.5
    num2 = 7.2

    # Calling the add function
    print('This is the call to the imported add function')
    result = example.add(num1, num2)  # Calling the add function
    print('The addition of {} + {} is {}'.format(num1, num2, result))
    print()
    subTotal = calculateSales()  # Calling the calculateSales function
    tax = salesTax(subTotal, TAX_RATE)  # Calling the salesTax function
    totalPrice = totalSalesPrice(subTotal, tax)  # Calling the totalSalesPrice function

    print()
    print('The subtotal is {:.2f}'.format(subTotal))
    print('The tax is {:.2f}'.format(tax))
    print('The total price is ${:.2f}'.format(totalPrice))
