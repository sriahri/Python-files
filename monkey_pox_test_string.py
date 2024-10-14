def isValidString(s):
    if s:
        if s[0] == 'M':  # If starts with M
            if s[1] != '0':  # Number of tests  != 0
                total = ''
                positive = ''
                negative = ''
                i = 1
                while s[i] != '+' and s[i] != '-':
                    total += s[i]  # find total tests
                    i += 1
                total = int(total)
                if i < len(s) and s[i] == '+':
                    i += 1
                    while i < len(s) and s[i] != '-':
                        positive += s[i]  # positive tests
                        i += 1
                    if len(positive) > 1 and positive[1] == '0':
                        return False
                    if s[i] == '-':
                        i += 1
                        while i < len(s):
                            negative += s[i]  # negative tests
                            i += 1
                    if len(negative) > 1 and negative[1] == '0':
                        return False
                if i < len(s) and s[i] == '-':
                    i += 1
                    while i < len(s) and s[i] != '+':
                        negative += s[i]  # negative tests
                        i += 1
                    if len(negative) > 1 and negative[1] == '0':
                        return False
                    if s[i] == '+':
                        i += 1
                        while i < len(s):
                            positive += s[i]  # positive tests
                            i += 1
                    if len(positive) > 1 and positive[1] == '0':
                        return False
                if positive == '' or not positive.isnumeric():
                    return False
                if negative == '' or not negative.isnumeric():
                    return False
                positive = int(positive)
                negative = int(negative)
                if total == positive + negative:  # total test != positive + negative
                    return True
    return False


if __name__ == '__main__':
    s = 'M1+0-1'
    print('{} is valid: {}'.format(s, isValidString(s)))
    s = 'M5-2+3'
    print('{} is valid: {}'.format(s, isValidString(s)))
    s = 'm1+0-1'
    print('{} is valid: {}'.format(s, isValidString(s)))
    s = 'M1+-1'
    print('{} is valid: {}'.format(s, isValidString(s)))
    s = 'M1+1-'
    print('{} is valid: {}'.format(s, isValidString(s)))
    s = 'M1+0-1k'
    print('{} is valid: {}'.format(s, isValidString(s)))
    s = 'M5+00003-0002'
    print('{} is valid: {}'.format(s, isValidString(s)))
    s = 'M5+0-0'
    print('{} is valid: {}'.format(s, isValidString(s)))
