# Write your solution here
from random import randint
def lottery_numbers(amount: int, lower: int, upper: int):
  number_pool = []
  while len(number_pool) < amount:
    number = randint(lower, upper)
    if number not in number_pool:
      number_pool.append(number)
    number_pool.sort()
  return number_pool


if __name__=="__main__":
  print(lottery_numbers(7, 1, 40))
