def closestNumbers(array, v):
    start = 0  # shows the start of the window
    length = len(array)
    end = length - 1  # Shows the end of the window
    # Here, we are looking for 5 elements
    # so we need to get the window of length 5.
    while end - start >= 5:
        # If the left left element in the window is closer
        # then we need to move the window to left by 1.
        if abs(array[start] - v) > abs(array[end] - v):
            start += 1
        # If the right element in the window is closer
        # then we need to move the window to right by 1.
        else:
            end -= 1
    return array[start:end + 1]


print(closestNumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 7))
