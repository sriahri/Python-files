def breaktime(n, mat):
    new = [i for i in mat]

    new.sort(key=lambda x: x[0])
    res = []
    end = new[0][1]

    for i in new[1:]:
        if end < i[0]:
            res.append([end, i[0]])
        end = max(end, i[1])
    return res


n  = int(input())

schedule = []
for i in  range(n):
    schedule.append(list(map(int, input().split())))
