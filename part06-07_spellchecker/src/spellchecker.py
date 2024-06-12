# write your solution here
def spell_checker(sentence: str):
  dictionary = []
  
  with open("wordlist.txt") as sentence_file:
    for line in sentence_file:
      line = line.replace("\n", "")
      dictionary.append(line)
    
    sentence = sentence.split(" ")
  checked = ""
  for word in sentence:
    if word.lower() not in dictionary:
      checked += "*" + word + "*"
    else:
      checked += word
    checked += " "
  print(checked)


sentence = input("Write text: ")
spell_checker(sentence)