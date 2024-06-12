# Write your solution here
from difflib import get_close_matches
def spell_checker(sentence: str):
  dictionary = []
  suggested = {}
  
  with open("wordlist.txt") as sentence_file:
    for line in sentence_file:
      line = line.replace("\n", "")
      dictionary.append(line)
    
    sentence = sentence.split(" ")
  checked = ""
  for word in sentence:
    if word.lower() not in dictionary:
      s = get_close_matches(word, dictionary)
      suggested[word] = s
      checked += "*" + word + "*"
    else:
      checked += word
    checked += " "
  print(checked)
  print("suggestions:")
  for incorrect, correct in suggested.items():
    line = f"{incorrect}: "
    for element in correct:
      line += element + ", "
    print(line[:-2])

sentence = input("Write text: ")
spell_checker(sentence)