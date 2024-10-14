months = {1: ["January", 31],
          2: ["February", 28],
          3: ["March", 31],
          4: ["April", 30],
          5: ["May", 31],
          6: ["June", 30],
          7: ["July", 31],
          8: ["August", 31],
          9: ["September", 30],
          10: ["October", 31],
          11: ["November", 30],
          12: ["December", 31]}


def is_leap_year(year):
    if (year % 400 == 0) and (year % 100 == 0):
        return True
    elif (year % 4 == 0) and (year % 100 != 0):
        return True
    return False


def is_valid_month(month):
    if 1 <= month <= 12:
        return True
    return False


def is_valid_day(month, day, year):
    is_leap = is_leap_year(year)
    if is_leap and month == 2:
        if day <= 29:
            return True
        return False
    else:
        days = months[month][1]
        if day <= days:
            return True
        return False


def split_date(date_string):
    l = date_string.split('/')
    month = int(l[0])
    day = int(l[1])
    year = int(l[2])

    return month, day, year


def is_valid_format(date_string):
    if len(date_string) == 10:
        return True
    return False


def full_date_string(date_string):
    month, day, year = split_date(date_string)
    month_name = months[month][0]
    result = month_name + ' ' + str(day) + ', ' + str(year)
    return result


def is_valid_date(date_string):
    month, day, year = split_date(date_string)
    if is_valid_format(date_string) and is_valid_month(month) and is_valid_day(month, day, year):
        return True
    return False
