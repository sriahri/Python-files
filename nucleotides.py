# Function for calculating GC content.
def calculateGCContent(file): 
    f = open(file,'r') # Opening the file in read mode.
    l = f.readlines() # Reading all the content of the file line by line into a list.
    g = 0 # Variable for storing the count of 'G'
    c = 0 # Variable for storing the count of 'C'
    total = 0 # Variable for storing the count of 'C' + 'G' + 'A' + 'T'.
    for i in l:
        if '>' not in i: # For checkimg whether the entry sequence is started or not.
            g += i.count('G') # Counting the 'G' and incrementing it.
            c += i.count('C') # Counting the 'C' and incrementing it.
            total += len(i) # Updating the total.
    return (g+c)/total # Returning the proportion of the G or C nucleotides.

x = (calculateGCContent('E:/idledoc/DNA1.fa'))
print(round(x,2)) # Rounding the result to 2 decimal places.