# Write your solution here
def add_words(fn_word:  str, en_word: str):
  with open("dictionary.txt", "a") as word_file:
    en_word = en_word.lower()
    fn_word = fn_word.lower()
    en_word = en_word + ":"
    word_file.write(f"{en_word:<30}{fn_word:<30}\n")



def read_words(search_term: str):
  matched_words = {}
  with open("dictionary.txt") as word_file:
    for line in word_file:
      line = line.strip()
      data = line.split(":")
      if search_term.lower() in data[0] or search_term.lower() in data[1]:
        matched_words[data[1].strip()] = data[0].strip()
    return matched_words


def main():
  while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    option = int(input("Function: "))

    if option == 1:
      fn = input("The word in Finnish: ")
      en = input("The word in English: ")
      add_words(fn, en)
      print("Dictionary entry added")

    elif option == 2:
      searched_word = input("Search term: ")
      found = read_words(searched_word)
      for fn, en in found.items():
        print(f"{fn} - {en}")
    elif option == 3:
      print("Bye!")
      break

main()