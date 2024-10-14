text = "gsv yvhg kiltiznh ziv dirggvm hl gszg xlnkfgrmt nzxsrmvh xzm kviulin gsvn jfrxpob. " \
       "zohl, gsv yvhg kiltiznh ziv dirggvm hl gszg sfnzm yvrmth xzm fmwvihgzmw gsvn xovziob. " \
       "z tllw vhhzbrhg zmw z tllw kiltiznnvi szev z olg rm xlnnlm."

words = text.split()
words = [i.strip('\n') for i in words]

converted_words = []
for word in words:
    converted_word = ""
    for character in word:
        if character.isalpha():
            value = ord(character)
            value = abs(value-219)
            converted_character = chr(value)
            converted_word += converted_character
        else:
            converted_word += character
    converted_words.append(converted_word)

for word in converted_words:
    print(word)
print(' '.join(converted_words))
