# Write your solution here
# Write your solution here
from datetime import datetime, timedelta
import csv

def final_points():

  start_time_file = {}
  end_time_file = {}
  list = {}
  max = timedelta(hours = 3)
  final = {}
  
  with open("start_times.csv") as start_file, open("submissions.csv") as sub_file:
    
    for line in csv.reader(start_file, delimiter = ";"):
      start_time_file[line[0]] = datetime.strptime(line[1], "%H:%M")
  
    for line in csv.reader(sub_file, delimiter = ";"):
      name = line[0]
      task = line[1]
      point = line[2]
      start_time = start_time_file[name]
      end_time = datetime.strptime(line[3], "%H:%M")
      
      if  end_time - start_time > max:
        continue
        
      if (name, task) not in list:
        list[name, task] = point
      elif point > list[name, task]:
        list[name, task] = point
  
  for name_task, points in list.items():
    name = name_task[0]
    if name not in final:
      final[name] = int(points)
    else:
      final[name] += int(points)
  
  return final
        

if __name__ =="__main__":
  print(final_points())