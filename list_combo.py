list1 = ['This is', 5, 'and it is bigger than', 2.8]  # The actual list given

# Loop through the list and convert all the elements to string
for i in range(len(list1)):
    list1[i] = str(list1[i])

# Join all the elements of the list separated by space
result = ' '.join(list1)
print(result)  # Print the result
new_list = [result, "but smaller than 10"]  # Create a new list with the required contents
final_result = ', '.join(new_list)  # Join the list separated by ,.
print(final_result)  # Print the result

# Open the file and write the contents to it.
file = open("Result.txt", 'w')
file.write(final_result)
file.close()

# Open the file and read the contents of it.
file = open("Result.txt")
lines = file.readlines()

print(lines)  # Print the contents of the file.
