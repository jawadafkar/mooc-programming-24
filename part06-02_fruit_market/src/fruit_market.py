# write your solution here
def read_fruits():
  with open("fruits.csv") as list_fruit:
    fruit_dic = {}
    for line in list_fruit:
      line = line.replace("\n", "")
      line = line.split(";")
      fruit_dic[line[0]] = float(line[1])
    return fruit_dic
  


if __name__ == "__main__":
  print(read_fruits())
    