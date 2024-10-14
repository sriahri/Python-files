from turtle import *
t =Turtle() # Creating a turtle object
r = 100 # radius of the circle
penup() # Not drawing a line
pendown()
t.fillcolor('blue') # Filling a color of face with blue
t.begin_fill()
t.circle(r) # Drawing a circle for face.
t.end_fill()
t.penup()
t.setpos(130,120) # Move the position to the required coordinates
hideturtle()
t.pd()
t.fillcolor('red') # Fill ears with red
t.begin_fill()
t.circle(50) # Draw ears with radius 50
t.end_fill()
t.penup()
t.setpos(-130,120) 
t.pd()
t.fillcolor('red') 
t.begin_fill()
t.circle(50) # Draw another ear
t.end_fill()
t.pu()
t.setpos(-50,100) 
t.pd()
t.fillcolor('red')
t.begin_fill()
t.circle(20) # Draw eye
t.end_fill()
t.pu()
t.setpos(50,100)
t.pd()
t.fillcolor('red')
t.begin_fill()
t.circle(20) # Draw another eye
t.end_fill()
t.hideturtle()
