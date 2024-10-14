class Snake:
    snakes_made = 0

    def __init__(self, length):
        self.id = Snake.snakes_made
        Snake.snakes_made += 1
        self.length = length

    def elongate(self, amount=1):
        self.length += amount

    def __str__(self):
        ascii_snake = ""
        for i in range(self.length):
            ascii_snake += '~'
        ascii_snake += '>'
        print(ascii_snake)

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        if self.length == other.length:
            return True


if __name__ == '__main__':
    snake = Snake(2)
    print("The snake 1 id is {}".format(snake.id))
    print("The snake 1 length is {}".format(snake.length))
    snake.elongate(10)
    print("The snake 1 length is {}".format(snake.length))
    snake.__str__()
    snake2 = Snake(4)
    print("The snake 2 length is {}".format(snake2.length))
    print("The snake 2 id is {}".format(snake2.id))
    snake2.__str__()
