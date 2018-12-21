'''
Abdallah Aboelela
Attempt at Sudoku Solver
Start date: 20 December, 2018

TO DOs:
1. take inputs and create board
DONE 2. check if row completed (row_complete)
DONE 3. check if column completed
DONE 4. check if box completed
DONE 5. check if board completed (boolean), using 2, 3, 4
DONE 6. given square (coordinates), function to check what values are possible based on position 
        if it's empty (maybe use a separate dictionary?)
7. helper that assigns all empty squares the set of possible values using 6
8. Take a board, a position, and an assigned number, 
  and removes the number from possible options for all other empty slots it conflicts with
9. Recursive function that takes prepared board (see 7):
  a. Base case: board completed, return board
  b. Recursive case: go through each empty position and if its list of possible numbers is length 1,
    use 8 to adjust board and continue, send finished version back to recursive case.
    
unsolved board e.g.
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

# The center position indexes of each box
BOXES_TO_CHECK = [(1, 1), (1, 4), (1, 7), (4, 1), (4, 4), (4, 7), (7, 1), (7, 4), (7, 7)]

def row_complete(board, num_row):
  ''' Checks if a row has been completed correctly
  Inputs:
    board: (list of lists of ints) the sudoku board
    num_row: (int) the row index
  Returns: (bool) True if the row has been completed correctly, 
            false otherwise
  '''
  row = board[num_row]
  duplicate_checker = {}
  if 0 in row:
    return False
  else:
    for num in range(9):
      if duplicate_checker.get(num, False) or type(num) == set:
        return False
      else:
        duplicate_checker[num] = True
    
    return True
    
def col_complete(board, num_col):
  ''' Checks if a column has been completed correctly
  Inputs:
    board: (list of lists of ints) the sudoku board
    num_col: (int) the column index
  Returns: (bool) True if the row has been completed correctly, 
            false otherwise
  '''
  col = {}
  for row in board:
    num = row[num_col]
    if num == 0 or col.get(num, False) or type(num) == set:
      return False
    else:
      col[num] = True
  return True
  
def box_helper(position):
  ''' Returns the index of the center position in a box
  Inputs:
    position: (tuple of ints) the row and col indexes of the position
  Returns: (tuple of ints) the row and col indexes of the center position
            of the box which the original position is a part of
  '''
  if position[0] < 3:
    x = 1
  elif position[0] >= 3 and position[0] < 6:
    x = 4
  else:
    x = 7
    
  if position[1] < 3:
    y = 1
  elif position[1] >= 3 and position[1] < 6:
    y = 4
  else:
    y = 7
  return x, y
  
def box_complete(board, position):
  ''' Checks if a box has been completed correctly
  Inputs:
    board: (list of lists of ints) the sudoku board
    position: (tuple of ints) the row and col indexes of the position
  Returns: (bool) True if the box has been completed correctly, 
            false otherwise
  '''
  x, y = box_helper(position)
  duplicate_checker = {}
  for i in range(x-1, x+2):
    for j in range(y-1, y+2):
      num = board[i][j]
      if num == 0 or duplicate_checker.get(num, False) or type(num) == set:
        return False
      else:
        duplicate_checker[num] = True
  return True
  
def board_complete(board):
  ''' Checks if the board has been completed correctly
  Inputs:
    board: (list of lists of ints) the sudoku board
  Returns: (bool) True if the board has been completed correctly, 
            false otherwise
  '''
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
  
def possible_values_at_position(board, position):
  ''' Returns a set of the possible values for a given position
  *Assumes the position is empty (0) and the row, col, and box the position
    is associated with only contain ints
  Inputs:
    board: (list of lists of ints) the sudoku board
    position: (tuple of ints) the row and col indexes of the position
  Returns: (set) integers that would be possible at this position
  '''
  assert(board[position[0]][position[1]] == 0)
  
  not_possible_values = board[position[0]][:]
  
  col = []
  for i in range(9):
    col.append(board[i][position[1]])
  not_possible_values += col
    
  box = []
  x, y = box_helper(position)
  for i in range(x-1, x+2):
    for j in range(y-1, y+2):
      box.append(board[i][j])
  not_possible_values += box
  
  not_possible_values = set(not_possible_values)
  
  return set(range(1, 10)) - not_possible_values

def starter(board):
  ''' Initializes the board, by replaicng empty positions with the appropriate
  sets from the function possible_values_at_position
  Inputs:
    board: (list of lists of ints) the sudoku board
  Returns: None
  
  THE ISSUE IS HERE, THE COPY PART DOESN'T WORK AS EXPECTED
  '''
  copy = board[:] # WHY ISN'T THIS COPYING CORRECTLY
  for i in range(9):
    for j in range(9):
      if copy[i][j] == 0:
        print(i, j)
        print(copy)
        board[i][j] = possible_values_at_position(copy, (i, j))
        print("exited pvap call")
  return None
  



# Everything below is for debugging purposes
  
def zeros(board):
  l = []
  for i in range(9):
    for j in range(9):
      if board[i][j] == 0:
        l.append((i, j))
  return l

def temp(board):
  l = zeros(board)
  for pos in l:
    print(possible_values_at_position(board, pos))

incomplete_board = [[8, 7, 6, 0, 1, 0, 3, 9, 2],
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
