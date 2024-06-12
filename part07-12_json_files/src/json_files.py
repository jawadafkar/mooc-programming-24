# Write your solution here
import json
def print_persons(filename: str):
  with open(filename) as file:
    file_data = file.read()
  data = json.loads(file_data)
  
  for part in data:
    line = ""
    line += f"{part["name"]} {part["age"]} years ("

    if len(part["hobbies"]) > 0:
      for item in part["hobbies"]:
        line += f"{item}, "
      line = line[:-2] + ")"
    
    else:
      line += ")"
    print(line)


if __name__ == "__main__":
  print_persons("file4.json")