# Write your solution here
def create_tuple(x: int, y: int, z: int):
  num = [x, y, z]
  tup = (min(num), max(num), sum(num))
  return tup




if __name__ == "__main__":
    print(create_tuple(5, 3, -1))
