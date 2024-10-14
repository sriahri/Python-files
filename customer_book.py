b = ""
def customer_book_selection():
    global b
    a = 'If you would like to buy a book.'
    print(a)
    b = input('Please enter the number of book you want here: ')

def complete_transaction():
    global b
    first_name = input('Please enter your first name: ')
    last_name = input('Please enter your last name: ')
    address = input("Please enter your address: ")
    city = input('Please enter the city: ')
    state = input('Please enter the state: ')
    zip_code = input('Please enter the zip code: ')
    print('Customer address info:', first_name, last_name, address, city, state, zip_code)
    print('The value of b is',b)
    print('THANK YOU FOR SHOPPING WITH US!')

customer_book_selection()
complete_transaction()