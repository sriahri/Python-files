s = input()
res = ord(s[0])
for i in s[1:]:
    res = res ^ ord(i)
print(res)