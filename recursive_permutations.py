def string_permutations(s):
    l = list(s)
    result = []
    # If length of string is 1, return as is
    if len(s) == 1:
        return s
    # Enumerate the list and then generate permutations
    for i, j in enumerate(l):
        for k in string_permutations(l[:i] + l[i + 1:]):  # Recursive call
            result += [j + k]  # Store them in a list

    unique = {}  # Dictionary to store only unique values
    for value in result:
        if value not in unique:  # If the permutation is not present in the dictionary, we add it
            unique[value] = 1
    return unique.keys()  # Returning the unique permutations


if __name__ == '__main__':
    s = input('Enter the string: ')
    permutations = string_permutations(s)
    print('The permutations are:')
    # Printing the permutations
    for permutation in permutations:
        print(permutation)
