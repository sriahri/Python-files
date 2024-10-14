import turtle
colors = ['green', 'blue', 'red', 'yellow']
length = 200
count = 0
while count < 4:
    side = 0
    turtle.color(colors[count])
    turtle.begin_fill()
    while side < 4:
        turtle.forward((4-count) * 50)
        turtle.left(90)
        side = side + 1
        turtle.write(colors[count], font=('Arial', 16, "bold"))
    turtle.end_fill()
    count = count + 1
turtle.done()
