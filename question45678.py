a1 = 'abhishek,is,a,good,boy'
# 4a)
split_string = a1.split(',')
print(split_string)

# 4b
print(a1.split(',', 0))
print(a1.split(',', 1))
print(a1.split(',', 2))

# 5
a2 = 'Abhishek is a nice boy'
print(a2.replace('nice boy', 'James Bond'))

# 6
print(a2[:8])

# 7
print(a2[-3:-1] + a2[-1])

# 8
name = 'John Smith'
salary = 100000
print('Hello my name is {} and my expected salary is {}, hurray!'.format(name, salary))
