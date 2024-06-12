# Write your solution here
from string import ascii_lowercase, digits
from random import choice, shuffle
def generate_strong_password(length: int, num, sym):
  special_chars = "!?=+-()#"
  combination = ascii_lowercase
  password = []
  password.append(choice(ascii_lowercase))
  pass_str =""
  
  if num and len(password)< length:
    password.append(choice(digits))
    combination += digits
  
  if sym and len(password) < length:
    password.append(choice(special_chars))
    combination += special_chars

  while len(password) < length:
     password.append(choice(combination))
  
  shuffle(password)
  
  for item in password:
    pass_str += item
  return pass_str

if __name__=="__main__":
  for i in range(10):
    print(generate_strong_password(5, False, True))