# Write your solution here

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

def add_number(sudoku: list, row_no: int, column_no: int, number:int):
  sudoku[row_no][column_no] = number



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

  print_sudoku(sudoku)
  add_number(sudoku, 0, 0, 2)
  add_number(sudoku, 1, 2, 7)
  add_number(sudoku, 5, 7, 3)
  print()
  print("Three numbers added:")
  print()
  print_sudoku(sudoku)