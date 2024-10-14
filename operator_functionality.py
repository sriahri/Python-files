def main():
    operand1 = float(input("Enter a number: "))
    operator = input("Enter an operator: ")

    # Step 1: If the user entered an operator other than
    # *, /, +, - then display an error message and terminate
    # with exit().

    if operator != '*' and operator != '/' and operator != '+' and operator != '-':
        print("ERROR: Invalid operator")
        exit()

    operand2 = float(input("Enter a number: "))

    # Step 2: Determine if the operator entered was / (division)
    # and the second operand was zero. If so, display an error
    # message and terminate with exit().

    if operator == '/' and operand2 == 0:
        print("ERROR: Cannot divide with 0.")
        exit()

    # Step 3: Calculate and store the answer into the
    # variable result

    result = None

    # Checking if the operator is +, if so, result is sum of the 2 numbers
    if operator == '+':
        result = operand1 + operand2
    # Checking if the operator is -, if so, result is difference of the 2 numbers
    elif operator == '-':
        result = operand1 - operand2
    # Checking if the operator is *, if so, result is product of the 2 numbers
    elif operator == '*':
        result = operand1 * operand2
    # Checking if the operator is /, if so, result is quotient of the 2 numbers
    else:
        result = operand1 / operand2

    print()
    print("The result: ", result)


main()
