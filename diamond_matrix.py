import numpy as np


def create_diamond_matrix(size):
    # Create an empty matrix filled with zeros
    matrix = np.zeros((size, size), dtype=int)

    if size % 2 != 0:
        # Fill the upper half of the matrix
        for i in range(size // 2):
            matrix[i, size // 2 - i: size // 2 + i + 1] = 1

        # Fill the lower half of the matrix
        for i in range(size // 2, size):
            matrix[i, i - size // 2: size - (i - size // 2)] = 1

    else:
        # Fill the upper half of the matrix
        for i in range(size // 2):
            matrix[i, (size // 2 - i) - 1: size // 2 + (i + 1)] = 1

        # Fill the lower half of the matrix
        for i in range(size // 2, size):
            matrix[i, i - size // 2: size - (i - size // 2)] = 1
    return matrix


# Set the size of the diamond matrix
matrix_size = 8

# Create the diamond matrix
diamond_matrix = create_diamond_matrix(matrix_size)

# Print the resulting matrix
print(diamond_matrix)
