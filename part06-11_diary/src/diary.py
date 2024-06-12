# Write your solution here

def write(file_path:  str, sentence: str):
  with open(file_path, "a") as file:
    file.write(sentence + "\n")

def read(file_path: str):
  with open(file_path) as file:
    content = file.read()
    print(content)


def my_diary(file_path):
  while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    option = int(input("Function: "))
  
    if option == 1:
      string = input("Diary entry: ")
      write(file_path, string)
      print("Diary saved")
      
    
    elif option == 2:
      print("Entries:")
      read(file_path)
      
    elif option == 0:
      print("Bye now!")
      break

my_diary("diary.txt")