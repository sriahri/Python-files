def countPalindromes(input1, input2):
    l = input1.split()
    c = 0
    for i in l:
        if i == i[::-1]:
            c += 1
    return c