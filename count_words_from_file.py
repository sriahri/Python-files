def main():
    cache = {}
    while True:

        filename = input('Enter the filename: ')
        words_count = {}
        if filename == 'quit':
            break
        if filename in cache:
            print('filename already cached')
            words_count = cache[filename]
        else:
            file = open(filename, 'r')
            lines = file.readlines()
            for line in lines:
                words = line.split()
                for word in words:
                    word = word.strip().strip(',').strip('.')
                    if word in words_count:
                        words_count[word] += 1
                    else:
                        words_count[word] = 1
            cache[filename] = words_count

        print('Word\t\tCount')
        for word, count in words_count.items():
            print('{}: {}'.format(word, count))


if __name__ == '__main__':
    main()
