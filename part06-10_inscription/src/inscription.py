# Write your solution here
name = input("Whom should I sign this to: ")
file_name = input("Where shall I save it: ")
string = (f"Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")
with open(file_name, "w") as my_file:
  my_file.write(string)
  

