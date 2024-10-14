input1 = int(input())
input2 = int(input())
input3 = int(input())
input4 = list(map(int, input().split()))

input4.sort(reverse=True)
new_items = input4.copy()
buy = []
print(new_items)
print(input2)
for i in range(input1):
    print(new_items[i])
    if input2 >= new_items[i]:
        buy.append(input4[i])
        print(buy)
        input2 -= new_items[i]
        new_items = [j*2 for j in new_items]

print(buy)
total = sum(buy)
print(total)
print(total * (2**input3))
