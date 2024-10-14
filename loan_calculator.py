def calculate_simple_interest(P, N, R):
    return P + (P * N * R) / 100  # Simple interest is calculated


def calculate_compound_interest(P, N, R):
    return P * (1 + R / 100) ** N  # Compound interest is calculated


if __name__ == '__main__':
    choice = 'Y'
    while choice.upper() == 'Y':
        p = float(input("Enter the principal amount: "))  # Read principal amount
        while p <= 0:  # If principal amount less than 0, read again till valid input is read.
            print("Please enter principal amount > 0")
            p = float(input("Enter the principal amount: "))
        n = int(input("Enter the number of years: "))  # Read number of years
        while n <= 0:  # If number of years less than 0, then repeat until valid input is received
            print("Enter the number of years > 0")
            n = int(input("Enter the number of years: "))
        r = int(input("Enter the rate of interest: "))  # Read rate of interest
        while r <= 0:  # Until valid input is received, read the rate of interest
            print("Enter the rate of interest > 0")
            r = int(input("Enter the rate of interest: "))

        print("Simple interest is {}".format(calculate_simple_interest(p, n, r)))  # Simple interest
        print("Compound interest is {}".format(calculate_compound_interest(p, n, r)))  # Compound interest

        choice = input("Do you want to continue(Y/N): ")  # If the user wants to continue.
