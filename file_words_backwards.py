filename = input('Enter the file name to open: ')  # Get the filename
file = open(filename)  # Open the file
lines = file.readlines()  # Read all the lines from file

for line in lines:
    line = line.strip()
    words = line.split()  # Get all the words from file
    for word in words:
        print(''.join(word[::-1]), end=' ')  # print every word backwards
    print()
