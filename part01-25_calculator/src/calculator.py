# Write your solution here
num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
oprtion = input("Operation")

if oprtion == "subtract":
    print(f"{num1} - {num2} = {num1 - num2}")
if oprtion == "add":
    print(f"{num1} + {num2} = {num1 + num2}")
if oprtion == "multiply":
    print(f"{num1} * {num2} = {num1 * num2}")