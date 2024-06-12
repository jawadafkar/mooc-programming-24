# Write your solution here

tempf = int(input("Please type in a temperature (F): "))

tempc = (tempf - 32) * 5/9

less_than_zero = tempc < 0

print(f"{tempf} degrees Fahrenheit equals {tempc} degrees Celsius")

if less_than_zero:
    print("Brr! It's cold in here!")