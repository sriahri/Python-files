text = input().lower().split() # Taking the input from the user and convert it to lower case
# Words that are not taken into account for counting.
words = ['for', 'i', 'a', 'is', 'and', 'are', 'the', 'in', 'to', 'me', 'my', 'it', 'of', 'we', 'be', 'our']
# Initializing empty dictionary.
dictionary = {}
print()
# Looping through all the words in the text.
for i in text:
    # Checking whether the word is not present in the words list.
    if i not in words:
        # If the word is already present in the dictionary, we increase the count by 1.
        if i in dictionary.keys():
            dictionary[i] += 1
        # If the element is not present in the dictionary, we add it to the keys.
        else:
            dictionary[i] = 1

# Sort the dictionary based on the count of word.
required_result = sorted(dictionary.items(), key = lambda x:x[1], reverse = True)
# Printing the top most word.
print('The top most word is',required_result[0][0],'with the count of',required_result[0][1],'times.')
print()
# Printing the second top most word.
print('The second top most word is',required_result[1][0],'with the count of',required_result[1][1],'times.')