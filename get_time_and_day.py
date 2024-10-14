import time


def convert(seconds):
    days = seconds // 86400
    seconds = seconds % 86400
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return days, hour, minutes, seconds


def greet(current_time):
    days, hours, minutes, seconds = convert(current_time)
    if 0 <= hours < 12:
        print('Good morning!')
    elif 12 <= hours < 6:
        print('Good afternoon!')
    else:
        print('Good evening!')


current_time = time.time()
days, hours, minutes, seconds = convert(current_time)
print('The number of days since the start of epoch is {}'.format(days))
print('The number of hours since the start of epoch is {}'.format(hours))
print('The number of minutes since the start of epoch is {}'.format(minutes))
print('The number of seconds since the start of epoch is {}'.format(seconds))
greet(current_time)
