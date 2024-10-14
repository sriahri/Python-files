def maximaOrMinima(a, b, c):
    mini = 999999999999999
    maxi = 0
    for i in range(-100, 100):
        if (a > 0):
            if (a*(i**2) + b * i + c > mini):
                mini = a*(i**2) + b * i + c
        else:
            if (maxi > a*(i**2) + b * i + c):
                maxi = a*(i**2) + b * i + c
    if a > 0:
        return mini
    return maxi