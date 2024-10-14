s1 = input('Enter the string 1: ')
s2 = input('Enter the string 2: ')

i = 0
res = []
while i < len(s2):
    if s1 in s2[i:]:
        res.append(i + s2[i:].index(s1))
        i += s2[i:].index(s1) + len(s1) + 1
    else:
        break

s1 = s1[::-1]
i = 0
while i < len(s2):
    if s1 in s2[i:]:
        res.append((i + s2[i:].index(s1)) * -1)
        i += s2[i:].index(s1) + len(s1) + 1
    else:
        break

res.sort()
print(res)

print('After the abs done on the list')
for i in range(len(res)):
    res[i] = abs(res[i])

res.sort()
print(res)
