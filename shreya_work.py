w = int(input())
n = int(input())

work_pending = list(map(int, input().split()))

difference = list()

for i in work_pending:
    difference.append(w-i)

difference.sort(reverse=True)
shreya_help = 0
result = -1
for i in range(len(difference)):
    shreya_help += difference[i]
    if shreya_help >= w:
        result = i+1
        break
print(result)
