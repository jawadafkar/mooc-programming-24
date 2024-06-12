# Write your solution here
list = []
user = ""
i = 1
while user != "x":
    print("The list is now", list)
    user = input("a(d)d, (r)emove or e(x)it: ")
    
    if len(list) == 0:
       if user == "d":
            list.append(i)
       elif user == "r":
            continue
    elif len(list) != 0:
        if user == "d":
            list.append(i+1)
        elif user == "r":
            list.pop(-1)

    if len(list) != 0:
        i = list[-1]
print("Bye!")