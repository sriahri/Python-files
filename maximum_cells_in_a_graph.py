def canReach(board, nRows, nCols):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[False] * nCols for _ in range(nRows)]

    def dfs(r, c):
        stack = [(r, c)]
        count = 0
        while stack:
            x, y = stack.pop()
            if 0 <= x < nRows and 0 <= y < nCols and board[x][y] == 'O' and not visited[x][y]:
                visited[x][y] = True
                count += 1
                for dr, dc in directions:
                    nx, ny = x + dr, y + dc
                    if 0 <= nx < nRows and 0 <= ny < nCols and board[nx][ny] == 'O' and not visited[nx][ny]:
                        stack.append((nx, ny))
        return count

    max_nodes = 0
    for r in range(nRows):
        for c in range(nCols):
            if board[r][c] == 'O' and not visited[r][c]:
                max_nodes = max(max_nodes, dfs(r, c))

    print(max_nodes)


def main():
    # Read input dimensions
    S = input().strip().split()
    nRows = int(S[0])
    nCols = int(S[1])

    # Read the board
    board = []
    for _ in range(nRows):
        board.append(input().strip().split())

    # Call canReach function and print the result
    print(canReach(board, nRows, nCols))


if __name__ == "__main__":
    main()
