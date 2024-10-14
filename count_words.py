def countWords(sentence):
    sentence = sentence.strip()
    sentence = list(sentence)
    for i in range(len(sentence)):
        if not sentence[i].isalpha() and not sentence[i].isdigit() and sentence[i] != ' ':
            sentence[i] = ' '
    sentence = ''.join(sentence)
    words = sentence.split()
    count = 0
    for word in words:
        word = word.strip()
        if word:
            count += 1
    return count


tData = []
tData.append("Simple testing data that contains 8 words only.")
tData.append("""Student Practice - In the empty cell below, write a function countwords(), which count the number of words (not unique) in a sentense provided by the call statement.""")
tData.append("""Student practice - In the empty cell below, write a function countwords (para), which count the  number of words (not unique) in a sentense provided by the call statement.""")
tData.append("""Student Practice:In the empty cell below, write a function countwords(), which count the number of words (not unique) in sentense provided by the call statement.""")
tData.append("""Student Practice - In the empty cell below;write a function countwords(), which count the number of words (not necessary-unique) in a sentense provided by the call statement.""")
oData = [8, 27, 28, 26, 28]

correct = True
print('Testing...', end="")
for idx in range(0, len(tData)):
    print(' {0:n}'.format(idx + 1), end='')
    if countWords(tData[idx]) != oData[idx]:
        correct = False
        break

if correct:
    print('\nCongratulations! Perfect')
else:
    print("\nuhh, not quite right yet!")
