# Write your solution here
i = 1
j = 1
num = int(input("Please type in a number: "))
while num >= i:
    j = 1
    while num >= j:
        print(f"{i} x {j} = {i*j}")
        j += 1
    i += 1