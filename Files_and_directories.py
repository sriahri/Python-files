import os

path = input("Enter the path: ")
if os.path.exists(path):
    list_of_files = os.listdir(path)
    number_of_files_and_folders = len(list_of_files)
    number_of_folders = 0
    number_of_files = 0
    for each in list_of_files:
        a = path + '/' + str(each)
        if os.path.isdir(a):
            number_of_folders += 1
        elif os.path.isfile(a):
            number_of_files += 1
    print("{} files and folders. {} folder(s). {} file(s)".format(number_of_files_and_folders, number_of_folders,
                                                                  number_of_files))

else:
    print("No such path found")
