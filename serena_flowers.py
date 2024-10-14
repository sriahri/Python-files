def maxi(a,b,c):
    minimum = 999999999
    maximum = 0
    x = 0
    if a > 0:
        for i in range(-100,101):
            x = a * i * i + b * i + c
            minimum = min(x,minimum)
        return minimum
    else:
        for i in range(-100,101):
            x = a * i * i + b * i + c
            maximum = max(x,maximum)
        return maximum
print(maxi(-2,-8,10))