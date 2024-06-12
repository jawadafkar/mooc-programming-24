# Write your solution here
string = input("Word: ")

left = (28 - len(string)) // 2
right = 28 - (left + len(string))

print("*" * 30)
print( "*" + left * " " + string + right * " " + "*" )
print("*" * 30)
