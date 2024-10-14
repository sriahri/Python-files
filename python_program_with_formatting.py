# IMPORT STATEMENTS

import os
import csv


# FUNCTION DEFINITIONS

def get_expenses():
    expenses = []
    if os.path.exists('expenses.csv'):
        with open('expenses.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                expenses.append(row)
    return expenses


def add_expense(expenses):
    category = input('Enter the category: ')
    vendor = input('Enter the vendor: ')
    amount = input('Enter the amount: ')
    date = input('Enter the date: ')
    expense = [category, vendor, amount, date]
    expenses.append(expense)
    return expenses


def get_total(expenses):
    total = 0.0
    for expense in expenses:
        total += float(expense[2])
    return total


def get_total_by_category(expenses):
    category = input('Enter the category: ')
    total = 0.0
    for expense in expenses:
        if expense[0] == category:
            total += float(expense[2])
    return total


def get_total_by_vendor(expenses):
    vendor = input('Enter the vendor: ')
    total = 0.0
    for expense in expenses:
        if expense[1] == vendor:
            total += float(expense[2])
    return total


def save_expenses(expenses):
    with open('expenses.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(expenses)


# Program Logic


def print_menu():
    print('1. Add an expense')
    print('2. Get total of all expenses')
    print('3. Get total of expenses by category')
    print('4. Get total of expenses by vendor')
    print('5. Quit')


def main():
    expenses = get_expenses()
    while True:
        print_menu()
        choice = input('Enter your choice: ')
        if choice == '1':
            expenses = add_expense(expenses)
        elif choice == '2':
            total = get_total(expenses)
            print('Total:', total)
        elif choice == '3':
            total = get_total_by_category(expenses)
            print('Total:', total)
        elif choice == '4':
            total = get_total_by_vendor(expenses)
            print('Total:', total)
        elif choice == '5':
            save_expenses(expenses)
            break
        else:
            print('Invalid choice')


if __name__ == '__main__':
    main()
