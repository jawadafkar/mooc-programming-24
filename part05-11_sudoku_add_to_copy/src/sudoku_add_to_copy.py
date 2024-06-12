# Write your solution here
def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
  sudoku_copy = []
  for row in sudoku:
    sudoku_copy.append(row[:])
  sudoku_copy[row_no][column_no] = number
  return sudoku_copy


def print_sudoku(sudoku: list):

  for row in range(9):
    for col in range(9):

      if col == 3 or col == 6:
        print(" ", end = "")
      
      if sudoku[row][col] == 0:
        print("_", end = " ")
      else:
        print(sudoku[row][col], end = " ")
    
    print()
    if row == 2 or row == 5:
      print()



if __name__ == "__main__":
  sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
  ]

  grid_copy = copy_and_add(sudoku, 0, 0, 2)
  print("Original:")
  print_sudoku(sudoku)
  print()
  print("Copy:")
  print_sudoku(grid_copy)