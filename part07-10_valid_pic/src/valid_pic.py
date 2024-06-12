# Write your solution here
from datetime import datetime
def is_it_valid(pic: str):
  
  check = "0123456789ABCDEFHJKLMNPRSTUVWXY"
  validity = True
  day = pic[:2]
  month = pic[2:4]
  year = pic[4:6]
  id = pic[7:10]
  cntrl_chr = pic[10]
  digits = pic[0:6] + id
  cent_symbol = pic[6]
  
  
  if cent_symbol not in "+-A":
    validity = False
  
  if cent_symbol == "-":
    full_year = "19" + year
  elif cent_symbol == "+":
    full_year = "18" + year
  else:
    full_year = "20" + year
  
  try:
    date = datetime(int(full_year), int(month), int(day))
    print(date)

    if check[ int(digits) % 31] != cntrl_chr:
      validity = False
    elif len(pic) != 11:
      validity = False
  
  except ValueError:
    validity = False
  
  return validity


if __name__ == "__main__":
  print(is_it_valid("290200A1239"))