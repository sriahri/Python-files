import re # The regular expression module for stripping the whitespaces and punctuations.
file = open("gutenberg_text.txt",'r') # opening the file
text = file.read() # Reading the content from the file.
text = text.lower() # converting all the content to lower case.
words = re.findall('[a-z]+', text) # taking in only the letters.
excluding_words = ['a', 'an', 'the', 'in', 'up', 'on', 'for', 'by', 'of', 'under', 'onto', 'into', 'and', 'or', 'if', 'whether', 'why', 'what', 'who', 'whom', 'where', 'which']
print('The total number of words are ',len(words)) # printing the total number of words.
d = {} # Dictionary
for i in words: # For each word
    if i in d: # IF the word is already in the dictionary.
        d[i] += 1 # increase the frequency.
    else:
        d[i] = 1 # Adding the element to the dictionary.
print('The number of unique words are', len(d.keys())) # Number of unique words.
# Sorting the dictionary based on the frequency.
sorted_dictionary = sorted(d.items(), key = lambda x:x[1], reverse = True) 
count = 1
# Printing the top 100 frequent items
if len(sorted_dictionary) >= 100:
    for i in sorted_dictionary[:100]:
        print(count, ':',i[0],i[1])
        count += 1
else:
    for i in sorted_dictionary:
        print(count, ':',i[0],i[1])
        count += 1
count = 1
# Printing the top 100 frequent items excluding the given words.
for i in sorted_dictionary:
    if i[0] not in excluding_words:
        print(count, ':',i[0],i[1])
        count += 1
    if count > 100:
        break