# Write your solution here
print("Person 1:")
p1 = (input("Name: "))
p1_age = int(input("Age: "))
print("Person 2:")
p2 = (input("Name: "))
p2_age = int(input("Age: "))

if p1_age > p2_age:
    print(f"The elder is {p1}")
elif p1_age < p2_age:
    print(f"The elder is {p2}")
else:
    print(f"{p1} and {p2} are the same age")
