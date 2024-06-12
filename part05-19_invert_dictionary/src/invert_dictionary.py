# Write your solution here
def invert(words:  dict):
  new_words = {}
  for key in words:
    new_words[words[key]] = key
  words.clear()
  for key in new_words:
    words[key] = new_words[key]

if __name__ == "__main__":
  s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
  invert(s)
  print(s)