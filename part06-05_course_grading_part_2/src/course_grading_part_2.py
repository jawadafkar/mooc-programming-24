# wwite your solution here
def grade_calculator(student, exercise, exam):
  students_name = {}
  students_exercise = {}
  students_exam = {}
  students_exam_and_exerciese = {}
  grades = {}
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

  with open(exam) as exam_file:
    for line in exam_file:
      sum = 0
      line = line.replace("\n", "")
      parts = line.split(";")
      if parts[0] == "id":
        continue
      for exam in parts[1:]:
        sum += int(exam)
      students_exam[parts[0]] = sum

  for id, exercise_points in students_exercise.items():
    if id in students_exam:
      students_exam_and_exerciese[id] = students_exam[id] + (exercise_points // 4)

  for id, exam_points in students_exam_and_exerciese.items():
    if exam_points >= 28:
      grades[id] = 5
    elif exam_points >= 24:
      grades[id] = 4
    elif exam_points >= 21:
      grades[id] = 3
    elif exam_points >= 18:
      grades[id] = 2
    elif exam_points >= 15:
      grades[id] = 1
    else:
      grades[id] = 0

  for id, name in students_name.items():
    if id in grades:
      grade = grades[id]
      print(f"{name} {grade}")
    else:
      print(f"{name} {0}")

student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_data = input("Exam points: ")
grade_calculator(student_info, exercise_data, exam_data)
#grade_calculator("students1.csv", "exercises1.csv", "exam_points1.csv")