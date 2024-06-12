# Write your solution here
from string import ascii_uppercase
def run(program:  list):
  printable_list = []
  # define variable names and assign 0 to all of them inside a dictionary
  variable = {}
  for char in ascii_uppercase:
    variable[char] = 0
    
  i = 0
  b = 0
  while i < len(program):
    p = program[i].split(" ")
  
  # Mov command functionality
    if p[0] == "MOV":
      if p[2] in ascii_uppercase:
        variable[p[1]] = variable[p[2]]
      else:
        variable[p[1]] = int(p[2])
  
  # ADD command functionality
    elif p[0] == "ADD":
      if p[2] in ascii_uppercase:
        variable[p[1]] += variable[p[2]]
      else:
        variable[p[1]] += int(p[2])
  
  # SUB command functionality
    elif p[0] == "SUB":
      if p[2] in ascii_uppercase:
        variable[p[1]] -= variable[p[2]]
      else:
        variable[p[1]] -= int(p[2])
  
  # MUL command functionality
    elif p[0] == "MUL":
      if p[2] in ascii_uppercase:
        variable[p[1]] *= variable[p[2]]
      else:
        variable[p[1]] *= int(p[2])
    
  # PRINT command functionality
    elif p[0] == "PRINT":
      if p[1] in ascii_uppercase:
        printable_list.append(variable[p[1]])
      else:
        printable_list.append(int(p[1]))
    
  # IF functionality
    elif p[0] == "IF":
      jump = p[5] + ":"
      
      if p[2] == "==":
       if p[3] in ascii_uppercase: 
          if variable[p[1]] == variable[p[3]]:
            i = program.index(jump)
       else:
          if variable[p[1]] == int(p[3]):
            i = program.index(jump)

      if p[2] == "!=":
       if p[3] in ascii_uppercase: 
          if variable[p[1]] != variable[p[3]]:
            i = program.index(jump)
       else:
          if variable[p[1]] != int(p[3]):
            i = program.index(jump)

      if p[2] == "<":
       if p[3] in ascii_uppercase: 
          if variable[p[1]] < variable[p[3]]:
            i = program.index(jump)
       else:
          if variable[p[1]] < int(p[3]):
            i = program.index(jump)

      if p[2] == "<=":
       if p[3] in ascii_uppercase: 
          if variable[p[1]] <= variable[p[3]]:
            i = program.index(jump)
       else:
          if variable[p[1]] <= int(p[3]):
            i = program.index(jump)

      if p[2] == ">":
       if p[3] in ascii_uppercase: 
          if variable[p[1]] > variable[p[3]]:
            i = program.index(jump)
       else:
          if variable[p[1]] > int(p[3]):
            i = program.index(jump)

      if p[2] == ">=":
       if p[3] in ascii_uppercase: 
          if variable[p[1]] >= variable[p[3]]:
            i = program.index(jump)
       else:
          if variable[p[1]] >= int(p[3]):
            i = program.index(jump)
  
  # JUMP functionality 
    elif p[0] == "JUMP":
      jump = p[1] + ":"
      i = program.index(jump)
 
  # END breaks the loop
    elif p[0] == "END":
      break
    
    i += 1

  return printable_list


if __name__ =="__main__":
  program1 = []
  program1.append("MOV A 1")
  program1.append("MOV B 2")
  program1.append("PRINT A")
  program1.append("PRINT B")
  program1.append("ADD A B")
  program1.append("PRINT A")
  program1.append("END")
  result = run(program1)
  print(result)