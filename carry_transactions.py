def carry_out_transactions(balance, transactions_tuple):
    deposits = 0
    withdrawals = 0
    for transaction in transactions_tuple:
        if transaction < 0:
            withdrawals += transaction * -1
        else:
            deposits += transaction
        balance += transaction

    return balance, deposits, withdrawals


if __name__ == '__main__':
    results = carry_out_transactions(100, (500, -200, 50))
    print("Balance $", results[0], sep="")
    print("Deposits $", results[1], sep="")
    print("Withdrawals $", results[2], sep="")

    results = carry_out_transactions(5400, (100, -400, 500, -800, 600, -100, -200, 50, 0, -200))
    print("Balance $", results[0], ", deposits $", results[1], ", withdrawals $", results[2], sep="")
