Fname = str(input("Enter logic function name (and, or, not): ")).upper()
A = int(input("Enter value of condition A: "))
B = int(input("Enter value of condition B: "))
condition1 = Fname == 'AND'
condition2 = A == 1 and B == 1
condition3 = A == 0 and B == 0
condition4 = A == 0 and B == 1
condition5 = A == 1 and B == 0

if condition1:
    if condition2:
        print('and logic function result = 1')
    elif condition3:
        print('and logic function result = 0')
    elif condition4:
        print('and logic function result = 0')
    elif condition5:
        print('and logic function result = 0')
    else:
        print('Wrong for A/B')
else:
    print('Wrong for condition')
