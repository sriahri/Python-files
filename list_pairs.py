def pairs(input_list):
    n = len(input_list)
    output_list = []
    if n < 2:
        return []
    for i in range(n-1):
        output_list.append([input_list[i], input_list[i+1]])
    return output_list


print(pairs(['a', 'b', 'c']))
print(pairs(['a', 'b']))
print(pairs(['a']))
print(pairs([]))
print(pairs([1, 'a', ['b', 2]]))
