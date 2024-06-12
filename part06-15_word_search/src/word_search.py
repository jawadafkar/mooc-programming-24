# Write your solution here
def find_words(search_term: str):
  found_words = []
  with open("words.txt") as words_file:
    for word in words_file:
      word = word.replace("\n", "")

      
      # dot wildcard code
      if len(word) == len(search_term) and "." in search_term:
        
        found = ""
        for i in range(len(word)):
          if search_term[i] == word[i] or search_term[i] == ".":
            found += word[i]
          else:
            found = ""
        
        if len(found) == len(word):
          found_words.append(found)

      # star at end wildcard code
      elif search_term[-1] == "*" and word.startswith(search_term.replace("*", "")):
        found_words.append(word)

      # star wildcard at first code
      elif search_term[0] == "*" and word.endswith(search_term.replace("*", "")):
        found_words.append(word)
      
      # without any wildcard
      else:
        if word == search_term:
          found_words.append(word)

    return found_words
        

if __name__ == "__main__":
  print(find_words("*vokes"))