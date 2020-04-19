import pandas as pd


def get_solved_sudoku(sudoku):
    data_frame = pd.DataFrame(sudoku)
    solve(data_frame)
    print("-------------------------------")
    for row in data_frame.index:
        if row % 3 == 0 and row != 0:
            print("|---------|---------|---------|")

        for col in data_frame.columns:
            if col % 3 == 0 and col != 0:
                print("|", end='')
            if col == 0:
                print("|", end="")
            if col == 8:
                print(" " + str(data_frame.at[row, col]), end=" |\n")
            else:
                print(" " + str(data_frame.at[row, col]) + " ", end='')
    print("-------------------------------")


def find_empty(frame):
    for row in frame.index:
        for col in frame.columns:
            if frame.iat[row, col] == 0:
                return row, col
    return None


def check_validity(frame, num, pos):
    # check column
    for row in frame.index:
        if frame.at[row, pos[1]] == num and pos[1] != row:
            return False

    # check row
    for col in frame.columns:
        if frame.at[pos[0], col] == num and pos[0] != col:
            return False

    # check 3x3 block
    block_of_row = pos[0] // 3
    block_of_col = pos[1] // 3
    block = frame.iloc[block_of_row * 3:block_of_row * 3 + 3, block_of_col * 3:block_of_col * 3 + 3]
    for i in block.index:
        for j in block.columns:
            if block.at[i, j] == num and pos != (i, j):
                return False

    return True


def solve(frame):
    find = find_empty(frame)
    if not find:
        return True
    else:
        row, col = find

    for num in range(1, frame.index.size + 1):
        if check_validity(frame, num, (row, col)):
            frame.iat[row, col] = num

            if solve(frame):
                return True

            frame.iat[row, col] = 0
    return False
