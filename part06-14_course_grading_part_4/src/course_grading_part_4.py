# tee ratkaisu tänne
def readfile(filename1: str, filename2: str, filename3: str):
  student_data = {}
  exam_points = 0
  with open(filename1) as student_file, open(filename2) as exercise_file, open(filename3) as exam_file:
    for line in student_file:
      line = line.replace("\n", "")
      data = line.split(";")
      student_data
      if data[0] == "id":
        continue
      name = data[1] + " " + data[2]
      student_data[data[0]] = [name]
    
    for line in exercise_file:
      line = line.replace("\n", "")
      data = line.split(";")
      if data[0] == "id":
        continue
      pts = 0
      for point in data[1:]:
        pts += int(point)
      exercise_points = pts // 4
      student_data[data[0]].append(pts)
      student_data[data[0]].append(exercise_points)

    for line in exam_file:
      line = line.replace("\n", "")
      data = line.split(";")
      if data[0] == "id":
        continue
      exam_points = 0
      for point in data[1:]:
        exam_points += int(point)
      student_data[data[0]].append(exam_points)
      total = add_total(student_data, data[0])
      grades = grade(total)
      student_data[data[0]].append(grades)



  return student_data

def grade(points):
    if points >= 28:
      return 5
    elif points >= 24:
      return 4
    elif points >= 21:
      return 3
    elif points >= 18:
      return 2
    elif points >= 15:
      return 1
    else:
      return 0

def add_total(data, id):
  total = data[id][2] + data[id][3]
  data[id].append(total)
  return total

def save_files(file, course_name):
  with open("results.txt", "w") as text_file, open("results.csv", "w") as csv_file:
    text_file.write(f"{course_name[0]}, {course_name[1]} credits\n")
    text_file.write("======================================\n")
    text_file.write("name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade\n")
    for id, list in file.items():
      text_file.write(f"{list[0]:<30}{list[1]:<10}{list[2]:<10}{list[3]:<10}{list[4]:<10}{list[5]:<10}\n")
    
    for id, list in file.items():
      csv_file.write(f"{id};{list[0]};{list[5]}\n")

def read_course(filename):
  course_info = []
  with open(filename) as course:
    for line in course:
      line = line.replace("\n", "")
      data = line.split(":")
      course_info.append(data[1].strip())
    return course_info



student_file = input("Student information: ")
exercise_file = input("Exercises completed: ")
exam_file = input("Exam points:")
course_file = input("Course information: ")
data = readfile(student_file, exercise_file, exam_file)
course = read_course(course_file)
save_files(data, course)
