def average_steps(file, number_of_days):
    file.seek(0)
    lines = file.readlines()
    steps = list(map(int, lines))
    return sum(steps[:number_of_days]) / number_of_days


def open_input_file(filename):
    try:
        file = open(filename)
        return file
    except Exception:
        print('File not found')
        return None


def main():
    filename = input('Enter the filename: ')
    file = open_input_file(filename)

    if file:
        prev_avg = 0
        for i in range(12):
            avg = average_steps(file, 30*(i+1))
            total_steps = avg * 30 * (i+1)
            prev_steps = prev_avg * 30 * (i-1)
            print((total_steps - prev_steps)/30)
            prev_avg = avg


main()
