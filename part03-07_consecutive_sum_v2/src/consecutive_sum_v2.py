# Write your solution here
num = 1
sum = 1
limit = int(input("Limit: "))
con = f"{num}"
while sum < limit:
    
    num += 1
    sum += num
    con += f" + {num}"
    
print(f"The consecutive sum: {con} = {sum}")