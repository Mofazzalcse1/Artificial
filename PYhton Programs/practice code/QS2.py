import numpy as np

grid = [[1, 4, 0, 3],
        [0, 0, 4, 0],
        [3, 0, 0, 0],
        [0, 0, 3, 2]]


def possible(row, column, number):
    global grid

    for i in range(0, 4):
        if grid[row][i] == number:
            return False

    for i in range(0, 4):
        if grid[i][column] == number:
            return False

    x0 = (column // 2) * 2
    y0 = (row // 2) * 2
    for i in range(0, 2):
        for j in range(0, 2):
            if grid[y0 + i][x0 + j] == number:
                return False

    return True


def solve():
    global grid
    for row in range(0, 4):
        for column in range(0, 4):
            if grid[row][column] == 0:
                for number in range(1, 5):
                    if possible(row, column, number):
                        grid[row][column] = number
                        solve()
                        grid[row][column] = 0

                return

    print(np.matrix(grid))


solve()
