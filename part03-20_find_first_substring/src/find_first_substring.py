# Write your solution here
string = input("Please type in a word: ")
charc = input("Please type in a character: ")

index = string.find(charc)
if index != -1 and len(string)>= index + 3:
    print(string[index:index+3])