s, d, res, x, k = input(), {'aaaaa':'A','aaaab':'B','aaaba':'C','aaabb':'D','aabaa':'E','aabab':'F','aabba':'G','aabbb':'H','abaaa':'I','abaab':'J','ababa':'K','ababb':'L','abbaa':'M','abbab':'N','abbba':'O','abbbb':'P','baaaa':'Q','baaab':'R','baaba':'S','baabb':'T','babaa':'U','babab':'V','babba':'W','babbb':'X','bbaaa':'Y','bbaab':'Z'},'','', 0
print(len(s))
for i in s:
    if i.isalpha and i.isupper():
        x += 'a'
    elif i.isalpha and i.islower():
        x += 'b'
while  k < len(x):
    print(x[k:k+5])
    res, k= res + d[x[k:k+5]], k + 5
    print(res)
    #k = k + 5
print(res)