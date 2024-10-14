def isBraid(u, v, w):
    i,j = 0,0 # Declaring the varibles i and j to use them as the pointers for u and v respectively.
    for letter in w: # Traverse through the string w
        # Since, the string w can be formed by a catenation of strings u and v
        # only the strings are to be considered so we check each character 
        # with the characters of the strings u and v.
        if i < len(u) and letter == u[i]: 
            i += 1 # We increment the value of index of u.
        elif j < len(v) and letter == v[j]:
            j += 1 # We increment the value of index of v.
        else:
            return False # If the letter is not the first character in u or v, then it is false.
    return True # If all the letter's constraints are satisfied, then returns true.

u = input("Enter the string u: ")
v = input("Enter the string v: ")
w = input("Enter the string w: ")
print(isBraid(u, v, w))