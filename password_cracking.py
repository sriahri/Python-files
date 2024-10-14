for _ in range(int(input())):
    s = input().upper()
    d = {'A':1, 'E':1, 'I':1, 'O':1, 'U':1}
    res = ''
    for i in s:
        if i not in d:
            res += '*'+i.lower()
    print(res)