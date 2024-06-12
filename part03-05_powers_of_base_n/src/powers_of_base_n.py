# Write your solution here'
limit = int(input("Upper limit: "))
base = int(input("Base: "))
i = 0 
while base**i <= limit:
    print(base**i)
    i += 1