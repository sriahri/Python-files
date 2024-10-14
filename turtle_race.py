import random
import turtle

turtle1 = turtle.Turtle()
turtle1.pencolor("blue")

turtle2 = turtle.Turtle()
turtle2.penup()
turtle2.goto(0, 50)
turtle2.pencolor("green")
turtle2.pendown()

turtle3 = turtle.Turtle()
turtle3.penup()
turtle3.goto(0, -50)
turtle3.pencolor("orange")
turtle3.pendown()

turtle1.speed(1)
turtle2.speed(1)
turtle3.speed(1)

turtle1_progress = 0
turtle2_progress = 0
turtle3_progress = 0

while turtle1_progress < 300 and turtle2_progress < 300 and turtle3_progress < 300:
    forward_distance = random.randint(15, 30)
    turtle1.forward(forward_distance)
    turtle1_progress += forward_distance
    forward_distance = random.randint(15, 30)
    turtle2.forward(forward_distance)
    turtle2_progress += forward_distance
    forward_distance = random.randint(15, 30)
    turtle3.forward(forward_distance)
    turtle3_progress += forward_distance

if turtle1_progress >= 300:
    print("Turtle1 Wins")
elif turtle2_progress >= 300:
    print("Turtle2 Wins")
elif turtle3_progress >= 300:
    print("Turtle3 Wins")
