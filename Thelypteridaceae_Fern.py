import turtle
import random

pen = turtle.Turtle()
pen.speed(100000000000)
pen.color("green")
pen.penup()

x = 0
y = 0
for n in range(110000):
    pen.goto(65 * x, 37 * y - 252)  # 37 is to scale the fern and -252 is to start the drawing from the bottom.
    pen.pendown()
    pen.dot()
    pen.penup()
    r = random.random()  # to get probability
    r = r * 100
    xn = x
    yn = y
    if r < 2:  # elif ladder based on the probability
        x = 0
        y = 0.25 * yn - 0.4
    elif r < 85:
        x = 0.95*xn + 0.005*yn - 0.002
        y = -0.005*xn + 0.93*yn + 0.5
    elif r < 93:
        x = 0.035*xn - 0.2*yn - 0.09
        y = 0.16*xn + 0.04*yn + 0.02
    else:
        x = -0.04*xn + 0.2*yn + 0.083
        y = 0.16*xn + 0.04*yn + 0.12
