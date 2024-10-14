def isFloat(input_change):
    try:
        float(input_change)
        return True
    except Exception:
        return False


change = input('change owed: ')
while isFloat(change) is False or float(change) < 0:
    change = input('change owed: ')

change = float(change)
number_coins = 0
change = round(change, 2)
change = int(change * 100)
number_coins += change // 25
change = change % 25
number_coins += change // 10
change = change % 10
number_coins += change // 5
change = change % 5
number_coins += change

print(number_coins)
