# Write your solution here
age = int(input("What is your age? "))

if age >= 5:
    print(f"Ok, you're {age} years old")
elif age < 0 or age > 130:
    print("That must be a mistake")
else:
    print("I suspect you can't write quite yet...")