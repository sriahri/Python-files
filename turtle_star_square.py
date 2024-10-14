from turtle import * # Missing line 1
pencolor('black')
setpos(-100,-50)
st()
clear()
for times in range(4): # Loop 1
    for section in range(5): # Loop 2
        forward(40)
        left(144)
    penup()
    forward(40)
    left(90)
    forward(60)
    right(90)
    pendown() # Missing Line 2
    for section in range(4): # Loop 3
        forward(40) # Missing Line 3
        left(90)    # Missing Line 4
    penup() # Missing Line 5
    right(45)
    forward(60)
    pendown()
ht()
