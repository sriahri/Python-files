import turtle


def draw_circles():
    for i in range(1, 5):
        t.color('red')
        t.begin_fill()
        t.circle(10 * i)
        t.end_fill()
        t.up()
        t.sety((10 * i) * -1)
        t.down()


def draw_square_on_click():
    for i in range(4):
        t.forward(200)
        t.left(90)


def draw_on_drag():
    x = 100
    y = 200
    t.ondrag(None)
    t.setheading(t.towards(x, y))

    turtle.goto(x, y)


t = turtle.Turtle()
t.color('yellow')
turtle.title('Simple Graphics')
draw_circles()
turtle.mainloop()
t.onclick(draw_square_on_click)
t.ondrag(draw_on_drag)
