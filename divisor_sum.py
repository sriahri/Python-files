def divisor_sum(number):
    from math import sqrt
    i = 2
    divisors = [1]
    while i <= sqrt(number):
        if number % i == 0:
            if i == number // i:
                divisors.append(i)
            else:
                divisors.append(i)
                divisors.append(number//i)
        i += 1
    res = sorted(divisors)
    res = [str(i) for i in res]
    res = ' + '.join(res)
    return res + ' + = ' + str(eval(res))


if __name__ == '__main__':
    print(divisor_sum(36))
