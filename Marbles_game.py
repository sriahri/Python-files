input1 = int(input())
input2, input3 = map(int, input().split())

numbers = [False for i in range(input1 + 2)]

if input2 <= input1:
    numbers[input2] = True
if input3 <= input1:
    numbers[input3] = True

count = 1
for i in range(min(input2, input3), input1 + 1):
    if numbers[i]:
        if i + input2 < input1:
            numbers[i+input2] = True
        if i + input3 < input1:
            numbers[i + input3] = True

        count += 1


print(count)
