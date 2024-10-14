def readFileLine(n):
    # Opening the file
    f = open("address.txt","r")
    # Reading the file line by line into a list
    text = f.readlines()
    # Returning the nth line from the file
    return text[n-1]

while True:
    # Taking input from the user the line number
    line_number = int(input("Enter the line number: "))
    # Printing the nth line from the file
    print(readFileLine(line_number))
    # Asking the whether he needs to continue or not..?
    choice = input('Do you want to continue(Y/N): ')
    # If the user do not want to continue, he exits.
    if choice == 'N' or choice == 'n':
        break