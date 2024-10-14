def duplicate(string, x):
    if x == 0:
        return ''
    return string + duplicate(string, x - 1)

print(duplicate('dog', 3))