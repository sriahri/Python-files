#
# Student Name - Replace with your name!
# Date - Replace with the date!
# This program calculates the total cost for items purchased at Bargain
# Used Books. The program outputs the total cost before tax, the sales tax,
# and the total after tax.
#

# Global Constants - Use these in your program where it makes sense
TAX_RATE = 0.07  # 7% sales tax
PB_MAX = 50
PB_COST = 2.50
HB_MAX = 20
HB_COST = 7.00
MAG_MAX = 35
MAG_COST = 3.95


# The get_item_count function takes one parameter:
#    max_allowed - Maximum number of items the user can enter
#
# This function will ask the user to enter the number of items and
# validate the number entered is between 0 and the max_allowed
# inclusive. The number of items the user enters is returned.


def get_item_count(MAX):  # You should fill in the parameters needed
    number_of_items = int(input("Enter the number of items: "))
    while number_of_items < 0 or number_of_items > MAX:
        print("Number of items must be between 0 and {}".format(MAX))
        number_of_items = int(input("Enter the number of items: "))

    return number_of_items


# The get_item_total function takes two parameters:
#     num_items - Number of items
#     unit_price - The cost of each item
#
# This function calculates the total cost for the items and
# returns that value.
def get_item_total(num_items, unit_price):  # You should fill in the parameters needed
    return num_items * unit_price


# The calc_and_display_receipt function will calculate all the
# necessary values and display the receipt. It takes three parameters:
#    pb_total - Total cost of paperbacks
#    hb_total - Total cost of hardbacks
#    m_total  - Total cost of magazines
#
# This function will calculate total before tax, the tax on the total,
# and the total after tax is added. The receipt should display the
# total cost of paperbacks, hardbacks, and magazines IF the item cost
# is greater than 0. The receipt should also include the subtotal, tax,
# and total.


def calc_and_display_receipt(pb_total, hb_total, m_total):  # You should fill in the parameters needed
    if pb_total:
        print('Paperbacks: ${:.2f}'.format(pb_total))
    if hb_total:
        print('Hardbacks: ${:.2f}'.format(hb_total))
    if m_total:
        print('Magazines: ${:.2f}'.format(m_total))

    total = pb_total + hb_total + m_total
    print('-----------------------------------')
    print('Subtotal: {:.2f}'.format(total))
    print('Tax: {:.2f}'.format(total * 0.07))
    print('Amount due: {:.2f}'.format(total + total * 0.07))


# main function


def main():
    print('Paperbacks')
    pb_item_count = get_item_count(PB_MAX)
    pb_total = get_item_total(pb_item_count, PB_COST)
    print('Hardbacks')
    hb_item_count = get_item_count(HB_MAX)
    hb_total = get_item_total(hb_item_count, HB_COST)
    print('Magazines')
    m_item_count = get_item_count(MAG_MAX)
    m_total = get_item_total(m_item_count, MAG_COST)

    calc_and_display_receipt(pb_total, hb_total, m_total)


# Call the main function.
main()
