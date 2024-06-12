# Write your solution here
from datetime import datetime, timedelta
import csv

def cheaters():
  cheaters_list = []
  start_time_file = {}
  end_time_file = {}
  max = timedelta(hours = 3)
  
  with open("start_times.csv") as start_file, open("submissions.csv") as sub_file:
    
    for line in csv.reader(start_file, delimiter = ";"):
      start_time_file[line[0]] = datetime.strptime(line[1], "%H:%M")
  
    for line in csv.reader(sub_file, delimiter = ";"):
      name = line[0]
      time = datetime.strptime(line[3], "%H:%M")
      
      if name not in end_time_file:
        end_time_file[name] = time
      elif time > end_time_file[name]:
        end_time_file[name] = time

    for name in start_time_file:
      if end_time_file[name] - start_time_file[name] > max:
        if name not in cheaters_list:
          cheaters_list.append(name)
  return cheaters_list
        

if __name__ =="__main__":
  print(cheaters())