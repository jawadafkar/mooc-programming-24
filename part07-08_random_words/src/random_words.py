# Write your solution here
from random import choice
def words(n: int, beginning: str):
  random_words = []
  words = read(beginning)
  if len(words) >= n:
    for i in range(n):
      select = choice(words)
      if select not in random_words:
        random_words.append(select)
  else:
    raise ValueError
  return random_words


def read(beginning: str):
  selected = []
  with open("words.txt") as words_file:
    for word in words_file:
      word = word.replace("\n", "")
      if word.startswith(beginning):
        selected.append(word)
    return selected
    
if __name__=="__main__":
  word_list = words(3, "ca")
  for word in word_list:
    print(word)