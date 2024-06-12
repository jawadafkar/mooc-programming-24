# Write your solution here
def dict_of_numbers():
  numbers = {}
  
  ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" ]
  second = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
  tens = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

  for i in range(100):
    
    if i < 10:
      numbers[i] = ones[i]
    
    elif i >= 10:

      if i % 10 == 0:
        index = (i // 10) - 1
        numbers[i] = tens[index]
      elif i < 20:
        index = (i % 10) - 1
        numbers[i] = second[index]
      else:
        index = i % 10
        t = ((i - index) // 10) - 1
        numbers[i] = tens[t] + "-" + ones[index]

  return numbers




if __name__ == "__main__":
  numbers = dict_of_numbers()
  print(numbers[2])
  print(numbers[11])
  print(numbers[45])
  print(numbers[99])
  print(numbers[0])