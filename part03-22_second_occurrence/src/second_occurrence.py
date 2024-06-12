# Write your solution here
string = input("Please type in a string: ")
sub = input("Please type in a substring: ")

index = string.find(sub)
size_of_sub = len(sub)

while True:
    string = string[index + size_of_sub:]
    if string.find(sub) != -1:
        index += string.find(sub) + size_of_sub
        print(f"The second occurrence of the substring is at index {index}.")
        break
    else:
        print("The substring does not occur twice in the string.")
        break
    