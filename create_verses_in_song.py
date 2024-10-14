verse = """{}, {}, bo-b{}
Banana-fana fo-f{}
Fee-fi-mo-{}
{}!"""

while True:
    name = input('Name to use: ')
    if name.lower() == 'quit':
        print('OK. Goodbye!')
        break
    X = name
    Y = name[1:]
    if name[0] not in ['B', 'F', 'M']:
        third_line = 'm' + Y
    if name[0] in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']:
        Y = X.lower()
        third_line = 'm' + Y
    if name[0] in ['B', 'F', 'M']:
        third_line = Y

    complete_verse = verse.format(X, X, Y, Y, third_line, X)
    print(complete_verse)


