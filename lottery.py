def simulate_lottery(transaction_amount, target_set):
    import random
    random.seed(191)  # IMPORTANT: Please DO NOT change this line.
    customer_list = [] # For storing the customer elements
    balls_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # Balls list
    if transaction_amount > 100:
        print('You have the chance to participate in the lottery')
    for i in range(2 * len(target_set) + 1): # No. of chances for the customer
        customer_ball = random.choice(balls_list) # Random choice for customer ball
        print('You picked {}'.format(customer_ball))
        # If ball is already present, then add else remove
        customer_list.append(customer_ball) if customer_ball not in customer_list else customer_list.remove(
            customer_ball)

    target_set.sort() # Sort the target set
    customer_list.sort() # Sort the customer list
    print('The target set is {}'.format(target_set))
    print('The customer set is {}'.format(customer_list))
    # If customer list is part or equal to target list
    if target_set in customer_list:
        print('You have won the lottery....')
    else:
        print('You did not win the lottery....')


transaction_amount = float(input('Enter the transaction amount: '))
target_set = list(map(int, input('Enter the target set: ').split()))
simulate_lottery(transaction_amount, target_set)
