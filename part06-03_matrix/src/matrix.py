# write your solution here

def read_file():
  with open("matrix.txt") as matrix:
    matrix_file = []
    for line in matrix:
      line = line.replace("\n", "")
      line = line.split(",")
      matrix_file.append(line[:])
  return matrix_file


def matrix_sum():
    matrix = read_file()
    sum = 0 
    for row in matrix:
      for number in row:
        sum += int(number)
    return sum
      
def matrix_max():
    matrix = read_file()
    max = 0 
    for row in matrix:
      for number in row:
        if int(number)> max:
          max = int(number)
    return max

def row_sums():
  matrix = read_file()
  row_sum = []
  for row in matrix:
      sum = 0
      for number in row:
        sum += int(number)
      row_sum.append(sum)
  return row_sum

if __name__ == "__main__":
  print(matrix_sum())
  print(matrix_max())
  print(row_sums())

