def check_if_value_in_range(value, minimum, maximum, error_message):
    if not minimum <= value <= maximum:
        print(error_message)
        exit(1)


def check_if_value_is_binary(value, error_message):
    if not value == 0 or value == 1:
        print(error_message)
        exit(1)


def decide_pass_fail(value, threshold):
    if value >= threshold:
        return 'PASS'
    return 'FAIL'


lab1 = float(input('Enter lab1 marks: '))
msg = 'Value not in the given range'
check_if_value_in_range(lab1, 0, 70, msg)
lab2 = float(input('Enter lab2 marks: '))
check_if_value_in_range(lab2, 0, 50, msg)
lab3 = float(input('Enter lab3 marks: '))
check_if_value_in_range(lab2, 0, 44, msg)
project1 = float(input('Enter project1 marks: '))
check_if_value_in_range(project1, 0, 100, msg)
project2 = float(input('Enter project2 marks: '))
check_if_value_in_range(project2, 0, 120, msg)
marks1 = float(input('Enter mid-semester marks: '))
check_if_value_in_range(marks1, 0, 90, msg)
marks2 = float(input('Enter end-semester marks: '))
check_if_value_in_range(marks2, 0, 120, msg)

final_marks = lab1 * 0.1 / 3 + lab2 * 0.1 / 3 + lab3 * 0.1 / 3 + \
              project1 * 0.15 + project2 * 0.15 + \
              marks1 * 0.25 + marks2 * 0.3
print(decide_pass_fail(final_marks, 50))
