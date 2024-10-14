file = open("US_Constitution.txt", 'r') # Open file
lines = file.readlines() # Read lines from file 
unique_words = set() # Declare a set
for i in lines:
    words = i.split() # generate words from lines
    for j in words:
        # process each word
        word = j.strip('\n').strip(',').strip('.').strip(';').strip('!').lower()
        unique_words.add(word) # Add words to set
for i in unique_words:
    print(i)