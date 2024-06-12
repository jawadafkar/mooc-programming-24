# Write your solution here
def filter_incorrect():
  with open("lottery_numbers.csv") as file, open("correct_numbers.csv", "w") as correct:
    for line in file:
      line = line.replace("\n", "")
      week = line.split(";")
      week = week[0].split(" ")
      lottery = line.split(";")
      lottery = lottery[1].split(",")
      
      try:
        #check if week is int type
        weeknumber = int(week[1])

        #check for repeated number in lottery numbers
        for i in range(len(lottery)):
          for j in range(i+1, len(lottery)):
            if int(lottery[i]) == int(lottery[j]):
              raise ValueError
        
        #check if lottery numbers are in range between 1 and 39
          if int(lottery[i]) < 1 or int(lottery[i]) > 39:
            raise ValueError
        
        #check if threre are exactly seven lottery numbers
        if len(lottery) < 7:
          raise ValueError

      except ValueError:
        continue
      
      correct.write(line +"\n")


if __name__=="__main__":
  filter_incorrect()