import numpy as np


def solve_equation(A, b):
    print(np.linalg.solve(A, b))


if __name__ == '__main__':
    A = np.array([[-3, -1], [4, 1]])
    b = np.array([1, 3])

    solve_equation(A, b)

    A = np.array([[1, -2], [7, -3]])
    b = np.array([-2, 19])
    solve_equation(A, b)
