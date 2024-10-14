filename = input('Enter the file name to open: ')  # Get the filename
file = open(filename, 'w')  # Open the file

print('Write some content to file: ')
while True:
    line = input()  # enter blank line to end writing
    if not line:
        break
    file.write(line + "\n")  # write to file
file.close()
