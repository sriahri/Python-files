from graphics import *


def main():
    win = GraphWin("My window", 300, 300)
    input_box = Entry(Point(50, 30), 8)
    input_box.draw(win)
    win.getMouse()
    word = input_box.getText()
    msg = Text(Point(25, 50), word)
    msg.setFill("red")
    msg.draw(win)
    win.getMouse()
    win.close()


main()
