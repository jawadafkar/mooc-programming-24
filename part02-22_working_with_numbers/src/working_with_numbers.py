# Write your solution here
count = 0
sum_of_nums = 0
Positive = 0

print("Please type in integer numbers. Type in 0 to finish.")
while True:
    num = int(input("Number:"))
    if num == 0:
        break
    elif num > 0:
        Positive += 1
    count += 1
    sum_of_nums = sum_of_nums + num

print("... the program asks for numbers")
print("Numbers typed in ", count)
print("The sum of the numbers is ", sum_of_nums)
print("The mean of the numbers is ", sum_of_nums / count)
print("Positive numbers ", Positive)
print("Negative numbers ", count - Positive)