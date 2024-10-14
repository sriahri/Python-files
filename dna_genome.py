import random # For random choicee of dna sequence
file = open("output.fas", "w") # Open file to write to it.
proteins = ['A', 'C', 'G', 'T'] # A, C, T, G are the nucleotides
lengths = [21, 24, 27, 30] # Length of the seqeunce
sequences = []
for i in range(5):
    dna_length = random.choice(lengths) # Randomly select from the list
    dna = ""
    for j in range(dna_length):
        dna += random.choice(proteins)
    sequences.append(dna)
    file.write(">sequence{} {}\n".format(i+1, dna)) # Write sequence to file.