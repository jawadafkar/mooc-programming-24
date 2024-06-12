# Write your solution here
def who_won(game_board: list):
  p1 = 0
  p2 = 0
  for row in game_board:
    for score in row:
      if score == 1:
        p1 += 1
      elif score == 2:
        p2 += 1
  if p1 > p2:
    return 1
  elif p1 < p2:
    return 2
  else:
    return 0