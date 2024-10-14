l = list(map(int,input().split()))
s = [l[0]]
x = l[0]
for i in range(1, len(l)):
    if i%2 == 0:
        x += l[i]
    else:
        x -= l[i]
    s.append(x)
ind = s.index(max(s))
# print(s[:ind])
# print(ind)
for i in range(len(s[:ind])):
    print(' '*s[i], end = '')
print('o')
for i in range(len(s[:ind-1])):
    print(' '*(s[i]), end="")
print((s[ind-1] - 1)*' ', end="")
print('/|\\')
for i in range(len(s[:ind-1])):
    print(' '*(s[i]), end="")
print((s[ind-1] - 1)*' ', end="")
print('< >')
