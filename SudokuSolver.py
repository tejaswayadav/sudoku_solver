test_sudoku = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


# This function prints above list of lists in a sudoku format.
def print_sudoku(sudoku):
    for i_row in range(len(sudoku)):
        if i_row % 3 == 0 and i_row != 0:
            print("---------|---------|---------")

        for i_col in range(len(sudoku[i_row])):
            if i_col % 3 == 0 and i_col != 0:
                print("|", end='')
            if i_col == 8:
                print(" " + str(sudoku[i_row][i_col]))
            else:
                print(" " + str(sudoku[i_row][i_col]) + " ", end='')
