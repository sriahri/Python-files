import re


def get_words_from_file(filename):
    f = open(filename, encoding='utf-8')
    lines = f.readlines()
    start_index = 0
    end_index = 0
    for i in range(len(lines)):
        if lines[i].startswith('*** START OF'):
            start_index = i
        if lines[i].startswith('*** END'):
            end_index = i
    valid_lines = lines[start_index:end_index + 1]
    valid_words = []
    for line in valid_lines:
        words_on_line = re.findall("[a-z]+[-'][a-z]+|[a-z]+[']?|[a-z]+", line)
        # print(words_on_line)
        for word in words_on_line:
            valid_words.append(word)

    return valid_words


if __name__ == '__main__':
    filename = 'sample.txt'
    valid_words = get_words_from_file(filename)
    print(filename + ' loaded ok.')
    print('{} valid words found.'.format(len(valid_words)))
    print('Valid words list')
    print('\n'.join(valid_words))
