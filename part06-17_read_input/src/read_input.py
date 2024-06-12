# Write your solution here
def read_input(text: str, min: int, max: int):

    while True:
      
      try:
        num = int(input(text))
        if num < max and num > min:
          return num
      
      except ValueError:
        pass

      print(f"You must type in an integer between {min} and {max}")


if __name__ =="__main__":
  number = read_input("Please type in a number: ", 5, 10)
  print(f"You type in: {number}")