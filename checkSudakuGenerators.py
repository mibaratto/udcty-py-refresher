# Exercise 2: Check Sudoku
# Sudoku is a logic puzzle where a game is defined by a partially filled 9 x 9 square of digits where each square contains one of the digits 1, 2, 3, 4, 5, 6, 7, 8, 9. For this question we will generalize and simplify the game.

# Your task is to check sudoku squares for correctness.

# To do this, you will define a function, check_sudoku, that takes as input a square list of lists representing an n x n sudoku puzzle solution and returns the boolean True if the input is a valid sudoku square and returns the boolean False otherwise.

# A valid sudoku square satisfies these two properties:

# Each column of the square contains each of the whole numbers from 1 to n exactly once.

# Each row of the square contains each of the whole numbers from 1 to n exactly once.

# You may assume that the input is square and contains at least one row and column.


# Define a function check_sudoku() here:
def check_sudoku(square):
    return None
    
# Test cases
correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]
incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]
incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]
incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]
incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]
incorrect5 = [ [1, 1.5],
               [1.5, 1]]

    
print(check_sudoku(incorrect))
#>>> False
print(check_sudoku(correct))
#>>> True
print(check_sudoku(incorrect2))
#>>> False
print(check_sudoku(incorrect3))
#>>> False
print(check_sudoku(incorrect4))
#>>> False
print(check_sudoku(incorrect5))
#>>> False