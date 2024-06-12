# Write your solution here
from random import choice
def roll(die: str):
  A = [3, 3, 3, 3, 3, 6]
  B = [2, 2, 2, 5, 5, 5]
  C = [1, 4, 4, 4, 4, 4]
  if die == "A":
    return choice(A)
  elif die == "B":
    return choice(B)
  elif die == "C":
    return choice(C)

def play(die1: str, die2: str, times: int):
  d1_win = 0
  d2_win = 0
  draw = 0
  
  for i in range(times):
    d1 = roll(die1)
    d2 = roll(die2)
    if d1 > d2:
      d1_win += 1
    elif d1 < d2:
      d2_win += 1
    elif d1 == d2:
      draw += 1
  
  return (d1_win, d2_win, draw)

if __name__ == "__main__":
  result = play("A", "C", 1000)
  print(result)
  result = play("B", "B", 1000)
  print(result)
