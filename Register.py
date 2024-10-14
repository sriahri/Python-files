from BankAccount import BankAccount
def main():
    bankAccount = BankAccount()
    n = int(input('Enter the number of transactions: '))
    count = 0
    for i in range(n):
        s = input('Enter transaction type: ').lower()
        amount = float(input('Enter transaction amount: '))
        if s == 'deposit':
            if bankAccount.deposit(amount):
                print('Transaction was successful. Your account balance is ${0:.2f}'.format(bankAccount.getBalance()))
                count += 1
            else:
                print('Transction rejected')
        elif s == 'withdraw':
            if bankAccount.withdraw(amount):
                 print('Transaction was successful. Your account balance is ${0:.2f}'.format(bankAccount.getBalance()))
                 count += 1
            else:
                print('Transction rejected')
    print('After {} transactions, your balance is ${}'.format(count, round(bankAccount.getBalance(), 2)))

main()