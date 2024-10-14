Board_List = ["Thursday Night Soccer Match", "Calculus Tutoring Wednesday Through Friday", "Join The Arrow Club",
              "Help Wanted At The Student Union", "Trivia Night"]

print(Board_List)

list_1 = ["Hello", "World"]
list_2 = ["Hey", "John"]
list_3 = ["what", "shall", "we", "do"]

master_list_1 = [list_1, list_1, list_1, list_2, list_2, list_2, list_3, list_3, list_3]
print(master_list_1)
master_list_2 = [list_1, list_2, list_3, list_1, list_2, list_3, list_1, list_2, list_3]
print(master_list_2)

master_list_3 = master_list_1.copy()
print(master_list_3)
master_list_3.sort()
print(master_list_3)
