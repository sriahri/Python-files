def assistance(household_income, number_of_children):
    assistance_amount = 0
    if 30000 <= household_income <= 40000 and number_of_children >= 3:
        assistance_amount = 1500 * number_of_children

    elif 20000 <= household_income < 30000 and number_of_children >= 2:
        assistance_amount = 1000 * number_of_children

    elif household_income < 20000:
        assistance_amount = 2000 * number_of_children

    return assistance_amount
