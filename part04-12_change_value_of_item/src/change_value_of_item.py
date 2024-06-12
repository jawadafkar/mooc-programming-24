# Write your solution here
list = [1, 2, 3, 4, 5]
i = 0
while i != -1:
    i = int(input("index: "))
    if i == -1:
        continue

    value = int(input("New value: "))
    list[i] = value
    print(list)