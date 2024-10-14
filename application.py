from date_functions import is_valid_date, full_date_string

d = input()

if is_valid_date(d):
    print("{} is a valid date".format(full_date_string(d)))
else:
    print("{} is not a valid date".format(d))
