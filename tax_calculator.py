income = float(input('Enter the income: '))
total_tax = 0
if income >= 9950:
    print('Below $9,950: {}'.format(9950*0.1).rjust(25))
    total_tax += 9950*0.1
elif income - 0 > 0:
    print('Below $9,950: {}'.format(income*0.1).rjust(25))
    total_tax += income*0.1

if income >= 40525:
    print('$9,950 - $40,525: {}'.format((40525-9950)*0.12).rjust(25))
    total_tax += (40525-9950)*0.12
elif income - 9950 > 0:
    print('$9,950 - $40,525: {}'.format((income - 9950) * 0.12).rjust(25))
    total_tax += (income - 9950) * 0.12

if income >= 86375:
    print('$40,525 - $86,375: {}'.format((86375 - 40525) * 0.22).rjust(25))
    total_tax += (86375 - 40525) * 0.22
elif income - 40525 > 0:
    print('$40,525 - $86,375: {}'.format((income - 40525) * 0.22).rjust(25))
    total_tax += (income - 40525) * 0.22

if income >= 164925:
    print('$86,375 - $164,925: {}'.format((164925 - 86375) * 0.24).rjust(25))
    total_tax += (164925 - 86375) * 0.24
elif income - 86375 > 0:
    print('$86,375 - $164,925: {}'.format((income - 86375) * 0.24).rjust(25))
    total_tax += (income - 86375) * 0.24

if income >= 209425:
    print('$164,925 - $209,425: {}'.format((209425 - 164925) * 0.32).rjust(25))
    total_tax += (209425 - 164925) * 0.32
elif income - 164925 > 0:
    print('$164,925 - $209,425: {}'.format((income - 164925) * 0.32).rjust(25))
    total_tax += (income - 164925) * 0.32

if income >= 523600:
    print('$209,425 - $523,600: {}'.format((523600 - 209425) * 0.35).rjust(25))
    total_tax += (523600 - 209425) * 0.35
    print('After $523,600: {}'.format((income - 523600) * 0.37).rjust(25))
    total_tax += (income - 523600) * 0.37
elif income - 209425 > 0:
    print('$209,425 - $523,600: {}'.format((income - 209425) * 0.35).rjust(25))
    total_tax += (income - 209425) * 0.35

print('Total tax is ${}'.format(total_tax))
print('Effective tax rate is {}%'.format(round((total_tax/income)*100, 1)))
