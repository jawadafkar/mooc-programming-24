# Write your solution here
student = int(input("How many students on the course?"))
size = int(input("Desired group size?"))

group = (student + size - 1) // size

print(f"Number of groups formed: {group}")
