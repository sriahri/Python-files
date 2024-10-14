def paranthese_balanced(trinomial):
    parantheses = ['()']
    while any(x in trinomial for x in parantheses):
        for br in parantheses:
            trinomial = trinomial.replace(br, '')
    return not trinomial

def calc(trinomial):
    return eval(trinomial)


def check_operators_and_operands(trinomial):
    trinomial = trinomial.replace('( ', '')
    trinomial = trinomial.replace(') ', '')
    l = trinomial.split()
    operands, operators = 0
    for i in l:
        if i.isnumeric():
            operands += 1
        elif i == '+' or i == '*':
            operators += 1
        else:
            print('Invalid operator input')
    if not (operators == 2 and operands == 3):
        print("Invalid formula")