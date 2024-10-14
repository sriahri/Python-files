if __name__ == '__main__':
    years = int(input('enter the number of years: '))
    old_branches_previous_year = 0
    new_branches_previous_year = 1
    old_branches_current_year = old_branches_previous_year + new_branches_previous_year
    new_branches_current_year = old_branches_previous_year * 2

    print("n(0): {}".format(new_branches_current_year))
    print("a(0): {}".format(old_branches_current_year))

    for i in range(years):
        print("n({}): {}".format(i + 1, new_branches_current_year))
        print("a({}): {}".format(i + 1, old_branches_current_year))

        old_branches_previous_year = old_branches_current_year
        new_branches_previous_year = new_branches_current_year

        new_branches_current_year = old_branches_previous_year * 2
        old_branches_current_year = old_branches_previous_year + new_branches_previous_year
