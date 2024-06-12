# Write your solution here
import json
import urllib.request
from math import floor

def retrieve_all():

  # Request and read data from the specified address
  address = "https://studies.cs.helsinki.fi/stats-mock/api/courses"
  request = urllib.request.urlopen(address)
  data = json.loads(request.read())
  list_of_courses = []

  # look for necessary data that we want and return them as a list
  for p in data:
    if p["enabled"]:
      list_of_courses.append((p["fullName"], p["name"], p["year"], sum(p["exercises"])))
  return list_of_courses

def retrieve_course(course_name: str):

  #Request data from server and read it
  address = f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats"
  request = urllib.request.urlopen(address)
  data = json.loads(request.read())

  #d efine data types
  course_data = {}
  students = 0
  total_exercises = 0
  total_hours = 0

  # Reading necessary data that we want
  for week, week_data in data.items():
    if week_data["students"] > students:
      students = week_data["students"]

    total_exercises += week_data["exercise_total"]
    total_hours += week_data["hour_total"]
  
  # Assign the data to a dictionary to return
  course_data["weeks"] = len(data)
  course_data["students"] = students
  course_data["hours"] = total_hours
  course_data["hours_average"] = floor(total_hours/students)
  course_data["exercises"] = total_exercises
  course_data["exercises_average"] = floor(total_exercises/students)
  return course_data

if __name__ == "__main__":
  print(retrieve_course("docker2019"))