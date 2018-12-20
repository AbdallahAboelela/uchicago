'''
Abdallah Aboelela
Attempt at Sudoku Solver
Start date: 20 December, 2018
'''

'''
Functions:
1. take inputs and create board
DONE 2. check if row completed (row_complete)
DONE 3. check if column completed
DONE 4. check if box completed
DONE 5. check if board completed (boolean), using 2, 3, 4
6. given square (coordinates), function to check what values are possible based on position 
  if it's empty (maybe use a separate dictionary?)
7. helper that assigns all empty squares the list of possible values using 6
8. Take a grid, a position, and an assigned number, 
  and removes the number from possible options for all other empty slots it conflicts with
9. Recursive function that takes prepared grid (see 7):
  a. Base case: board completed, return board
  b. Recursive case: go through each empty position and if its list of possible numbers is length 1,
    use 8 to adjust board and continue, send finished version back to recursive case.
    
grid e.g.
i j  0  1  2  3  4  5  6  7  8
0  [[8, 7, 6, 0, 1, 0, 3, 9, 2]
1   [0, 2, 9, 0, 7, 0, 0, 5, 0]
2   [4, 0, 5, 2, 9, 0, 7, 0, 8]
3   [7, 4, 1, 5, 6, 0, 0, 0, 3]
4   [5, 0, 2, 0, 0, 4, 0, 6, 1]
5   [0, 0, 3, 1, 0, 0, 0, 0, 0]
6   [0, 1, 0, 0, 0, 0, 2, 4, 0]
7   [0, 5, 4, 0, 0, 8, 0, 3, 7]
8   [2, 9, 0, 0, 4, 1, 6, 8, 0]]
'''

def row_complete(board, num_row):
  row = board[num_row]
  duplicate_checker = {}
  if 0 in row:
    return False
  else:
    for num in range(9):
      if duplicate_checker.get(num, False):
        return False
      else:
        duplicate_checker[num] = True
    
    return True
    
def col_complete(board, num_col):
  col = {}
  for row in board:
    num = row[num_col]
    if num == 0 or col.get(num, False):
      return False
    else:
      col[num] = True
  return True
  
def box_helper(position):
  if position[0] in [1, 4, 7]:
    x = position[0]
  else:
    if position[0] < 3:
      x = 1
    elif position[0] >= 3 and position[0] < 6:
      x = 4
    else:
      x = 7
  if position[1] in [1, 4, 7]:
    y = position[1]
  else:
    if position[1] < 3:
      y = 1
    elif position[1] >= 3 and position[1] < 6:
      y = 4
    else:
      y = 7
  return x, y
  
def box_complete(board, position):
  x, y = box_helper(position)
  duplicate_checker = {}
  for i in range(x-1, x+2):
    for j in range(y-1, y+2):
      num = board[i][j]
      if num == 0 or duplicate_checker.get(num, False):
        return False
      else:
        duplicate_checker[num] = True
  return True
  
BOXES_TO_CHECK = [(1, 1), (1, 4), (1, 7), (4, 1), (4, 4), (4, 7), (7, 1), (7, 4), (7, 7)]
def board_complete(board):
  for num_row in range(9):
    if row_complete(board, num_row):
      pass
    else:
      return False
      
  for num_col in range(9):
    if col_complete(board, num_col):
      pass
    else:
      return False
  
  for box in BOXES_TO_CHECK:
    if box_complete(board, box):
      pass
    else:
      return False
  return True
    

  
''' FOR DEBUGGING PURPOSES

incomplete board = [[8, 7, 6, 0, 1, 0, 3, 9, 2], 
[0, 2, 9, 0, 7, 0, 0, 5, 0], 
[4, 0, 5, 2, 9, 0, 7, 0, 8], 
[7, 4, 1, 5, 6, 0, 0, 0, 3], 
[5, 0, 2, 0, 0, 4, 0, 6, 1], 
[0, 0, 3, 1, 0, 0, 0, 0, 0],
[0, 1, 0, 0, 0, 0, 2, 4, 0],
[0, 5, 4, 0, 0, 8, 0, 3, 7],
[2, 9, 0, 0, 4, 1, 6, 8, 0]]

complete_wo_boxes = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
[2, 3, 4, 5, 6, 7, 8, 9, 1],
[3, 4, 5, 6, 7, 8, 9, 1, 2],
[4, 5, 6, 7, 8, 9, 1, 2, 3],
[5, 6, 7, 8, 9, 1, 2, 3, 4],
[6, 7, 8, 9, 1, 2, 3, 4, 5],
[7, 8, 9, 1, 2, 3, 4, 5, 6],
[8, 9, 1, 2, 3, 4, 5, 6, 7],
[9, 1, 2, 3, 4, 5, 6, 7, 8]]
  
true_box = [[1, 3, 5],[2, 7, 9],[8, 6, 4]]
'''







  
  
