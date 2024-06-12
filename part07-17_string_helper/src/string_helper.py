# Write your solution here
from string import ascii_letters, whitespace, digits

def change_case(orig_string: str):
  new_string = "" 
  for char in orig_string:  
    if char.islower() or char in whitespace:
      new_string += char.upper()
    elif char.isupper() or char in whitespace:
      new_string += char.lower()
    else:
      new_string += char

  return new_string

def split_in_half(orig_string: str):
  half = len(orig_string) // 2
  p1 = orig_string[:half]
  p2 = orig_string[half:]
  
  return p1, p2

def remove_special_characters(orig_string: str):
  allowed = ascii_letters + digits + whitespace
  new_str = ""
  for char in orig_string:
    if char in allowed:
      new_str += char
    
  return new_str

