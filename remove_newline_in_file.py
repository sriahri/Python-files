if __name__ == '__main__':
    filename = "RandomTextFile.txt"
    file = open(filename, 'r')
    lines = file.readlines()
    result = []
    file.close()
    for i in lines:
        i = i.strip().strip("\n")
        if i is not None and len(i) > 0:
            result.append(i)
    file = open(filename, 'w')
    for i in result:
        file.write(i)

    file.close()