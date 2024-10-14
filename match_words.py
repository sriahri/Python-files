def MatchWordsD(filename, word_list):
    file = open(filename,'r') # Opening the file
    lines = file.readlines()  # Reading text from file line by line
    d = {} # Initialize empty dictionary
    for i in word_list:
        d[i] = 0 # Adding the elements in wordlist as keys to dictionary
    for i in lines: # Iterating through all the lines
        for j in i.split(): # Iterating through each word of the current line
            if j in word_list: # If the word is present in word list.
                if j in d: # We increase the count of that word.
                    d[j] += 1
    return d #Returnig the dictionary

worddic = MatchWordsD("JackandJill.txt", ["Jack", "Jill", "up", "river"])
print(worddic)