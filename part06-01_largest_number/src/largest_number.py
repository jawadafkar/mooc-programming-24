# write your solution here
def largest():
  with open("numbers.txt") as text_file:
    largest = 0
    for number in text_file:
      number = number.replace("\n", "")
      number = int(number)
      if number > largest:
        largest = number
    return largest

if __name__ == "__main__":
  print(largest())