def my_math(integer, operator):
    digits = []
    result = 1
    for i in integer:
        digits.append(int(i))
    if operator == '+':
        return sum(digits)
    elif operator == '*':
        for i in digits:
            result *= i
    else:
        result = -1
    return result    
def main():
    integer, operator = input("Input positive integer and operator(+ or *): ").split()
    result = my_math(integer, operator)
    if result != -1:
        print(f"Result: {result}")
    else:
        print("Invalid Operator")
        
main()