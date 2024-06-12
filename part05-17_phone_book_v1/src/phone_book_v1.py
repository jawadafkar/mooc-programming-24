# Write your solution here
phonebook = {}
while True:
  value = int(input("command (1 search, 2 add, 3 quit): "))
  if value == 3:
    print("quitting...")
    break
  elif value == 2:
    name = input("Name: ")
    phone_num = input("phonebook: ")
    phonebook[name] = phone_num
    print("ok!")
  elif value == 1:
    name = input("Name: ")
    if name in phonebook:
      print(phonebook[name])
    else:
      print("no number")