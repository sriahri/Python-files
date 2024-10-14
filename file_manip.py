file_name = input()

user_file = open(file_name)
output_list = user_file.readlines()

my_dict = {}
show_list = []
show_list_split = []

# Starting from first item in list, add every other item in list as key
# and every value inbetween is the value associated with the preceeding key
# if one key with multiple values, append list
for index in range(len(output_list)):
    temp_list = []
    list_object = output_list[index].strip("\n").split(':')
    if index + 1 < len(output_list) and (index % 2 == 0):
        int(list_object[0])
        if list_object[0] in my_dict:
            output_list[index + 1].strip("\n")
            my_dict[list_object[0]].append(output_list[index + 1])
        else:
            output_list[index + 1].strip("\n")
            temp_list.append(output_list[index + 1])
            my_dict[list_object[0]] = temp_list

# Sort by keys (years) from least amount of years to greatest amount of years
print(my_dict)
sorted_my_dict = sorted(my_dict)
my_dict_sorted_by_keys = dict(sorted_my_dict)

# Change from dictionary to list
for x in my_dict.keys():
    show_list.append(my_dict[x])

# Split the list of lists into a single list
for x in show_list:
    for i in x:
        show_list_split.append(i)

    # Sort list and output
    show_list_split.sort()

f = open("output_keys.txt", "w")
for key, value in my_dict_sorted_by_keys.items():
    str(key)
    f.write(key + ":")
    for item in value[:-1]:
        f.write(item + ";")
    f.write(value[-1])
    f.write("\n")
f.close()

f2 = open("output_titles.txt", "w")
for item in show_list_split:
    f2.write(item)
f2.close()
