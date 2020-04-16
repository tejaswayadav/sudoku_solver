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


# Returns the tuple of (row, column) of the first empty position it finds.
def find_empty(sudoku):
    for i_row in range(len(sudoku)):
        for i_col in range(len(sudoku[i_row])):
            if sudoku[i_row][i_col] == 0:
                return i_row, i_col   # row, col

    return None


# Checks if the number to be validated is currently valid at the given position.
def check_validity(sudoku, num_to_be_validated, position):
    # check for num to be validated in the row of position tuple
    for i_col in range(len(sudoku[0])):
        if sudoku[position[0]][i_col] == num_to_be_validated and position[1] != i_col:
            return False

    # check for num to be validated in the column of position tuple
    for i_row in range(len(sudoku)):
        if sudoku[i_row][position[1]] == num_to_be_validated and position[0] != i_row:
            return False

    # check for num to be validated in a 3x3 box of position tuple
    box_row = position[0] // 3
    box_col = position[1] // 3
    for i_row in range(box_row*3, box_row*3 + 3):
        for i_col in range(box_col*3, box_col*3 + 3):
            if sudoku[i_row][i_col] == num_to_be_validated and (i_row, i_col) != position:
                return False

    return True


# Solves sudoku by using above methods
def solve_sudoku(sudoku):
    find = find_empty(sudoku)
    if not find:
        return True
    else:
        row, col = find

    for num_to_be_entered in range(1, 10):
        if check_validity(sudoku, num_to_be_entered, (row, col)):
            sudoku[row][col] = num_to_be_entered

            # checking recursively
            if solve_sudoku(sudoku):
                return True
            sudoku[row][col] = 0
    return False
