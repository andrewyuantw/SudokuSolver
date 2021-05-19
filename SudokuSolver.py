import numpy as np

# Checks if a value, x, can be placed in the slot puzzle[row][col]
def putNum(col, row, x, puzzle):

    # Check if x is already in the row
    for i in puzzle[row]:
        if i == x:
            return False

    # Check if x is already in the column
    for i in range(9):
        if x == puzzle[i][col]:
            return False

    # Check if x is in the 3 by 3 mini block
    for i in range(3 * int(col / 3), 3 * int(col/3) + 3):
        for r in range(3 * int(row / 3), 3 * int(row/3) + 3):
            if puzzle[r][i] == x:
                return False

    # If we pass all three tests, then yes, x can be placed in the slot
    return True

# Goes through each slot in the 9 by 9 array, seeing what values can be placed
def sudoku(puzzle):
    for x in range(9):
        for y in range(9):

            # Check if this slot is currently empty
            if puzzle[x][y] == 0:
                numOfFits = 0
                for test in range(1,10):
                    if (putNum(y, x, test, puzzle)):
                        numOfFits += 1
                        correct = test
                # If there is only one possible fit for the slot...
                if numOfFits == 1:
                    puzzle[x][y] = correct

    # Goes through the puzzle to see if there are any empty slots left
    for x in range(9):
        for y in range(9):

            # If there are, we make a recursive call
            if puzzle[x][y] == 0:
                sudoku(puzzle)
    return puzzle

# To use the program, input your Sudoku puzzle into the 9 by 9 array below 
# Be sure to put 0 for empty slots

puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

print(np.matrix(sudoku(puzzle)))
