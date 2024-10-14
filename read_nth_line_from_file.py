def read_file(file_to_read, n):
    file = open(file_to_read)
    lines = file.readlines()
    file.close()
    if len(lines) >= n - 1:
        return lines[n - 1]


f = open('trial.txt', 'w')
for i in range(20):
    f.write('This is line number ' + str(i + 1) + '\n')
f.close()

assert read_file('trial.txt', 13) == 'This is line number 13\n'
assert read_file('trial.txt', 6) == 'This is line number 6\n'
