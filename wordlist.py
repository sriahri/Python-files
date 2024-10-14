from csv import writer

file = open('word_list.txt', 'r')
words_list = file.readlines()
words = []
for i in words_list:
    if (i[0] == 's' or i[0] == 'S') and len(i) == 6:
        words.append(i.strip('\n'))
file.close()
csv_file = open('words.csv', 'w', newline='')
csv_writer = writer(csv_file)
csv_writer.writerow(['s_words'])
for i in words:
    csv_writer.writerow([i])

csv_file.close()
