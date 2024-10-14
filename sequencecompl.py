file = open("Sequences_Final.fasta", 'r') # Open the file in read mode.
line = file.readlines() # Read the text from the file lines.
output_file = open("Sequences_Compl.fasta",'w') # Open the file in write mode.
id = line[0] # Id is present in index 0
text = line[1][::-1] # Reverse the sequence
print('ID is :',id) # Print the id
print('Sequence is :',text) # Print the text
output_file.write(id) # Write the id to the file 
output_file.write('\n')
output_file.write(text) # Write the sequence to the file
output_file.close() # Close the file
file.close()