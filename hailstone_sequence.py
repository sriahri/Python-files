n = int(input('Enter the number: '))
count = 1
while n != 1:
    print(n, end=" ")
    if n % 2 == 0:
        n = n // 2
    else:
        n = n * 3 + 1
    count += 1
    if count % 10 == 0:
        print()
print(1)
