import os.path


def main():
    filename = "students.txt"
    abs_file_path = os.path.abspath(filename)
    dir_name = os.path.dirname(abs_file_path)

    print()
    print()
    print("Absolute Path : ", abs_file_path)
    print('Directory : ', dir_name)
    print('Base Name : ', os.path.basename(abs_file_path))

    print('File Size : ', os.path.getsize(filename))
    print('Is File? : ', os.path.isfile(filename))
    print('Is Directory? : ', os.path.isdir(filename))

    file = open(filename)
    lines = file.readlines()
    students = []
    for i in lines:
        students.append(i.split())

    for i in students:
        print('name : {}'.format(i[0]))
        print('Age: {}'.format(i[1]))
        marks = list(map(int, i[2:]))
        print('Average : {}'.format(sum(marks) / len(marks)))
        print()
        print()


if __name__ == '__main__':
    main()
