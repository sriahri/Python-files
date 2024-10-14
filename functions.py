def constant_function(a):
    return a + 10


def linear_function(numbers):
    result = 0
    for i in range(len(numbers)):
        result += numbers[i]

    return result


def quadratic_function(numbers):
    result = 0
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            result += numbers[i] + numbers[j]

    return result
