# Write your solution here
i = 0
string = []
while True:
    word = input("Word: ")
    if word in string:
        break
    else:
        string.append(word)
        i += 1
print(f"You typed in {i} different words")
