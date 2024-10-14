import turtle # Import the turtle module. It enables to create pictures.
turtle.shape('circle') # Used to set the turtle shape as circle.
xdir = 1 # Initialize the value of xdir to -1
ydir = 1 # Initialize the value of ydir to -1
x = 1    # Initialize the value of x to -1
y = 1    # Initialize the value of y to -1
wn = turtle.Screen() # Returns a singleton object of a turtleScreen subclass.
wn.bgcolor('pink') # Set the background color as pink.
t = turtle.Turtle() # Creating turtle object.
l = int(input('Enter the length of rectangle: ')) # Taking input the length of the rectangle
b = int(input('Enter the width of rectangle: '))  # Taking input the breadth of the rectangle
# Drawing the rectangle
t.forward(l) # Move forward by l units
t.left(90)   # Rotate left by 90 degrees
t.forward(b) # Move forward by b units
t.left(90)   # Rotate left by 90 degrees
t.forward(l) # Move forward by l units
t.left(90)   # Rotate left by 90 degrees
t.forward(b) # Move forward by b units
t.left(90)   # Rotate left by 90 degrees
while True:  # While loop for repeating the steps continuously.
    turtle.penup()
    x = x + 3 * xdir # Increment the value of x by 3 * xdir
    y = y + 3 * ydir # Increment the value of y by 3 * ydir
    turtle.goto(x+turtle.window_width()/2 , y + turtle.window_height()/2) # Move the turtle to the absolute position.
    # If the circle hits any of the boundary of the rectangle, it stops moving and the game stops.
    if (x >= 0 and x <= l) or (y >= 0 and y <= b):
        break
    if x >= turtle.window_width()/2: # Check whether x >= window_width / 2
        xdir = -1 # Assign the value of xdir to -1
    if x <= -turtle.window_width()/2:# Check whether x <= -window_width / 2
        xdir = 1  # Assign the value of xdir to 1
    if y >= turtle.window_height()/2:# Check whether y >= window_height / 2
        ydir = -1  # Assign the value of ydir to -1
    if y <= -turtle.window_height()/2:# Check whether y <= -window_height / 2
        ydir = 1   # Assign the value of ydir to 1
    #turtle.Terminator
turtle.mainloop()
