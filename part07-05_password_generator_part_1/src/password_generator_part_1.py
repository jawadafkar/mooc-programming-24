# Write your solution here
from string import *
from random import *
def generate_password(length: int):
  password = ""
  while len(password) < length:
    password += choice(ascii_lowercase)
  return password

if __name__=="__main__":
  for i in range(10):
    print(generate_password(8))

