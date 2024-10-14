import sys

length = int(input())  # 2
number = int(input())  # 23

if length != len(str(number)):
    print('does not match')
    sys.exit(0)
dialpad = {"2": ['a', 'b', 'c'], "3": ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'],
           '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
number = str(number)

number_of_combinations = 1
for i in str(number):
    number_of_combinations *= len(dialpad[i])

print(number_of_combinations)


def combo(number, current_index, result, length):
    if current_index == length:
        print(''.join(result))
        return
    if number[current_index] == 1 or number[current_index] == 0:
        return
    for i in range(len(dialpad[number[current_index]])):
        result.append(dialpad[number[current_index]][i])
        combo(number, current_index + 1, result, length)
        result.pop()


combo(number, 0, [], length)
