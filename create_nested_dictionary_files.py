main_dict = {'CS': [{'1101': ['ahmad m', 'ahmandm@abc.com', '500']}, {'1102': ['yousef z', 'yousefz@abc.com', '580']}],
             'SWE': [{'2101': ['sara w', 'saraw@abc.com', '450']}, {'2102': ['ahmad x', 'ahmandx@abc.com', '600']}]}


def create_file(dictionary):
    file = open('empInfo.txt', 'w')
    file.write('Dept,Id,Name,Email,Salary\n')
    for i in dictionary.keys():
        item = main_dict[i]
        for j in item:
            for k in j.keys():
                file.write(i + ',' + k + ',' + j[k][0] + ',' + j[k][1] + ',' + j[k][2] + '\n')
    file.close()


def update_file(extra_record):
    file = open('empInfo.txt', 'a')
    for i in extra_record.keys():
        for item in extra_record[i].keys():
            file.write(i + ',' + item + ',' + extra_record[i][item][0] + ',' + extra_record[i][item][1] + ',' +
                       extra_record[i][item][2] + '\n')
    file.close()


def read_from_file():
    file = open('empInfo.txt', 'r')
    lines = file.readlines()
    for i in lines:
        x = i.split(',')
        for item in x:
            print(item, end='\t')


if __name__ == '__main__':
    create_file(main_dict)
    inp = {'CS': {'1103': ['khaled e', 'khalede@abc.com', '630']}}
    update_file(inp)
    read_from_file()
