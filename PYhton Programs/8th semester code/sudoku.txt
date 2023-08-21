import numpy as np

# suduku=[]
# print("please use 0 in please of blank spaces.")
# for i in range(4):
#     row = list(input(f"enter the element of row without any spase and comma :"))
#     row = [int(i) for i in row]
#     suduku.append(row)
# print(np.matrix(suduku))
suduku = [[1, 4, 0, 3],
          [0, 0, 4, 0],
          [3, 0, 0, 0],
          [0, 0, 3, 2]]


def possible(row, column, number):
    global suduku

    for i in range(0, 4):
        if suduku[row][i] == number:
            return False

    for i in range(0, 4):
        if suduku[i][column] == number:
            return False

    box_x = (column // 2) * 2
    box_y = (row // 2) * 2
    for i in range(0, 2):
        for j in range(0, 2):
            if suduku[box_y + i][box_x + j] == number:
                return False

    return True


def solve():

    for row in range(0, 4):
        for column in range(0, 4):
            if suduku[row][column] == 0:
                for number in range(1, 5):
                    if possible(row, column, number):
                        suduku[row][column] = number
                        solve()
                        suduku[row][column] = 0

                return

    print(np.matrix(suduku))


solve()
