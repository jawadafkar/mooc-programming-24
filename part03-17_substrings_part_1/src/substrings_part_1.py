# Write your solution here

string = input("Please type in a string: ")
length = len(string) - 1
i = 0
out = ""
while i <= length:
    out +=string[i]
    print(out)
    i += 1
