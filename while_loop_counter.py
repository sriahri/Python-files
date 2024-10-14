n = int(input('Enter a number: '))
count = 0

while n >= 0:
    n -= 7
    count += 1

print('The value of n after subtracting 7 for {} times is {}'.format(count, n))
print('The count is', count)
