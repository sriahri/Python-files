def is_balanced(expr):
    parentheses = ['()', '{}', '[]']
    while any(symbol in expr for symbol in parentheses):
        for br in parentheses:
            expr = expr.replace(br, '')
    return not expr


def read_file(filename):
    file = open(filename)
    lines = file.readlines()
    expression = ''
    for line in lines:
        for char in line:
            if char in ['{', '}', '[', ']', '(', ')']:
                expression += char

    if is_balanced(expression):
        return True
    else:
        return False


if __name__ == '__main__':
    filename = "financial_data.txt"
    print(read_file(filename))
