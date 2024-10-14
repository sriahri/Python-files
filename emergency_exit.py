def emergency_exit(points):
    minimum = points[0]
    maximum = points[0]
    n = len(points)
    for i in range(n):
        if points[i] > maximum:
            maximum = points[i]
        if points[i] < minimum:
            minimum = points[i]

    average = (maximum + minimum) / 2
    left_points = 0
    right_points = 0
    for i in range(n):
        if points[i] < average:
            left_points += 1
        else:
            right_points += 1

    if (maximum + minimum) % 2 == 0:
        average = int((maximum + minimum / 2))
    elif left_points > right_points:
        average = int(average)
    else:
        average = int(average) + 1
    return average


if __name__ == '__main__':
    points = [2, 16, 8, 19, 5, 12]
    print('The emergency exit will be located at', emergency_exit(points))
