from math import log10 # Import log from the math library

# Ask for the minimum value
minimum_number = float(input("What is the minimum value? "))
# Ask for maximum value
maximum_number = float(input("What is the maximum value? "))
# Ask for step size
step_size = float(input("What is step size? "))

# Printing according to the format
print("\t  0\t1\t2\t3\t4\t5\t6\t7\t8\t9\n")
print('--------------------------------------------------------------------------------------------')
i = minimum_number
# Till it reaches the maximum number
while i < maximum_number:
    i = round(i, 4) # Round off to 4 digits
    print(format(i, ".4f"), end = "\t")
    number = i
    for j in range(10): # For 10 Columns
        res = log10(number)
        number = number + 0.01 # Increase for each column
        res = round(res, 4)
        print(format(res, ".4f"), end = '\t')
    i += step_size # Increase for step size
    print()
        