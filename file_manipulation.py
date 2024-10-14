# Open the file inp.txt in read mode.
f = open('inp.txt', 'r')
# Read the content from the file
content = f.read()
# Split the content from the file using a delimiter '.\n'
# Because it is said that all the lines are ending with . 
# and by default it ends with \n except for the last line.
lines = content.split('.\n')
# For the last line, we replace the . with empty character.
lines[-1] = lines[-1].replace('.', '')
# Traverse through all the lines.
for i in range(len(lines)):
    # Split the line into number of words
    words = lines[i].split()
    # Check whether the last word starts with l
    # Check whether the length of first word and length of last word are equal.
    if words[-1][0] == 'l' and len(words[-1]) == len(words[0]):
        # Print the line number and the words
        print('Line', i, ':',words[0], words[-1])