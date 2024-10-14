s = input()
i = 0
x = len(s)
res = []
while i < x-2:
    r = s[i:i+3]
    if r == r[::-1]:
        if r not in res:
            res.append(r)
    i += 1
for i in range(len(res)):
    if i == len(res)-1:
        print(res[i],end='')
    else:
        print(res[i],end=', ')

# S = input()
# ans = set()
# N = len(S)
# for i in range(2*N - 1):
#     left = i // 2
#     right = left + i % 2
#     while 0 <= left and right < len(S) and S[left] == S[right]:
#         ans.add(S[left: right+1])
#         left -= 1
#         right += 1
# res = list(ans)
# for i in range(len(res)-1,-1,-1):
#     if i == 0 and len(res[i]) == 3:
#         print(res[i],end='')
#     elif len(res) == 3:
#         print(res[i],end=', ')