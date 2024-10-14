def altTab(input1, input2, input3):
    x = input3.pop(input2 - 1)
    input3.insert(0, x)
    return input3

input1 = int(input())
input2 = int(input())
input3 = list(map(int, input().split()))
print(altTab(input1, input2, input3))