def islandPerimeter(grid):
    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                res += 4
                if i - 1 >= 0 and grid[i - 1][j] == 1:
                    res -= 1
                if j - 1 >= 0 and grid[i][j - 1] == 1:
                    res -= 1
                if i + 1 < len(grid) and grid[i + 1][j] == 1:
                    res -= 1
                if j + 1 < len(grid[0]) and grid[i][j + 1] == 1:
                    res -= 1
    return res

