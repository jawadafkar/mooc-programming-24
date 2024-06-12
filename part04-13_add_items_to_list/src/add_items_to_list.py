# Write your solution here
list = []
item = int(input("How many items: "))
i = 0
while item > i:
    value = int(input(f"Item {i+1}: "))
    list.append(value)
    i += 1
print(list)