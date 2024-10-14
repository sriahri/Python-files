import re # import re module
# Function that returns the set of words from the file.
def wordSetFromFile(filename):
    file = open(filename,'r') # Open the file
    source_string = file.read().lower() # Read the content and convert it to lower case.
    file.close() # Close the file.
    words = re.findall('[a-zA-Z]+', source_string) # Extracting only the alphabets in the text.
    return set(words) # Returning the set of words.

# Function used to print the common words in both the files.
def print_common_words(filename1, filename2):
    words1 = wordSetFromFile(filename1) # Calling the function for set of words from file1.
    words2 = wordSetFromFile(filename2) # Callinf the function for set of words from file2.
    common_words = list(words1 & words2) # finding the common words in both files.
    common_words.sort() # Sorting the common words alphabetically.
    for i in common_words: # printing the common words one per line.
        print(i)
print_common_words("engltreaty.txt", "maoritreaty.txt")