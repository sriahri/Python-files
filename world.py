class World:
    def __init__(self, num_rows, num_cols):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.x = 0
        self.y = 0

    def playerLocation(self):
        return self.x, self.y

    def numRows(self):
        return self.num_rows

    def numCols(self):
        return self.num_cols

    def moveUp(self):
        if self.y < self.num_rows - 1:
            self.y += 1
            return True
        return False

    def moveDown(self):
        if self.y > 0:
            self.y -= 1
            return True
        return False

    def moveLeft(self):
        if self.x > 0:
            self.x -= 1
            return True
        return False

    def moveRight(self):
        if self.x < self.num_cols - 1:
            self.x += 1
            return True
        return False

    def moveTo(self, x_pos, y_pos):
        if 0 <= x_pos < self.numCols() and 0 <= y_pos < self.numRows():
            self.x = x_pos
            self.y = y_pos
            return True
        return False


number_of_rows = 5
number_of_cols = 4

world = World(number_of_rows, number_of_cols)
print(world.playerLocation())
print(world.numRows())
print(world.numCols())

print(world.moveUp())
print(world.playerLocation())
print(world.moveRight())
print(world.playerLocation())
print(world.moveDown())
print(world.playerLocation())
print(world.moveLeft())
print(world.playerLocation())
print(world.moveTo(3, 4))
print(world.playerLocation())
