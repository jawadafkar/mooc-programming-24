# Write your solution here

def user_input():
  string = ""
  points = []
  while True:
    string = (input("Exam points and exercises completed:"))
    
    if len(string) != 0:
      points.append(string.split())    
    else:
      break
  return points


def calculate(item1, item2):
  percent = int(item2) / 100
  total= int(item1) + int(percent * 10)
  return total


def cal_grades(list):
  grade = [0, 0, 0, 0, 0, 0]
  
  for item in list:
    if int(item[0]) < 10:
      grade[0] += 1
    elif calculate(item[0], item[1]) >= 28:
      grade[5] += 1
    elif calculate(item[0], item[1]) >= 24:
      grade[4] += 1
    elif calculate(item[0], item[1]) >= 21:
      grade[3] += 1
    elif calculate(item[0], item[1]) >= 18:
      grade[2] += 1
    elif calculate(item[0], item[1]) >= 15:
      grade[1] += 1
    elif calculate(item[0], item[1]) >= 0 and int(item[0]) >= 10:
      grade[0] += 1
  return grade

def pass_percent(list):
  fail = list[0]
  total = 0
  for item in list:
    total += item
  passed = total - fail
  return (passed / total) * 100


def points_avg(list):
  avg = sum(list) / len(list)
  return avg


def main():
  all_points_list = user_input()
  
  total_list = []
  for item in all_points_list:
    total_list.append(calculate(item[0], item[1]))

  avrg = points_avg(total_list)
  grade_list = cal_grades(all_points_list)
  percent_passed = pass_percent(grade_list)

  print("Statistics:")
  print(f"Points average: {avrg}")
  print(f"Pass percentage:{percent_passed: .1f}")
  print("Grade distribution:")
  for i in range(5, -1, -1):
    print(f"{i}: {grade_list[i]* "*"}")


main()

