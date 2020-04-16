# sudoku_solver
This a generic Sudoku solver created in Python programming language.
I've created this project while learning Backtracking Algorithm in python programming language.

## Functions
#### function `print_sudoku(sudoku=listOfLists) `
This function prints a list of lists into a specified sudoku format.

#### function `find_empty(sudoku=listOfLists) `
Returns the tuple of (row, column) of the first empty position it finds.

#### function `check_validity(sudoku=listOfLists, num_to_be_validated=int, position=tuple)`
Checks if the number to be validated is currently valid at the given position by checking in the row, column and the block as per the rules of sudoku.