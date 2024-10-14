def dup(string1, string2, x):
    if x == 0:
        return ''
    else:
        if x%2 == 0:
            return string1 + dup(string1, string2, x - 1)
        else:
            return string2 + dup(string1, string2, x - 1)
    
print(dup('dog', 'cat', 4))