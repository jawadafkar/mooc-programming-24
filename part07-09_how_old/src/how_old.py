# Write your solution here
from datetime import datetime

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

birth_date = datetime(year, month, day)
new_millennium_date = datetime(1999, 12, 31)
if new_millennium_date > birth_date:
  date = new_millennium_date - birth_date
  print(f"You were {date.days} days old on the eve of the new millennium.")
else:
  print("You weren't born yet on the eve of the new millennium.")