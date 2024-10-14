def pyramid(n):
    """
    Creates a pyramid with n layers

    Parameters:
        n (int): The number of layers in the pyramid.

    Returns:
        xp (list): List of x-coordinates of points forming the pyramid.
        yp (list): List of y-coordinates of points forming the pyramid.
    """
    xp = []  # List to store x-coordinates
    yp = []  # List to store y-coordinates

    for i in range(n):
        # Calculate the width of the current layer
        width = 2 * (n-i) - 1

        # Calculate the starting x-coordinate for the current layer
        start_x = -(width - 1) / 2
        layer_x = [start_x, start_x + width - 1, start_x + width - 1, start_x]
        layer_y = [i, i, i + 1, i + 1]
        # Append the x and y coordinates for the current layer
        for j in range(width):

            xp.append(start_x + j)
            yp.append(i)

    return xp, yp


# Main program (do not change)

import matplotlib.pyplot as plt

xp, yp = pyramid(15)
plt.axis("equal")
plt.grid()
plt.plot(xp, yp, color="gold", lw=5)
plt.show()
