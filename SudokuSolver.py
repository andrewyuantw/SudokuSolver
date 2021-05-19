import numpy as np

def putNum(col,row,x, puzzle):
    for i in puzzle[row]:
        if i == x:
            return False
    for i in range(9):
        if x == puzzle[i][col]:
            return False
    for i in range(3 * int(col / 3), 3 * int(col/3) + 3):
        for r in range(3 * int(row / 3), 3 * int(row/3) + 3):
            if puzzle[r][i] == x:
                return False
    return True

def sudoku(puzzle):
    
    for x in range(9):
        for y in range(9):
            if puzzle[x][y] ==0:
                numOfFits = 0
                for test in range(1,10):
                    if (putNum(y,x,test,puzzle)):
                        numOfFits += 1
                        correct = test
                if numOfFits == 1:
                    puzzle[x][y] = correct
    for x in range(9):
        for y in range(9):
            if puzzle[x][y] ==0:
                sudoku(puzzle)
    return puzzle

# To use the program, input your Sudoku puzzle into the 9 by 9 array below 

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
