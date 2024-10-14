import random


# method to get user input for n
def get_number():
    n = input("Enter an integer number: ")
    # check if the input is a number
    if n.isnumeric():
        # check if the number is greater than 0
        if int(n) > 0:
            # return the number to the main
            return n
        # return the error message
        else:
            return "Integer value should be greater than 0."
    else:
        return "invalid input"


# method to perform the write operation on the file
def write_numbers(fname, n):
    # open the file in write mode
    file = open(fname, 'w')
    # write n numbers to the file
    for i in range(n):
        # random number generation between 100-15000 inclusive
        number = random.randint(100, 15000)
        # write the generated random number to the file
        file.write(str(number) + '\n')
    # close file
    file.close()


# method to read the file contents
def read_numbers(fname):
    # variables for count,total and average
    count = 0
    total = 0
    avg = 0

    # open the file in read mode
    f = open(fname, "r")
    # for each value x in the file
    for x in f:
        # count the numbers present in the file
        count = count + 1
        # add the numbers
        total = total + int(x)

    # close file
    f.close()
    # compute the average of all the numbers
    avg = total / count

    # display the variable's values
    print("count of the numbers: ", count)
    print("total of the numbers: ", total)
    print("average of the numbers: ", avg)


# driver code (main function)
def main():
    # call the get_number function and store the return value in n
    n = get_number()
    # check if the return value is a number
    if n.isnumeric():
        # perform further operations...
        # get the file name
        fname = input("Enter file name: ")
        # call to write numbers in the file
        write_numbers(fname, int(n))
        # call to read numbers from the file
        read_numbers(fname)

    # if the return value is an error message
    else:
        # print the error message and exit the program.
        print(n)


# call the main function
main()