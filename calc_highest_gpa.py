if __name__ == '__main__':
    filename = input("Enter the file name: ")
    file = open(filename, 'r')
    lines = file.readlines()
    gpa_max = 0
    res_name = None
    for line in lines:
        gpa, name = line.split("\t")
        if float(gpa) > gpa_max:
            gpa_max = float(gpa)
            res_name = name

    print("The valedictorian is:{}".format(res_name))
