N, x = map(int, input().split())
days_in_months = list(map(int, input().split()))


res_days_in_year = []
for day in days_in_months:
    for x in range(1, day + 1):
        res_days_in_year.append(x)

res = 0
for i in range(x):
    res += res_days_in_year[i]

length = len(res_days_in_year)

curr_sum = res
for i in range(x, length):
    curr_sum += abs(res_days_in_year[i] - res_days_in_year[i - x])
    res = max(res, curr_sum)

print(res)
