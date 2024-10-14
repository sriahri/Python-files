import statistics

if __name__ == '__main__':
    answer = 'y'
    while answer == 'y':
        month = input('Please enter the name of the month to be processed: ')
        month_file = input('Please enter the file of the month to be processed: ')

        print('List of temperatures corresponding to the month {}'.format(month))

        print('Lowest temperature'
              '')