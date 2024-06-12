# Write your solution here
def filter_solutions():
  correct = []
  incorrect = []
  sign = ""
  #opening the file
  with open("solutions.csv") as file:
    for line in file:
      num2 = ""
      line = line.replace("\n", "")
      data = line.split(";")

      # convert calculation part to int so we can calculate
      for digit in data[1]:
        if digit == "-":
          sign = "-"
          num = num2
          num2 = ""
        elif digit == "+":
          sign = "+"
          num = num2
          num2 = ""
        else:
          num2 += digit
      if sign == "-":
        number = int(num) - int(num2)
      else:
        number = int(num) + int(num2)
      
      if number == int(data[2]):
        correct.append([line])
      else:
        incorrect.append([line])
    
    #write to the file correct.csv
    with open("correct.csv", "w") as file:
      for data in correct:
        row = ""
        for word in data:
          row += f"{word}"
        print(row)
        file.write(row + "\n")
  
        #write to the file incorrect.csv
    with open("incorrect.csv", "w") as file:
      for data in incorrect:
        row = ""
        for word in data:
          row += f"{word}"
        file.write(row + "\n")


if __name__ == "__main__":

  filter_solutions()