def update_board(position, value, board):
    x, y = position[0], position[1]
    if not board[x][y]:
        board[x][y] = value


board_three = [
    [6, 8, 5, 1, 3, 2, 9, 4, 7],
    [7, 3, 4, 5, 9, 8, 2, 1, 6],
    [2, 1, 9, 7, 6, 4, 8, 5, 3],
    [9, 2, 6, 8, 7, 1, 5, 3, 4],
    [8, 5, 1, 3, 4, 9, 6, 7, 2],
    [4, 7, 3, 2, 5, 6, 1, 8, 9],
    [5, 6, 8, 4, 2, 7, 3, 9, 1],
    [3, 4, 2, 9, 1, 5, 7, 6, 8],
    [1, 9, 7, 6, 8, 3, 4, 2, None]
]
update_board((8, 8), 5, board_three)

for i in board_three:
    print(i)
