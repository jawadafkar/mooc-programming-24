# Write your solution here
def add(phonebook:  dict):
  name = input("Name: ")
  number = input("Number: ")
  if name in phonebook:
    phonebook[name].append(number)
  else:
    phonebook[name] = []
    phonebook[name].append(number)
  print("ok!")

def search(phonebook: dict):
  name = input("Name: ")
  if name in phonebook:
    for number in phonebook[name]:
      print(number)
  else:
    print("no number")
      


def main():
  phonebook = {}
  while True:
    user = int(input("command (1 search, 2 add, 3 quit):"))
    if user == 3:
      print("quitting...")
      break
    elif user == 2:
      add(phonebook)
    elif user == 1:
      search(phonebook)
    else:
      continue


main()