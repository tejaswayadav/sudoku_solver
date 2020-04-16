from SudokuSolver import *

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


test_sudoku_alt = [
    [0, 0, 9, 8, 0, 0, 0, 0, 0],
    [5, 0, 0, 6, 0, 0, 2, 0, 0],
    [6, 0, 0, 1, 0, 3, 0, 7, 0],
    [0, 4, 0, 3, 0, 0, 0, 9, 0],
    [0, 0, 8, 0, 7, 0, 1, 0, 0],
    [0, 5, 0, 0, 0, 2, 0, 3, 0],
    [0, 1, 0, 2, 0, 4, 0, 0, 5],
    [0, 0, 2, 0, 0, 1, 0, 0, 3],
    [0, 0, 0, 0, 0, 8, 6, 0, 0]
]

# print_sudoku(test_sudoku)
# print(find_empty(test_sudoku))
# print(check_validity(test_sudoku, 6, find_empty(test_sudoku)))

print_sudoku(test_sudoku_alt)
print("---------------------------------------")
solve_sudoku(test_sudoku_alt)
print("---------------------------------------")
print_sudoku(test_sudoku_alt)

