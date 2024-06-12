# Write your solution here
from fractions import Fraction
def fractionate(amount: int):
  fract_list = []
  i = 0
  while amount > i:
    fract_list.append(Fraction(1, amount))
    i += 1
  return fract_list

if __name__ == "__main__":
  for p in fractionate(3):
    print(p)

  print()

  print(fractionate(5))