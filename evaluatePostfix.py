def evaluate(input1):
    l = []
    for i in input1:
        if i.isnumeric():
            l.append(i)
        else:
            val1 = l.pop()
            val2 = l.pop()
            if i == '/':
                x = '//'
                l.append(str(eval(val2+x+val1)))
            else:   
                l.append(str(eval(val2+i+val1)))
    return int(l.pop())