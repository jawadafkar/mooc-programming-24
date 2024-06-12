# Write your solution here
def histogram(word: str):
  characters = {}

  for char in word:
    if char not in characters:
      characters[char] = 0
    characters[char] += 1
  for key in characters:
    print(key, end = " ")
    print(characters[key] * "*")
  
if __name__ == "__main__":
  histogram("abba")