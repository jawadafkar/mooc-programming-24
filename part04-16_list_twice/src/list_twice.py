# Write your solution here
list = []
num = 1
while True:
    num = int(input("New item: "))
    if num == 0:
        break
    list.append(num)
    sorted_list = sorted(list)
    print("The list now:", list)
    print("The list in order:", sorted_list)
print("Bye!")