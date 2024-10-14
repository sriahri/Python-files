def update(contactDict, list_of_values):
    error_count = 0
    for value in list_of_values:
        action = value[0]
        name = value[1]
        mail_id = value[2]
        if action == '+':
            if name not in contactDict:
                contactDict[name] = mail_id
            else:
                error_count += 1
        elif action == '/':
            if name in contactDict:
                contactDict[name] = mail_id
            else:
                error_count += 1
        elif action == '-':
            if name in contactDict:
                contactDict.pop(name)
            else:
                error_count += 1
        else:
            error_count += 1
    return contactDict, error_count


if __name__ == '__main__':
    contactDict = {'john': 'john@abc.com', 'steve': 'steve@abc.com', 'danny': 'danny@abc.com'}
    list_of_values = (
        ('+', 'carlos', 'carlos@abc.com'), ('/', 'john', 'john123@abc.com'), ('-', 'danny', 'danny@abc.com'),
        ('@', 'steve', 'steve@abc.com'))
    contactDict, errorCount = update(contactDict, list_of_values)

    print('The updated contact dictionary is ')
    print(contactDict)
    print('The error count is', errorCount)
