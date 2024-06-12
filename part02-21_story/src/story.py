# Write your solution here
words = ""
last = ""
while True:
    word = input("Please type in a word: ")
    if word == "end" or word == last:
        print(words)
        break
    last = word
    words += word + " "
    
