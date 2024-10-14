import time

from functions import *


def time_f(func, paramter, trials):
    time_taken = 999999999999999999999999999999
    for i in range(trials):
        start = time.time()
        func(paramter)
        end = time.time()
        time_taken = min(time_taken, end - start)
    print("Time taken by {} for {} trials is {}".format(func, trials, time_taken))
    return time_taken


def call_time_f():
    times = {}
    time_taken = time_f(constant_function, 10, 100)
    times['const'] = list([time_taken])
    time_taken = time_f(constant_function, 10, 200)
    val = times['const']
    val.append(time_taken)
    times['const'] = val
    time_taken = time_f(constant_function, 10, 400)
    val = times['const']
    val.append(time_taken)
    times['const'] = val
    time_taken = time_f(constant_function, 10, 600)
    val = times['const']
    val.append(time_taken)
    times['const'] = val
    time_taken = time_f(constant_function, 10, 800)
    val = times['const']
    val.append(time_taken)
    times['const'] = val
    numbers = [i for i in range(1, 100000)]
    time_taken = time_f(linear_function, numbers, 100)
    times['linear'] = list([time_taken])
    time_taken = time_f(linear_function, numbers, 200)
    val = times['linear']
    val.append(time_taken)
    times['linear'] = val
    time_taken = time_f(linear_function, numbers, 400)
    val = times['linear']
    val.append(time_taken)
    times['linear'] = val
    time_taken = time_f(linear_function, numbers, 600)
    val = times['linear']
    val.append(time_taken)
    times['linear'] = val
    time_taken = time_f(linear_function, numbers, 800)
    val = times['linear']
    val.append(time_taken)
    times['linear'] = val
    time_taken = time_f(quadratic_function, numbers, 100)
    times['quadratic'] = list([time_taken])
    time_taken = time_f(quadratic_function, numbers, 200)
    val = times['quadratic']
    val.append(time_taken)
    times['quadratic'] = val
    time_taken = time_f(quadratic_function, numbers, 400)
    val = times['quadratic']
    val.append(time_taken)
    times['quadratic'] = val
    time_taken = time_f(quadratic_function, numbers, 600)
    val = times['quadratic']
    val.append(time_taken)
    times['quadratic'] = val
    time_taken = time_f(quadratic_function, numbers, 800)
    val = times['quadratic']
    val.append(time_taken)
    times['quadratic'] = val
    print('{}\t{}\t{}\t{}\t'.format('trials', 'const', 'linear', 'quadratic'))
    print('{}\t\t{}\t\t{}\t\t{}'.format(100, times['const'][0], times['linear'][0], times['quadratic'][0]))
    for i in range(1, 5):
        print('{}\t\t{}\t\t{}\t\t{}'.format(i * 200, times['const'][i], times['linear'][i], times['quadratic'][i]))


if __name__ == '__main__':
    call_time_f()
