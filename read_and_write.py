def read_user_name():  # Function to read the name
    first_name = input("Enter the first name: ")
    last_name = input("Enter the last name: ")

    return first_name, last_name


def read_scores():  # function to read the scores
    test_score_1 = float(input("Enter the score for test 1: "))
    test_score_2 = float(input("Enter the score for test 2: "))
    test_score_3 = float(input("Enter the score for test 3: "))

    return test_score_1, test_score_2, test_score_3


# Function to compute the average
def compute_average(test_score_1, test_score_2, test_score_3):
    return (test_score_1 + test_score_2 + test_score_3) / 3


# Function to print everything
def print_everything(first_name, last_name, test_score_1, test_score_2, test_score_3):
    print('HI {}'.format(first_name + ' ' + last_name))
    print('Your Score')
    print('test 1: {}'.format(test_score_1))
    print('test 2: {}'.format(test_score_2))
    print('test 3: {}'.format(test_score_3))
    print('Your avg: {}'.format(compute_average(test_score_1, test_score_2, test_score_3)))


# main block of code
if __name__ == '__main__':
    fir_name, las_name = read_user_name()
    te1, te2, te3 = read_scores()
    print_everything(fir_name, las_name, te1, te2, te3)
