if __name__ == '__main__':
    # Part a
    print("------Part 1 GPA-------")
    credit_hours = 15
    grade_points = 47
    print('Jane Campos GPS for {} grade points and {} credit hours is {:.1f}'
          .format(grade_points, credit_hours, grade_points / credit_hours))

    # Part b

    print('---------Part 2------------\n--------------ComputerClub----------')
    number_of_cases = 29
    selling_price = 1.5
    cost_price = 1
    government_tax = 0.1

    total_cost_price = number_of_cases * 100 * cost_price
    total_selling_price = number_of_cases * 100 * selling_price
    gross_profit = total_selling_price - total_cost_price
    student_government = gross_profit * government_tax
    computer_club = gross_profit - student_government

    print('Total income from {} cases sold is ${}'.format(number_of_cases, total_selling_price))
    print('Total cost of {} cases sold is ${}'.format(number_of_cases, total_cost_price))
    print('Gross Profit ${}'.format(gross_profit))
    print('Student government receives ${}'.format(student_government))
    print('Computer club receives ${}'.format(computer_club))
