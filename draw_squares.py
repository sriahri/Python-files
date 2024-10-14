import turtle


# Draws square at position x, y with side length = width and color.
def squares(x, y, width, color):
    turtle.up()  # To go to the position, lift the pen up
    turtle.goto(x, y)  # Go to the position.
    turtle.down()  # Start drawing
    turtle.pencolor(color)  # Set the color
    turtle.forward(width)  # Move forward for specified width
    turtle.left(90)  # Turn left 90 degrees
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)


if __name__ == '__main__':
    squares(100, 0, 100, "blue")
    squares(-150, -100, 50, "red")
    squares(-200, 170, 75, "green")
    turtle.mainloop()
