# Write your solution here
num = 1

while True:
    num = int(input("Please type in a number: "))
    if num < 1:
        break
    factorial = num
    i = num - 1
    
    while i >= 1:
        factorial *= i
        i -= 1
    
    print(f"The factorial of the number {num} is {factorial}")
print("Thanks and bye!")