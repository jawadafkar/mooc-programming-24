# Write your solution here
num = int(input("Please type in a number: "))
i = 1
j = 2
while i <= num:

    while i+1 == j and j <= num:
        print(j)
        j += 2
    print(i)
    i += 2

