# write your solution here

def grade_calculator(student, exercise):
  students_name = {}
  students_exercise = {}
  with open(student) as student_file:
    for line in student_file:
      line = line.replace("\n", "")
      parts = line.split(";")
      if parts[0] == "id":
        continue
      students_name[parts[0]] = parts[1] + " " + parts[2]
  
  with open(exercise) as exercise_file:
    for line in exercise_file:
      sum = 0
      line = line.replace("\n", "")
      parts = line.split(";")
      if parts[0] == "id":
        continue
      for point in parts[1:]:
        sum += int(point)
      students_exercise[parts[0]] = sum

  for id, name in students_name.items():
    if id in students_exercise:
      points = students_exercise[id]
      print(f"{name} {points}")


student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
grade_calculator(student_info, exercise_data)