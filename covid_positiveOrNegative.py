#This functions returns whether the result is POSITIVE or NEGATIVE

def covidResult(virus_composition, blood_composition):
    len1 = len(virus_composition) # finding the length of virus_composition
    len2 = len(blood_composition) # finding the length of blood_composition
    i = 0
    j = 0
    while i < len1 and j < len2: # Traversing till the end of both strings.
        # If the character in the blood_composition is equal to virus_composition, 
        # then we procced to the next character in blood_composition.
        if virus_composition[i] == blood_composition[j]: 
            j = j + 1
        i = i + 1
    if j == len2: # If we reach to the end of blood_composition, 
        #then it is a subseqeunce of virus_composition
        return 'POSITIVE'
    return 'NEGATIVE'

virus_composition = input() # Reading the virus_composition.
number_of_people = int(input()) # Reading the number of people
for i in range(number_of_people):
    blood_composition = input() # Reading the blood_composition.
    print(covidResult(virus_composition, blood_composition)) # Printing the result of evry candidate
