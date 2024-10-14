file = open('wordlist.txt')
lines = file.readlines()
count = 0
total_words = 0
for line in lines:
    line = line.strip().strip('.')
    words = line.split()
    for word in words:
        if 'r' in word or 's' in word or 't' in word or 'l' in word or 'n' in word or 'e' in word:
            count += 1
        total_words += 1

percentage = (count/total_words) * 100
print('The number of words contain at least one of the letters r, s, t, l, n, e is', count)
print('The percentage of words that contain at least one of the letters r, s, t, l, n, e is', percentage)
