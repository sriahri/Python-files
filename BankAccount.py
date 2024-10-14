"""
The BankAccount class consists of balance amount.
Initially, the balance starts from 0. It can perform deposit and with drawl operations.
We also get the current balance of the account.
"""


class BankAccount:
    def __init__(self, name, account_number, type_of_account, balance):
        self.name = name
        self.account_number = account_number
        self.type_of_account = type_of_account
        self.balance = balance

    def assign_initial_value(self, value):
        self.balance = value

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        else:
            print('Deposit amount ${} is less than 0'.format(amount))
            return False

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            print('Withdrawl amount ${} is higher than the cuurent balance {}'.format(amount, round(self.balance, 2)))
            return False

    def get_balance(self):
        return self.balance


if __name__ == '__main__':
    account = BankAccount('Jack', 'BA121', 'Savings', 0)
    account.assign_initial_value(2000)
    account.deposit(1200)
    print(account.get_balance())
    account.withdraw(700)
    print(account.get_balance())
