total_population = 330  # Total Population is 330 Million
rate_given = 1.2
vaccination_populated = 32  # 32 Million people already vaccinated

period = float(input('Target time period (in weeks): '))
rate = (float(input('Daily Vaccination increase rate (in %): ')) / 100) * rate_given

daily_vaccines = rate_given # First day vaccines
number_of_days = period * 7 # Number of days
# Since it is an arithmetic progression, here, the difference rate is 0.12, start = 1.2 and n = 49
# Based on that we used the formula of number of vaccines at the end of 49 days.
# Here, S = (n/2)*(2*start + (n-1) * rate)
total_vaccines = (number_of_days/2) * (2 * daily_vaccines + (number_of_days - 1) * rate)
# for i in range(1, int(number_of_days)):
#     daily_vaccines = daily_vaccines + rate
#     total_vaccines += daily_vaccines
percentage_vaccinated = ((vaccination_populated + total_vaccines) * 100) / total_population
immune_required_population = 0.8 * total_population - vaccination_populated

# Based on the same above formula, we have calculated rate and the percentage.
needed_rate = (((immune_required_population * 2) / number_of_days) - (2 * rate_given)) / (number_of_days - 1)
needed_rate = (needed_rate / 1.2) * 100
print('Percentage of people vaccinated by the end of the target period '
      '{} days or {} week(s) is {:.2f}%.'.format(period * 7,
                                                 period,
                                                 percentage_vaccinated))
print('Daily increase rate needed to reach heard immunity (80% of population) is {:.2f}%'.format(needed_rate))
