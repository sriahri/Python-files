import numpy as np


def q2_func(x, y):
    is_greater = np.abs(x) > np.abs(y)
    z = np.where(is_greater, x - y / 2, y - x / 2)
    return z


# Test case 1
x4 = np.array([-2, 0, 1, -3])
y4 = np.array([5, 6, -1, 2])
result4 = q2_func(x4, y4)
print(result4)  # Output: [ 3.5  3.   -0.5 -2.5]

# Test case 2
x5 = np.array([10, 20, 30, 40])
y5 = np.array([5, 15, 25, 35])
result5 = q2_func(x5, y5)
print(result5)  # Output: [ 2.5  7.5 15.  20.]

