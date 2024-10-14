def enc(string):
    l = list(string)
    l.sort(reverse=True)
    print(l)
    result = ''
    for i in l:
        if i == 's':
            result += '1'
        elif i == 'x':
            result += '9'
        elif i == 't':
            result += '13'
        elif i == 'h':
            result += '50'
        else:
            result += i
    result = 'bot' + result
    return result


if __name__ == '__main__':
    result = enc("hives")
    print(result)
    assert result == "botv1i50e"
