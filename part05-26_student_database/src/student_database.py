# Write your solution here
def add_student(database: dict, name: str):
  data = []
  database[name] = data



def print_student(database: dict, name: str):
  found = {}
  courses_completed = 0
  sum = 0
  
  for student in database:
    
    if student == name:
      found[student] = database[student]
      courses_completed = len(found[name])
  
  if name in found:
      print(f"{name}:")
      
      if found[name] == []:
        print(" no completed courses")
      else:  
        print(f" {courses_completed} completed courses:")
        for key, value in found.items():
          for value in found[key]:
            print(f"  {value[0]} {value[1]}")
            sum += value[1]
        print(f" average grade {sum/courses_completed}")
  else:
      print(f"{name}: no such person in the database")
  


def add_course(database: dict, name: str, course: tuple):

  for data in database[name]:
    if data[0] == course[0] and data[1] > course[1]:
      return
    elif data[0] == course[0] and data[1] < course[1]:
      database[name] = []
  if course[1] != 0:
    database[name].append(course)



def summary(database: dict):
  num_of_students = len(database)
  courses = {}
  avgs = {}
  max_course = ""
  best_avg = ""
  max_course_number = 0
  max_avg_number = 0
  for student, course_and_grade in database.items():
    sum_avg = 0
    sum_course = 0
    for data in course_and_grade:
       sum_avg += data[1]
       sum_course += 1
       
    courses[student] = sum_course
    avgs[student] = sum_avg/sum_course
  
  for name in courses:
     if courses[name]> max_course_number:
        max_course_number = courses[name]
        max_course = name
     if avgs[name] > max_avg_number:
        max_avg_number = avgs[name]
        best_avg = name

  print("students", num_of_students)
  print(f"most courses completed {max_course_number} {max_course}")
  print(f"best average grade {max_avg_number} {best_avg}")





if __name__ == "__main__":
  students = {}
  add_student(students, "Peter")
  add_course(students, "Peter", ("Software Development Methods", 5))
  add_course(students, "Peter", ("Software Development Methods", 1))
  print_student(students, "Peter")
