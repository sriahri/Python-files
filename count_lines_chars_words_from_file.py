filename = input()
file = open(filename, 'r')
lines = file.readlines()
lines_count = len(lines)
words_count = 0
characters_count = 0
for line in lines:
    words = len(line.split())
    words_count += words
    characters_count += len(line)

print('Enter the input file name: The file contains {} characters, {} words, and {} lines'
      .format(characters_count, words_count, lines_count))
