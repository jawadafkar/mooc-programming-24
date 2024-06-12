# Write your solution here
def sudoku_grid_correct(sudoku: list):
  
  #check rows
  for row in sudoku:
    checked = []
    for number in row:
      if number > 0 and number in checked:
        return False
      checked.append(number)
  
  # Check columns
  for i in range(0, 9):
    checked = []
    for row in sudoku:
      if row[i] > 0 and row[i] in checked:
        return False
      checked.append(row[i])
    checked = []
  
  # Check 3X3 blcoks
  for row in range(0, 9, 3):
    for col in range(0, 9, 3):
      checked = []
      for i in range(row, row + 3):
        for j in range(col, col + 3):
          if sudoku[i][j] in checked and sudoku[i][j] > 0:
              return False
          checked.append(sudoku[i][j])
  return True


if __name__ == "__main__":
  sudoku2 = [
  [2, 6, 7, 8, 3, 9, 5, 0, 4],
  [9, 0, 3, 5, 1, 0, 6, 0, 0],
  [0, 5, 1, 6, 0, 0, 8, 3, 9],
  [5, 1, 9, 0, 4, 6, 3, 2, 8],
  [8, 0, 2, 1, 0, 5, 7, 0, 6],
  [6, 7, 4, 3, 2, 0, 0, 0, 5],
  [0, 0, 0, 4, 5, 7, 2, 6, 3],
  [3, 2, 0, 0, 8, 0, 0, 5, 7],
  [7, 4, 5, 0, 0, 3, 9, 0, 1]
  ]

  print(sudoku_grid_correct(sudoku2))