# Write your solution here
from datetime import datetime, timedelta
file_name = input("Filename: ")
start_date = input("Starting date: ")
day_amount = int(input("How many days: "))
date = datetime.strptime(start_date, "%d.%m.%Y")
end_date = date + timedelta(days = day_amount - 1)
list_hours = {}

print("Please type in screen time in minutes on each day (TV computer mobile):")

with open(file_name, "w") as file:
  
  
  file.write(f"Time period: {date.strftime("%d.%m.%Y")}-{end_date.strftime("%d.%m.%Y")}\n")
  for i in range(day_amount):
    d = date + timedelta(days = i)
    hours = input(f"Screen time {d.strftime("%d.%m.%Y")}: ")
    list_hours[f"{d.strftime("%d.%m.%Y")}"] = hours.split()
  
  total = 0
  for date, h in list_hours.items():
    for i in range(len(h)):
      total += int(h[i])

  avg = total/day_amount

  
  file.write(f"Total minutes: {total}\n")
  file.write(f"Average minutes: {avg}\n")
  for date, hour in list_hours.items():
    file.write(f"{date}: {hour[0]}/{hour[1]}/{hour[2]}\n")
